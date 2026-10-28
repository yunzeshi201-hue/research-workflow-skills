---
name: research-papers
description: "Analyze, classify, and synthesize papers from a user-specified local folder and online literature. Produce a cited comparative report and proposed file categories; organize files under the original folder only after the user accepts the concrete plan. Works independently or as bounded support for a research stage."
---

# Research Papers

Turn a local collection, an online search, or both into an inspectable evidence corpus, a useful classification, and a comparative literature report. A paper-analysis request does not require choosing a new research field, building a website, or completing the four-stage research workflow.

## Establish the task and source boundary

Reuse the user's topic, question, existing categories, preferred language, and demonstrated knowledge. Determine whether they want analysis only or also physical file organization. Do not assume a beginner curriculum. If comprehension is relevant, offer a short sourced concept explanation and a task-specific understanding check; keep inventory and other independent work moving. A request to organize familiar papers does not require passing a quiz.

For local papers, ask for the source folder path if it is missing. A request to author this skill is not permission to search the user's computer for papers. Read only the named folder and the agreed recursion scope; never substitute a whole-PC search. Use available local-file/PDF tools. If local access is unavailable, explain what access is needed without claiming to have inspected files.

By default, supplement the collection with relevant online literature: missing foundational work, closest related studies, recent developments, methods, and contrary findings. Respect a local-only instruction. Do not make the report depend on a complete online search when access is limited; disclose its coverage. Search with public bibliographic metadata or generic scientific terms. Private drafts, annotations, unpublished results, local paths, and document contents are not automatically authorized for upload or external search.

Record the intended output location according to the user's current output rules. Reports, extraction caches, and proposed plans can be written there before classification acceptance. Do not create classification folders or rearrange source files during analysis.

## Build and analyze the corpus

Read [corpus-analysis.md](references/corpus-analysis.md) for inventory, deduplication, extraction, online supplementation, and report requirements.

1. Inventory the specified collection without modifying it. Record each file, its identity, reading status, and any access or extraction failure. Link supplements and versions rather than counting them as independent studies.
2. Inspect available texts and relevant figures. A filename, abstract, OCR extract, or citation record is not evidence that the full paper was read. Mark what supports each summary.
3. Search online within the stated topic and purpose. Record queries, search date, inclusion decisions, verified identifiers, and inspected locations. Keep online additions distinguishable from locally held papers while deduplicating shared studies.
4. Propose a classification suited to the user's decision. Explain category boundaries, evidence for assignment, cross-category tags, and uncertain assignments. Prefer one primary physical category per paper, with secondary labels in the index.
5. Write a complete report for the declared, actually processed corpus: classification, paper-level summaries, cross-paper synthesis, methods and evidence comparisons, disagreements, gaps, and a referenced reading route. Reconcile all inventoried records, including deferred and unreadable ones. A large unfinished corpus must be labeled partial rather than silently sampled and called complete.

Use independent extraction or search branches when helpful, but reconcile identifiers, categories, and evidence centrally. Parallel analysis does not authorize concurrent edits to the source collection.

## Present the classification before organizing

The report must show the proposed categories, their definitions and paper counts, representative papers, and ambiguous cases. When physical organization is requested, also provide a file-level source-to-destination mapping. For a large library, provide the complete mapping as an attached table and a readable summary in the report. Include the exact source root, proposed folder names, and whether operations are copies or moves. Distinguish online-only records from files actually present.

Ask whether the user accepts this specific classification and operation plan. Explain that this checkpoint follows the requested review-before-filing workflow. A general request to sort the collection is not acceptance of categories that have not yet been shown. Clear acceptance of an already presented plan can be reused without another confirmation. Partial acceptance or requested category changes unlock only clearly approved, separable operations; otherwise revise the plan first.

If the user wants only a report, deliver it and stop without creating category folders. Accepting a literature report is not by itself an instruction to modify source files.

## Apply an accepted file plan

Read [folder-organization.md](references/folder-organization.md) before any source-folder mutation.

Create the accepted category subfolders beneath the original user-specified root. Use non-destructive copies by default, explicitly described in the plan. Moves require the user's clear request or acceptance of a plan explicitly specifying moves. Do not overwrite, delete duplicates, silently rename originals, or relocate unrelated files. Preserve original bytes, map every operation, verify destination contents, and report skipped or failed actions. A file discovered after approval is not silently added to the approved operation set.

Online supplementation does not automatically mean downloading every paper. Cite online-only sources in the report and index. Download only through legitimate available access when included in the user's requested scope, and include such downloads in the proposed placement plan. Never claim an online-only paper has been filed locally.

## Work independently or return to the coordinator

Standalone mode ends with the report, portable index, and optional verified organization manifest. It does not need a website or a research-stage acceptance record. The file-plan approval is a separate decision from scientific scope, questions, or corpus acceptance.

When called by `research-guide`, inherit the active stage and its scope. Early stages can use a bounded subset or comparison; a standalone whole-library request remains a separate deliverable. Return verified records, source locations, category suggestions, and evidence gaps. Do not mark a stage accepted, expand an accepted corpus, build a website, or draft the stage-4 review merely because this skill completed an analysis. The coordinator can propose using this corpus at the appropriate checkpoint.

Keep source documents, local paths, completed reports, approvals, and manifests in private project storage. The reusable skill contains only general instructions.
