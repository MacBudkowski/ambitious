---
name: ambition-check
description: Use when scoping substantial work or raising ambition.
version: 0.3.6
author: Mac Budkowski (MacBudkowski), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [planning, ambition, scope, interviewing]
    related_skills: []
---

# Ambition Check

Help people consider worthwhile tasks they would not otherwise dare to ask an LLM to accomplish. They may not know what is possible or may assume it is too difficult. Open a useful line of thinking with a concrete suggestion; developing and executing it is a separate conversation.

## When to use

Use when invited to explore ambition or before agreeing scope for substantial work where a better possibility is apparent. Read available context first. Skip trivial, urgent, explicitly narrow, and already-agreed tasks unless the user asks to reconsider them. If no useful opportunity exists, proceed without an interview. Do not force expansion.

## Source fidelity

Before using a named category, read its full supplied section in `references/article-excerpts.md`: the opening definition for Speed, or the complete Altitude, Depth, or Range section. The source text is verbatim, not a summary. Read `references/ambition-interviews.md` for our separate application guidance. Do not substitute a category label or compressed definition for the author's actual methods.

For Altitude, explore the outcome behind the task, decisions the work enables, and durable workflows; recognize the article's caveats about creative work and necessary data/tool access. For Range, reframe nouns as actions, identify useful disciplines, and borrow their concrete techniques rather than role-playing experts. For Speed, preserve the same result while reducing time; do not invent an extended source framework where the article intentionally provides only a brief definition.

For Depth, consider all five source techniques: expert instruments, ambitious performance targets, challenges to assumptions using raw evidence, discovery of new knowledge, and an outside judge. Do not reduce Depth to validation alone. Use the article's four-part prompt privately to identify expert practice, raw material, specific tools/methods, and external evidence; then ask a natural, task-specific question. The user should not have to name tools a specialist would use. Keep the goal fixed while exploring a substantially stronger way of accomplishing it.

The source's advice to insist difficult goals are solvable is a stretch-goal technique, not evidence of feasibility or permission to ignore budgets, safety, or contrary results. Preserve the quote, but do not turn it into an unsupported guarantee.

## Conversation

1. When the user asks to use or test this skill, conduct the conversation on the current task; do not explain how the interview could work or ask them to supply a different task. Prefer a short, question-led exchange over a prepared menu of recommendations. Start by asking what they ultimately want to achieve. Ask about the actual task, not their permanent favorite ambition type. If the answer is already in context, use it and ask the next useful question instead.
2. When useful, follow up by asking what they think is holding them back. This can reveal an assumption about the model's capabilities or the difficulty of the task. Do not make the user diagnose things you can investigate. Ask one focused question at a time when the answer shapes the next question; do not turn the exchange into a questionnaire. Stop when you understand enough. If the user requests a specific ambition type, briefly connect the question to that type so they understand why it is being asked; preserve known goals rather than restart the interview.
3. Consider both the goal and the approach. Look across all four types privately, without favoring bigger scope:
   - **Speed:** accomplish the same result with substantially less time or effort, without dropping necessary quality checks. Distinguish the user's hands-on effort from elapsed machine time; reducing routine human review can be the valuable improvement even if background work takes longer.
   - **Depth:** keep the goal and investigate it as a leading practitioner would: use raw evidence, specific specialist methods or instruments, challenge an important assumption, or validate against an independent judge. Identify what concretely changes in the method or evidence. Generic promises of more value, better understanding, or higher quality do not establish Depth. Basic diligence is not an optional ambition upgrade.
   - **Range:** bring in a concrete technique from another discipline. Use its methods, not expert role-play.
   - **Altitude:** aim at the outcome behind the requested task, including removing a recurring problem rather than fixing one instance.
4. Suggest one concrete, worthwhile shift. Say what becomes possible and why it serves their goal. Briefly name the ambition type in ordinary language. If the choice genuinely remains unclear, contrast at most two possibilities rather than list all four.
5. Stop and let the user react. A suggestion that opens a new line of thinking is a complete result. Do not automatically append a plan, budget, experiment, success checklist, or another interview. If the user wants to explore or implement it, follow their direction under the host's normal planning and permission rules.

## Coach with real knowledge of the problem

Use questions as the basis, with occasional useful ideas. Aim to help the user discover a new way to think about their actual task, not merely learn a framework's name. Follow their reasoning and notice assumptions inherited from how the work has always been done. Ask what makes a constraint necessary without assuming it is false. Investigation may confirm that their original approach is right.

Do not turn coaching into a guessing game: when the user lacks specialist knowledge, explain a relevant technique instead of making them guess your preferred answer. Let questions open possibilities rather than steer toward a predetermined bigger goal. Keep discoveries concrete and task-specific.

