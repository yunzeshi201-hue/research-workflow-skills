# Corpus and Evidence Records

The corpus is the website's source of truth and the later review's evidence base. Keep it portable and versioned rather than embedding all research content directly in page components.

## Scope and search record

Start from the accepted subfield and question IDs. Record what is included, excluded, and deferred. Relevant boundaries may include system, population, task, conditions, date range, publication types, or the role of adjacent work. A newly discovered direction can be recorded as a proposal; it does not silently become an accepted question.

For each search batch, retain the date, database or source site, actual query, filters, citation-trail source, and access limitations. Preserve screening decisions and reasons for exclusions. Search failure means no matching record was found within this search, not that no prior work exists.

Expand according to coverage gaps. A useful addition may supply a contrary result, a missing method, a boundary condition, a stronger control, or a closer predecessor. More records with the same evidence limitation may add little. No universal paper count establishes readiness for a review.

## Paper identity and provenance

Each paper record needs a stable local ID and verified bibliographic identity. Prefer a DOI or another persistent identifier; retain the canonical source URL. For records without such an identifier, use a stable local ID and a verified citation rather than inventing a DOI.

Retain title, authors, venue or repository, publication date, identifier, canonical URL, source of metadata, and verification date. Distinguish online publication from issue year when they differ. Record corrections, withdrawals, or retractions when found and relevant to interpretation.

Normalize identifiers for deduplication. For papers without identifiers, use title, author, and date comparisons as candidates for review rather than merging by fuzzy similarity alone. Link preprint, accepted manuscript, published article, correction, supplement, and dataset manifestations. Related versions of one study do not constitute independent replications.

## Minimum evidence model

Use the project schema if one exists. Otherwise create records that carry the following information without imposing a particular database technology:

| Entity | Essential content |
|---|---|
| Question | Accepted ID, wording, scope, current version, and why it matters |
| Paper | Stable ID, verified citation and persistent links, version relationships, access and reading status |
| Question-paper relation | Question ID, paper ID, role such as foundational/supporting/challenging/methodological/experimental guidance, and reason for relevance |
| Evidence item | Stable ID, paper ID, question IDs, system or task, conditions, method, observation or derivation, author interpretation, supported claim, limitations, and precise source locator |
| Figure/panel evidence | Stable figure/panel IDs, paper and evidence IDs, method/protocol mappings, authors' intended claim, axes/signal, control, supported inference, limitations, and inspection status |
| Asset | Source, paper and evidence IDs, figure/panel locator, caption summary, reuse status, attribution, and file or external link |
| Search and screening entry | Query or discovery route, date, decision, reason, scope, and access gaps |
| Snapshot | Version, creation date, accepted scope/question versions, included record IDs, data export locations, and integrity identifier |

Use explicit missing or unassessed states. An empty field must not become a false negative, a zero-valued measurement, or a claim that a method was not used.

Use [figure-evidence.md](figure-evidence.md) for the linked image, panel, method, and claim records. Preserve many-to-many relations and the paper's recorded method list. A link-only figure, an inspected image, and an uninspected figure must not share one undifferentiated verified status.

## Important articles for practical research

Recommend articles because they help a consequential research step. A highly cited paper may orient the field while a careful methods paper or protocol supplies the practical information needed now. Do not rank importance by citation count, venue, or recency alone.

Use explicit roles: methods or protocol, calibration/control, analysis/validation, and research exemplar. Connect each recommendation to an accepted question and its required evidence. A paper can have several roles; distinguish primary method authority from an application that uses the method.

For an experimental-guidance card, record:

- The question or decision it helps answer and why it is a priority at this stage.
- The verified citation and exact methods, protocol, figure, or supplementary-information locator, with access and inspection status.
- The studied system and conditions, the measured quantity, and the evidence the method can produce.
- The available preparation, acquisition, processing, and analysis steps at the level actually documented.
- Calibration, controls, artifacts, independent checks, and uncertainty relevant to the intended inference.
- Which principles or steps transfer, which system-specific settings require revalidation, and what assumptions make that judgment conditional.
- Missing implementation details, unavailable supplements, and any reason the paper cannot yet serve as a practical protocol.

Keep source-reported parameters separate from proposed settings. Never invent a missing parameter or transfer a reported value into a new system without justification. An abstract-only application may be relevant reading while remaining unsuitable as experimental instructions.

These cards support learning and study design. They do not claim an experiment has been executed or authorize instrument operation. When the article is insufficient, name the exact missing documentation or validation needed before execution.

## Evidence rather than headline summaries

For each consequential claim preserve this sequence:

`system or task -> method/representation -> observation -> control or comparison -> interpretation -> supported conclusion -> limit`

Separate experiments, simulations, theoretical proposals, and reviews. A proposed capability is not a demonstrated result. A fitted component is not automatically a distinct entity. A plot shape or similar numerical value is not enough to transfer an interpretation to another system.

Record the measurement or evaluation conditions needed to interpret and compare evidence. Preserve units, definitions, uncertainty, normalization, and model assumptions when quantitative values are extracted. Unclear or conflicting quantities can remain visible with warnings but must not enter a numerical comparison as if they were directly compatible.

Locate the actual support in a figure, panel, table, theorem, methods section, supplement, or dataset. State whether a control was performed on the study's own system or cited from other work. Several methods applied to different samples or conditions should not be presented as one matched evidence chain without justification.

## Access and reading status

Use labels such as metadata verified, abstract read, partial text inspected, full text read, and specific evidence checked. Track accessible material separately from inspected material. A downloaded document is not a completed reading.

Keep main-text reading, supplementary reading, and figure/panel inspection as separate fields. A paper can have verified metadata and a partially inspected figure while its complete methods remain unread. Label each claim according to the material actually checked.

An abstract-only record can help discover relevant work and summarize the abstract's explicit claims. It cannot support detailed statements about controls, numerical methods, figure contents, or evidence quality that were not inspected. Keep those missing checks visible in both the website and review export.

Do not present paper counts at different reading levels as interchangeable. Coverage summaries should distinguish indexed papers, inspected papers, evidence-checked records, and unresolved source access.

## Snapshot and review readiness

Export records in a portable structured format such as JSON or CSV and citations in a reusable bibliography format when supported. Preserve one-to-many evidence relations; a flat paper table alone may lose critical claim-level context.

Record a deterministic version or content hash for the reviewed snapshot. Include the exact question versions, search cutoff, exclusions, unresolved conflicts, and access gaps. Validate references between IDs and ensure no included evidence points to a missing paper or an unaccepted replacement question.

The accepted snapshot may contain known gaps if they are explicit and the user accepts a review with that scope. A website listing many sources does not itself establish sufficient evidence to answer every selected question.
