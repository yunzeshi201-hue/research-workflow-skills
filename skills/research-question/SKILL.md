---
name: research-question
description: "Stage 2 of the gated research workflow: turn an accepted subfield into a prioritized set of important, bounded questions with nearest prior work, experimental reading guidance, and feasible evidence routes."
---

# Research Question

Require a user-accepted stage-1 subfield and its current artifact revision before selecting the stage-2 question set. Inspect `research/workflow-state.json` or an equivalent project record and the actual user-decision evidence. Reuse verified acceptance without reconfirming it. If missing, stale, or merely asserted by an agent, present the subfield checkpoint and stop before stage-2 work. A direct skill invocation does not waive this gate; record any explicit later user override separately.

A bounded provisional question set may be accepted with disclosed source gaps and verification tasks for library building. This settles what to investigate, not whether the questions are novel. An undefined or internally conflicting question set is not ready for acceptance.

Produce a question whose answer would change an explanation, prediction, design choice, or justified claim. A topic, available instrument, interesting correlation, or list of experiments is not yet that question.

Use the current aim and supplied evidence. Ask only for missing context that changes the question, such as the target system, constraints, or intended decision. Continue with labeled assumptions where the answer is not essential. Do not expand a narrow question into a full field survey.

Anchor the question in the project brief: what the researcher already did, what the observations support, what is currently inferred, and what they want to establish next. When deeper reasoning could change the decision, use the guide's automatic consultation procedure within this stage: supply the context, dispatch to an authorized same-project chat, wait, verify the answer, and revise the question or feasibility sketch. Prefer ChatGPT 6-Pro, then ChatGPT Thinking; Work/Codex consultations use GPT-6.1 Sol. Keep product and model identities explicit. If the route is unavailable, report the concrete limitation and continue independent evidence work; do not silently revert to asking the user to paste a prompt.

## Locate the unknown

Classify the gap before calling it a research opportunity:

| Status | Required next work |
|---|---|
| Unknown to the researcher | Learn the relevant concept or reproduce the established argument. |
| Apparently unresolved within a bounded search | Check the closest prior work, its conditions, and the exact remaining claim. |
| Known but not verified in this setting | Decide whether replication or transfer would change an important conclusion. |
| Blocked by measurement, computation, access, or identifiability | Test feasibility, seek a different observable, or narrow the question. |

These statuses can coexist. Missing evidence in a supplied folder is not evidence that the literature lacks an answer. If current source access is unavailable, state that novelty is unassessed and give a search plan. Do not invent papers, dates, findings, or claims of being first.

## Build the dependency chain

Work through the following chain, skipping parts already established:

1. **Aim:** What would become understandable or possible if this work succeeded?
2. **Bottleneck:** Which uncertainty currently prevents that outcome?
3. **Construct:** What property, process, or mathematical object must be defined? Distinguish quantities that sound similar but require different evidence.
4. **Bounded unknown:** State the system, conditions, comparison, target quantity, and scope. Avoid combining several independent unknowns into one question.
5. **Rivals or approaches:** Identify plausible explanations, models, constructions, or search strategies. Include mundane artifacts when relevant. Do not force hypotheses onto descriptive or exploratory work.
6. **Discriminating evidence:** Identify the observation, derivation, counterexample, or benchmark that would distinguish the alternatives or meet the stated objective.
7. **Decision:** Explain what each plausible result changes in the parent question and what work follows.

For every proposed micro-question, complete: "If the answer is A rather than B, we would change ___ in the parent claim or plan." If nothing changes, demote it to background learning or remove it from the critical path. A useful dependency may establish a prerequisite without resolving the whole aim.

## Audit the inference

Trace the proposed argument:

`observation -> processing or model -> inferred quantity -> mechanism or function`

For each step, record the assumption, supporting evidence, and an alternative that could produce the same result. Mark direct observations separately from model-dependent estimates and interpretations. Audit raw-data quality and calibration before treating a proxy as the target quantity.