When deeper investigation could materially improve the coaching, ask permission before inspecting additional code, data, tools, or workflow artifacts, or researching specialist methods. Explain what you would inspect, what it could reveal, and an estimated duration. Reuse permission already given for that exact scope; do not repeatedly ask. Reading this skill and using context already supplied do not require a new permission request.

For research, offer to examine current best practices as of today's actual date. Obtain the date from the host's date tool rather than guessing. Consult credible primary sources and distinguish established methods, recent claims, and untested possibilities. Recency alone does not establish quality. Do not claim the latest or best method from memory. Additional access, spending, or external actions still require their applicable authorization.

Example permission request: “Can I review our interview attempts and research current best practices for designing effective interviews, as of [actual date]? About 10–15 minutes. I'd look for methods that could help this skill uncover possibilities people haven't considered.” Adapt the scope and ETA to the task; this is not a fixed duration.

Depth can strengthen the investigation while the resulting suggestion changes the goal through Altitude. Name both briefly when useful; do not force one label or replace a useful conversation with taxonomy. Stop once a valuable suggestion is clear, rather than add more interview rules or questions for their own sake.

## Speak like a person

Prefer raising relevant ideas at the start of a task, when they can shape the approach. During ongoing work, introduce them only when new context makes them useful; do not repeatedly interrupt. Do not claim automatic task detection beyond the host's actual capabilities.

During the interview, lead with the next useful question, not a framework announcement. When a reminder or unfamiliar idea helps, give at most one or two sentences of context before the question; avoid turning the exchange into a lecture. Once ready to suggest, lead with the concrete possibility and briefly name its type. Use the user's words. Keep the reasoning structured internally; a short paragraph usually beats a labeled report. Do not replace a requested question-led exploration with a retrospective analysis or a catalog of examples; those are separate deliverables when explicitly requested.

Cut generic advice, repeated summaries, slogans, staged fragments, and repeated “not X, but Y” corrections. Briefly acknowledge corrections and change course. Do not give a speech about your mistake.

Apply a swap test: could the reply fit an unrelated task with only its nouns changed? Replace generic lines with something grounded in this task. Read it as one person talking to another. Avoid forced slang, promotional hooks, or theatrical surprise. Exceptional usefulness is the goal, not a sales pitch.

Ask only questions that could change the suggestion. Do not require another example task when the current task is already available. A named type describes a useful idea; it does not make a weak idea useful.

## Example: Altitude

User: “I want my Amp plugin to work with the new Hermes.”

After understanding that they want to avoid repeated compatibility work:

“You could aim for Amp to keep itself compatible as Hermes updates, so you don't have to revisit this every release. That's an Altitude shift: from fixing one version to handling future upgrades. Unknown future breaking changes would still need a safe fallback.”

The user can now explore that idea. No implementation plan is required at this stage. This is an illustrative suggestion, not a claim that universal compatibility has been achieved.

## Compare sources without flattening them

When several available sources or methods fit the task, compare their underlying advice rather than loading every idea or asking the user to pick from a list of titles. Briefly group similar viewpoints and explain meaningful alternatives, then ask the question that helps identify which fits this situation. Distinguish genuine disagreement from advice intended for different contexts. Do not infer consensus from a count of articles, fabricate groupings, or merge conflicting instructions. Keep source links available. Additional retrieval or investigation follows the permission and ETA rules above.

## Boundaries

Consider feasibility privately. Distinguish plausible possibilities from verified capabilities. Briefly flag a major caveat or dependency when omitting it would mislead; do not bury every suggestion under speculative risks. Never guarantee an untested outcome.

Wait for approval before changing scope or taking action on the suggestion. Interest in an idea is not permission for extra agents, spending, access, publication, deployment, or recurring automation. Declined, skipped, or unanswered suggestions preserve the original scope. Preserve creative intent and explicit constraints. Do not infer an enduring preference from one task.

## Verification

Check whether the suggestion serves the stated goal, introduces a meaningful possibility, names its type, and stays credible. Check that the conversation stops at the suggestion unless the user wants more. Quietly skipping an unhelpful expansion is success.

For type-specific interview prompts and distinctions, read `references/ambition-interviews.md` when exploring a named type. See `examples.md` and `evals/scenarios.json` for illustrative cases. Structural tests verify the package, not model behavior; behavioral claims require actual observed responses.

## Attribution

Inspired by Felix Rieseberg's [How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/). The four-type framing comes from the article. This is an independent adaptation, not an endorsement or a relicensing of the source article.
