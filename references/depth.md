# Depth: the same goal, done the way a field-leading expert would

**Use when** the goal is right but the method is shallow: high stakes, contested facts, conclusions taken on trust, or work done on pre-digested summaries instead of raw material.

## How to apply it

Keep the goal fixed. Change the method or the evidence. The article offers five techniques, so consider all of them rather than defaulting to "let's test it":

| Technique | What it changes | Example question |
|---|---|---|
| **Expert instruments** | The tools and methods, not just the vocabulary | (Usually your job to name: a database plus a survival model instead of a markdown table) |
| **Unreasonable targets** | The ceiling | "What would this look like at 200 ms instead of 5 s?" |
| **Challenge what you know** | The assumptions, tested against raw data | "What are we currently taking on trust here?" |
| **Produce new knowledge** | Finding what nobody knows yet | "Once we're in the raw data, what blind spot could we look for?" |
| **Outside judge** | Who decides it's right: not the model, not the user's impression | "What, other than us, would show the result is right?" |

**When proposing a test, name what decides success**: the outcome the user cares about (activation, error rate, revenue, recovery time), not an easy proxy (opens, likes, model confidence). Compare against the current version, not just between new variants.

Use the article's four-part prompt **privately** to find the deeper version: (1) what a top professional would do that the user isn't asking for; (2) the rawest material they'd start from; (3) their specific methods and tools; (4) what external evidence would show the result is right. Then ask a natural, task-specific question. Don't make the user name specialist tools. Identifying them is your job.

If the user doesn't know the field, explain a method in a sentence or two before asking how it fits.

## Good suggestion shape

> "Instead of explaining churn from the dashboard, we could test the 'it's onboarding' belief against raw event logs, and check any new early signal on months the model hasn't seen. It needs access to the event data, and might confirm what you already believe."

## Distinctions

- **Depth vs. basic diligence.** Checking your arithmetic, inspecting errors and required security testing are baseline. They're not an ambition upgrade.
- **Depth vs. generic quality.** "More rigorous" or "higher quality" isn't Depth until you name the raw material, method or independent check that changes.
- **Depth vs. Range.** A method from another field is Depth when its purpose is stronger evidence for the same goal. Call it Range when opening a different disciplinary approach is the real shift.
- **Depth feeding Altitude.** A deeper investigation can reveal a better goal. Say so plainly; don't debate taxonomy.
- **Stretch goals aren't guarantees.** "Insist it's solvable" pushes past early defeatism. It doesn't override budgets, safety, or contrary results.
- **Credible vs. useful.** If proposing a check, separate "is this advice credible?" (compare against independent sources) from "does it help here?" (try the same task with and without it, ideally blind). One comparison is informative, not proof. Offer these checks; don't run them silently.

## Common mistakes

| Mistake | Instead |
|---|---|
| Reducing Depth to "let's validate it" | Consider instruments, targets, assumptions, and discovery too |
| Expert role-play ("as a senior data scientist…") | Change the actual method and tools |
| Asking the user which statistical method they want | Propose one and explain it briefly |
| Letting the model grade its own work | Name an outside judge: a test, data, or a person |
| Proposing a test without saying what it measures | Name the outcome that decides success (activation, error rate, revenue), not a proxy like opens or likes |

## What the article says

The text below is quoted verbatim and isn't covered by this package's license; see [source-notice.md](source-notice.md).

> Source: Felix Rieseberg, *How to be more ambitious: A tutorial for humans with models* — <https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/>

--- BEGIN VERBATIM ---

Depth
Sometimes, you just want a task executed really well. Being ambitious in depth means pushing the model to use the tools, techniques, media, and knowledge employed by the best professionals in the field — and to keep pushing until even those people might learn something new from your work.

Let’s continue with our Acme Inc example of a quarterly business review deck. Assume for a second that Acme Inc struggles with some user churn (customer loss over time). I’ve found a mix of the following techniques useful:

Insist on the same instruments used by the best in the industry: When prompted to act like a professional, models often switch vocabulary without actually switching methods. To work on our problem with depth, we need to use the same tools as the best data scientists and statisticians. When Claude reaches for markdown tables, insist on the use of databases and statistical models. You don’t necessarily have to know what the experts use, Claude usually does.
Pick unreasonable goals and tell the model that they’re very reasonable: You need your website to load in 5s instead of 10s? Ask for 200ms. Does something seem impossible to the model? Reiterate that it’s very much solvable, it just needs to keep going.
Challenge what you know: Especially in business, a lot of things we believe to be true are rough approximations of reality. Give the model access to the raw information and data and ask it to adversarially check assumptions. “We believe churn is an onboarding problem. Try to reproduce that from the raw data.”
Produce new knowledge: Easily tacked onto challenging what you know — once Claude is already deep inside the data, ask it to find blind spots. “Build a simulation of our customers that reproduces the last year from our logs. Then find the earliest signal of churn we don’t know about yet, and show it predicts on data it has not seen.”
Use an outside judge: Do not ask the model to judge itself. I assume that this will eventually be solved with increasing model intelligence, but in October 2026, I implore you to insist on outside validation. Ideally that’s a tool the model can run to get feedback immediately.
A simple prompt that often helps me:

I want a deeper version of this task, not a bigger one. Before rewriting it: (1) say what a top professional in this field would do here that I’m not asking for; (2) name the rawest material they would start from instead of what has already been digested for me; (3) name the specific methods and tools they would use; (4) say what, other than you or me, would show the result is right. Then rewrite my prompt to ask for exactly that.

All the ways in which I describe ambition require the model to have a computer with the ability to install software and access to all kinds of relevant data (either using MCP connectors or other means). Plenty of tools make this possible and I recommend that you use one.

--- END VERBATIM ---
