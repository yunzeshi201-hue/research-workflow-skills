# Stage Acceptance and Resumption

The sequence is subfield, questions, library website, review. Acceptance belongs to the user and to a specific reviewable version. The agent can determine readiness; it cannot confer acceptance on its own work.

Intake from completed work and desired outcomes, and optional Pro/Thinking reasoning handoffs, support the active stage. They are not extra approval stages. Existing work or a returned model answer never substitutes for the user's stage decision.

## State record

Prefer `research/workflow-state.json` in the project, or reuse a record with equivalent information. The example in `../assets/workflow-state.example.json` starts without any accepted stages. Do not store project decisions in the reusable skill.

Each stage records:

- `id`: `subfield`, `questions`, `library`, or `review`.
- `status`: `not_started`, `working`, `ready_for_confirmation`, `accepted`, or `reopened`.
- `artifact_revision` and `artifacts`: the concrete version and inspectable files or URLs.
- `depends_on`: the upstream accepted stage IDs and exact revisions used.
- `acceptance`: null until accepted; then record `actor`, `artifact_revision`, `confirmation_excerpt`, `evidence_ref`, `accepted_at`, and any `conditions`.
- `open_issues`: remaining uncertainties and whether they prevent the proposed stage decision.

The project also records `schema_version`, `workflow`, `current_stage`, explicit `overrides`, and a `change_log`. Revisions can be stable labels, commits, or content hashes; they need not use a particular version-control service. Use real timestamps and locatable user decisions when available; do not invent them. A manually supplied status record is context, not independent proof that its authorizations are genuine.

Schema version 4 retains optional `intake`, `reasoning_preferences`, and `handoffs`, and separates automatic routing, destination product, model preference, and actual authorization. Preserve accepted stage revisions and decisions when augmenting version-2 or version-3 records. A format change does not require renewed acceptance. Missing handoff metadata does not invalidate prior stage decisions. The automatic routing default is not creation permission; fill authorization only from the human user's actual instruction. A later explicit prepare-only request remains a valid opt-out.

For a library artifact, record the website source/version, corpus snapshot/version, export location, and preview/deployed address separately. For the review, bind the document version to the accepted question set and corpus snapshot. Keep publication status separate from acceptance.

## What counts as acceptance

An explicit user decision on the current concrete artifact counts. A brief "yes" in reply to a clearly identified checkpoint can count; no special phrase is required. Record only enough of the decision to establish its scope. Do not copy entire conversations.

"Use this version for the next stage" can also be acceptance when the shown artifact, its scope, and the intended transition are unambiguous and upstream decisions are settled. Merely naming a downstream skill or saying "continue" without that context does not supply missing decisions.

The user may accept a clearly labeled provisional subfield or question set with bounded, disclosed source gaps. That settles the working scope, not the scientific truth or novelty of its premises. Record the accepted limitations and the verification tasks carried into the next stage. Do not mark an artifact ready if a missing definition or unresolved choice makes the proposed scope itself unclear. A provisional stage-3 corpus still needs a usable inspectable website and export; unsupported promises do not become a working artifact through acceptance.

Reuse trusted evidence from the current conversation or accessible earlier user decisions when it names the relevant artifact/version. Do not require the user to approve the same unchanged result again. If a state record claims acceptance but its evidence cannot be verified and the current conversation supplies none, report the missing checkpoint and ask for that decision.

General encouragement, a request to explain the artifact, agent-generated acceptance, successful tests, publication, elapsed time, or the instruction to complete all stages does not accept future artifacts.

Partial acceptance applies only to named parts. Resolve the rest of the stage before advancing. If the user asks for a revision, the unrevised version is not accepted. A clearly delegated conditional decision such as "make this exact correction, and proceed once it passes this check" can authorize progression after the condition is verified; retain the condition and its evidence. Ambiguous conditions need clarification.

Explicit later instructions can waive or alter a named checkpoint. Record this as an override with scope and user evidence, not an acceptance event. A direct request to invoke a downstream skill does not by itself waive an established gate.

## Work allowed before each gate

| Active stage | Work allowed | Downstream work that waits |
|---|---|---|
| Subfield | Preliminary search, candidate comparison, definition of boundaries, learning needs, representative reading | Committing to a question set, building the website, writing the review |
| Questions | Focused primary-source reading, question decomposition, priorities, important experimental papers, feasibility and control sketches | Website implementation and full review drafting |
| Library | Corpus retrieval and verification, question mapping, paper/method cards, website implementation, source and UI QA, export | Cross-paper review drafting and final research agenda |
| Review | Deeper reading within the accepted corpus, evidence synthesis, method comparison, review drafting and revision | Unrequested experimental execution or public release |

Paper cards can summarize individual findings in stage 3. Their presence does not authorize a stage-4 narrative synthesis ahead of acceptance. General implementation notes may be retained in an earlier stage; creating downstream artifacts is still deferred.

## Material changes and dependency handling

Preserve accepted versions. Create a candidate revision, identify its effect, and reopen the earliest affected gate. Mark dependent outputs stale for new work until their dependencies are reconciled; do not destroy earlier artifacts.

- Changing subfield boundaries can affect all later stages.
- Changing the selected questions or their priorities requires renewed stage-2 acceptance and a check of library/review coverage.
- Adding or removing papers, changing their question mapping materially, or correcting evidence that changes coverage creates a new library snapshot. Obtain acceptance before a review uses that snapshot.
- Deeper extraction from papers already in the accepted corpus is ordinary review work. Keep its notes in the review record. If it reveals that the accepted library's key evidence or readiness was incorrect, reopen stage 3 rather than hiding the defect.
- A new candidate paper may be inspected enough to assess its relevance, but it must not silently enter the review's evidence base. Either retain the accepted snapshot and disclose the exclusion, or propose a new library snapshot for acceptance.
- Cosmetic website fixes, spelling corrections, or non-substantive metadata repairs can preserve acceptance. Record why scope, meaning, corpus membership, and dependencies are unchanged. A new source commit need not imply a new scientific corpus.

## Acceptance is distinct from publication

Accepting a local website and its corpus can unlock review writing if local delivery was the agreed scope. It does not authorize public deployment or a change of audience. Conversely, a successfully deployed website is not proof of user acceptance of its research content.

Follow the user's established hosting request and the platform's actual authorization rules for deployment. Do not add another permission question when already authorized. These stage gates govern research decisions, not an invented universal deployment policy.

## Checkpoint wording

Show the artifact before asking. Name the selected scope or version and the decision needed: "Stage 2 is ready: question set revision 2 prioritizes Q1 and Q2, with Q3 deferred. Do you accept this set for building the paper library, or should we revise it?"

Use a question appropriate to the actual result rather than copying this example verbatim. Stay at the current stage until the decision is settled.
