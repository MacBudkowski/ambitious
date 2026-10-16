# Speed: ask for the same result in a fraction of the time

**Fits when** the result is already right and time is the real cost: the user's hands-on hours, or waiting.

The essay calls Speed "the bread and butter for AI's economic value" and skips it as needing "little creativity". So use it only when time is clearly the constraint, and make it bold: not "a bit faster" but a different order of magnitude.

## How to build the ladder

- **Find where the time goes.** Their own attention (writing, reviewing, chasing) or machine time?
- **Rung 1: do it once, reuse it.** A template, script or saved prompt for the repeated part.
- **Rung 2: hands off except decisions.** The model does the whole routine and brings the user only the exceptions, each as a specific decision.
- **Top rung: an order of magnitude.** Ask for the 2-hour job in 5 minutes, or the weekly task to run itself, with the same checks.

## Example ladder

Request: *"Every Monday I text each no-show patient one by one to rebook. Takes 2 hours. Write the text."*

1. > "Write the text with merge fields for name, missed date and a booking link, so I can send it to everyone in one go from our practice software."
2. > "Write a weekly routine: export last week's no-shows, generate a personalised text for each, and give me one list to approve and send in under 10 minutes."
3. > "Set this up so no-shows get a friendly rebooking text automatically the morning after, and I only see the people who reply with a question."

*Needs:* the practice software's export or texting feature. *Check:* Monday time spent, and rebooking rate before vs. after.

## Common mistakes

| Mistake | Instead |
|---|---|
| Reducing the problem instead of the time (fewer no-shows) | That's Altitude; good, but label the rung for what it is |
| Skipping checks to go faster | Keep the checks; automate them |
| Promising a time saving | Give it as an estimate |

## What the article says

The article covers Speed only in its opening definitions. The text below is quoted verbatim and isn't covered by this package's license; see [source-notice.md](source-notice.md).

> Source: Felix Rieseberg, *How to be more ambitious: A tutorial for humans with models* — <https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/>

--- BEGIN VERBATIM ---

I think of ambition in four types: Speed, Altitude, Depth, and Range.

Speed: The same work in less time, the bread and butter for AI’s economic value: If you need some code written, I’ll do it faster with Claude. Well established and requires little creativity in how you approach AI, so I’ll skip this one.
Altitude: Going up in abstraction and considering the outcome rather than the individual task.
Depth: Considering a task the way a field-leading expert would. Rather than operating at the task’s layer, we go one level deeper and touch the underlying data, tools, and problems.
Range: Drawing on multiple fields rather than just the one the task might need at the surface, using knowledge, tools, and techniques you normally wouldn’t.
I primarily use Claude (duh) but my advice is not model-specific.

--- END VERBATIM ---
