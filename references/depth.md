# Depth: ask for it done the way the best in the field would

**Fits when** the goal is right but the method is shallow: high stakes, contested facts, conclusions taken on trust, work done from summaries instead of raw material, or a result "good enough" only because nobody pushed.

## How to build the ladder

The essay lists five techniques. Each makes a good rung; the top rung usually combines several.

| Technique | What the user would ask for |
|---|---|
| **Expert instruments** | The tools real experts use, not just their vocabulary: "use a database and a survival model, not a markdown table" |
| **Unreasonable target** | A goal far past the obvious one: "you need 5 s, ask for 200 ms", and insist it's solvable |
| **Challenge what you know** | Raw data plus an adversarial check: "We believe churn is an onboarding problem. Try to reproduce that from the raw data." |
| **Produce new knowledge** | Something nobody knows yet: "find the earliest signal of churn we don't know about, and show it predicts on data it hasn't seen" |
| **Outside judge** | A check that isn't the model grading itself: tests, held-out data, a real metric, ideally a tool it can run |

**The essay's meta-prompt** is itself a great rung, because it makes the model find the deeper version for the user:

> "I want a deeper version of this task, not a bigger one. Before rewriting it: (1) say what a top professional in this field would do here that I'm not asking for; (2) name the rawest material they would start from instead of what has already been digested for me; (3) name the specific methods and tools they would use; (4) say what, other than you or me, would show the result is right. Then rewrite my prompt to ask for exactly that."

Fill it in with the user's task, or go one step further and write the deeper prompt yourself.

## Example ladder

Request: *"Can I tell the customer our defect rate is basically zero? We sample 5 parts per batch of 2,000; no failures in 60 batches."*

1. > "Tell me what defect rate our sampling can actually support, with a confidence bound, and how to word it honestly in the quality summary."
2. > "Design a sampling plan that would let us claim under 0.1% defects at 95% confidence, and tell me what it would cost per batch."
3. > "Pull our last year of inspection, returns and customer-complaint data, find which process step predicts defects, and show it on months the analysis hasn't seen."

*Needs:* inspection and returns records. *Check:* the bound holds up against customer returns; the predictor works on held-out months.

## Distinctions

- **Depth vs. basic diligence.** Checking arithmetic and running required tests is baseline, not ambition.
- **Depth vs. Range.** A method from another field is Depth when it's the expert method for *this* field's question; it's Range when bringing in a different discipline is the point.
- **Stretch target ≠ guarantee.** The unreasonable target pushes past early defeatism. It doesn't override budgets, safety or contrary results.

## Common mistakes

| Mistake | Instead |
|---|---|
| "Act as a senior data scientist" | Name the actual instrument or method |
| A modest target | Push the number: 10x, the expert benchmark, or "find what nobody knows" |
| Model grades its own work | Name the outside judge |
| Asking the user which method to use | Propose it; that's your job |

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
