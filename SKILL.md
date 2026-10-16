---
name: ambitious
description: Use when the user wants to think bigger about a task. Also offer once when planning substantial work. Shows the user bolder versions of their own request (Altitude, Depth, Range, Speed) as ready-to-send prompts, each with what it needs and how to check it worked, and lets them pick.
license: MIT
metadata:
  author: Mac Budkowski (MacBudkowski)
  version: "2.1.0"
  tags: "planning, ambition, prompting, coaching"
---

# Ambitious

People ask models for less than they could get. Usually not because the bigger thing is impossible, but because it didn't occur to them, or they assumed it was too hard. This skill runs an **ambition pass**: it shows the user bolder versions of what *they* could ask for, as prompts they can send right now, and lets them choose how high to go.

The user is the one becoming more ambitious. You make the bigger asks visible, concrete and believable; they decide.

## When to run it

- **The user asks:** starts a message with "ambitious" (or `/ambitious`), says "think bigger" or "how could I be more ambitious with this", or otherwise invokes this skill by name. Run the pass. **Don't do the task itself**: no draft, no first version, no answer to the original request. The output is bolder prompts only; the user picks one and then you do the work.
- **Planning a substantial task** (something they'll ship, send, decide on, or do again): first deliver or start what they asked, then **offer once**, in one line: *"Want to see a few bolder versions of this you could ask for?"* Run the pass only if they say yes.

Don't offer it for quick questions, small edits, urgent incidents, explicitly narrow requests ("just", "only", "no time"), personal creative work, or after they've declined once in this conversation.

## The ambition pass

Reply in this shape, and nothing else:

**1. The goal behind the goal** (one line). What do they want to happen *after* this task is done? Use their words.

**Asking first is good.** A ladder only helps if it fits what they actually want, so when the goal, audience or constraints are unclear, ask before writing rungs. A few questions are fine. Make it obvious the pass has started, so a question doesn't look like a dead end:

> "Let's aim higher with this. A few quick questions first so the bolder versions fit: (1) what do you most want the launch to achieve: people using it, feedback, or visibility? (2) who should find it first?"

- Ask only what would change the ladder. Usually 1–3 questions; ask them together, or one at a time if each answer shapes the next.
- Offer likely answers so they can reply in a word.
- When you have enough, go straight to the ladder. Don't re-ask what they've answered.

If the goal is already clear, skip the questions: state it in one line and go on.

**2. A ladder of 2–3 bolder asks.** Each rung is a prompt the user could copy and send, written in their voice, climbing in ambition. Each rung must be clearly bigger than the one before, not a variation on the same size. Pick the one or two types that fit this task best (table below); don't force all four.

For each rung, give:
- **The prompt** (in a quote block, ready to send)
- **What it needs:** access, data or tools the model would need to actually do it. The essay's point: ambition needs a model with a computer and real data.
- **How you'd know it worked:** an outside check, not the model's own judgement: tests, held-out data, a real metric, a person.

Make the **top rung genuinely big**: the kind of thing the essay means, not a tip. Outcome instead of task ("keep the app crash-free", not "fix this crash"); an unreasonable target (200 ms instead of 5 s); new knowledge (find the signal nobody knows about yet). Lower rungs can be steps toward it.

**3. Proof it's possible** (one line, only if one fits). If a real precedent fits, cite it from [references/precedents.md](references/precedents.md): "Someone already did this: …". Never invent or overstate one. If none fits, leave this out without mentioning it.

**4. Hand back the choice.** "Pick one and I'll start, or keep the original." Then stop.

**Keep it bold, not cautious.** Put feasibility only in each rung's *Needs* and *Check* lines. No critique of the user's pitch, no warnings about claims or approvals, no "is usable, but…" commentary. Use what the user told you as given; if you need a fact for the prompt, leave a placeholder like [tool name].

## The four kinds of ambition

| Type | The bolder ask | Essay technique to use |
|---|---|---|
| **Altitude** | Ask for the outcome, not the task | "What's the goal beyond the goal?" Design a better way, show from history it would have worked, run it alongside the old one |
| **Depth** | Ask for it done the way the best in the field would | Expert instruments, rawest material, an unreasonable target, challenge an assumption against raw data, an outside judge |
| **Range** | Ask for methods from other fields | Replace the noun with a verb, then ask which fields do that verb best; borrow their methods, never role-play experts |
| **Speed** | Ask for the same result in a fraction of the time | Only when time is the real constraint; the essay treats it as the least creative type |

Before writing rungs for a type, read its file. It has how to apply it plus the essay's original text: [altitude](references/altitude.md) · [depth](references/depth.md) · [range](references/range.md) · [speed](references/speed.md).

**The Depth meta-prompt.** For Depth, the essay's own prompt is often the best top rung, filled in for this task: *"I want a deeper version of this task, not a bigger one. Before rewriting it: (1) say what a top professional in this field would do here that I'm not asking for; (2) name the rawest material they would start from; (3) name the specific methods and tools they would use; (4) say what, other than you or me, would show the result is right. Then rewrite my prompt to ask for exactly that."*

## Example

> **User:** Can you fix this crash in the sync module? Third one this month.
>
> **Agent:** *(fixes the crash, then)* Want to see a few bolder versions of this you could ask for?
>
> **User:** Sure.
>
> **Agent:** **The goal behind the goal:** you want sync to stop crashing, not to fix crash #4 next week.
>
> 1. > "Find what this month's three sync crashes have in common, fix the root cause, and add a regression test for each."
>    *Needs:* the three stack traces and repo access. *Check:* the tests fail on the old code and pass on the new.
> 2. > "Feed the sync module malformed, empty and out-of-order server data until it breaks, then fix everything you find."
>    *Needs:* a way to run the module in isolation. *Check:* a fuzz run (thousands of random inputs) with zero crashes.
> 3. > "Keep sync crash-free: watch our crash reports daily, reproduce any new sync crash, open a fix with a test, and tell me only when you need a decision."
>    *Needs:* crash-report access, a version-to-commit map, a test machine per platform. *Check:* sync crash count per week, trending to zero.
>
> Felix Rieseberg did roughly rung 3 for his apps (see precedents). Pick one and I'll start, or we leave it at today's fix.

More examples: [references/examples.md](references/examples.md).

## Guardrails

- Rungs are options, not plans. Don't start any of them until the user picks one. Interest isn't permission for spending, new access, extra agents or recurring automation.
- Never guarantee a rung will work. "Insist it's solvable" is a way to push past early defeatism, not evidence.
- Ground every rung in this task. **Swap test:** if a rung would fit an unrelated request with the nouns changed, rewrite it.
- If they pick the original, do the original well, without a second pitch.

## Attribution

Based on Felix Rieseberg's essay [How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/). Independent adaptation; not endorsed by the author.
