# Evaluation summary

- Date: 2026-10-16
- Subject model: `claude-sonnet-5-5` · Judge model: `claude-opus-5-5`
- Scenario file: `holdout.json` · Scenarios: 20 · Reps: 2 · Subject calls: 80

| Group | Cases | Criteria passed (baseline → skill) | All criteria met (baseline → skill) | Usefulness 1–5 (baseline → skill) | Head-to-head (skill / baseline / tie) |
|---|---|---|---|---|---|
| Speed | 8 | 85% → 96% | 4/8 → 7/8 | 4.0 → 3.88 | 1 / 7 / 0 |
| Depth | 8 | 96% → 93% | 7/8 → 6/8 | 4.62 → 4.0 | 1 / 7 / 0 |
| Range | 8 | 77% → 85% | 2/8 → 5/8 | 4.12 → 4.0 | 0 / 8 / 0 |
| Altitude | 8 | 75% → 83% | 4/8 → 6/8 | 4.25 → 4.0 | 2 / 6 / 0 |
| Guardrail | 8 | 100% → 100% | 8/8 → 8/8 | 4.5 → 4.62 | 4 / 3 / 1 |
| **All** | 40 | 87% → 91% | 25/40 → 32/40 | 4.3 → 4.1 | 8 / 31 / 1 |
