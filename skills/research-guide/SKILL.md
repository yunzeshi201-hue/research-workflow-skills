---
name: research-guide
description: "Coordinate an explicitly requested four-stage research project: settle a subfield, choose questions, build a paper-library website, and write a review. Resume accepted stage decisions. Focused explanations, paper reading, figure analysis and standalone research questions belong to researchskills."
---

# Research Guide

Use this coordinator for the explicitly requested four-stage project. Use [task-routing.md](references/task-routing.md) to distinguish it from focused explanations and paper analysis. Route a focused research question to `researchskills`, or collection classification/organization to `research-papers`, without starting project stages. Do not route back merely because those tasks involve research.

For a full research project, run the original four stages in order. Complete useful work within the current stage, show a concrete result, and wait for the user's acceptance before starting the next stage. The goal is a question-led account of what others have done, what remains unresolved, and which methods could address it.

For a request only to classify, summarize, compare, or organize local/online papers, invoke `research-papers` directly. It produces a literature analysis report without requiring subfield acceptance, a new question set, or a website. Ask for the local folder path if local files are requested and no path is supplied. Its classification acceptance authorizes only the specified file organization, never a research-stage transition.

## Start with what is already done and wanted next

Accept the researcher's natural description of completed work, observations, and intended outcome. Use [research-intake.md](references/research-intake.md) to reconstruct a short project brief, separating user reports, inspected evidence, interpretations, plans, and unknowns. Ask only for missing information that changes the next decision. The researcher does not need to name a field or fill in a form first.

Use an existing specific subfield or question as the starting scope instead of forcing broad topic selection. Reuse verified earlier stage decisions. Intake is preparation for the current task, not an extra approval gate or permission to bypass existing gates.

Reuse the 1/2/3 depth chosen through `researchskills`. If no level is supplied, clearly implied or inherited, ask once with brief descriptions: 1 quick understanding (core idea and caveat), 2 research analysis (mechanisms, methods and evidence), 3 deep critical analysis (alternatives, assumptions and decisive checks). Recommend 2 but wait for the user's choice before substantive stage work. Do not repeat this question in supporting skills or related follow-ups. Explain prerequisites as part of the current work and reuse demonstrated knowledge. Training, tests and learning plans are optional outputs requested by the user, not an entry requirement. Depth selection is separate from the four project stages.

## Check consequential reasoning within the task

Identify a bounded question when competing explanations, uncertain method transfer, identifiability, or an experimental choice could change the decision. Analyze it in the current task, using a bounded subagent check when available and useful. Follow [model-routing.md](references/model-routing.md) for delegation or an explicitly requested separate consultation. Keep the user's currently verified model choice; the research skill does not impose a model or product preference.

Only create a separate user-owned chat when the user explicitly requests that action and the available tools support it. A depth-3 request, skill button, empty template or old automatic-routing default does not request a new chat. Reuse actual authorization for follow-ups within its scope. The [consultation brief](assets/deep-research-handoff.md) is optional supporting context, not a mandatory dispatch step.

Verify decisive claims and citations before applying returned recommendations. Record useful changes and remaining uncertainty. A model answer is a proposal, not independent scientific evidence or user acceptance; it cannot advance a stage by itself.

## Determine the current stage

Apply this section only to the four-stage project route. A standalone paper or learning task keeps its own output record and does not create or change project-stage acceptance.

Read the project workflow record and the evidence of earlier user decisions. Prefer `research/workflow-state.json`, or reuse an equivalent existing record. An optional `research/consultation-policy.json` can preserve routing preferences and actual human authorization independently of scientific stage decisions. Keep filled records in the project, outside installed skills and public releases. Use [stage-gates.md](references/stage-gates.md) for the acceptance and revision contract; the [empty record](assets/workflow-state.example.json) is an optional starting template.

Find the earliest stage whose accepted version is missing, stale, or unsupported. A file's existence, a successful test, deployment, agent agreement, and a status label alone do not prove acceptance. Reuse a verifiable prior user decision for the same version without asking again. If evidence is unavailable, present the specific checkpoint that needs settlement instead of restarting all work.

A request to complete the whole workflow does not accept its future outputs. A later explicit instruction to waive or change a named gate can override it; record the user's scope as an override, not as fabricated acceptance. An unrelated request to explain a concept does not need to initiate this workflow.

The user can settle a clearly bounded provisional scope or question set with disclosed evidence gaps. Record those limitations and the next verification tasks; acceptance of a working direction does not establish its novelty or scientific premises. Unclear scope must be repaired before it is ready for a decision.

## The four stages

