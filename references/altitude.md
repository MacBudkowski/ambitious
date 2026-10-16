# Altitude: aim at the outcome behind the task

**Use when** the request is the user's best guess at a step toward something larger: the task recurs, it exists to support a decision or meeting, or fixing one instance leaves the underlying problem in place.

## How to apply it

1. **Find the goal beyond the goal.** "What do you want to happen after this is done?" or "What will this let you decide?"
2. **Find the recurring burden.** "After this fix, what would you still have to keep doing yourself?"
3. **Raise the target one level.** Move from one fix to preventing the problem class, from a report to the decision it serves, or from one-off tasks to a durable workflow that needs the user less often.
4. **Name what the higher level needs.** Durable workflows usually need access and tooling: crash reports, version-to-commit mapping, test machines, data connectors. Say so briefly. It's often the real work.

A useful tell from the article: if there will be meetings about the work, Altitude is probably worth considering.

## Good suggestion shape

> "Rather than a better weekly budget deck, you could aim for leaders hearing about overspend the week it starts: an exception alert from the same data, checked against last year's history to see whether it would have caught past problems sooner. That's Altitude ambition: aiming at what the report is for, not just the report. It would replace a format people know, so it's worth trying alongside the deck first."

## Limits

- **Creative work.** Altitude works best when there's a real outcome to serve. For a poem or a personal piece, the work *is* the outcome. Don't swap it for a business goal.
- **No guarantees.** "Keep the plugin compatible with future releases" is a direction, not a promise. Unknown breaking changes still need a fallback.
- **Approval before replacing the deliverable.** Suggesting a different deliverable is fine. Building it instead of the one requested is not.

## Common mistakes

| Mistake | Instead |
|---|---|
| Inflating every task into strategy | Only raise altitude when the user's real goal is higher |
| "Just automate the whole thing" | Name the specific outcome and what access it needs |
| Promising the higher outcome will work | State the main dependency or uncertainty |

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
