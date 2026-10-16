# Ambitious

**An agent skill that helps you ask AI for more than you would have thought to.**

*(Based on Felix Rieseberg's essay [How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/))*

Most people ask a model for the task in front of them: fix this crash, write this email, make this deck. They rarely ask for what they actually want: an app that stays crash-free, a meeting with the right person, leaders who catch problems early. Usually not because it's impossible, but because it didn't occur to them.

Ambitious shows you **bolder versions of your own request**, as prompts you can send right away. It asks a few questions if it needs to, finds the goal behind your goal, and gives you a ladder of 2–3 prompts that climb from "a better version" to "the thing the essay means". You pick one, or keep your original.

## What it looks like

> **You:** /ambitious I need my plugin to work with the new host release. Honestly I'm tired of fixing this every release.
>
> **Agent:** **The goal behind the goal:** You want your plugin to survive host releases without another repair job landing on you.
>
> **1. Fix this release—and explain the recurring breakage**
>
> > "Get my plugin working with the new host release. Compare this failure with previous compatibility fixes, identify what keeps breaking, and add tests that reproduce those failures."
>
> *Needs:* Plugin source, old and new host versions, previous fixes or bug reports.
> *Check:* Tests reproduce the failures before the fix; the plugin's affected features work in the actual new host afterward.
>
> **2. Make host upgrades a tested event, not a repair project**
>
> > "Stop patching host-version assumptions throughout my plugin. Use our history of breakages to design a small compatibility boundary, migrate the affected code, and test it against supported host versions and available prereleases. Show that the checks would have caught our previous failures."
>
> *Needs:* Repository history, runnable host versions, a defined support range, and CI access.
> *Check:* Historical failures are caught by the tests; real-host checks pass across the supported versions.
>
> **3. Take release compatibility off my plate**
>
> > "Build a compatibility-maintenance workflow for my plugin: detect new host releases and prereleases, run realistic plugin checks, reproduce regressions, and prepare tested fixes before users hit them. Bring me only decisions that require changing plugin behavior or dropping support. Prove it against past breaking releases, then run it alongside my current process for one release cycle."
>
> *Needs:* Release feeds, repeatable host test environments, CI and repository access, plus an agreed automation budget and approval boundaries.
> *Check:* Replay past releases to measure which breakages it catches; during the live cycle, track missed regressions and how often you still have to intervene.
>
> Pick one and I'll start, or keep the original.

A real reply from a live test of the current skill.

## How it works

1. **You ask for it** (`/ambitious`, "think bigger", "how could I be more ambitious with this"), or the agent offers once, in one line, when you're planning something substantial.
2. **It asks a few questions** if the goal, audience or limits are unclear, so the bolder versions fit what you actually want.
3. **It shows the ladder:** the goal behind your goal, then 2–3 ready-to-send prompts, each clearly bigger than the last. Each says what it needs (access, data, tools) and how you'd know it worked (an outside check, not the model grading itself). When a real precedent fits, it cites one: "someone already did this".
4. **You pick.** It doesn't do the task until you choose. No draft, no critique of your idea, just bolder options.

## Four kinds of ambition

From the essay:

| Type | The bolder ask | Example |
|---|---|---|
| **Altitude** | Ask for the outcome, not the task | Stop fixing crashes one by one; ask for the app to stay crash-free |
| **Depth** | Ask for it done the way the best in the field would | Test "churn is an onboarding problem" against raw logs; set a 200 ms target instead of 5 s |
| **Range** | Ask for methods from other fields | Redesign a shift handoff with nursing's SBAR and aviation's read-back |
| **Speed** | Ask for the same result in a fraction of the time | A 2-hour Monday chore that runs itself, with the same checks |

## Install

The skill is a plain folder of Markdown in the open [Agent Skills](https://agentskills.io/specification) format, with no dependencies, API keys or background services.

- **Agents with skill support:** copy the `ambitious` folder into your agent's skills directory (for example `~/.claude/skills/` for Claude Code), then start a new session.
- **Agents without skill support:** add `SKILL.md` to the system prompt or project instructions, with `references/` alongside if the agent can read files.

### Optional: let the agent offer it

Add this to your standing instructions:

> For substantial work, you may offer the `ambitious` skill's ambition pass once, in one line. Run it only if the user says yes. Don't offer it for quick questions, urgent work or explicitly narrow requests.

## What's inside

```
SKILL.md               The ambition pass: when to run it, questions, the ladder
references/
  altitude.md          How to build each type's ladder, plus the essay's
  depth.md               original text for that type only
  range.md
  speed.md
  examples.md          Full example passes, and when not to offer
  precedents.md        20 real, sourced cases of ambitious work with AI
  source-notice.md     Rights and attribution for the quoted essay text
evals/                 Earlier automated evaluation and a blind-ranking page
tests/test_package.py  Structural checks (files, links, frontmatter, quote integrity)
```

## How it was built

This skill went through two designs. The first (git tag `v1.0.0-suggest`) had the agent add one short suggestion after answering; it tested well against an automated judge but felt timid in real use. An independent review pointed out why: the judge rewarded restraint, and the essay is about *you* asking for more, not the agent adding a tip. The current design came from trying it by hand on real tasks and adjusting after each try. The earlier evaluation data is kept in `evals/` for reference.

## Credits

Created by [Mac Budkowski](https://github.com/MacBudkowski). The four-type framework is from Felix Rieseberg's essay, linked above. This is an independent adaptation, not endorsed by the author.

## License

MIT for this package's original content; see [LICENSE](LICENSE). Quoted essay text is excluded; see [references/source-notice.md](references/source-notice.md).
