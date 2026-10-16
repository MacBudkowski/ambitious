# Range: ask for methods from other fields

**Fits when** the usual approach keeps failing the same way, or the task's surface discipline is too narrow for what it's really trying to do.

## How to build the ladder

The essay gives two techniques:

1. **Replace the noun with a verb.** A quarterly review isn't "a deck"; it's *"getting busy people to believe a story about cause and effect, and to decide under uncertainty, in 30 minutes."* The verb tells you which fields have something to offer.
2. **Assemble the crew.** "The deck needs to be amazing, otherwise aliens will blow up Earth. What kind of team will humanity get together?" For the QBR: an analyst, a journalist, an editor; a motion and audio designer; a red team of a short seller and a forensic accountant.

Then turn that into rungs:

- **Rung 1: one borrowed method**, named with its field: "Run a cognitive walkthrough (from interaction design) on every screen of the guide."
- **Rung 2: two or three fields combined**, each doing what it does best.
- **Top rung: the full crew**, working in parallel (subagents if the user's tool supports them), each producing a real artifact, plus a red team that tries to break the result.

**Borrow methods, never costumes.** The essay: "Don't ask the model to write a short seller, ask it to do what a short seller does to research their position." Each crew member's line in the prompt names what they *do*, not who they *are*.

## Example top rung

Request: *"Riders keep standing at the closed bus stop. Write a better notice."* As a verb: *"redirect people who aren't reading, in the few seconds they're standing there."*

> "Treat the closed stop as a wayfinding problem. Use what airport signage designers do (one message, visible from 30 m, arrow plus distance), what behavioural scientists do (put the cue where the decision happens: on the pole, at eye level, at the old stop), and what UX researchers do (watch five riders arrive and note where they look). Give me the notice, a placement plan, and a 2-day test to see if fewer people wait at the wrong stop."

*Needs:* nothing beyond a phone camera and the stop. *Check:* count riders waiting at the closed stop before and after.

## Example borrowings

| Problem as a verb | Field | Method |
|---|---|---|
| Get people through a flow without confusion | Interaction design | Cognitive walkthrough |
| Remember ideas when they matter | Learning science | Retrieval practice; task-linked cues |
| Hand over fragile cases between shifts | Nursing / aviation | SBAR handoff (situation, background, assessment, recommendation); read-back |
| Cover shifts despite no-shows | Hospitals / airlines | Standby rota; overbooking buffer sized from past no-shows |
| Prevent the same human error | Lean manufacturing | Poka-yoke: make the mistake impossible or obvious |
| Find where a plan is wrong | Finance | Short-seller or forensic-accountant analysis |

## Common mistakes

| Mistake | Instead |
|---|---|
| "Imagine a panel of experts…" | Name what each field *does* and the artifact it produces |
| A borrowed idea with no named field | Name the field: "a standby rota, as hospitals use" |
| Generic automation presented as Range | Automation isn't a borrowed method; consider Speed |

## What the article says

The text below is quoted verbatim and isn't covered by this package's license; see [source-notice.md](source-notice.md).

> Source: Felix Rieseberg, *How to be more ambitious: A tutorial for humans with models* — <https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/>

--- BEGIN VERBATIM ---

Range
In short, being ambitious in range means that we consider our work from the perspective of different fields — more fields than would have been economical in the past. This isn’t a particularly unique insight, every single heist movie spends the first 30 minutes assembling a diverse cast of characters and talents. As AI products make it easier and easier to run multi-agent systems (with multiple threads, orchestrators, or simply subagents), I’ve seen really interesting results by imploring Claude to bring in additional fields.

Putting this into practice isn’t easy; it requires you to be creative. Until I saw my colleague Alex Albert use Blender to render interior designs, I never considered using Claude for 3D environments for my homepage — even though I’ve previously made video games! However, this is easily where I see the most magic happen.

So, how do we do this? I use the following techniques:

Try to replace the nouns with verbs: An old trick from The Art of Innovation by Tom Kelley and Jonathan Littman. A quarterly review isn’t “a deck”. It’s “getting busy people to believe a story about cause and effect, and to decide under uncertainty, in 30 minutes”. Having the verbs makes it easier for both me and Claude to understand which fields might bring in a unique and useful perspective.
Assemble the crew: The deck needs to be amazing, otherwise aliens will blow up Earth. What kind of team will humanity get together? For production quality, I’d bring in an analyst, a journalist, and an editor. If it has to be presented, probably a motion and audio designer, too. It might be useful to employ an adversarial “red team”, too, so let’s bring in a short seller and a forensic accountant.

It is easy to accidentally engage in role play, which will make your transcript weirder without improving the actual outcome. Use this method to find fields and techniques. Don’t ask the model to write a short seller, ask it to do what a short seller does to research their position.

All the ways in which I describe ambition require the model to have a computer with the ability to install software and access to all kinds of relevant data (either using MCP connectors or other means). Plenty of tools make this possible and I recommend that you use one.

--- END VERBATIM ---
