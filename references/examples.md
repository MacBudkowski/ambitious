# Examples

Illustrative ambition passes, not evaluation results. Each shows the shape: goal behind the goal, a 2–3 rung ladder of prompts the user could send, what each needs, how they'd know it worked, then hand back the choice.

## Offering it at planning time

> **User:** Help me put together the weekly customer report.
>
> **Agent:** *(drafts the report structure, then)* Want to see a few bolder versions of this you could ask for?

One line, once. If they say no or ignore it, carry on.

## Altitude: a recurring complaint

> **User:** Tenant in 4B says the radiator isn't heating again, third time since October. Draft a reply saying a tech comes Thursday.
>
> **Agent:** *(drafts the reply, then, after the user says yes to the offer)*
>
> **The goal behind the goal:** stop getting the same heating complaints, not just answer this one.
>
> 1. > "Ask Thursday's tech to log the root cause in 4B, not just bleed the radiator, and draft a checklist they can use in every unit."
>    *Needs:* the tech's notes. *Check:* whether 4B complains again this winter.
> 2. > "Go through every heating complaint across our 3 buildings since October, find the pattern (floors, risers, times), and tell me which fix would remove most of them."
>    *Needs:* the complaint log. *Check:* the pattern explains most past complaints.
> 3. > "Design a pre-winter steam-heat maintenance plan for all 60 units, show from this year's complaints that it would have prevented most of them, and draft the budget case for the owner."
>    *Needs:* complaint and maintenance records, rough costs. *Check:* complaints next winter vs. this one.
>
> Pick one and I'll start, or we just send the reply.

## Depth: a claim taken on trust

> **User:** Can I tell the customer our defect rate is basically zero? 5 parts sampled per 2,000, no failures in 60 batches.
>
> **Agent:** *(answers: no, 300 samples with zero failures supports roughly "under 1% at 95% confidence"; suggests wording; then offers)*
>
> **The goal behind the goal:** a quality claim you can stand behind when the customer checks.
>
> 1. > "Give me the honest confidence bound for our sampling and three ways to word it in the quarterly summary."
> 2. > "Design a sampling plan that would support 'under 0.1% defects at 95% confidence' and estimate its cost per batch."
> 3. > "I want a deeper version of this, not a bigger one. Before rewriting it: (1) say what a top quality engineer would do here that I'm not asking for; (2) name the rawest material they'd start from; (3) name the specific methods and tools; (4) say what, other than you or me, would show the result is right. Then rewrite my prompt to ask for exactly that."
>
> *Check for all:* the claim survives a look at customer returns.

## Range: the usual fix keeps failing

> **User:** Our grief text line's shift handoffs keep missing people who were fragile earlier. Better template?
>
> **Agent:** *(gives a template, then offers)*
>
> **The goal behind the goal:** nobody in a fragile state gets missed at shift change.
>
> 1. > "Rebuild the template on SBAR, the handoff structure nurses use (situation, background, assessment, recommendation), with a 'fragile' flag that must be read back by the incoming supporter."
> 2. > "Combine nursing's SBAR handoff with aviation's read-back and a pilot-style checklist for the first 10 minutes of a shift."
> 3. > "Run a red-team pass: take last month's anonymised handoff notes and find every case where a fragile signal was in the notes but missed, then redesign the handoff so each would have been caught."
>
> *Needs:* anonymised past notes for rung 3. *Check:* missed-fragile cases per month.

## Invoked directly: prompts only

> **User:** ambitious cold email to Revolut's VP of Engineering about our code-review tool. It's faster and better for AI agents. I want a short meeting.
>
> **Agent:** **The goal behind the goal:** a meeting where Revolut sees your tool working on their kind of agent code, not another vendor email.
>
> 1. > "Research Revolut's public engineering blog, talks and job posts for how they use AI coding agents, then write a 90-word email to their VP of Engineering that opens with one real, cited observation and asks for 15 minutes about [tool name]."
>    *Needs:* web access, [tool name] and one proof point. *Check:* every claim about Revolut links to a source.
> 2. > "Run [tool name] and our current reviewer on 50 agent-generated pull requests from public fintech repos, measure review time and real bugs caught, and write the email around that one striking number."
>    *Needs:* the tool, a sandbox, public repos. *Check:* the bugs are confirmed by a human reviewer, not the tool.
> 3. > "Build the case Revolut can't ignore: a reproducible benchmark of code review for AI-agent pull requests, published openly, with a personalised run on a Revolut open-source repo. Then design a 30-account outreach sequence to VPs of Engineering who use coding agents, led by that benchmark."
>    *Needs:* the tool, compute, a list of target accounts. *Check:* meeting rate per 30 sends versus your current outreach.
>
> Pick one and I'll start, or keep the original.

No draft email, no critique of "faster and better". Just the ladder.

## When not to offer

- "What temperature should red wine be stored at? Just the number." → Answer it.
- "Production is down." → Incident first. No ladder.
- "Boarding in 10 minutes, need a one-line text to my host." → Write the line.
- "Polish this poem, keep its voice." → Polish it.
- The user already said no to bolder versions in this conversation → don't ask again.
