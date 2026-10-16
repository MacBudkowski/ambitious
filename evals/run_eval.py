#!/usr/bin/env python3
"""Behavioral evaluation for the stay-ambitious skill.

For every scenario in evals/scenarios.json, a subject model answers the prompt
twice in fresh contexts: once with a plain assistant system prompt (baseline)
and once with the skill loaded (SKILL.md plus its reference files). A separate
judge model then:

  1. scores each response against the scenario's pass criteria, without being
     told which arm produced it; and
  2. compares the two responses head-to-head in random A/B order.

Dependency-free (stdlib only). Talks to any OpenAI-compatible
/chat/completions endpoint.

    EVAL_BASE_URL=http://127.0.0.1:8317/v1 \
    EVAL_SUBJECT_MODEL=claude-sonnet-5-5 \
    EVAL_JUDGE_MODEL=claude-opus-5-5 \
    python3 evals/run_eval.py --reps 1 --out evals/results/latest

Optional: EVAL_API_KEY (sent as a bearer token), --only id1,id2, --workers N.
Writes raw.jsonl (every response and verdict) and summary.json/summary.md.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import os
import random
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BASELINE_SYSTEM = (
    "You are a capable AI assistant helping a user with their work. "
    "Respond to the user's message directly. You cannot run tools in this "
    "conversation; reply in text only."
)


def skill_system() -> str:
    parts = [BASELINE_SYSTEM, "", "The following skill is loaded. Follow it.", ""]
    parts.append("=== SKILL.md ===\n" + (ROOT / "SKILL.md").read_text())
    for name in ("speed", "depth", "range", "altitude", "examples"):
        p = ROOT / "references" / f"{name}.md"
        parts.append(f"=== references/{name}.md (available on demand) ===\n" + p.read_text())
    return "\n".join(parts)


def chat(model: str, system: str, user: str, max_tokens: int = 16000, temperature: float = 0.7) -> str:
    base = os.environ.get("EVAL_BASE_URL", "http://127.0.0.1:8317/v1").rstrip("/")
    body = json.dumps({
        "model": model,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
    }).encode()
    headers = {"Content-Type": "application/json"}
    key = os.environ.get("EVAL_API_KEY")
    if key:
        headers["Authorization"] = f"Bearer {key}"
    last = None
    for attempt in range(6):
        try:
            req = urllib.request.Request(base + "/chat/completions", data=body, headers=headers)
            with urllib.request.urlopen(req, timeout=180) as r:
                data = json.load(r)
            choice = data["choices"][0]
            content = choice["message"]["content"] or ""
            if choice.get("finish_reason") == "length":
                raise ValueError("completion truncated at max_tokens")
            if not content.strip():
                raise ValueError("empty completion")
            return content
        except Exception as e:  # network / rate limit: back off and retry
            last = e
            time.sleep(min(60, 2 ** attempt * 3))
    raise RuntimeError(f"chat failed after retries: {last}")


def extract_json(text: str) -> dict:
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        raise ValueError("no JSON in judge output: " + text[:200])
    return json.loads(m.group(0))


def judge_call(model: str, prompt: str, max_tokens: int) -> dict:
    last = None
    for _ in range(3):
        try:
            return extract_json(chat(model, JUDGE_SYSTEM, prompt, max_tokens=max_tokens, temperature=0))
        except ValueError as e:  # truncated or malformed JSON: ask again
            last = e
    raise RuntimeError(f"judge returned unparseable output: {last}")


JUDGE_SYSTEM = (
    "You are a strict, impartial evaluator of AI assistant replies. You judge "
    "only what the reply actually says. Return JSON only."
)


def judge_criteria(model: str, scenario: dict, response: str) -> dict:
    crit = "\n".join(f"{i + 1}. {c}" for i, c in enumerate(scenario["pass_criteria"]))
    prompt = f"""User message to the assistant:
<<<
{scenario['prompt']}
>>>

Assistant reply:
<<<
{response}
>>>

Score the reply against each criterion. A criterion passes only if the reply clearly satisfies it.
Criteria:
{crit}

Also rate overall usefulness to this user from 1 (unhelpful) to 5 (exceptionally useful).
Return JSON: {{"criteria": [{{"n": 1, "pass": true, "why": "<short>"}}, ...], "usefulness": <1-5>}}"""
    out = judge_call(model, prompt, 1500)
    out["criteria"] = out.get("criteria", [])[: len(scenario["pass_criteria"])]
    return out


def judge_pairwise(model: str, scenario: dict, a: str, b: str) -> dict:
    prompt = f"""User message:
<<<
{scenario['prompt']}
>>>

Reply A:
<<<
{a}
>>>

Reply B:
<<<
{b}
>>>

