# Stay Ambitious

**An agent skill that helps you ask AI for more than you would have thought to.**

Most people ask a model for the task in front of them: fix this crash, make this deck, rewrite this guide. They rarely ask for what they actually want, such as an app that stays crash-free, leaders who catch problems early, or users who stop getting lost. That's usually not because it's impossible. It's because nobody suggested it.

Stay Ambitious teaches your agent to notice those moments, ask one or two good questions, and offer **one concrete, more ambitious possibility**. Then it stops and lets you decide. It doesn't make every task bigger, and it stays quiet when a task should simply be done.

## What it looks like

> **You:** I need my plugin to work with the new host release. Honestly I'm tired of fixing this every release.
>
> **Without the skill:** a five-step general guide to plugin compatibility (adapter layer, public APIs, feature detection, CI, version ranges…).
>
> **With the skill:** "Since you want to stop fixing this every release, you could aim for the plugin to stay compatible on its own: a small contract test suite for exactly the host APIs your plugin depends on, run automatically against the host's beta builds, so a breaking change shows up as a failing test before the release ships. That's **Altitude** ambition: going after the outcome behind the task (a plugin that keeps working) rather than the individual fix. It depends on the host publishing pre-release builds. Want me to start with the fix for this release?"

Both are real responses from the [evaluation](#does-it-work) (lightly trimmed).

## Four kinds of ambition

Based on Felix Rieseberg's essay [*How to be more ambitious: A tutorial for humans with models*](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/):

| Type | The shift | Example |
|---|---|---|
| **Speed** | Same result, much less time or effort | A day-long weekly report becomes an hour, with the same checks |
| **Depth** | Same goal, done the way a field-leading expert would | Test "churn is an onboarding problem" against raw logs before spending a quarter on it |
| **Range** | Borrow a concrete technique from another field | Run a usability *cognitive walkthrough* on a guide users keep misreading |
| **Altitude** | Aim at the outcome behind the task | Stop fixing crashes one by one; aim for keeping the app crash-free |

## Does it work?

We ran 18 scenarios through a fresh model twice, once without the skill and once with it. There are three or more per ambition type, plus "guardrail" cases where the right move is to *not* expand scope. A separate judge model scored every reply against the scenario's criteria without knowing which version wrote it, then picked a winner head-to-head in random order.

<!-- EVAL_TABLE_START -->
Latest run (`claude-sonnet-5-5` answering, `claude-opus-5-5` judging, 18 scenarios, 1 rep each):

| Group | Cases | Criteria passed (baseline → skill) | All criteria met (baseline → skill) | Usefulness 1–5 (baseline → skill) | Head-to-head (skill / baseline / tie) |
|---|---|---|---|---|---|
| Speed | 3 | 100% → 100% | 3/3 → 3/3 | 4.33 → 4.0 | 1 / 2 / 0 |
| Depth | 3 | 82% → 100% | 1/3 → 3/3 | 4.0 → 4.0 | 1 / 2 / 0 |
| Range | 3 | 55% → 91% | 0/3 → 2/3 | 4.0 → 3.67 | 0 / 3 / 0 |
| Altitude | 3 | 50% → 100% | 0/3 → 3/3 | 3.0 → 3.67 | 1 / 2 / 0 |
| Guardrail | 6 | 92% → 100% | 5/6 → 6/6 | 4.17 → 4.17 | 3 / 3 / 0 |
| **All** | 18 | 76% → 98% | 9/18 → 17/18 | 3.94 → 3.94 | 6 / 12 / 0 |

**How to read this:**

- **The skill reliably does its job.** With it, replies met every criterion in 17 of 18 scenarios, against 9 of 18 without it. The biggest gains are in Altitude, Depth and Range, which a model rarely brings up on its own. Guardrails held: no scope creep on typos, incidents, declined ideas or poems.
- **A generic judge still often prefers the baseline head-to-head (12 of 18).** When asked only "which reply is more useful?", the judge tends to reward the longer, more complete deliverable. The skill deliberately offers one idea and stops. Whether that trade is right for you is a judgment call; this number is reported rather than hidden.
- **Iterations so far.** Earlier runs (`results/2026-10-16-v1`, `-v2`) showed the skill withholding the requested work and using bare labels like "That's an Altitude shift". Both were fixed: the skill now delivers or offers the original request, and names the type with a plain explanation beside it.

One run on one model pairing is evidence, not proof. Re-run with `--reps 3` for tighter numbers.
<!-- EVAL_TABLE_END -->

Full replies and per-criterion verdicts are in [`evals/results/`](evals/results/). Re-run it yourself:

```sh
EVAL_BASE_URL=<openai-compatible-endpoint>/v1 \
EVAL_SUBJECT_MODEL=<model> EVAL_JUDGE_MODEL=<different-or-stronger-model> \
python3 evals/run_eval.py --reps 3 --out evals/results/my-run
```

## Install

The skill is plain Markdown with no dependencies, API keys or background services.

**Hermes Agent:** copy this folder to `~/.hermes/skills/stay-ambitious/` (or your active profile's `skills/` directory) and start a new session. Invoke it with `/stay-ambitious`.

**Claude Code:** copy it to `~/.claude/skills/stay-ambitious/` (personal) or `.claude/skills/stay-ambitious/` (per project).

**Other agents:** use your host's skill loader for `SKILL.md` and its `references/` folder. If your host has no skill loader, paste `SKILL.md` into the system prompt or project instructions. Only Hermes has been tested.

### Optional: let the agent check on its own

Skills load when a task matches their description. To make the check more dependable, add this to your standing instructions:

> Before agreeing scope for substantial work, load the `stay-ambitious` skill and consider whether Speed, Depth, Range, or Altitude would materially help. Skip trivial, urgent, explicitly narrow, or already-agreed tasks.

This is an instruction, not a guaranteed hook. The agent still decides.

## What's inside

```
SKILL.md               The procedure: when to use, how to interview, when to stop
references/
  speed.md             How to apply each type, plus the article's original text
  depth.md               for that type only, so an agent loads just what it needs
  range.md
  altitude.md
  examples.md          Same request with four different answers; quiet skips
  source-notice.md     Rights and attribution for the quoted article text
evals/
  scenarios.json       18 behavioral test cases with pass criteria
  run_eval.py          With/without-skill runner and blind judge (stdlib only)
  results/             Recorded runs: raw replies, verdicts, summary
tests/test_package.py  Structural checks (files, links, frontmatter, quote integrity)
```

Run the structural checks with `python3 -m unittest discover -s tests -v`. They check the package, not model behavior; the evaluation covers behavior.

## Design principles

- **One suggestion, then stop.** A good idea that opens a new line of thinking is the whole deliverable. Plans come later, if you want them.
- **Selective, not inflationary.** Bigger isn't better. Typos, incidents, declined ideas and creative work keep their scope.
- **Coach, don't quiz.** The agent brings the specialist knowledge. You shouldn't have to guess which technique it's thinking of.
- **Interest is not approval.** No extra spending, access, agents or automation without an explicit yes.
- **Author's words, loaded on demand.** Each type's file includes the essay's original text for that type only.

## Credits

Created by [Mac Budkowski](https://github.com/MacBudkowski) with Hermes Agent. The four-type framework is from Felix Rieseberg's essay, linked above. This is an independent adaptation, not endorsed by the author.

## License

MIT for this package's original content; see [LICENSE](LICENSE). Quoted article text is excluded; see [references/source-notice.md](references/source-notice.md).
