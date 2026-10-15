# Ambition Check

A portable AI-agent skill for choosing the right kind of ambition **for the task**: Speed, Depth, Range, or Altitude.

It helps an agent ask a short, relevant mini-interview, expose meaningful tradeoffs, and propose a stronger approach without automatically inflating scope. It can also decide that the original task is already right.

## What it does

1. Read context and identify what limits the value of the task.
2. Ask only missing questions (usually 2–3, not a mandatory form).
3. Recommend one direction, or contrast two when the tradeoff is unresolved.
4. Suggest a concrete possibility, briefly name its type, and flag any major caveat.
5. Let the user react. Planning and execution come later, if requested.

No API keys, background services, model-specific features, or additional agents are required. The procedure is portable; discovery and automatic loading depend on your agent host. Compatibility with other hosts has not been runtime-tested.

## Install in Hermes

Copy this directory into `<active-profile-home>/skills/ambition-check/`. Use the active profile, not another profile's directory. Start a new session for reliable discovery. You can invoke `/ambition-check` explicitly.

For selective automatic use, add this trigger to your existing standing instructions:

> Before agreeing scope for substantial work, load `ambition-check` and assess whether Speed, Depth, Range, or Altitude would materially improve the result. Follow its task-specific interview and approval process when useful. Skip trivial, urgent, explicitly narrow, and already-agreed tasks unless explicitly asked to reconsider them.

This is instruction-driven loading, not a plugin or guaranteed runtime hook. The skill itself does not edit your configuration.

## Other agents

Use your host's documented skill installation mechanism for the root `SKILL.md` and its companion files. If it has no skill loader, supply `SKILL.md` as task context. Do not assume the Hermes slash command works elsewhere.

## Examples and evaluation

Read [examples.md](examples.md). Behavioral cases and pass/fail criteria live in [evals/scenarios.json](evals/scenarios.json).

Run structural checks from this directory:

```sh
python3 -m unittest discover -s tests -v
```

These tests check packaging and required text, **not model behavior**. For behavioral evaluation, provide each scenario to an agent with and without the skill in fresh sessions, record its response, and judge it against every criterion. Compare on the same model and settings. Do not call scenarios passed until actual responses have been inspected. No model evaluation results are bundled in this initial release.

## Files

- `SKILL.md`: portable procedure and safeguards
- `examples.md`: task-specific applications
- `evals/scenarios.json`: behavioral evaluation cases
- `tests/test_package.py`: dependency-free structural checks
- `LICENSE`: MIT license for this original adaptation

## Attribution

Inspired by Felix Rieseberg's [How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/), which introduces Speed, Altitude, Depth, and Range. This repository contains an independent adaptation, not a copy of the article. The MIT license does not relicense the source article. No affiliation or endorsement is implied.

Created by [Mac Budkowski](https://github.com/MacBudkowski), with Hermes Agent.

## Source quotations and publication

`references/article-excerpts.md` preserves the supplied four definitions and full Altitude, Depth, and Range sections verbatim, with attribution. Speed has only a brief treatment in the original article, preserved here. These quotations are excluded from the MIT license. Before publishing the quoted reference, resolve permission for redistribution or use a link-based edition. The original article and our interview guidance are separate sources; consult both when applying a named category.