Which reply better serves this user's real goal: more useful, grounded in their task, respecting their constraints and scope, and not padded? Ties are allowed.
Return JSON: {{"winner": "A" | "B" | "tie", "why": "<one sentence>"}}"""
    return judge_call(model, prompt, 800)


def run_case(scenario: dict, rep: int, subject: str, judge: str, sys_skill: str, seed: int) -> dict:
    responses = {
        "baseline": chat(subject, BASELINE_SYSTEM, scenario["prompt"]),
        "skill": chat(subject, sys_skill, scenario["prompt"]),
    }
    verdicts = {arm: judge_criteria(judge, scenario, text) for arm, text in responses.items()}
    rng = random.Random(f"{seed}-{scenario['id']}-{rep}")
    skill_is_a = rng.random() < 0.5
    a, b = (responses["skill"], responses["baseline"]) if skill_is_a else (responses["baseline"], responses["skill"])
    pw = judge_pairwise(judge, scenario, a, b)
    w = pw.get("winner", "tie")
    pref = "tie" if w == "tie" else ("skill" if (w == "A") == skill_is_a else "baseline")
    return {
        "id": scenario["id"], "pillar": scenario["pillar"], "rep": rep,
        "responses": responses, "verdicts": verdicts,
        "pairwise": {"preferred": pref, "skill_was": "A" if skill_is_a else "B", "why": pw.get("why", "")},
    }


def summarize(rows: list[dict], meta: dict) -> dict:
    by: dict = {}
    for r in rows:
        for key in (r["pillar"], "ALL"):
            s = by.setdefault(key, {"n": 0, "crit_total": 0, "pass": {"baseline": 0, "skill": 0},
                                    "full": {"baseline": 0, "skill": 0}, "useful": {"baseline": 0, "skill": 0},
                                    "pref": {"skill": 0, "baseline": 0, "tie": 0}})
            s["n"] += 1
            s["crit_total"] += len(r["verdicts"]["skill"]["criteria"])
            for arm in ("baseline", "skill"):
                c = r["verdicts"][arm]["criteria"]
                passed = sum(1 for x in c if x.get("pass"))
                s["pass"][arm] += passed
                s["full"][arm] += int(passed == len(c) and len(c) > 0)
                s["useful"][arm] += float(r["verdicts"][arm].get("usefulness", 0))
            s["pref"][r["pairwise"]["preferred"]] += 1
    table = {}
    for k, s in by.items():
        table[k] = {
            "cases": s["n"],
            "criteria_pass_rate": {a: round(s["pass"][a] / max(1, s["crit_total"]), 3) for a in s["pass"]},
            "all_criteria_met": {a: f"{s['full'][a]}/{s['n']}" for a in s["full"]},
            "mean_usefulness": {a: round(s["useful"][a] / s["n"], 2) for a in s["useful"]},
            "head_to_head": s["pref"],
        }
    return {"meta": meta, "results": table}


def to_markdown(summary: dict) -> str:
    m = summary["meta"]
    lines = [
        "# Evaluation summary", "",
        f"- Date: {m['date']}",
        f"- Subject model: `{m['subject']}` · Judge model: `{m['judge']}`",
        f"- Scenario file: `{m.get('scenario_file', 'scenarios.json')}` · Scenarios: {m['scenarios']} · Reps: {m['reps']} · Subject calls: {m['subject_calls']}",
        "", "| Group | Cases | Criteria passed (baseline → skill) | All criteria met (baseline → skill) | Usefulness 1–5 (baseline → skill) | Head-to-head (skill / baseline / tie) |",
        "|---|---|---|---|---|---|",
    ]
    order = ["speed", "depth", "range", "altitude", "guardrail", "ALL"]
    for k in order:
        if k not in summary["results"]:
            continue
        r = summary["results"][k]
        cp, fm, u, h = r["criteria_pass_rate"], r["all_criteria_met"], r["mean_usefulness"], r["head_to_head"]
        name = "**All**" if k == "ALL" else k.capitalize()
        lines.append(f"| {name} | {r['cases']} | {cp['baseline']:.0%} → {cp['skill']:.0%} | {fm['baseline']} → {fm['skill']} | "
                     f"{u['baseline']} → {u['skill']} | {h['skill']} / {h['baseline']} / {h['tie']} |")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--reps", type=int, default=1)
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--only", default="")
    ap.add_argument("--scenarios", default=str(ROOT / "evals" / "scenarios.json"),
                    help="scenario file (e.g. evals/holdout.json for the independent set)")
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--resume", action="store_true",
                    help="keep completed cases in OUT/raw.jsonl and run only the missing ones")
    ap.add_argument("--out", default=str(ROOT / "evals" / "results" / "latest"))
    args = ap.parse_args()

    subject = os.environ.get("EVAL_SUBJECT_MODEL", "claude-sonnet-5-5")
    judge = os.environ.get("EVAL_JUDGE_MODEL", "claude-opus-5-5")
    scenarios = json.loads(Path(args.scenarios).read_text())
    if args.only:
        wanted = set(args.only.split(","))
        scenarios = [s for s in scenarios if s["id"] in wanted]
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    sys_skill = skill_system()

    rows, failures = [], []
    raw_path = out / "raw.jsonl"
    if args.resume and raw_path.exists():
        rows = [json.loads(l) for l in raw_path.read_text().splitlines() if l.strip()]
    done_keys = {(r["id"], r["rep"]) for r in rows}
    jobs = [(s, r) for s in scenarios for r in range(args.reps) if (s["id"], r) not in done_keys]
    print(f"{len(rows)} cases already done, {len(jobs)} to run", flush=True)
    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex, open(raw_path, "a" if args.resume else "w") as raw:
        futs = {ex.submit(run_case, s, r, subject, judge, sys_skill, args.seed): (s["id"], r) for s, r in jobs}
        for f in cf.as_completed(futs):
            cid, rep = futs[f]
            try:
                row = f.result()
                rows.append(row)
                raw.write(json.dumps(row) + "\n")
                raw.flush()
                print(f"done {cid}#{rep}: preferred={row['pairwise']['preferred']}", flush=True)
            except Exception as e:
                failures.append({"id": cid, "rep": rep, "error": str(e)})
                print(f"FAIL {cid}#{rep}: {e}", file=sys.stderr, flush=True)

    rows.sort(key=lambda r: (r["pillar"], r["id"], r["rep"]))
    meta = {"date": time.strftime("%Y-%m-%d"), "subject": subject, "judge": judge,
            "scenario_file": Path(args.scenarios).name,
            "scenarios": len(scenarios), "reps": args.reps, "subject_calls": 2 * len(rows),
            "failures": failures}
    summary = summarize(rows, meta)
    (out / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    (out / "summary.md").write_text(to_markdown(summary))
    print(to_markdown(summary))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
