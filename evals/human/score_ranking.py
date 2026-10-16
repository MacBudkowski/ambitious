#!/usr/bin/env python3
"""Un-blind and summarise human ranking results.

Usage:
    python3 score_ranking.py [results.json] [key.json] [--out summary.md]

Defaults: results.json, key.json and summary.md next to this script.
Prints per-system mean rank, % first place, % "Yes" on the boldness
question (plus % Yes-or-Somewhat), and a per-prompt table. Writes the same
report as Markdown to summary.md. Python 3 standard library only.
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent


def pct(n, d):
    return "%.0f%%" % (100.0 * n / d) if d else "-"


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c).replace("|", "\\|").replace("\n", " ") for c in r) + " |")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("results", nargs="?", default=str(HERE / "results.json"))
    ap.add_argument("key", nargs="?", default=str(HERE / "key.json"))
    ap.add_argument("--out", default=str(HERE / "summary.md"))
    args = ap.parse_args()

    results = json.loads(Path(args.results).read_text(encoding="utf-8"))
    key = json.loads(Path(args.key).read_text(encoding="utf-8"))
    warnings = []
    if results.get("build_id") and key.get("build_id") and results["build_id"] != key["build_id"]:
        warnings.append("results.json build_id (%s) does not match key.json (%s) - labels may be wrong. "
                        "Rebuild-with-same-input or use the matching key." % (results["build_id"], key["build_id"]))

    ranks = defaultdict(list)          # system -> [rank, ...]
    firsts = defaultdict(int)
    ranked_prompts = defaultdict(int)  # system -> prompts where it got a rank
    bold = defaultdict(lambda: defaultdict(int))  # system -> answer -> count
    per_prompt = []
    systems = set()
    for m in key["prompts"].values():
        systems.update(m.values())

    for a in results.get("answers", []):
        pid = str(a["prompt_id"])
        mapping = key["prompts"].get(pid)
        if mapping is None:
            warnings.append("Prompt %s is in results but not in key - skipped." % pid)
            continue
        r = a.get("ranks", {}) or {}
        b = a.get("bolder", {}) or {}
        for label, system in mapping.items():
            if label in r:
                ranks[system].append(int(r[label]))
                ranked_prompts[system] += 1
                if int(r[label]) == 1:
                    firsts[system] += 1
            if label in b:
                bold[system][b[label]] += 1
        order = sorted((lbl for lbl in r if lbl in mapping), key=lambda lbl: int(r[lbl]))
        per_prompt.append({
            "id": pid,
            "order": " > ".join(mapping[l] for l in order) or "(not ranked)",
            "bold": ", ".join("%s: %s" % (mapping[l], b[l]) for l in sorted(b) if l in mapping) or "-",
            "note": (a.get("note") or "").strip(),
            "complete": a.get("complete", False),
        })

    rows = []
    for s in systems:
        rs = ranks[s]
        nb = sum(bold[s].values())
        rows.append((
            sum(rs) / len(rs) if rs else float("inf"), s,
            ["%.2f" % (sum(rs) / len(rs)) if rs else "-",
             pct(firsts[s], ranked_prompts[s]),
             pct(bold[s]["yes"], nb),
             pct(bold[s]["yes"] + bold[s]["somewhat"], nb),
             str(ranked_prompts[s])],
        ))
    rows.sort(key=lambda x: (x[0], x[1]))
    sys_table = md_table(["System", "Mean rank (1 = best)", "% 1st place", "% Yes (bolder)", "% Yes+Somewhat", "Prompts ranked"],
                         [[s] + cols for _, s, cols in rows])
    prompt_table = md_table(["Prompt", "Ranking (best > worst)", "Bolder?", "Note"],
                            [[p["id"] + ("" if p["complete"] else " *"), p["order"], p["bold"], p["note"] or "-"]
                             for p in per_prompt])

    n_done = sum(1 for p in per_prompt if p["complete"])
    report = ["# Human blind-ranking summary", "",
              "- Results: `%s` (exported %s)" % (Path(args.results).name, results.get("exported_at", "?")),
              "- Prompts answered: %d (complete: %d) of %d in key" % (len(per_prompt), n_done, len(key["prompts"])),
              "- Boldness question: *Would this make me ask for something bolder than I would have?*", ""]
    if warnings:
        report += ["**Warnings:**", ""] + ["- " + w for w in warnings] + [""]
    report += ["## By system", "", sys_table, "", "## By prompt", "", prompt_table, ""]
    if n_done < len(per_prompt):
        report += ["\\* = prompt not fully answered.", ""]
    text = "\n".join(report)
    print(text)
    Path(args.out).write_text(text, encoding="utf-8")
    print("\nWrote %s" % args.out, file=sys.stderr)


if __name__ == "__main__":
    main()
