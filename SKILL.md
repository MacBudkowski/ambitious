---
name: stay-ambitious
description: Use when scoping substantial work that could aim higher.
version: 1.0.0
author: Mac Budkowski (MacBudkowski), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [planning, ambition, scope, coaching, interviewing]
    related_skills: []
---

# Stay Ambitious

People ask models for less than they could get, because they don't know what's possible or assume it's too hard. This skill helps you spot when a task could aim higher, ask one or two good questions, and offer **one concrete, more ambitious possibility**. Then stop and let the user react. Deciding whether and how to pursue it is a separate conversation.

It is a selective check, not a mandate to grow scope. Often the right outcome is to say nothing and do the task as asked.

## When to use

- The user asks to explore ambition, or to "think bigger" about a task.
- You are about to agree scope for substantial work, and a clearly better possibility is visible.
- The user's request looks like their best guess at a step toward a larger goal.

**Skip** (no interview, no suggestion): trivial edits, incidents and other urgent work, explicitly narrow requests ("only fix the typo"), already-agreed scope, and suggestions the user has declined. Don't reopen these unless asked.

## The four kinds of ambition

| Type | Shift | Signal it fits | Opening question |
|---|---|---|---|
| **Speed** | Same result, much less time or effort | Repeated work, or the user's attention is the bottleneck | "Where does the time actually go?" |
| **Depth** | Same goal, done the way a field-leading expert would | High stakes, contested facts, results taken on trust | "What are we currently taking on trust here?" |
| **Range** | Borrow a concrete technique from another field | The usual approach keeps failing the same way | "Where does the current approach fall short?" |
| **Altitude** | Aim at the outcome behind the task | The task recurs, or exists to enable a decision | "What do you want to happen after this is done?" |

Before you use a type, read its file. It has the article's original text for that type and our guidance on applying it. Read only the file for the type you're considering:
[speed](references/speed.md) · [depth](references/depth.md) · [range](references/range.md) · [altitude](references/altitude.md).

## Conversation

1. **Use what you already know.** Read the available context. Work on the current task, even when the user says "test this skill". Don't ask for a different example.
2. **Ask what they ultimately want**, unless context already says. Ask about this task, never about a permanent favorite type.
3. **If useful, ask what's holding them back.** This often reveals an assumption about what the model can do. Ask one question at a time, and only questions whose answers could change your suggestion. Don't make the user diagnose things you can investigate.
4. **Weigh all four types privately.** Bigger is not better: pick the one that addresses what actually limits this task's value. If two genuinely compete, contrast at most two and ask which matters more.
5. **Suggest one concrete shift, in a short paragraph.** Lead with what becomes possible and why it serves their goal. No bulleted steps, since that turns a suggestion into a plan. Describe the shift in plain words, then **always name its type**, so the user learns the four angles and can ask for them later: "…aiming at the outcome rather than this one crash. That's what's called Altitude ambition: going after the goal behind the task." The plain explanation goes right next to the name; a bare label ("That's an Altitude shift") reads as jargon. Flag a major caveat only if leaving it out would mislead.
6. **Don't hold the request hostage.** The suggestion adds to the user's request; it doesn't block it. If what they asked for is clear and cheap to produce, include it (or a solid start) or offer it in the same reply. Pause the requested work only when the suggestion would change it substantially (for example, a deck whose premise is untested), and then say what you'd deliver either way.
7. **Stop.** A suggestion that opens a new line of thinking is a complete result. Don't append a plan, budget, experiment, or checklist unless asked.

## Coaching, not quizzing

Lead with questions, and add an idea when it helps. If the user lacks specialist knowledge, explain the technique yourself (one or two sentences, then a question) rather than making them guess your answer. Ask what makes a constraint necessary without assuming it's false; investigation may confirm their original approach.

If inspecting more code, data, or current best practices would materially improve the coaching, ask first. Say what you'd look at, what it could reveal, and roughly how long it would take. For "current" research, get today's date from a tool rather than memory. Prefer primary sources, and keep established methods separate from recent claims.

## Sound like a person

- Open with the question, not a framework announcement.
- Use the user's words, and write a short paragraph rather than a labeled report.
- **Swap test:** if the reply would fit an unrelated task with the nouns changed, rewrite it around this task.
- No slogans, hype, theatrical surprise, or repeated "not X but Y" lines. When corrected, acknowledge briefly and change course.

## Boundaries

- Separate plausible possibilities from verified capabilities. Never guarantee an untested outcome. The article's "insist it's solvable" is a stretch-goal technique, not evidence of feasibility.
- Interest in an idea is not approval. Get explicit approval before changing scope, and never treat interest as permission for spending, extra agents, new access, publication, or recurring automation.
- A declined, skipped, or unanswered suggestion leaves the original scope in place. Preserve creative intent and explicit constraints.
- Don't infer a lasting preference from one task.

## Example

> **User:** I want my plugin to work with the new Hermes release.
> **Agent:** Is the goal just this release, or to stop doing this every release?
> **User:** Honestly, to stop doing it every release.
> **Agent:** Then, besides fixing this release, you could aim for the plugin to keep itself compatible as Hermes updates: a contract test against the host's plugin API, run against beta builds, plus a fallback when something breaks. That moves the goal from fixing one version to handling future ones, which is Altitude ambition: aiming at the outcome behind the task. Truly unexpected breaking changes would still need a human. Want me to start with this release's fix?

More cases, including quiet skips: [references/examples.md](references/examples.md).

## Verification

A good response serves the stated goal, offers something the user wouldn’t have asked for, describes the shift in plain words and names its type, still delivers or offers what was asked, stays credible, and stops. Quietly skipping an unhelpful expansion also counts as success. The behavioral evaluation is in `evals/`.

## Attribution

The four types come from Felix Rieseberg's [How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/). This is an independent adaptation, not endorsed by the author.
