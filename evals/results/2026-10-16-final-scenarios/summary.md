# Evaluation summary

- Date: 2026-10-16
- Subject model: `claude-sonnet-5-5` · Judge model: `claude-opus-5-5`
- Scenario file: `scenarios.json` · Scenarios: 18 · Reps: 2 · Subject calls: 72

| Group | Cases | Criteria passed (baseline → skill) | All criteria met (baseline → skill) | Usefulness 1–5 (baseline → skill) | Head-to-head (skill / baseline / tie) |
|---|---|---|---|---|---|
| Speed | 6 | 95% → 100% | 5/6 → 6/6 | 4.5 → 4.67 | 6 / 0 / 0 |
| Depth | 6 | 100% → 100% | 6/6 → 6/6 | 4.83 → 4.67 | 1 / 5 / 0 |
| Range | 6 | 59% → 96% | 0/6 → 5/6 | 4.0 → 4.67 | 4 / 2 / 0 |
| Altitude | 6 | 70% → 95% | 1/6 → 5/6 | 3.17 → 4.17 | 5 / 1 / 0 |
| Guardrail | 12 | 92% → 100% | 10/12 → 12/12 | 3.92 → 3.92 | 6 / 4 / 2 |
| **All** | 36 | 84% → 98% | 22/36 → 34/36 | 4.06 → 4.33 | 22 / 12 / 2 |
