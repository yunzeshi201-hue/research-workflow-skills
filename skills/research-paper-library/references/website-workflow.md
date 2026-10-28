# Building the Literature Website

Implement the website only after the earlier workflow gates have been satisfied. Use this reference for stage-3 work; it does not authorize a new research direction or the next-stage review.

## 1. Choose the delivery and source model

Inspect any specified existing site and its current source before editing. Preserve its identity, audience, stored data, and unrelated behavior. If no site is specified, create a separate project in the user's workspace. Keep research corpus data separate from generated presentation assets so the same records can serve the site and the review.

Choose the simplest architecture that meets the accepted behavior:

- A read-only static website is appropriate for a versioned, curated corpus and browser-side filtering. Clearly label its corpus cutoff and snapshot.
- A site that saves shared edits, imports new records, or synchronizes notes needs a persistent data service and appropriate access controls.
- Browser-local notes or bookmarks are useful if their device/browser scope is explicit and an export is available. They are not a substitute for shared persistence.

Do not add live retrieval, authentication, analysis engines, or scheduled refresh merely because the platform supports them. When requested, state how their data will be fetched, checked, stored, and reconciled with the accepted snapshot.

## 2. Use the available website workflow

If a website-building skill or connected platform is available, discover it and read its current instructions. Use its supported source-opening, preview, validation, and deployment workflow. For Sites, the current Sites skill owns platform-specific commands and publication behavior; this research skill owns the scientific content and stage acceptance.

Do not hardcode tool names, authentication methods, hosting manifests, or runtime limits from a previous environment. If a platform is unavailable, build and verify a local website using available tools and describe the delivery limit. A local usable preview can be submitted for stage acceptance if that delivery matches the user's request.

Publication and stage acceptance are distinct. Follow the user's requested audience and existing authorization for hosting; preserve existing access when updating. A request to create a skill package alone is not a request to create or publish a live website. Do not publish private notes or unpublished research simply because the website source is public.

## 3. Build a question-centered vertical slice

Implement a working slice using verified records representing the selected questions and evidence types. The slice should let a reader:

1. Choose an accepted question or relevant filter.
2. Find a paper and understand why it belongs.
3. Inspect the observation, inference, and evidence limitation.
4. Open the exact source or locate the cited evidence.
5. Export the selected records with their provenance.

This validates the information model before broad corpus expansion. Sample records must be labeled as fictional during development and excluded from the real corpus unless they are retained in a clearly separate demonstration mode.

Favor one main searchable table or card list with expandable detail. Add comparison views, reading paths, or method guides when they answer a concrete user need. Avoid many sections that repeat the same evidence in different language.

## 4. Show what methods can establish

For an evidence-oriented site, provide a short method explanation near the relevant filter or results. It should describe the observable, the inference enabled, assumptions, major ambiguities, and what additional evidence is commonly needed in this context.

Keep different taxonomy dimensions separate. A physical measurement family, detection channel, preparation or control protocol, analysis method, and plotted representation may all describe one paper. A single flat list can mislead if it treats them as equivalent categories. Use only facets that help the accepted questions.

A paper detail view should connect the specific method to the actual observed signature, the process or capability it supports, and what remains unproven. Explain complementary evidence by the ambiguity it removes. Agreement between two readings that share a confound is not independent confirmation.

Provide a practical-reading path when the researcher needs to learn how to perform a study. Start with the accepted question and required evidence, then show the suitable method, priority protocol or methods paper, calibration/control reference, and analysis/validation reference as available. Explain why each source is useful rather than presenting an unranked reading list.

Let readers filter by these article roles and by whether the relevant protocol or supplementary information was actually inspected. A concise main card should show the reading priority, exact locator, evidence provided, and implementation readiness. Expandable details should preserve conditions, documented steps, transfer limits, controls, and missing information. Do not replace missing procedural detail with a confident generated protocol.

## 5. Handle figures and quantitative evidence carefully

Use [figure-evidence.md](figure-evidence.md) for the default claim-and-figure reading flow. Attach inspected key article figures when their source and reuse conditions are established. Show the authors' intended claim, observable signal, relevant control/comparison, supported inference, and limits beside the corresponding panels. If reuse is not established, provide the exact source link and an original explanation with a visible image gap.

Inspect a figure before explaining its contents. Preserve axes, units, legends, and essential context. Label crops or annotations, and keep the original source available. A conceptual redraw must be labeled as such; it must not resemble an unreported experimental result.

Explain the observed pattern, relevant control, supported conclusion, and remaining alternative beside the figure. Do not copy lengthy captions or full paper text as the default form of explanation. Do not treat pixels in a figure as raw arrays or infer unreported precision from an image.

Keep method-to-panel relations explicit so filters and detail views show matching evidence. Preserve all recorded methods on the paper card and qualify completeness when full text or supplements remain unchecked. Inspect a user-specified reference website for transferable reading and interaction patterns, while keeping its research content outside reusable public skills.

## 6. Expand by gaps and preserve changes

After the first slice works, add papers according to the coverage assessment. Reuse stable IDs and maintain version relations. Do not overwrite verified annotations with unreviewed imported summaries. Keep the source of automated suggestions visible until they are checked.

When editing an existing site, inspect the latest source before combining concurrent work. Test that the added records and filters preserve existing accepted behavior. Avoid creating parallel sites or conflicting corpora when the request is to update one existing resource.

Changes to spelling, layout, or a verified metadata error normally stay within stage 3. A changed subfield, question wording that alters scope, or new inclusion policy affecting the review must be returned to the relevant checkpoint. Record the impact and preserve the previous snapshot.

## 7. Deliver accurately

Run the relevant checks in [site-acceptance.md](site-acceptance.md). Present the usable site, what is implemented, the corpus cutoff/version, and material limitations. Report local QA and hosting status separately. Successful deployment does not establish that every page was visually inspected after deployment.

Submit the specific site and corpus version for user acceptance. Do not start writing the stage-4 review during implementation, curation, or acceptance waiting. Paper notes and a coverage inventory remain within this stage.
