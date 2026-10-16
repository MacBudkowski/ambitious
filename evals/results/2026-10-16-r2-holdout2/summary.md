# Evaluation summary

- Date: 2026-10-16
- Subject model: `claude-sonnet-5-5` · Judge model: `claude-opus-5-5`
- Scenario file: `holdout2.json` · Scenarios: 20 · Reps: 2 · Subject calls: 80

| Group | Cases | Criteria passed (baseline → skill) | All criteria met (baseline → skill) | Usefulness 1–5 (baseline → skill) | Head-to-head (skill / baseline / tie) |
|---|---|---|---|---|---|
| Speed | 8 | 82% → 100% | 4/8 → 8/8 | 4.5 → 5.0 | 7 / 1 / 0 |
| Depth | 8 | 82% → 89% | 4/8 → 5/8 | 4.38 → 4.5 | 7 / 1 / 0 |
| Range | 8 | 70% → 93% | 2/8 → 6/8 | 4.12 → 4.25 | 4 / 4 / 0 |
| Altitude | 8 | 75% → 100% | 2/8 → 8/8 | 4.12 → 4.5 | 4 / 4 / 0 |
| Guardrail | 8 | 96% → 96% | 7/8 → 7/8 | 4.75 → 4.75 | 4 / 0 / 4 |
| **All** | 40 | 80% → 96% | 19/40 → 34/40 | 4.38 → 4.6 | 26 / 10 / 4 |
