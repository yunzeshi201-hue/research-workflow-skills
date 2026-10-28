---
name: research-field-map
description: "Stage 1 of the gated research workflow: compare evidence-backed directions, specify a subfield and its boundaries, and present them for user acceptance before selecting the important question set."
---

# Research Field Map

This is stage 1: specify the subfield. Inspect the project workflow record, preferably `research/workflow-state.json`, and any earlier user decisions. If this subfield version was already accepted, reuse that decision. If scope changes, create a revision and assess affected downstream dependencies.

Preliminary literature and representative question examples help select the subfield. Do not commit a stage-2 question set, implement a website, or draft the review before the user accepts the concrete subfield brief. On completion mark `subfield` as `ready_for_confirmation`; only clear user acceptance of that version changes it to `accepted`. File existence, silence, and a request to do the entire workflow are not acceptance. A later explicit gate override must be recorded as an override.

If literature access is unavailable, a clearly bounded provisional scope may still be presented for acceptance with explicit evidence gaps and verification tasks. Acceptance settles the working scope, not its scientific novelty; unclear scope itself must be resolved first.

Turn a named field into a justified choice of where to investigate next.
The user can instead begin with what they have already done and what they want next. Extract the implied subfield, observations, resource constraints, and desired decision; distinguish reported facts from inspected evidence and planned work. If a narrow scope already fits, refine that scope instead of forcing an unrelated field-ranking exercise. Reuse actual accepted context, not inferred approval from progress statements.
The result is a conditional recommendation with a concrete first inquiry.
Do not equate a popular topic, an unread literature, or a long list of papers with a research opportunity.

## Establish the decision

Use the field, intended contribution, background, available resources, and time horizon already supplied.
Show a short done/observed/interpreted/planned/desired summary when it helps verify the starting point. Ask only for missing details that change the scope decision. This intake is not another gate.
Ask only for information that could change the recommendation; continue useful mapping while it is missing.
If resources are unknown, show recommendations under explicit resource assumptions.
Do not assume access to equipment, proprietary data, specialist collaborators, or large computing budgets.
Respect a chosen direction: assess and narrow it instead of reopening the entire field without a reason.

Separate three questions:

- What does the researcher need to understand?
- What does the available literature leave unresolved?
- Which unresolved question can this researcher usefully investigate?

## Build an evidence-backed map

Identify the main subfields by the problems they address, not only their jargon or techniques.
For each relevant branch, record the central question, strongest established result, remaining limitation, and typical evidence.
Compare branches only on criteria they actually share; explain complementary roles when direct ranking is misleading.
Use reviews and authoritative teaching sources to orient the search, then inspect primary studies for decisive claims.
Verify current field-status claims before recommending a direction.
Search the obvious terminology, equivalent vocabulary, nearest prior work, and evidence that challenges the proposed gap.
Include negative results, failed approaches, replications, and changes in assumptions when relevant.

Keep a compact search record containing:

- Search date, source venues or databases, queries, and the coverage cutoff.
- Inclusion boundaries and meaningful exclusions.
- Closest relevant work and why it does or does not answer the proposed question.
- Unavailable full texts, language or indexing limits, and unresolved citation matches.

Trace each consequential claim to an inspected source location, such as a section, figure, table, or page.
Record access status: full text, partial text, abstract only, or metadata only.
Keep reported observations, authors' interpretations, and your own inferences distinct.
Do not imply full-text verification from an abstract or search snippet.
If current sources cannot be accessed, give a provisional map and identify what must be checked before commitment.

## Classify the uncertainty

Label each candidate as a learning gap, an established practical bottleneck, a documented disagreement, or a proposed open question.
For an open question, name the nearest existing answer and the exact condition, mechanism, bound, or scope it leaves unresolved.
State whether openness is explicit in a source or inferred from the inspected evidence.
Use "not found within this search" when that is all the search establishes.
An absence of search results does not establish novelty.
Check whether an apparent disagreement disappears after aligning definitions, conditions, measurement limits, or evaluation criteria.
Treat replication and measurement improvement as potentially valuable contributions even when the broad question is familiar.

## Recommend directions with visible tradeoffs

Assess the candidates using separate judgments:

- **Importance:** what understanding or capability would change if the question were answered?
- **Uncertainty:** what competing answers or unresolved limits remain, and on what evidence?
- **Tractability:** can available methods distinguish the answers within the relevant constraints?
- **Resource fit:** what access, skills, data, collaboration, and time are required?
- **Information value:** would an unsuccessful or negative outcome still narrow the question?

Use qualitative comparisons unless a defensible quantitative model is available.
Do not conceal tradeoffs inside an unexplained total score or equate publication volume with importance.
Recommend a small set justified by the evidence rather than a fixed number of options.
For each recommendation, include its strongest objection, the assumption most likely to fail, and a cheaper initial check.
State how the recommendation changes under different resource assumptions.
Distinguish a long-term direction from a first project that contributes to it.

## Finish with an actionable choice

Use [field-brief.md](references/field-brief.md) for the reviewable subfield brief.
End with the preferred subfield, boundaries, why it matters, assumptions, and a short learning/reading route. Recommend foundational and representative methods articles with verified links and access status, explaining what each teaches. Mark a source-dependent recommendation provisional when its evidence cannot be inspected.
Complete any necessary source or prerequisite checks within this stage, then ask the user to accept this specific brief or revise it. Proposed later research actions may illustrate tractability; do not execute a future-stage project to settle the scope.
Do not require an exhaustive survey before taking an informative first step.

For an ongoing project, preserve the selected direction, search limits, open assumptions, and next decision in project files when requested or needed for continuity.
Keep project evidence and personal context outside this installed skill.
After acceptance, `research-question` can select important questions and `research-guide` can coordinate the workflow. Before acceptance, remain in stage 1. If companions are unavailable, honor the same stage boundary directly.
Never claim that a recommended direction is guaranteed to be novel, feasible, or publishable.
