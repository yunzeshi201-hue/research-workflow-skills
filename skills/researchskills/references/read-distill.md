# Read and distill research papers

For a one-off explanation, paper summary or comparison of a few supplied excerpts, answer in the current chat at the selected depth and retain the actual access limits; no external catalog or Markdown files are required. Supplied fictional excerpts remain hypothetical examples, not verified publications. Apply the catalog and persistent-note steps below when the user requests a paper library, batch corpus, reusable distillation or saved notes. Do not turn a brief reading question into corpus construction.

## Establish the requested corpus

For a named research group or researcher, resolve identity using the official group/institution page and researcher identifiers when available. Distinguish current lab output, historical work by the principal investigator, collaborations, and merely citing papers. Record the inclusion rule, date range, publication types, and search cutoff. Infer routine scope from the request; ask only when identity or inclusion ambiguity would change the corpus substantially.

Build the catalog before calling a batch complete. Reconcile an official publication list with at least one independent bibliographic source when available. Paginate each source, follow older-year pages, and retain unresolved candidates. Log query/source, date, returned coverage, and exclusions. Deduplicate primarily by DOI, then title/authors/year; link preprint, accepted manuscript, and version of record as versions of one study. Keep corrections, retractions, and companion papers visible with their relationships.

For an explicit request for all papers, do not substitute a handpicked topical subset. Prioritize batches by relevance and accessibility while retaining every in-scope catalog entry. If complete enumeration cannot be established, label the catalog provisional and specify the missing source or pagination boundary. Evidence learning and critical evaluation are per-paper tasks, not just abstract collection.

## Record what was actually accessible

Track access and review separately for the main article and supplementary information. Use statuses such as `full_text`, `partial_text`, `abstract_only`, `search_excerpt_only`, `unavailable`, or `not_checked`, with source URL, version, and access date. Metadata verification, downloaded PDF, parsed text, visually inspected figure, and full reading are different accomplishments.

Prefer the version of record or an identifiable author manuscript, and primary experiments for quantitative or mechanistic claims. Abstracts and search snippets can seed a record but cannot stand in for the article or SI. Do not fill missing conditions or conclusions from a neighboring paper. If extraction drops equations, subscripts, units, or plot labels, inspect the relevant rendered page. Preserve body-caption-SI disagreements as conflicts until resolved; do not silently choose a plausible value.

## Produce one traceable note per paper

Write a Markdown note in the external library, using a stable paper ID and a descriptive filename. Link it from the catalog. Keep the note focused on the user's research question and long enough to preserve the evidence chain; avoid translating or reproducing an entire copyrighted paper. Use paraphrase and short source-located quotations where indispensable.

Each note should cover:

1. **Identity and access.** Verified title, authors/year, DOI or other stable ID, source URLs, article version, main-text/SI access and reading status.
2. **Research question and design.** What was varied, what was measured, sample/material identity, relevant structure and preparation, comparisons and controls, and the conditions needed to reproduce or compare the claim.
3. **Observed results.** Values, features, trends, and uncertainties anchored to figures, tables, sections, equations, or SI pages. Distinguish reported values from values estimated from plots and from our calculations.
4. **Authors' interpretation.** The assigned species or mechanism, the causal argument, and what evidence the authors use to support it. Preserve qualifiers and alternative explanations.
5. **Our evaluation.** What the evidence supports, what it leaves ambiguous, conflicts or missing controls, and transfer limits to the user's sample or question. A proposed alternative remains a hypothesis until tested.
6. **Reusable knowledge.** The experimental logic, discriminating control, transferable method, writing move, and follow-up question worth retaining. Link related and disagreeing studies rather than flattening them into consensus.

These are information requirements, not a mandatory verbose heading template. For inaccessible papers, create a clearly limited stub with known metadata, available evidence, and the retrieval gap; do not fabricate a full distillation. An abstract-only stub does not count as a read paper.

## Extract quantitative and spectral evidence carefully

Use [evidence-records.md](evidence-records.md) for row fields. Keep compound/material identity separate from sample identity: neat/blend/solution/film, composition, processing, substrate, environment, time regime, and excitation conditions can change the interpretation. Structural similarity permits a search expansion, not a silent identity substitution.

For spectroscopy, distinguish GSB, stimulated emission, excited-state/photoinduced absorption, and electroabsorption before assigning microscopic species. Store the signal definition and sign convention; positive or negative alone is insufficient. Keep peak centers, shoulders, band ranges, kinetic monitoring wavelengths, integration windows, and probe-range edges distinct. Record unit conversions or digitization as derived values with uncertainty.

Assess assignment evidence in context: selective excitation, neat/blend controls, electrochemical or chemical charging, sensitization, magnetic resonance, oxygen response, fluence dependence, time evolution, polarization, and calculations constrain different questions. Record which control was actually reported and read. Long lifetime alone does not prove charges; quenching alone does not establish a unique transfer pathway; a good kinetic fit alone does not identify a microscopic mechanism. Overlap, dynamic shifts, and derivative-shaped responses can invalidate a single-wavelength species label.

## Update the library without overstating progress

Persist completed notes as batches finish. Link each structured record back to its note and original source locator; preserve provenance when correcting a record. Maintain catalog counts for inclusion, access, distillation, and unresolved checks. Add cross-paper comparisons only after comparing the relevant sample conditions and definitions. Bibliographic completeness and evidential certainty are separate properties.
