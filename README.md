# Ambitious

**An agent skill that helps you ask AI for more than you would have thought to.**

*(Based on Felix Rieseberg's essay [How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/))*

Most people ask a model for the task in front of them: fix this crash, write this email, make this deck. They rarely ask for what they actually want: an app that stays crash-free, a meeting with the right person, leaders who catch problems early. Usually not because it's impossible, but because it didn't occur to them.

Ambitious shows you **bolder versions of your own request**, as prompts you can send right away. It asks a few questions if it needs to, finds the goal behind your goal, and gives you a ladder of 2–3 prompts that climb from "a better version" to "the thing the essay means". You pick one, or keep your original.

## What it looks like

> **You:** /ambitious cold email to Revolut's VP of Engineering about our code-review tool. It's faster and better for AI agents. I want a short meeting.
>
> **Agent:** **The goal behind the goal:** a meeting where Revolut sees your tool working on their kind of agent code, not another vendor email.
>
> 1. > "Research Revolut's public engineering blog, talks and job posts for how they use AI coding agents, then write a 90-word email to their VP of Engineering that opens with one real, cited observation and asks for 15 minutes."
>    *Needs:* web access, one proof point. *Check:* every claim about Revolut links to a source.
> 2. > "Run our tool and a standard reviewer on 50 agent-generated pull requests from public fintech repos, measure review time and real bugs caught, and write the email around that one striking number."
>    *Needs:* the tool, a sandbox, public repos. *Check:* bugs confirmed by a human reviewer, not the tool.
> 3. > "Publish an open benchmark of code review for AI-agent pull requests, with a personalised run on a Revolut open-source repo, then design a 30-account outreach sequence led by that benchmark."
>    *Needs:* the tool, compute, a target list. *Check:* meeting rate per 30 sends vs. current outreach.
>
> Pick one and I'll start, or keep the original.

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
