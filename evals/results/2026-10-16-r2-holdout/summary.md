# Evaluation summary

- Date: 2026-10-16
- Subject model: `claude-sonnet-5-5` · Judge model: `claude-opus-5-5`
- Scenario file: `holdout.json` · Scenarios: 20 · Reps: 2 · Subject calls: 80

| Group | Cases | Criteria passed (baseline → skill) | All criteria met (baseline → skill) | Usefulness 1–5 (baseline → skill) | Head-to-head (skill / baseline / tie) |
|---|---|---|---|---|---|
| Speed | 8 | 81% → 100% | 3/8 → 8/8 | 4.0 → 4.25 | 4 / 4 / 0 |
| Depth | 8 | 100% → 100% | 8/8 → 8/8 | 4.62 → 4.75 | 7 / 1 / 0 |
| Range | 8 | 85% → 88% | 4/8 → 5/8 | 4.12 → 4.62 | 3 / 5 / 0 |
| Altitude | 8 | 79% → 100% | 5/8 → 8/8 | 4.25 → 4.88 | 6 / 2 / 0 |
| Guardrail | 8 | 100% → 100% | 8/8 → 8/8 | 4.75 → 5.0 | 7 / 1 / 0 |
| **All** | 40 | 89% → 98% | 28/40 → 37/40 | 4.35 → 4.7 | 27 / 13 / 0 |
