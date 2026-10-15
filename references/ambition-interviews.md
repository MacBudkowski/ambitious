# Interviewing by ambition type

Use these prompts as adaptable examples, not a script. Reuse the known goal, ask one question whose answer will shape the next step, and follow the user's answer. Do not force a preferred type across tasks. These are guidance and acceptance criteria, not proof of a completed behavioral evaluation.

## Altitude: reconsider the outcome

Start with what the user ultimately wants. When it is unclear, ask what completing the immediate task would enable. Then explore the obstacle or recurring burden.

- Opening: “What do you ultimately want this to do for you?”
- Possible follow-up: “After this fix, what would you still have to keep doing yourself?”
- Suggestion shape: move from one repair to preventing or handling recurrence, when that serves the user's goal.

Changing a one-version compatibility fix into ongoing compatibility is Altitude because the desired outcome expands. Do not imply that arbitrary future versions can be guaranteed compatible.

## Depth: strengthen the method while keeping the goal

Coach with knowledge of the problem space: follow the user's thinking, help them examine inherited assumptions, and occasionally introduce unfamiliar methods. A strong outcome is a concrete new way of thinking about their task. Do not make the user guess specialist knowledge, assume their constraints are wrong, or steer toward an answer chosen in advance.

If the conversation alone is insufficient, offer a scoped investigation of relevant artifacts and current best practices. Ask permission, explain the likely value, and give an ETA before starting. Use the actual current date for dated research; ground findings in credible sources rather than claiming expertise through vocabulary. Keep the interview question-led when returning with findings. Depth in the investigation may support an Altitude shift in the eventual goal.

Read the full user-supplied Depth passage in `references/article-excerpts.md` first. The prompts below are our adaptations, not replacements for the source. Explore expert tools, stretch targets, raw-data challenges to assumptions, new discoveries, and outside validation; do not default every Depth conversation to asking how to test the result.

Consider what a leading practitioner would do that the user has not requested. Ask about the task's current ceiling, available raw material, or an assumption worth challenging. Offer specialist methods yourself rather than asking the user to choose methods they may not know.

Explain the lens briefly if needed: “For Depth, we're keeping the goal and looking at how to do the work more rigorously.” Then ask about a concrete uncertainty, the material available, or what could establish that the result is right. Do not make the user choose specialist methods they may not know; identifying those is the agent's job.

Possible questions, selected according to context:
- “What would convince you that these recommendations actually help?”
- “Is there an assumption here that we're currently taking on trust?”
- “Do we have actual examples and outcomes to compare, or only summaries?”

Use follow-ups to distinguish personal impressions, informed user feedback, and observed outcomes without asserting that only one kind can be useful. Then suggest a specific method that addresses the uncertainty.

Distinguish source credibility from practical usefulness. When relevant, offer two optional checks: compare important claims with credible independent sources, and try the same real task with and without the proposed method. Ask whether the user wants these checks; give an ETA before doing them. A fair comparison uses comparable conditions and, where useful, hides which version used the method when collecting the user's judgment. A single comparison is informative, not general proof. Retain the source's ideas and procedures, including applicability and limitations, rather than assuming a short summary preserves them. These checks supplement the other Depth techniques; they are not a mandatory testing pitch in every interview.

Examples:
- For a recommendation skill, compare suggestions on realistic tasks and ask task owners to judge usefulness without revealing which version produced them.
- For suspicious-email screening, evaluate against independently reviewed cases, especially genuine customers incorrectly flagged; model confidence is not ground truth.
- For prompt adoption, compare behavior with and without selected instructions on equivalent tasks rather than judge persuasive wording.

Name the raw material, method, or independent check that makes the idea deeper. Merely asking whether an idea solves the user's problem better is a value check, not sufficient evidence of Depth. Ordinary error inspection, numerical correctness, and required security testing remain baseline responsibilities.

A method associated with another discipline can support Depth when its main purpose is stronger evidence for the same goal. Use Range as the primary label when opening a different disciplinary approach is the meaningful shift. Explain the change rather than debate taxonomy.

## Range: explore another way to approach the problem

Start with what the person does, where it breaks down, and when help would matter. Reframe the artifact as an activity before selecting a useful discipline. For example, saving articles may really be about remembering and applying ideas when beginning work. Ask what happens between reading and applying, then when a cue would help. Reuse answers already given; do not force this sequence onto unrelated tasks.

Identify a concrete technique the user may not know to request. Introduce it in one or two sentences, then ask how it could fit their task. Keep the conversation question-led; do not ask the user to invent the cross-disciplinary connection.

For an article-to-skill tool, learning design can suggest task-linked reminders and opening questions. Research synthesis can suggest grouping overlapping advice and contrasting alternatives. These are illustrative possibilities, not proof of efficacy or requirements for every product. When combining sources, check whether apparent disagreement reflects different circumstances, preserve attribution, and avoid treating repeated claims as independent corroboration.

Illustrative synthesis prompt, only when the sources actually support it: “These articles recommend testing a small version early; those recommend customer research first. What's less clear here: whether you can build it, or whether people want it?”

- “How have you approached this so far, and where does that approach fall short?”
- Suggest a concrete borrowed method, such as a cognitive walkthrough to find confusing decision points, rather than asking the model to role-play a panel of experts.

## Speed: reduce time or effort without changing the result

Start by asking where time or effort goes. If the answer is ambiguous, distinguish hands-on attention from elapsed waiting time: “Are you worried about your time reviewing and correcting it, or how long the automated work takes?” Do not assume that faster model responses solve the user's problem.

When routine human review is the bottleneck, explore whether checks and clear corrections can be automated, with only unresolved cases brought to the user. Ask whether that division of work is acceptable. Exception-only review should present a specific decision rather than offload the whole review. This can save user attention even if automated processing takes longer. Also consider simpler elimination of repeated work; do not default every Speed opportunity to building automation.

For an article-to-skill product, a useful suggestion might be: draft the skill, try relevant example tasks, revise clear failures, and ask the user only about conflicting advice or ambiguous results. This is an illustrative Speed opportunity, not permission to build an evaluator, launch background work, or activate generated skills.

If the user asks how such testing would work, explain evaluations in plain language: example tasks with criteria for judging results. Include tasks where the method should help, cases where it should stay inactive, explicit constraints, and uncertain outcomes. For conversational methods, test follow-up exchanges as well as the opening response. Compare with and without the method under comparable conditions, and keep fresh examples aside so revisions do not merely fit the same tests.

Prefer observable checks; an independent, blinded comparison can help with subjective quality, but neither the generating model's confidence nor another model's approval proves correctness. Allow an unclear outcome and human escalation. Bound automated revision attempts and spending. Distinguish ready to try, needs judgment, and not ready; successful tests do not authorize automatic activation or broader access.

Keep these evaluation details for a requested follow-up rather than append them to every suggestion. If the user only wants lessons saved or a discussion, update the guidance without implementing the proposed product. Do not equate Speed with skipping verification or promise an arbitrary speedup without evidence.

## Stop at the useful suggestion

Name the type briefly and state why the possibility matters. Flag only consequential uncertainty. Leave implementation plans, evaluation protocols, budgets, and experiments for a follow-up unless requested. During live testing, an answer from the user advances the interview; it is not a request for commentary on how the skill is performing.
