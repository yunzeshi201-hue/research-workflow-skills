---
name: research-test-design
description: "Support research questions with experimental reading guidance, source-backed methods, and feasibility plans. Design or assess a study when requested, while respecting the active stage of the gated research workflow."
---

# Research Test Design

Choose the smallest action that can change a consequential research decision. A useful result may resolve a question, exclude an explanation, establish a bound, reveal a measurement limitation, or show that the proposed approach is not feasible.

This is a helper rather than a fifth stage. In a gated project, inspect the current workflow record and accepted prerequisites. During question selection, provide feasibility and experimental reading sketches; do not execute a future study or advance to website/review work. Standalone study-design requests or separately requested post-review research can use the full workflow. Use available tools without requiring companion skills.

## Read important experimental articles

Read [experimental-reading.md](references/experimental-reading.md) when the user needs important articles that explain how to perform or interpret an experiment. Build a verified reading route from the question to methods/protocols, controls, calibration, and analysis/validation. Explain the role, exact source location, transfer limits, and missing practical information for each article. Separate a source's reported procedure from a proposed adaptation. Use articles from the accepted library when supporting its review; propose a corpus revision if essential new papers are needed.

For substantive experiment proposals, also use [experiment-precedents.md](references/experiment-precedents.md). Deliver a comparison of what prior studies actually did and a step-to-source map for the proposed procedure. Attach verified citations and direct reference links in the deliverable, including Methods/SI/protocol locations. Distinguish direct precedents, related-method analogies, and new proposed adaptations. No prior experiment or missing setting may be invented to fill the table.

## Establish the decision

Start from the user's account of completed work and desired outcome. Label user-reported observations, inspected evidence, interpretations, and plans distinctly. The proposed next experiment should address the remaining uncertainty rather than repeat a completed task without a reason.

When a pilot result motivates the request, use [result-review.md](references/result-review.md) to assess the existing data and executed procedure before committing to another experiment. Missing raw data remain an access gap; do not imply that the audit has been performed.

Read the supplied question, evidence, constraints, and previous decisions. Identify:

- The claim or uncertainty to address and why resolving it would matter.
- What is already observed, what is inferred, and what is merely assumed.
- The decision that would change after a useful answer.
- Available data, instruments, expertise, time, and compute; label unknown capabilities instead of assuming access.

If the question is still broad, narrow it to one uncertainty and one decision. Do not require a complete proposal before making progress. Ask only for missing information that changes the design; continue source checks or design comparisons that do not depend on it.

## Select the evidence route

Read [study-plan.md](references/study-plan.md) for the relevant route and planning fields.

| Research need | Useful evidence route |
|---|---|
| Determine whether the answer is already known or a claimed gap is real | Targeted literature and prior-art check |
| Understand an existing observation | Data audit, reanalysis, or alternative model comparison |
| Distinguish proposed mechanisms | Intervention or other observation with different predictions under the alternatives |
| Discover an uncharacterized pattern | Explicitly exploratory measurement or analysis with a separate validation plan |
| Estimate a relationship without intervention | Observational study with stated assumptions and limits on causal interpretation |
| Establish a mathematical statement | Derivation, proof, counterexample, or a bound under explicit assumptions |
| Examine model consequences | Verified simulation, sensitivity analysis, and a stated empirical validation need |
| Assess an algorithm or method | Benchmark with meaningful baselines, independent evaluation, and resource accounting |
| Establish whether a larger study can work | Feasibility pilot with progression criteria |

Choose the route from the uncertainty. Do not default to collecting more data or using a familiar instrument. A derivation, existing dataset, or targeted search may remove the bottleneck more directly. A combination is appropriate when each component resolves a different limitation.

## Make the plan discriminate

For each candidate action, state the observable or formal output, alternatives it can distinguish, assumptions connecting output to claim, and outcomes that remain ambiguous. Include plausible nuisance explanations such as drift, selection, measurement artifacts, or implementation error where relevant.

Check whether the predicted differences are identifiable with the available design and resolvable given uncertainty. Name the limiting uncertainty or missing estimate. Do not invent sample sizes, thresholds, effect sizes, instrument limits, or resource availability.

Prefer a feasible action that changes the decision over a larger action that produces the same unresolved ambiguity. Compare cost, time, likely discrimination, and failure modes qualitatively unless defensible quantities are available. Treat expected information gain as a judgment unless it has actually been calculated.

## Produce an executable next step

Return a compact plan containing:

1. The narrowed question, intended claim, and decision it supports.
2. The chosen action and why it is preferable to the strongest feasible alternative.
3. Inputs, prerequisites, procedure, observable or formal output, and applicable controls or checks.
4. Precision, detectability, coverage, or proof obligations appropriate to the route, with a justified resource or sample-size basis.
5. An outcome-to-decision table, including inconclusive and invalid outcomes.
6. The immediate next action, its completion criterion, and the evidence needed before any larger commitment.

For experimental procedures, include the prior-study comparison, step-level source mapping, and attached reference list as part of this plan. Clearly distinguish what others demonstrated, what the researcher already did, and what is now proposed. Essential access, procedure, or transfer gaps mean the output is a feasibility/reading plan rather than execution-ready instructions.

Use only relevant planning fields. For a narrow result-interpretation request, return the supported conclusion, its limits, and the next decision without expanding it into a full study plan. A proof needs definitions and proof obligations, not a fabricated sample-size calculation. Define practical tolerances from the question and evidence, not from a universal significance threshold.

Execute searches, derivations, analyses, or computations only when authorized for the active stage or a separately requested study. A workflow-wide request does not bypass acceptance gates. For unavailable equipment or access, identify the missing prerequisite and provide only the protocol detail supported by inspected sources. Distinguish planned work, simulations, executed work, and observed results.

## Review results and iterate

When results are available, read [result-review.md](references/result-review.md). Verify the evidence-generating process before updating the scientific interpretation. Compare results with the recorded predictions and decision criteria; label later changes as revisions.

Report the strongest supported conclusion, remaining alternatives, and a decision to continue, revise, pivot, or stop. An unresolved outcome is valid when the design cannot discriminate, precision is inadequate, assumptions fail, or essential evidence is missing. A failed feasibility check does not establish that the underlying scientific claim is false.

Keep raw observations and executed procedures traceable. Recomputing the same result demonstrates computational reproducibility; it does not by itself establish that the model, measurement, or scientific conclusion is valid.

## Completion standard

The user should be able to identify what to do next, what that action can establish, how to recognize an uninformative result, and what each plausible outcome changes. If these are not yet defensible, return the smallest preparatory action that will make the design possible.
