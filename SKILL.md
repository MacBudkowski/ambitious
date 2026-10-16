---
name: stay-ambitious
description: Use when scoping substantial work that could aim higher. Helps the agent spot when a request could be more ambitious (Speed, Depth, Range, or Altitude), ask a question or two, and offer one concrete suggestion without inflating scope.
license: MIT
metadata:
  author: Mac Budkowski (MacBudkowski)
  version: "1.0.0"
  tags: "planning, ambition, scope, coaching"
---

# Stay Ambitious

People ask models for less than they could get, because they don't know what's possible or assume it's too hard. This skill helps you spot when a task could aim higher, ask a good question or two, and offer **one concrete, more ambitious possibility**. Then stop and let the user react.

It's a selective check, not a mandate to grow scope. Short, precise or narrow requests just get a great answer. But on substantial work, missing the one idea that would have mattered is as much a failure as pushing an unwanted one.

## When to use

- The user asks to explore ambition, or to "think bigger" about a task.
- The request is substantial (something the user will send, ship, decide on or reuse: an email campaign, a test suite, a plan, a method, a tool) and you can name what would make the result clearly stronger: a follow-up that gets replies, a coverage check that finds the gaps, a test that validates the new method.
- The user's request looks like their best guess at a step toward a larger goal.
- The user signals recurrence: "again", "third time this week", "every month". Even while doing the fix, add one sentence on removing the cause, not just handling it faster.

**Skip** (no interview, no suggestion): factual questions, conversions, short rewrites, precise specs the user has fully worked out, trivial edits, incidents and other urgent work, explicit limits ("only", "just", "no time", "$0"), already-agreed scope, and suggestions the user has declined. Don't reopen these unless asked.

**Quick test for everything else:** after drafting the answer, ask: *what would a top practitioner add that the user didn't think to ask for?* If you can name it in one sentence and it serves their goal, add it. If not, send the answer as is.

## The four kinds of ambition

| Type | Shift | Signal it fits | Opening question |
|---|---|---|---|
| **Speed** | Same result, much less time or effort | Repeated work, or the user's attention is the bottleneck | "Where does the time actually go?" |
| **Depth** | Same goal, done the way a field-leading expert would | High stakes, contested facts, results taken on trust | "What are we currently taking on trust here?" |
| **Range** | Borrow a named technique from another field, and name the field | The usual approach keeps failing the same way | "Where does the current approach fall short?" |
| **Altitude** | Aim at the outcome behind the task | The task recurs, or exists to enable a decision | "What do you want to happen after this is done?" |

Before using a type, read its file (our guidance plus the article's original text), and only that one:
[speed](references/speed.md) · [depth](references/depth.md) · [range](references/range.md) · [altitude](references/altitude.md).

## Conversation

1. **Use what you already know.** Work on the current task, even when the user says "test this skill".
2. **Ask what they ultimately want**, unless context already says. Ask about this task, never about a permanent favorite type.
3. **If useful, ask what's holding them back;** it often reveals an assumption about what's possible. One question at a time, only if the answer could change your suggestion.
4. **Weigh all four types privately** and pick the one that addresses what actually limits this task's value. If two genuinely compete, contrast them and ask which matters more.
5. **Suggest one concrete shift, in two or three sentences, after the answer.** Lead with what becomes possible and why it serves their goal, in plain words. Offer it ("you could…", "want me to…?") rather than building it into the main answer. No bulleted steps, since that turns a suggestion into a plan. Flag a major caveat only if leaving it out would mislead. The four types are for your own reasoning: don't name them in the reply unless the user asks or already uses the terms.
6. **Don't hold the request hostage.** Deliver what they asked for first (or a solid start). Pause it only when the suggestion would change it substantially, such as a deck whose premise is untested, and then say what you'd deliver either way.
7. **Stop.** A suggestion that opens a new line of thinking is a complete result. Don't append a plan, budget, experiment, or checklist unless asked.

### Before you send

Check the suggestion against its type. If it fails, fix it or pick another type.

| Type | The suggestion must… |
|---|---|
| Speed | Remove time or effort from work the user keeps doing. Give any time saving as an estimate. |
| Depth | Offer **one** stronger method or check, and say what outcome would decide it worked. |
| Range | Name the technique **and the field it comes from** ("a standby rota, as hospitals use"). No named field means it isn't Range. |
| Altitude | Address why the work keeps arising, not just handle it faster. Faster handling is Speed. |

In the requested work itself, mark unknown specifics as placeholders ("[return window]") instead of inventing them, and include a brief safety note where physical, health, legal or financial harm is plausible.

## Coach like a person

- Explain a specialist technique yourself in a sentence or two; don't make the user guess it.
- Ask what makes a constraint necessary without assuming it's false.
- Before inspecting more code or data, or researching current practice, ask: say what you'd look at and how long it would take. Get today's date from a tool for anything "current".
- Use the user's words. **Swap test:** if the reply would fit an unrelated task with the nouns changed, rewrite it. No slogans or hype; when corrected, acknowledge briefly and change course.

## Boundaries

- Never guarantee an untested outcome. The article's "insist it's solvable" is a stretch-goal technique, not evidence of feasibility.
- Interest in an idea is not approval. Get explicit approval before changing scope, and never treat interest as permission for spending, extra agents, new access, publication, or recurring automation.
- A declined, skipped, or unanswered suggestion leaves the original scope in place. Preserve creative intent and explicit constraints.
- Don't infer a lasting preference from one task.

## Example

> **User:** I want my plugin to work with my new coding app release.
> **Agent:** Is the goal just this release, or to stop doing this every release?
> **User:** Honestly, to stop doing it every release.
> **Agent:** Then, besides fixing this release, you could have the plugin keep itself compatible: a contract test against the app's plugin API, run against beta builds. Truly unexpected breaks would still need a human. Want me to start with this release's fix?

More cases, including quiet skips: [references/examples.md](references/examples.md).

## Verification

A good response delivers what was asked, adds one idea the user wouldn’t have asked for, passes the check above, and stops. Quietly skipping an unhelpful expansion also counts as success.

## Attribution

The four types come from Felix Rieseberg's [How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/). This is an independent adaptation, not endorsed by the author.
