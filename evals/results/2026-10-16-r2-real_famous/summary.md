# Evaluation summary

- Date: 2026-10-16
- Subject model: `claude-sonnet-5-5` · Judge model: `claude-opus-5-5`
- Scenario file: `real_famous.json` · Scenarios: 30 · Reps: 2 · Subject calls: 84

| Group | Cases | Criteria passed (baseline → skill) | All criteria met (baseline → skill) | Usefulness 1–5 (baseline → skill) | Head-to-head (skill / baseline / tie) |
|---|---|---|---|---|---|
| Depth | 8 | 89% → 82% | 5/8 → 3/8 | 3.88 → 4.12 | 6 / 1 / 1 |
| Altitude | 6 | 88% → 88% | 3/6 → 3/6 | 3.33 → 3.33 | 5 / 1 / 0 |
| Guardrail | 28 | 87% → 94% | 20/28 → 23/28 | 4.0 → 4.21 | 14 / 10 / 4 |
| **All** | 42 | 88% → 91% | 28/42 → 29/42 | 3.88 → 4.07 | 25 / 12 / 5 |
