#!/usr/bin/env python3
"""Diagnostic: re-judge head-to-head with the skill's closing type label removed.

The skill ends suggestions with a short note such as
"(This is what's called Altitude: aiming at the goal behind the task.)".
A judge who doesn't know the user installed an ambition skill can read that
as unexplained jargon. This script strips that one closing note from the
skill replies in an existing results folder and re-runs only the blind
pairwise comparison, to separate "the label costs points" from "the
substance is worse". It never changes the recorded main results.

    python3 evals/rejudge_without_label.py evals/results/<run>
"""
from __future__ import annotations

import concurrent.futures as cf
import json
import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_eval as R  # noqa: E402

LABEL = re.compile(r"\s*\((?:This|These) (?:is|are) what'?s called [^)]*\)", re.I)


def main() -> int:
    run = Path(sys.argv[1])
    judge = R.os.environ.get("EVAL_JUDGE_MODEL", "claude-opus-5-5")
    rows = [json.loads(l) for l in (run / "raw.jsonl").read_text().splitlines() if l.strip()]
    scen = {}
    for f in ("scenarios.json", "holdout.json", "holdout2.json"):
        p = R.ROOT / "evals" / f
        if p.exists():
            for s in json.loads(p.read_text()):
                scen[s["id"]] = s

    def one(r):
        skill = LABEL.sub("", r["responses"]["skill"]).strip()
        base = r["responses"]["baseline"]
        skill_is_a = random.Random(f"nolabel-{r['id']}-{r['rep']}").random() < 0.5
        a, b = (skill, base) if skill_is_a else (base, skill)
        w = R.judge_pairwise(judge, scen[r["id"]], a, b).get("winner", "tie")
        pref = "tie" if w == "tie" else ("skill" if (w == "A") == skill_is_a else "baseline")
        return r["pillar"], pref, skill != r["responses"]["skill"]

    out = {}
    stripped = 0
    with cf.ThreadPoolExecutor(max_workers=2) as ex:
        for pillar, pref, changed in ex.map(one, rows):
            stripped += changed
            for k in (pillar, "ALL"):
                out.setdefault(k, {"skill": 0, "baseline": 0, "tie": 0})[pref] += 1
    result = {"stripped_label_in": stripped, "cases": len(rows), "head_to_head_without_label": out}
    (run / "head_to_head_without_label.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
