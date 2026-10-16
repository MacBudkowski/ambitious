# Stay Ambitious

**An agent skill that helps you ask AI for more than you would have thought to.**

*(Based on Felix Rieseberg's essay [How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/))*

Most people ask a model for the task in front of them: fix this crash, make this deck, rewrite this guide. They rarely ask for what they actually want, such as an app that stays crash-free, leaders who catch problems early, or users who stop getting lost. That's usually not because it's impossible. It's because nobody suggested it.

Stay Ambitious teaches your agent to notice those moments, ask one or two good questions, and offer **one concrete, more ambitious possibility**. Then it stops and lets you decide. It doesn't make every task bigger, and it stays quiet when a task should simply be done.

## What it looks like

> **You:** I need my plugin to work with the new host release. Honestly I'm tired of fixing this every release.
>
> **Without the skill:** a five-step general guide to plugin compatibility (adapter layer, public APIs, feature detection, CI, version ranges…).
>
> **With the skill:** "Since you want to stop fixing this every release, you could aim for the plugin to stay compatible on its own: a small contract test suite for exactly the host APIs your plugin depends on, run automatically against the host's beta builds, so a breaking change shows up as a failing test before the release ships. It depends on the host publishing pre-release builds. Want me to start with the fix for this release?"

Both are real responses from the [evaluation](#does-it-work) (lightly trimmed).

## Four kinds of ambition

The four types, from the essay:

| Type | The shift | Example |
|---|---|---|
| **Speed** | Same result, much less time or effort | A day-long weekly report becomes an hour, with the same checks |
| **Depth** | Same goal, done the way a field-leading expert would | Test "churn is an onboarding problem" against raw logs before spending a quarter on it |
| **Range** | Borrow a concrete technique from another field | Run a usability *cognitive walkthrough* on a guide users keep misreading |
| **Altitude** | Aim at the outcome behind the task | Stop fixing crashes one by one; aim for keeping the app crash-free |

## Does it work?

We tested it the way you'd test any change: the same prompts sent to a fresh model with and without the skill. A separate judge model scored each reply against that prompt's criteria without knowing which version wrote it, then picked the better of the two in random order. Each set has at least four cases per ambition type, plus "guardrail" cases where the right move is *not* to expand scope.

<!-- EVAL_TABLE_START -->
Latest run: `claude-sonnet-5-5` answering, `claude-opus-5-5` judging, every prompt run twice with and twice without the skill (312 replies).

| Test set | Written by | Criteria passed (without → with) | All criteria met | Head-to-head (skill / without / tie) |
|---|---|---|---|---|
| Held-out set 3 (20 × 2) | Separate agent; never used for tuning | 74% → **89%** | 17/40 → **24/40** | 28 / 9 / 3 |
| Held-out set 2 (20 × 2) | Separate agent; used for one tuning round | 80% → **96%** | 19/40 → **34/40** | 26 / 10 / 4 |
| Held-out set 1 (20 × 2) | Separate agent; used for tuning | 89% → **98%** | 28/40 → **37/40** | 27 / 13 / 0 |
| Author scenarios (18 × 2) | Written alongside the skill | 80% → **98%** | 20/36 → **34/36** | 23 / 11 / 2 |

**How to read this:**

- **Trust the top row most.** Set 3 was written by an agent that never saw the skill, and no change was made in response to it. There, the skill raises criteria met from 74% to 89%, and the judge prefers its reply 28 times out of 40 (9 for the plain model, 3 ties).
- **It helps across every type.** The biggest gains are Range and Speed, ideas models rarely offer unprompted. Guardrails held throughout: no scope creep on a 10-minute deadline, a $0 budget, a pure factual question, emergencies, or personal creative work.
- **Known gaps** (from set 3): the extra idea sometimes grows into several ideas or a long paragraph; Range sometimes uses a borrowed technique without naming its field; Altitude sometimes targets a nearby problem rather than the recurring one.
- **What we changed along the way.** Earlier versions withheld the requested work and labelled ideas with framework terms ("That's an Altitude shift"), which judges read as jargon. Removing the label alone moved the head-to-head on set 1 from 9 to 28 wins out of 40 (`evals/rejudge_without_label.py`). Later rounds added a pre-send check per type, placeholders instead of invented facts, and safety notes where harm is plausible.

One model pairing is evidence, not proof. Every reply and verdict is in [`evals/results/`](evals/results/).
<!-- EVAL_TABLE_END -->

Re-run it yourself on any OpenAI-compatible endpoint:

```sh
EVAL_BASE_URL=<openai-compatible-endpoint>/v1 \
EVAL_SUBJECT_MODEL=<model> EVAL_JUDGE_MODEL=<different-or-stronger-model> \
python3 evals/run_eval.py --scenarios evals/holdout3.json --reps 2 --out evals/results/my-run
```

## Install

The skill is a plain folder of Markdown in the open [Agent Skills](https://agentskills.io/specification) format. It has no dependencies, API keys, tools or background services, so it works with any agent that can load skills, or with any model if you paste it in.

- **Agents with skill support:** copy the `stay-ambitious` folder into your agent's skills directory (for example `~/.claude/skills/` for Claude Code), then start a new session. Check your agent's documentation for its skills location.
- **Agents without skill support:** add `SKILL.md` to the system prompt or project instructions. Keep `references/` alongside it if the agent can read files, or paste in the one type you care about.

Only the main file is needed to start. The `references/` files load on demand, one ambition type at a time.

### Optional: let the agent check on its own

Skills load when a task matches their description. To make the check more dependable, add this to your standing instructions:

> Before agreeing scope for substantial work, load the `stay-ambitious` skill and consider whether Speed, Depth, Range, or Altitude would materially help. Skip trivial, urgent, explicitly narrow, or already-agreed tasks.

This is an instruction, not a guaranteed hook; the agent still decides.

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
  scenarios.json       18 author-written test cases with pass criteria
  holdout*.json        Three independent sets of 20, written without seeing the skill
  run_eval.py          With/without-skill runner and blind judge (stdlib only)
  rejudge_without_label.py  Diagnostic used to measure the cost of type labels
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

Created by [Mac Budkowski](https://github.com/MacBudkowski). The four-type framework is from Felix Rieseberg's essay, linked above. This is an independent adaptation, not endorsed by the author.

## License

MIT for this package's original content; see [LICENSE](LICENSE). Quoted article text is excluded; see [references/source-notice.md](references/source-notice.md).
