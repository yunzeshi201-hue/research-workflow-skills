---
name: research-review
description: "Write a question-led literature review from an accepted research paper-library website and its versioned evidence corpus. Use at stage 4 of the research workflow, after the subfield, important questions, and website corpus have been settled with the user."
---

# Research Review

Explain what prior work establishes, where the evidence disagrees or remains incomplete, and which questions remain worth investigating. Build the review from the accepted paper library and its selected questions.

## Check the stage before writing

This is stage 4 of the ordered workflow: subfield -> important questions -> paper-library website -> review. Read the project workflow record and the accepted artifacts. Proceed only when user acceptance is recorded for the current subfield scope, question set, and website/corpus version.

Use `research/workflow-state.json` when no equivalent project record exists. Check the upstream stages' `status`, `artifact_revision`, `depends_on`, and `acceptance` evidence. Dependencies must match the currently accepted artifact revisions. A stage marked `accepted` or an `actor: user` field alone is insufficient without a traceable user decision about that revision. A reopened or stale dependency must be settled before drafting proceeds.

Existing acceptance in a trusted user message may be recorded with its artifact/version context; do not ask for the same acceptance again. A completed website, successful checks, agent agreement, silence, or an initial request to complete all stages is not acceptance of a concrete stage result. A later explicit user instruction to change or bypass the sequence overrides this workflow; record its exact scope rather than inferring a broad exemption.

If a required acceptance is missing, present the actual current-stage artifact, unresolved issues, and the specific decision needed. Do not draft the review or silently manufacture approval. If a user explicitly asks only for critique of an existing review, perform that bounded critique without presenting it as completion of this stage.

A local website preview can satisfy stage 3 when that is the accepted deliverable. Public deployment is not an inherent prerequisite. The accepted library must be inspectable through accessible source records or a structured corpus export, with a stable snapshot identifier or version. An inaccessible site URL alone is insufficient evidence for drafting.

These instructions are self-contained. If `research-guide` is available in the skill catalog, use its project state conventions; otherwise retain the acceptance record and artifact versions in an equivalent project record.

## Freeze the source boundary

Record the accepted subfield, selected question IDs, corpus snapshot/version, literature cutoff, search boundaries, and known access gaps. Prefer a structured export or source dataset over extracting paper records from screenshots. Retain stable paper IDs and links back to question pages and paper details where available.

Confirm that the export matches the accepted website/corpus version. Keep the snapshot unchanged while drafting. Use project files for review notes and derived evidence records; installed skill folders contain reusable instructions only.

Deeper reading of included papers is part of this stage. Inspect primary text, methods, figures, and supporting information needed for decisive claims. Record what was actually accessible. Abstract-only records can support limited reported summaries; they cannot establish detailed controls, numerical comparability, or a mechanism that has not been examined.

If a crucial paper is absent, a key record is wrong, or the intended review exceeds the accepted questions, identify the effect on the review and return the change to the appropriate earlier stage. Obtain acceptance of a materially revised scope or corpus before integrating it as the new basis. Continue independent work on unaffected sections when useful, but do not treat the changed review as ready for final acceptance.

## Choose an honest review form

Use a focused critical narrative review unless the user requests another form and the source process supports it. A systematic or scoping review requires an appropriate protocol, documented search and screening, eligibility rules, and corresponding reporting; a large website or bibliography does not establish those properties.

State the intended reader and level of explanation from the request. Define only the concepts needed to understand the selected questions. Use the accepted scope to resolve routine outline choices rather than introducing an extra approval step for every section.

Read [review-outline.md](references/review-outline.md) to organize the review and [claim-audit.md](references/claim-audit.md) to verify its evidence.

## Synthesize across papers

Organize the main argument around the accepted questions. Within each question, explain the competing approaches or explanations, what evidence each contributes, their limits, and the current answer supported by the corpus. Use a historical sequence when it explains why the problem or interpretation changed.

Compare studies only after aligning their definitions, systems or populations, conditions, measurement procedures, evaluation criteria, and uncertainty. Distinguish genuine disagreement from different questions or operating regimes. Preserve incompatible results when their cause remains unresolved.

For each consequential claim, retain question ID, paper ID, source locator, access level, observation, interpretation, assumptions, and supporting or conflicting evidence. Separate an author's conclusion from the review's inference. A review article can provide orientation; trace decisive scientific claims to inspected primary evidence where available.

Do not count a preprint and its journal version, repeated analyses of one dataset, or multiple descriptions of the same experiment as independent confirmation. Explain the basis for agreement or confidence rather than declaring consensus from a paper count.

Translate evidence gaps into bounded research questions. Distinguish a missing observation, inadequate precision, nonidentifiability, an untested condition, an unresolved disagreement, and a gap in the searched corpus. Compare each proposed question with its nearest existing answer. Do not claim that no one has studied a problem merely because the accepted library lacks it.

## Connect the review to experimental decisions

Include a practical reading route when the selected questions require experiments. Identify the important primary, methods, protocol, control, calibration, and analysis papers already in the accepted library. Prioritize them by the experimental decision they inform and their evidential relevance rather than journal prestige or citation count alone.

For each proposed approach, state the uncertainty it can resolve, alternative methods, prerequisites, relevant source locations and conditions, essential controls, common artifacts, and analysis checks. Distinguish procedures that plausibly transfer from settings or assumptions that require validation in the intended system. Mark missing implementation details explicitly; do not invent working parameters.

Show what prior studies actually performed in a referenced comparison, rather than only listing method names. Map the proposed experimental sequence to those papers and their inspected Methods/SI/protocol locators, separating source-reported conditions from proposed adaptations. Attach the verified references to the review. Distinguish prior literature, the researcher's completed work, and future work; a model's proposed protocol is not a performed experiment.

Give a reading order with a concrete extraction or readiness task for each paper, followed by an evidence-based path for choosing a pilot or discriminating experiment. If a needed protocol paper is outside the accepted corpus, propose its addition and return it to stage 3 for acceptance before incorporating it. These are reviewed recommendations, not authorization to execute experiments.

## Draft and verify

Write precise scholarly prose. Match confidence to evidence, attach citations to the claims they support, and preserve numerical definitions, units, conditions, and uncertainty. Avoid promotional language, vague attributions, and promises of publication or discovery.

Resolve bibliographic entries from verified metadata. Check citation-to-claim fit, reference identity, version relations, and source locations. Reopen the decisive evidence for central, numerical, or disputed claims. Narrow unsupported claims or report the limit explicitly; do not invent citations or conceal access gaps behind a general reference.

Use comparison tables or diagrams when they clarify relationships. Every evidential entry must remain traceable. Label conceptual diagrams as synthesis and distinguish them from measured results. Render and inspect the chosen output format using available document tools when layout matters.

## Deliver and settle stage 4

Return the review in the requested format, its verified bibliography, the corpus/version and search-limit statement, and a compact claim-audit record. Explain the strongest supported answers, important remaining disagreements, and a small justified research agenda. Proposed experiments or calculations are implications of the review; do not execute a new research program as part of writing it.

Provide question and paper backlinks using stable IDs or verified URLs. Keep the review as a separate artifact unless the user requests website integration. Do not modify a deployed site or expand its sharing merely because the review is finished.

Mark the stage `ready_for_confirmation` only after the evidence and delivery checks pass or their remaining limitations are clearly presented for a bounded decision. Show the concrete deliverable and ask whether this stage is settled or needs revision. Record the user's acceptance of the reviewed `artifact_revision`, its evidence reference, and any conditions before marking the stage `accepted` and the workflow complete. Elapsed time or lack of a response does not close the gate.