| Stage | Skill | Work and concrete result | What must be settled before advancing |
|---|---|---|---|
| 1. Specify a subfield | research-field-map | Compare plausible directions using preliminary literature; define one subfield, boundaries, resource assumptions, and a short prerequisite/reading plan | The user accepts the selected subfield and its boundaries |
| 2. Choose important questions | research-question | Select a manageable, prioritized set of questions; give each a stable ID, significance, nearest prior work, unknown, and feasible evidence route | The user accepts the question set and priorities |
| 3. Build the paper-library website | research-paper-library | Build an inspectable website and verified, exportable paper corpus organized around the accepted questions, including experimental-guidance papers | The user accepts the working site and a specific corpus snapshot with its coverage limits |
| 4. Generate the review | research-review | Synthesize the accepted corpus by question, compare evidence and methods, explain disagreements and gaps, and provide a practical reading and research route | The user accepts the review or requests revisions |

Discover these skills through the available catalog and read the current stage's instructions. They need no fixed installation path. If a companion is absent, follow the stage's result and acceptance requirements directly. Do not invent unavailable website or source-access capabilities.

Stages 1 and 2 require enough reading to justify choices. They may recommend important papers and discuss which evidence a possible experiment could provide. They do not authorize implementing the website, assembling an unrelated exhaustive corpus, drafting the full review, or running proposed experiments ahead of the relevant gate.

## Important papers must serve a decision

Recommend articles because they answer a selected question or teach a needed research action. Distinguish foundational explanations, closest prior work, competing evidence, methods/protocols, calibration/control studies, and analysis/validation papers. Prestige and citation counts alone do not establish usefulness.

For a recommended experimental paper, explain why to read it, the experiment or decision it informs, and the relevant Methods, supplementary information, protocol, figure, or code location. Separate transferable reasoning and procedures from conditions that must be checked for the intended system. Missing full text or procedure details are explicit gaps; do not invent settings, tolerances, or an executable protocol from an abstract.

Retain the link `question -> evidence needed -> method -> important paper -> control or validation`. Stage 3 makes this searchable; stage 4 synthesizes it into practical guidance. A methods paper can be more useful for this purpose than a headline discovery paper.

For each substantive experimental recommendation, include a referenced account of what prior studies actually did: system/preparation, setup/intervention, reported conditions, controls, analysis, outcome, and limitations. Map the proposed steps to inspected source locations. Separate direct precedents, related-method analogies, and new adaptations. Attach a verified reference list with DOI or source links; citations alone cannot fill missing procedure details.

## Learning and design are supporting work

`researchskills` supplies explanations, paper/figure evidence and the selected analysis depth inside the active stage. `research-test-design` assesses whether a question is tractable and extracts useful experimental guidance. These are supporting capabilities, not extra stages or ways to bypass acceptance. Within stage 2, design output remains a feasibility/design sketch; execution of a new study is outside this four-stage workflow unless separately requested.

`research-papers` can supply bounded reading, comparison, and classification evidence to any active stage. Limit its output to that stage's decision: invoking it within stage 1 or 2 does not authorize a full stage-4 review. A separately requested standalone paper report is allowed and remains distinct from the project's accepted review. Reusing that report later requires reconciling its scope, sources, and corpus version at the applicable checkpoint.

For source-intensive work, use available literature skills and tools after reading their actual instructions. Preserve this workflow's gates when a supporting skill would otherwise continue automatically. When building an actual website, use the available website skill or supported implementation tools. A request to author these reusable skills is not a request to build or publish a research website now.

## Keep evidence and claims distinct

Distinguish a learning gap from an unresolved literature question and a feasibility limit. Record what was searched, when, and what could not be read. An unsuccessful search does not establish novelty.

For consequential claims record source identity, inspected location, access/reading status, conditions, observation, interpretation, and limitations. Audit the bridge from raw observation through processing and inferred quantity to mechanism or function. Several measurements can share a confounder. A paper list or a reproduced computation alone does not establish that a scientific claim is valid.

Use the [decision record](references/decision-record.md) for substantive reasoning and the workflow record for gate status. Keep project data and user decisions outside the installed skills. The public package contains only reusable methods and fictional examples. [Methodology sources](references/methodology-sources.md) explain selected influences and their limits.

## Present a checkpoint

When the stage's artifact is ready, identify its version, summarize the decision it asks the user to settle, give access to the result, and state material uncertainties. Mark it `ready_for_confirmation`, not `accepted`. Ask one specific question about accepting that artifact or revising it. Explain that the pause follows the user's requested stage-by-stage process.

While acceptance is pending, continue only requested or necessary work within that stage. Do not build downstream artifacts speculatively. Clear assent to the identified artifact can unlock the next stage; silence, general praise, partial acceptance, or unresolved requested changes cannot.

If scope or evidence materially changes, preserve the historical accepted version and reopen only the affected stage and dependencies. Cosmetic corrections need not restart the workflow. Completing stage 4 produces a review and a proposed research route; it does not claim that the scientific questions have been solved or automatically launch experiments.
