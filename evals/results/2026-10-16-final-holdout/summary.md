# Evaluation summary

- Date: 2026-10-16
- Subject model: `claude-sonnet-5-5` · Judge model: `claude-opus-5-5`
- Scenario file: `holdout.json` · Scenarios: 20 · Reps: 2 · Subject calls: 80

| Group | Cases | Criteria passed (baseline → skill) | All criteria met (baseline → skill) | Usefulness 1–5 (baseline → skill) | Head-to-head (skill / baseline / tie) |
|---|---|---|---|---|---|
| Speed | 8 | 85% → 100% | 4/8 → 8/8 | 3.88 → 4.12 | 6 / 2 / 0 |
| Depth | 8 | 93% → 100% | 6/8 → 8/8 | 4.25 → 4.62 | 6 / 1 / 1 |
| Range | 8 | 85% → 96% | 4/8 → 7/8 | 4.12 → 4.88 | 5 / 3 / 0 |
| Altitude | 8 | 79% → 100% | 5/8 → 8/8 | 4.25 → 4.88 | 8 / 0 / 0 |
| Guardrail | 8 | 92% → 100% | 6/8 → 8/8 | 4.5 → 4.88 | 7 / 0 / 1 |
| **All** | 40 | 87% → 99% | 25/40 → 39/40 | 4.2 → 4.67 | 32 / 6 / 2 |
