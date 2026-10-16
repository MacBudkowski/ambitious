# Altitude: ask for the outcome, not the task

**Fits when** the request is the user's best guess at a step toward something larger: the task recurs, it feeds a decision or a meeting, or fixing one instance leaves the problem in place.

## How to build the ladder

The essay's own example is a ladder. For a quarterly business review deck, it climbs from "fill in the template" to:

1. *Understand it:* "Tell me what changed this quarter, why, and what we should do about it." (give the model all the data, not just the template numbers)
2. *Decide:* "Work out which three decisions are most urgent… and start working on potential directions with for/against arguments."
3. *Replace the task with the outcome:* "The review exists so leadership catches problems early and moves money and people to the right places. Design a better way to do that than a quarterly deck, show from our own history that it would have caught things sooner, and run it beside the current one for a quarter."

Build yours the same way:

- **Find the goal beyond the goal.** "What do you want to happen after this is done?" "What will this let you decide?" If there will be meetings about the work, there's usually a higher goal.
- **Rung 1: understand.** Ask the model to explain what's really going on, with full data.
- **Rung 2: decide or prevent.** Ask for the decision the work serves, or for removing the cause of a recurring problem.
- **Top rung: own the outcome.** Ask the model to keep the outcome true over time ("keep our apps crash-free"), or to design something better than the original deliverable, prove it against history, and run it alongside the old way.
- **Name what the top rung needs.** Durable workflows need plumbing: Felix first had to give Claude crash reports, a version-to-commit map, and Windows, macOS and Linux machines. That setup is often the real first step; say so.

## Example top rung

> "Our tenants keep reporting the same steam-heat problems. Look at every heating complaint across our 3 buildings since October, find the pattern, propose a maintenance schedule that would have prevented most of them, and draft the case for it to the owner."
> *Needs:* the complaint log and maintenance records. *Check:* complaint count next winter versus this winter.

## Limits

- **Creative work.** For a poem or a personal piece, the work *is* the outcome. Don't offer Altitude there.
- **No guarantees.** "Keep it crash-free" is a direction, not a promise. Say which failures would still need a human.
- **Today's task still matters.** The ladder is an offer; the original request still gets done unless the user picks a rung instead.

## Common mistakes

| Mistake | Instead |
|---|---|
| Top rung is a template or macro for the same task | That's Speed. Altitude removes the reason the task exists |
| "Just automate everything" | Name the outcome and the access it needs |
| Generic strategy talk | Use the user's own numbers, systems and names |

## What the article says

The text below is quoted verbatim and isn't covered by this package's license; see [source-notice.md](source-notice.md).

> Source: Felix Rieseberg, *How to be more ambitious: A tutorial for humans with models* — <https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/>

--- BEGIN VERBATIM ---

Altitude
We often flippantly call this “letting the model operate at a higher abstraction”. When you give the model a task, it’s executing your best guess at how to get the outcome you want. To be more ambitious in altitude, ask yourself — what do you want to happen next? What’s the goal beyond the goal? At the beginning of last year, I still asked Claude to fix individual crashes for me. Eventually I asked Claude to simply keep our apps crash-free.

Let’s consider an everyday (dare I say mundane?) office task. You’re at Acme Inc, an imagined company, where you need to put together a deck for the quarterly business review (QBR). Given a bunch of data, Claude will happily make you some slides. Maybe you even have a template and it just needs to fill it in. That’s hardly comparable to finding a new planet, so let’s look at some concrete steps to make our approach more ambitious. We’ll start basic and get a little bit more ambitious with each step:

As input, most reviews want to know what changed this quarter, why, and what should be done about it. Resist the urge to just update whatever numbers are in the template — give the model too as much data as you can get your hands on so it can understand your business: “Tell me what changed this quarter, why, and what we should do about it.”
Meetings (the good kind, anyway) ideally end with some decisions. Ask Claude: “Work out which three decisions are most urgent in the face of everything you’ve learned, and start working on potential directions with for/against arguments.”
QBRs are from a time when good reviews required humans to carefully sift through data, figure out what the data means, and if the business should adjust. Ask Claude: “The review exists so leadership catches problems early and moves money and people to the right places. Design a better way to do that than a quarterly deck, show from our own history that it would have caught things sooner, and run it beside the current one for a quarter.”
The altitude approach works best if you really are after some ultimate outcome; it works less well for creative endeavors. A good tell-tale sign that ambition in altitude is a good idea is if you’re going to have meetings to discuss whatever you’re working on. There are currently limits (“Claude, go make money” doesn’t seem to work for most businesses by itself in 2026), but I generally see that models seem to be able to operate at higher levels of abstraction the more capable they become.

Altitude is also where people find durable workflows that take the human out of the loop, making it less necessary for you to constantly update the model with task after task. Doing this well often involves changing your workflow — in order to let Claude make sure our app is crash-free, I first had to make sure it can easily fetch crash reports, understand which app version maps to what git commit, and give it access to Windows, macOS, and Linux computers so it can actually independently reproduce and verify fixes.

All the ways in which I describe ambition require the model to have a computer with the ability to install software and access to all kinds of relevant data (either using MCP connectors or other means). Plenty of tools make this possible and I recommend that you use one.

--- END VERBATIM ---
