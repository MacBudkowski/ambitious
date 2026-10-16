# Evaluation summary

- Date: 2026-10-16
- Subject model: `claude-sonnet-5-5` · Judge model: `claude-opus-5-5`
- Scenario file: `holdout3.json` · Scenarios: 20 · Reps: 2 · Subject calls: 80

| Group | Cases | Criteria passed (baseline → skill) | All criteria met (baseline → skill) | Usefulness 1–5 (baseline → skill) | Head-to-head (skill / baseline / tie) |
|---|---|---|---|---|---|
| Speed | 8 | 65% → 88% | 2/8 → 5/8 | 3.88 → 4.25 | 3 / 5 / 0 |
| Depth | 8 | 93% → 93% | 6/8 → 6/8 | 4.5 → 4.5 | 7 / 1 / 0 |
| Range | 8 | 53% → 84% | 0/8 → 3/8 | 3.75 → 4.12 | 7 / 1 / 0 |
| Altitude | 8 | 64% → 79% | 2/8 → 2/8 | 4.0 → 4.0 | 8 / 0 / 0 |
| Guardrail | 8 | 96% → 100% | 7/8 → 8/8 | 4.62 → 4.62 | 3 / 2 / 3 |
| **All** | 40 | 74% → 89% | 17/40 → 24/40 | 4.15 → 4.3 | 28 / 9 / 3 |
