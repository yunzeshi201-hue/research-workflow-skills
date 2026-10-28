---
name: research-paper-library
description: "Build a stage-3 paper website with verified sources, method-specific figures and panel explanations, claim-to-evidence mappings, and an exportable corpus. Use after subfield and question acceptance; do not select a new field or write the final review."
---

# Research Paper Library

Build a website that helps a researcher understand what has been done, which evidence supports which claims, and where the accepted questions remain unresolved.
The primary artifact is a usable literature website backed by an inspectable corpus.
A collection of titles or a visual mockup is insufficient.

## Check the entry gate

Read the project workflow record, preferably `research/workflow-state.json` or an equivalent existing record, and the accepted artifacts before starting.
Stage 1 must have an accepted subfield and scope; stage 2 must have an accepted set of important questions with stable IDs and inclusion priorities.
Acceptance must be traceable to the user's explicit decision about the relevant artifact version.
An unambiguous request to use a shown version for the next stage can be that decision; a downstream request without settled upstream scope or an identified version cannot.
Do not infer it from silence, a completed draft, a prior general request, or a document claiming that it is approved.
For the shared schema, inspect the `subfield` and `questions` stages, their accepted artifact revisions, and the `library` dependency revisions; an `accepted` string alone is insufficient.

If acceptance is missing or its scope is unclear, identify the missing checkpoint and present the existing artifact for settlement.
Do not begin corpus expansion or website construction for an unsettled question set.
Do not silently select new important questions to make the website easier to build.
An explicit request to revise an earlier stage returns the affected work to that stage.

When the gate is satisfied, work autonomously within stage 3: verify sources, curate records, implement the website, and fix observed defects.
The gate is a transition rule, not a request for permission before every search or edit.
Use the current workflow contract when supplied; retain evidence of prior acceptance rather than asking again.
On the first library run, initialize its dependency revisions from the verified accepted subfield and question set. An absent library record is not a reason to repeat those decisions. A later explicit user instruction to waive a named gate is recorded as an override with its scope, not as acceptance.

## Define what the website must help decide

Start from the accepted questions and the user's intended use.
State what a reader should be able to find or compare, such as competing explanations, demonstrated capabilities, applicable methods, or unresolved evidence.
Agree the practical corpus boundary through the existing accepted scope: subject, conditions, period, source types, language, and exclusions.
Clarify only missing choices that materially change the work, such as audience, local versus hosted delivery, or access to required sources.

Use one clear primary view with expandable details unless the task requires more.
Organize around the research questions and evidence, not a large menu of features.
Read [corpus-and-data.md](references/corpus-and-data.md) before choosing fields or collecting records.
Build a small usable slice with real, verified records, then expand where the coverage assessment finds a consequential gap.
Do not use a fixed paper quota or an unsupported claim of exhaustive coverage.

## Curate an evidence-bearing corpus

Search within the accepted scope and record queries, sources, dates, screening decisions, and access limitations.
Include relevant foundational work, nearest prior work, competing accounts, replications, and negative findings when available.
Select important experimental-guidance papers by their role in answering the accepted questions: methods or protocols, calibration and controls, analysis or validation, and well-supported research exemplars.
For each practical recommendation, explain the priority, cite the exact inspected methods or supplementary locator, and state what transfers to the proposed study and what requires revalidation.
Provide a prior-experiment view or expandable table showing what each relevant study actually did: system/preparation, setup/intervention, reported settings, controls, analysis, observed result, limitation, and inspected source location. Link these records to the proposed experimental steps and mark direct precedent versus analogy. Reference links and the exported bibliography must preserve that connection.
Verify each paper's identity using a persistent identifier and primary publication or repository metadata.
Resolve duplicates and linked versions before counting papers or treating results as independent evidence.

