# Analyze a Local and Online Literature Corpus

## Inventory and identity

Use the supplied root and agreed subfolder scope. If the user says the folder is their library, recursive inventory within that root is reasonable unless excluded; state the scope and exclude generated output folders from later rescans. Do not follow shortcuts, symbolic links, or directory junctions outside the agreed root. Identify reference-manager-managed libraries before proposing physical changes; their database and attachment relationships may require an export or the manager's supported interface.

Create a stable record ID for each study and a separate file/attachment ID where necessary. The portable index should retain:

| Record | Required information when available |
|---|---|
| Identity | Title, authors, year, venue, DOI or other verified identifier; conflicts and verification status |
| Provenance | Local, online, or both; source-relative file path; source URL; version relationship |
| Access | Metadata only, abstract, partial text, full text inspected; separate Methods, SI, and figure inspection |
| Content | Research question, system/context, design/method, reported result, authors' interpretation, limitations |
| Classification | Primary category, secondary tags, assignment reason, uncertainty, supporting location |
| Files | Relative path, byte size, content hash for planned operations, attachment/version links |
| Search | Discovery query/source, search date, inclusion or exclusion reason |

Store absolute source roots only in private operational records where needed; prefer source-relative paths in shareable exports. Do not publish private indexes automatically.

Deduplicate at two levels. Byte-identical files are file duplicates; matching verified identifiers and inspected content may establish publication versions of one study. Similar filenames or titles alone are not enough to merge records. Preserve all original files and identify duplicate groups without deleting them. Keep preprints, accepted manuscripts, published versions, corrections, retractions, and supplements linked with their distinct status. A correction or contradictory later paper is not merely a duplicate.

## Read with explicit limits

Use available local readers and the relevant PDF skill when pages, figures, or layout matter. Check extraction quality before relying on it. For scanned papers, use local OCR when available; flag uncertain formulas, tables, captions, or numbers and inspect the corresponding page image where possible. Unreadable, encrypted, damaged, or unsupported files remain in the inventory with a concrete reason and next action.

For each included paper, extract the question, approach, conditions, central observations, evidence supporting the claim, interpretation, controls, limitations, and relevance. Cite exact pages, sections, figures/panels, supplementary locations, or code. Keep observation, inference, and your own assessment separate. Summaries based only on abstracts must say so and cannot supply missing methods or detailed numerical results.

Where useful to the report, explain key inspected figures: intended claim, measured observable, relevant panel, supporting comparison/control, and limits. Retain attribution and reuse status if an image is reproduced. A text explanation with a source link is acceptable when the image cannot be included. Do not invent an image, measurement, citation, or missing protocol setting.

For experimental guidance, distinguish what prior studies actually did from a proposed adaptation. Include verified Methods/SI locations, reported preparation and setup, controls, analysis, result, and limitations. An absent condition stays missing. When available, the optional `research-test-design` companion can expand this evidence record within the current task's scope.

## Supplement online

Start from the collection's verified public topics, references, and unresolved comparisons. Search both foundational and recent work, primary methods/protocol papers, contradictory evidence, and relevant reviews. Verify identities against primary publication or repository records. A search snippet identifies a candidate; it is not a substitute for inspecting the source supporting a claim.

Record search sources, date, queries, scope, and selection reasons so the reader can see what was covered. Do not promise exhaustive coverage from a few searches or label a narrative report a systematic review without the necessary search and screening process. If the user requests systematic coverage, specify its protocol and deliver what is feasible, with omissions visible.

Add online records to the same study index while keeping their origin and reading status visible. When a locally held paper is found online, enrich its existing record instead of inflating the paper count. Distinguish an online bibliographic record from an acquired full text. Use available legitimate access; a missing full text is an access gap, not permission to bypass restrictions.

## Choose categories that answer a need

Choose the main classification axis from the user's purpose: research question, mechanism, method, application, evidence type, or another defensible axis. Avoid mixing unrelated axes at the same level without explaining the rule. Reuse useful existing user categories rather than inventing a new taxonomy automatically.

Give each category a definition, inclusion/exclusion rule, paper count, representative studies, and research relevance. Use secondary tags for overlapping methods or applications. One primary folder can hold the local file while the index supports multiple views; do not create multiple physical copies solely to satisfy every tag unless explicitly requested. Put genuinely unresolved assignments in a visible pending category in the proposal. Low confidence is a reason to inspect further or disclose uncertainty, not to guess from a filename.

## Report and export

A full analysis report for the declared corpus contains:

1. **Scope and coverage:** User purpose, local inventory totals, unique study count, online additions, excluded/deferred/unreadable records, search date, and access limits. Reconcile file counts separately from study counts.
2. **Classification proposal:** Category definitions, counts, membership, reasons, overlapping tags, and uncertain assignments. Include the complete file-placement table when organization is requested.
3. **Paper-level digest:** Each included study's question, method, findings, claim-to-evidence link, limits, and precise source locators. Longer digests may be appendices, but every inventoried item has a status.
4. **Cross-paper synthesis:** What categories establish, disagreements and their possible methodological/contextual causes, incomparable conditions, evidence strength, and unresolved questions. A list of abstracts is not synthesis.
5. **Method and experimental lessons:** What relevant studies did, controls that matter, transfer limits, and source-backed next reading or testing actions. Omit irrelevant experimental sections for nonexperimental tasks.
6. **Reading route and references:** Priorities appropriate to the user's knowledge, why each paper matters, verified identifiers/direct links, and any source-access gaps. Add a concise sourced foundation explanation only where it helps the reader interpret the report.
7. **Decision for the user:** Ask whether the shown categories and, if requested, the explicit copy/move plan are acceptable. Keep this decision separate from accepting scientific claims.

Deliver a machine-readable index (for example CSV or JSON) alongside the readable report when a collection is being processed. Include a bibliography export when useful. Keep report IDs and index IDs consistent. Check totals, membership, citations, and file links before delivery. For large collections, report progress by processed records and identified gaps; do not silently narrow a requested complete analysis.
