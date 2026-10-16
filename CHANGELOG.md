# Changelog

## 1.0.0 — 2026-10-16

Renamed from `ambition-check` to **stay-ambitious**, and restructured.

- **SKILL.md** rewritten: roughly half the length, a quick-reference table of the four types, a six-step conversation, and duplicate rules removed. General agent rules that weren't about ambition (over-engineering, simplification requests) moved out.
- **Per-type references:** `references/{speed,depth,range,altitude}.md` each pair practical guidance (how to apply it, a good suggestion shape, common mistakes) with the article's verbatim text for that type only. This replaces the single all-types excerpt file, so agents load only what they need.
- **Evaluation:** 18 scenarios covering all four types plus guardrails; `evals/run_eval.py` runs with/without-skill comparisons and judges them blind. The first recorded results are in `evals/results/`.
- **Host-neutral:** frontmatter follows the open Agent Skills spec; install instructions and examples no longer assume a particular agent.
- **Tests** now check links, frontmatter limits, per-type coverage and quote integrity (checksums), instead of exact phrases.
- **README** rewritten around what the skill does, a real before/after, results, and install steps for several hosts.

## 0.3.6 and earlier

Published as `ambition-check`. Earlier versions are in the repository history.
