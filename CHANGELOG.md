# Changelog

## 1.0.0 — 2026-10-16

Renamed from `ambition-check` to **stay-ambitious**, and restructured.

- **SKILL.md** rewritten: roughly half the length, a quick-reference table of the four types, a seven-step conversation, and duplicate rules removed. General agent rules that weren't about ambition (over-engineering, simplification requests) moved out.
- **Per-type references:** `references/{speed,depth,range,altitude}.md` each pair practical guidance (how to apply it, a good suggestion shape, common mistakes) with the article's verbatim text for that type only. This replaces the single all-types excerpt file, so agents load only what they need.
- **Behavior fixes found by evaluation:** the skill delivers the original request first instead of withholding it, keeps suggestions to one plain-language paragraph (no bulleted plans, no framework labels), treats recurrence ("third time this month") as a strong Altitude signal, requires Range ideas to name the field they borrow from, and requires Depth tests to name the outcome that decides success.
- **Evaluation:** 18 author-written scenarios plus three independent held-out sets of 20 prompts each, written by separate agents that never saw the skill. `evals/run_eval.py` runs with/without-skill comparisons and judges them blind; `--resume` re-runs only failed cases; truncated replies are rejected rather than scored. Results are in `evals/results/`.
- **Pre-send check:** each suggestion is checked against its type (Range names its field; Depth offers one check and its success measure; Altitude addresses the cause, not faster handling; Speed gives estimates, not promises). Unknown facts become placeholders; safety notes where harm is plausible.
- **Leans in on substantial work:** a "what would a top practitioner add?" check, an explicit skip list (facts, conversions, short rewrites, full specs, explicit limits), and the extra idea capped at two or three sentences, offered after the answer.
- **Real-prompt evaluation:** 63 real prompts (published by well-known practitioners, popular prompt collections, WildChat) with sources, plus a 32-prompt subset where ambition clearly matters.
- **Host-neutral:** frontmatter follows the open Agent Skills spec; install instructions and examples no longer assume a particular agent.
- **Tests** now check links, frontmatter limits, per-type coverage, host neutrality and quote integrity (checksums), instead of exact phrases.
- **README** rewritten around what the skill does, a real before/after, results, and install steps.

## 0.3.6 and earlier

Published as `ambition-check`. Earlier versions are in the repository history.
