#!/usr/bin/env python3
"""Build a blind-ranking web page from candidate replies.

Usage:
    python3 build_ranking.py [candidates.json] [--seed N]

Input (default: candidates.json next to this script):
    [{"id": "...", "prompt": "...", "source": "...",
      "candidates": {"<system>": "<markdown reply>", ...}}, ...]

Outputs (next to this script):
    ranking.html  - self-contained offline page (no system names inside)
    key.json      - which label (A/B/C/D) is which system, per prompt.
                    Keep this away from the person ranking.

Python 3 standard library only.
"""

import argparse
import hashlib
import json
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LABELS = "ABCDEFGH"
DEFAULT_SEED = 20261016


def load_candidates(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, list) or not data:
        sys.exit("Input must be a non-empty JSON list of prompts.")
    seen = set()
    for i, item in enumerate(data):
        for field in ("id", "prompt", "candidates"):
            if field not in item:
                sys.exit("Item %d is missing '%s'." % (i, field))
        pid = str(item["id"])
        if pid in seen:
            sys.exit("Duplicate prompt id: %s" % pid)
        seen.add(pid)
        cands = item["candidates"]
        if not isinstance(cands, dict) or len(cands) < 2:
            sys.exit("Prompt %s needs at least 2 candidates." % pid)
        if len(cands) > len(LABELS):
            sys.exit("Prompt %s has too many candidates (max %d)." % (pid, len(LABELS)))
    return data


def build(data, seed):
    """Return (page_items, key) with shuffled, neutrally-labelled candidates."""
    # Random per-prompt order, gently counterbalanced against position bias:
    # for each prompt draw several seeded shuffles and keep the one that best
    # evens out how often each system sits in each slot (A, B, ...).
    # Deterministic for a given seed and input.
    rng = random.Random(seed)
    slot_counts = {}  # (system, slot index) -> times placed there so far
    offsets = {}
    for item in data:
        pid = str(item["id"])
        best, best_cost = sorted(item["candidates"]), None
        for _ in range(40):
            perm = sorted(item["candidates"])
            rng.shuffle(perm)
            cost = sum(slot_counts.get((s, i), 0) for i, s in enumerate(perm))
            if best_cost is None or cost < best_cost:
                best, best_cost = perm, cost
        for i, s in enumerate(best):
            slot_counts[(s, i)] = slot_counts.get((s, i), 0) + 1
        offsets[pid] = best

    page_items, key_prompts = [], {}
    for item in data:
        pid = str(item["id"])
        systems = offsets[pid]
        labelled = []
        mapping = {}
        for label, system in zip(LABELS, systems):
            labelled.append({"label": label, "text": str(item["candidates"][system])})
            mapping[label] = system
        page_items.append({"id": pid, "prompt": str(item["prompt"]), "candidates": labelled})
        key_prompts[pid] = mapping
    blob = json.dumps(page_items, sort_keys=True, ensure_ascii=False)
    build_id = hashlib.sha256(("%s|%s" % (seed, blob)).encode("utf-8")).hexdigest()[:12]
    key = {"build_id": build_id, "seed": seed, "prompts": key_prompts}
    return build_id, page_items, key


def safe_json_for_script(obj):
    s = json.dumps(obj, ensure_ascii=False)
    # Prevent "</script>" or "<!--" inside data from breaking out of the tag.
    return s.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026") \
            .replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")


def leak_check(html, key):
    systems = set()
    for mapping in key["prompts"].values():
        systems.update(mapping.values())
    leaks = []
    for s in sorted(systems):
        if re.search(r"(?<![A-Za-z0-9_-])%s(?![A-Za-z0-9_-])" % re.escape(s), html, re.I):
            leaks.append(s)
    return leaks


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", nargs="?", default=str(HERE / "candidates.json"))
    ap.add_argument("--seed", type=int, default=DEFAULT_SEED)
    ap.add_argument("--outdir", default=str(HERE))
    args = ap.parse_args()

    data = load_candidates(args.input)
    build_id, items, key = build(data, args.seed)

    template = (HERE / "ranking_template.html").read_text(encoding="utf-8")
    html = template.replace("__BUILD_ID__", build_id).replace("__DATA_JSON__", safe_json_for_script(items))

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "ranking.html").write_text(html, encoding="utf-8")
    (outdir / "key.json").write_text(json.dumps(key, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print("Built %d prompts (build %s, seed %d)" % (len(items), build_id, args.seed))
    print("  page: %s" % (outdir / "ranking.html"))
    print("  key:  %s  (do not show this to the ranker)" % (outdir / "key.json"))
    leaks = leak_check(html, key)
    if leaks:
        print("WARNING: system names appear in the page text (probably inside a reply): %s"
              % ", ".join(leaks), file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