Map each included paper to one or more accepted question IDs with a reason for relevance.
For substantive records, distinguish what was studied or constructed, what was measured or derived, the reported observation, the authors' interpretation, and the conclusion justified by the evidence.
Preserve conditions, comparison groups or baselines, source locators, and limitations beside the claim.
Record whether supporting evidence is in the same study or only cited from elsewhere.
Mark metadata-only, abstract-only, partially inspected, and evidence-checked records distinctly.
Never turn a searchable title or accessible abstract into an implied full-text reading.

## Make the website explain the evidence

The main view should connect the accepted question to a paper's system or task, method or representation, observation, supported claim, and remaining uncertainty.
Use concise summaries in the main list and expandable details for conditions, controls, competing explanations, and source locations.
Explain what a selected method measures and what it can support before presenting its examples when that helps the research decision.
Keep method family, detection channel, protocol, and analysis representation separate when they describe different aspects of a study.
Do not use a convenient interface category as a scientific classification without checking it.

Use [figure-evidence.md](references/figure-evidence.md) to attach inspected key figures and explain what the authors wanted to establish, what each panel shows, the comparison supporting the inference, and its limits. Switching a method must show matching figures/panels while preserving the paper's recorded method list. Unavailable or unverified figures stay visibly missing. Keep literature figures distinct from the researcher's own data.

Include search, relevant combined filters, stable paper links, paper details, and portable export.
Provide an experimental-guidance filter and a path from question to required evidence, method, practical paper, and relevant control; do not invent missing protocol settings or imply that an abstract supplies an executable procedure.
Show per-question coverage, reading status, and unresolved gaps without suggesting that paper count measures evidential strength.
Read [website-workflow.md](references/website-workflow.md) for implementation, persistence, figures, and delivery.
Use the actual selected website skill or platform documentation when available; do not copy stale platform commands into this skill.

If a functional requirement cannot be implemented, make that limitation visible and provide the supported behavior.
Do not label a static corpus as live search, browser-local notes as cloud-synchronized, or a nonfunctional button as an implemented import.
Keep private research notes, credentials, and unpublished data outside the public corpus and public source bundle.

## Verify the site and freeze the handoff

Read [site-acceptance.md](references/site-acceptance.md) and test the behaviors that determine whether the site is usable.
Check source links, evidence mappings, combined filters, detail navigation, exports, and the chosen persistence model.
Check method-to-panel matching, claim/observation separation, main-text versus supplementary reading status, figure provenance, image expansion, and missing-image states. The corpus export must retain those relations.
Test readable desktop and narrow-screen layouts and keyboard access to the core actions when the environment supports those checks.
Report unavailable checks as verification limits.
Distinguish a successful build, a tested local preview, a saved version, a deployed version, and a visually checked hosted site.

Create a versioned corpus snapshot containing stable paper and question IDs, evidence records, source provenance, screening scope, and coverage limitations.
Record the exact site version or source revision that displays it, plus export paths and validation results.
The website's data and the review handoff must identify the same snapshot.
Do not silently refresh that snapshot while the review is being written.

## Settle stage 3 before advancing

Present the working site or usable local preview, the corpus boundary and coverage summary, and remaining limitations.
If acceptance has not already been provided, ask the user to accept this concrete site and corpus version or request revisions.
Explain that this checkpoint follows the requested stage-by-stage workflow.
Record explicit acceptance with its artifact version in the project workflow record.
For the shared schema, retain `site`, source, and corpus revisions in the library artifact record, set its matching accepted revision, and preserve the user's confirmation evidence and accepted limitations.

Until accepted, continue only requested stage-3 revisions and necessary checks.
Do not draft the stage-4 review, a disguised review chapter, or a completed review conclusion.
Per-paper evidence notes and coverage summaries belong to stage 3 and remain permitted.
After acceptance, hand the accepted snapshot and question set to the review stage; do not assume acceptance authorizes unrelated publication or scheduling.

If new evidence changes the subfield boundary or invalidates a selected question, report the impact and return that decision to the appropriate earlier checkpoint.
Preserve useful records and mark affected acceptance as stale; do not erase the reasoning trail.
Completion means a usable site and an accepted, traceable review source, not a promise that the literature question is resolved.