Check whether the proposed alternatives remain distinguishable given noise, resolution, nuisance variables, sampling, and model flexibility. If different explanations predict the same available observations, identify a different perturbation or observable. Repeating the same ambiguous measurement does not resolve structural non-identifiability.

Preserve the exact system and conditions of cited evidence. Similar systems supply analogies until transfer is justified. A mathematical component, fitted parameter, or database label does not automatically establish a real entity or causal mechanism.

## Establish what would count as an answer

Choose criteria appropriate to the work:

- **Explanatory or causal:** State rival predictions, relevant controls, and results that would weaken the preferred account. Explain what the design can and cannot identify.
- **Descriptive or exploratory:** Define the population or search space, sampling and measurement plan, useful precision or coverage, and how candidate findings will later be checked. Label post hoc hypotheses.
- **Theory:** State assumptions, the proposition or construction, proof obligations, known boundary cases, and what a counterexample would show. Numerical checks do not replace a required proof.
- **Computational or design:** Specify a baseline, target metric, constraints, held-out evaluation where appropriate, and tests for shortcuts or failure outside the tuning cases.

Predefine practical decision criteria where possible. Leave unknown numerical thresholds explicit and name the pilot, uncertainty estimate, or external requirement needed to set them. Do not invent precision or sample sizes.

## Select the important question set

Give each serious question a stable ID and compare scientific consequence, nearest existing answer, exact uncertainty, feasibility, and dependence on other questions. Recommend a manageable set with explicit priorities and deferred alternatives. A single critical question is valid; do not force a fixed number. Keep learning gaps, replication aims, and proposed open problems labeled.

For each selected question recommend verified important articles by role: closest precedent, competing evidence, method/protocol, calibration/control, or analysis/validation as relevant. Explain why to read each, what experimental decision it informs, and the exact inspected Methods/SI/figure/code location. Distinguish transferable procedure from system-specific conditions and missing practical details. Abstract-only access does not support invented operational instructions. A methods paper may be more useful than a widely cited headline result.

Use `research-test-design` when available for a feasibility sketch and experimental reading route, not to execute the proposed study. Connect each question to `needed evidence -> method -> important paper -> control -> decision`. This can establish whether the question is worth pursuing before stage 3.

For a proposed experimental route, list the closest inspected studies and what each actually did, with direct references and Methods/SI locators. Mark direct precedent versus related-system analogy. Link the proposed key steps and adaptations to this evidence; keep unreported settings missing rather than converting an attractive idea into an unsupported protocol.

## Deliver the stage-2 checkpoint

Use [question-card.md](references/question-card.md) for the question and dependency record. Read [worked-example.md](references/worked-example.md) when a concrete decomposition would help. Scale the output to the request; an early discussion may need only a short card and one dependency chain.

Return:

- A bounded main question, why its answer matters, and its evidence status.
- The few micro-questions on the critical path, with their links to the parent claim.
- The nearest relevant prior work and exact unresolved difference, or a clearly marked search task.
- The smallest useful next action, its possible outcomes, and the resulting continue, revise, stop, or pivot decisions.

Distinguish immediate literature or reasoning work needed to settle the questions from proposed later studies. Do not collect new observations, run a full study, implement the website, or draft the review merely because they appear in a question card.

Present the versioned prioritized question set, unresolved issues, important reading route, and its dependency on the accepted subfield revision. Mark `questions` as `ready_for_confirmation` and ask the user to accept or revise it. Only clear user acceptance unlocks `research-paper-library`; silence, praise, partial assent, or successful feasibility checks do not. Record the actual acceptance evidence and revision. If companions are absent, follow these gates directly.

Stop decomposition when the next task has a clear input, observable output, and decision consequence. Pivot when the question is already answered, cannot be distinguished with attainable evidence, loses its importance, or requires a prerequisite outside the current scope. Report what was learned even when no novel question survives.
