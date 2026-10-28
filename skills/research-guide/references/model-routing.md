# Automatic Research Consultations

The coordinator owns the whole loop: identify a consequential question, package the evidence, create a same-project chat, ask, wait, retrieve the answer, verify it, and adjust the active work. The user supplies the research situation and stage decisions, not a copied prompt.

## Resolve product, model, and authorization separately

| Destination | Model preference | Routing rule |
|---|---|---|
| Regular ChatGPT Chat | Exact requested ChatGPT 6-Pro model | Preferred research consultation route when supported and selectable |
| Regular ChatGPT Chat when Pro is unavailable | Available ChatGPT Thinking model | Same-product fallback under the user's preference |
| Work or Codex | GPT-6.1 Sol | Use for a requested Work/Codex consultation; do not substitute it for regular ChatGPT Chat without authorization |

Keep the exact requested label, selected product, configured model/mode, and verified execution identity separate. A Pro subscription, a model name, and a reasoning-effort setting are different things. Work/Codex with high reasoning effort is not proof of a ChatGPT Pro or ChatGPT Thinking run. Do not choose Astra as an implied substitute.

Inspect current app tools before routing. Prefer the app's supported creation, messaging, status, and reading tools. A tool that creates Work chats does not necessarily create regular ChatGPT chats. A missing selector means that route is unavailable through that tool, not that the user lacks Pro access. The [official model guide](https://learn.chatgpt.com/docs/models) describes Work/Codex model and reasoning controls; verify current availability on the actual destination. Preserve an explicitly requested model rather than replacing it with a newer or similarly named one.

Resolve a supported identifier from live capabilities before using it. For a Work/Codex tool that lists `gpt-6.1-sol`, use that identifier for the requested GPT-6.1 Sol selection. If the tool cannot select the required model, do not silently use its default. A listed model still needs a successful run; record runtime rejections truthfully.

An explicit human request to automatically create, ask, wait, and adjust provides standing authorization for that consultation loop within its stated project and purpose. Reuse it without repeated permission questions. A newer automatic instruction supersedes an earlier prepare-only instruction; a later explicit opt-out can reverse this. A model preference alone does not authorize changing the destination product. Public skill defaults and an empty state template do not grant permission on behalf of future users. If actual creation/messaging authorization is absent, ask once for that routing choice while completing the evidence packet.

Do not switch to browser automation merely because the app tool lacks the requested route. Use a browser route only when requested or separately authorized. If no permitted route can create the requested chat, record `unsupported_destination` or `unselectable_model`, retain the prepared context, and explain the concrete limitation. Continue independent work. Do not make prompt copying the default workaround or claim that the consultation ran.

## Run the loop

1. **Identify the decision.** Select a difficult inference, competing explanation, uncertain transfer, or important method choice. State what its answer could change. Routine metadata cleanup and straightforward factual retrieval do not need a new chat. If there is insufficient context for a bounded question, collect it in the current chat first.
2. **Build the packet.** Fill the [consultation brief](../assets/deep-research-handoff.md) internally with completed work, observations, interpretations, desired outcome, constraints, question, alternatives, inspected sources, contrary evidence, and accepted stage/evidence revisions. Include the source excerpts or accessible artifacts needed to reason. Do not assume project membership gives the receiving chat access to earlier conversations or local files.
3. **Resolve the exact project.** Use the app's project listing and current-chat context. Match project identity, backend, and host. A local project ID is not automatically a ChatGPT project ID; a similar name is insufficient. Do not create an unrelated cloud project, move the user's work, or choose a projectless destination to make the call succeed.
4. **Check for an existing consultation.** Match project, question ID, and evidence revision. Reuse a running or completed consultation for that same decision. Reconcile uncertain creation outcomes before retrying. A newly created chat should answer a new consequential question or a clearly justified new evidence revision.
5. **Create and ask once.** Pass the completed packet as the new chat's initial message. Store its returned identity immediately; do not submit the initial question again as a follow-up. Verify product, project, and configured model from returned metadata when available. Tell the receiving chat to answer there and not create further chats or edit shared artifacts.
6. **Wait for the actual answer.** Retain the status cursor and use supported bounded waits. A creation acknowledgment, commentary, elapsed time, or an idle label without a completed turn is not an answer. Retrieve the full final response if the status tool truncates it. Keep decisions that depend on the answer pending; independent work in the current stage can continue.
7. **Verify.** Check decisive citations, source locations, numerical settings, equations, and applicability against inspected evidence. Distinguish model proposals from published findings. Match the returned question/evidence revision to the current one; do not apply an answer whose premises have become stale without reconciliation.
8. **Apply and report.** Record recommendations adopted or rejected with reasons, remaining uncertainty, and the concrete change to the working artifact. Resume dependent work only after this verification. Report what the consultation changed, not just that another chat exists.

In Codex app environments, discover the current schemas for `list_projects`, `create_thread`, `wait_threads`, `read_thread`, and `send_message_to_thread`. Other environments may provide equivalent tools. Their names alone do not establish regular-Chat creation or exact-model support. A UI-only or unsupported route must not be reported as successfully automated.

## Clarification, interruption, and failure

When the consultation asks for clarification, answer from inspected project evidence if it is already available and follow-up messaging is authorized. Use the same chat. Ask the user only for consequential missing facts; do not invent them. The receiving chat returns clarification needs to the coordinator rather than starting another chain of chats.

A wait timeout remains pending. Use later bounded waits with the last cursor rather than resending the question. If execution fails, record the error, preserve the packet, and use only an authorized model/product fallback. A retry is appropriate for a known transient failure; limit recovery to one retry per unchanged error before reporting the blocker. An uncertain creation outcome must be reconciled before any retry.

If the user changes the question or model policy while a consultation runs, preserve that change, stop the obsolete run when a supported control exists, and mark its answer superseded if its premises no longer apply. Do not use an unrelated operation, such as moving a project, as a substitute for a stop control. If the run already finished, record that fact. No reply should be represented as coming from a different model after the fact.

Keep wait calls short enough to communicate progress. Do not promise to monitor after the active turn ends unless an available scheduled mechanism has actually been authorized and configured. Persist pending consultation identity and status so a later turn can resume without creating duplicates.

## Private consultation record

Record:

- Consultation ID, project identity/backend/host, question ID, brief/evidence revision, and current stage.
- Human creation and follow-up authorization references, requested route, fallback permissions, requested model, configured model/mode, and verification status of actual execution identity.
- Chat ID, initial dispatch status, wait cursor, real timestamps when available, retry count, and failure or clarification details.
- Lifecycle: `prepared`, `running`, `needs_input`, `answer_received`, `verified`, `applied`, `failed`, `blocked`, or `superseded`.
- Full answer reference, source checks, adopted/rejected recommendations, unresolved claims, and applied artifact revision.

Keep filled records and evidence packets in private project storage, outside the public skill release. An explicit prepare-only request leaves dispatch and actual selection empty; it is an opt-out from automatic consultation.

## Preserve the research gates

The consultation is support inside the active stage, not a fifth stage. Its completion or confidence cannot accept a subfield, question set, library snapshot, or review for the user. A verified recommendation may revise a working artifact. If it materially changes accepted scope, questions, or corpus, reopen the affected gate and reconcile dependent work before advancing. Model agreement is not independent experimental confirmation.
