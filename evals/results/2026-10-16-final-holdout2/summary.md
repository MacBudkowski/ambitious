# Evaluation summary

- Date: 2026-10-16
- Subject model: `claude-sonnet-5-5` · Judge model: `claude-opus-5-5`
- Scenario file: `holdout2.json` · Scenarios: 20 · Reps: 2 · Subject calls: 80

| Group | Cases | Criteria passed (baseline → skill) | All criteria met (baseline → skill) | Usefulness 1–5 (baseline → skill) | Head-to-head (skill / baseline / tie) |
|---|---|---|---|---|---|
| Speed | 8 | 86% → 96% | 5/8 → 7/8 | 4.5 → 4.62 | 6 / 2 / 0 |
| Depth | 8 | 79% → 82% | 4/8 → 4/8 | 4.38 → 4.38 | 6 / 2 / 0 |
| Range | 8 | 77% → 90% | 3/8 → 5/8 | 4.12 → 4.38 | 5 / 3 / 0 |
| Altitude | 8 | 68% → 79% | 1/8 → 4/8 | 3.88 → 4.12 | 5 / 3 / 0 |
| Guardrail | 8 | 100% → 100% | 8/8 → 8/8 | 4.62 → 5.0 | 4 / 1 / 3 |
| **All** | 40 | 81% → 89% | 21/40 → 28/40 | 4.3 → 4.5 | 26 / 11 / 3 |
