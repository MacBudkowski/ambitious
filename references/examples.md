# Examples

Illustrative exchanges, not evaluation results. The right type depends on what limits *this* task, not on the kind of task.

## One request, four possible answers

**Request:** "Help me prepare the weekly customer report."

Ask first what the report needs to enable. Depending on the answer:

| If the real problem is… | Type | Possible suggestion |
|---|---|---|
| It takes a whole day every week | **Speed** | Generate it from the same queries each week, keep the reconciliation checks, and surface only figures that fail them. |
| Nobody trusts the numbers | **Depth** | Trace each headline metric back to raw records and reconcile the definitions against an independent source. |
| It's accurate but nobody understands it | **Range** | Borrow from information design: lead with the one change that matters, and put detail behind it. |
| It exists so leaders catch surprises | **Altitude** | Replace the weekly artifact with an exception alert, and check it against past data to see whether it would have caught problems sooner. |

Offer the one that fits, not all four.

## A real tradeoff: contrast two

> **User:** I need churn insight, but I'm torn between an early warning next week and a solid explanation before we invest.
> **Agent:** Those pull in different directions. A simple warning from signals you already have would be live next week, but won't tell you *why* customers leave. That's the Speed option: faster, same data. Testing the causes against raw usage logs would give you something to invest on, but takes weeks and may stay partly uncertain. That's the Depth option: slower, but evidence you can invest on. Which decision is coming first?

## Coaching, not quizzing

> **User:** I want this plugin to keep working, but I don't know what techniques make updates easier.
> **Agent:** One common approach is a *contract test*: a small suite that exercises exactly the host APIs your plugin relies on, so a new release tells you what broke before users do. Which parts of the host does your plugin touch most?

The agent explains the technique instead of asking the user to guess it.

## Quiet skips

- "Fix this typo only." → Fix it. No interview.
- "Production is down, restore service." → Incident first. No strategy talk.
- "Sounds interesting, but keep the original scope." → Continue as originally agreed. Don't sneak in an experiment.
- "Polish this poem, keep its voice." → Polish it. Don't reframe a poem as a business outcome.
