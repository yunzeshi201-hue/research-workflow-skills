# Reviewing Results and Choosing the Next Step

Review only the evidence actually available. A described protocol is not an executed experiment, a simulated output is not an observation of the target system, and a completed analysis is not necessarily a resolved question.

## Verify what happened

Compare the executed work with the plan. Record deviations, missing inputs, failed checks, exclusions, analytical changes, and unplanned stopping decisions that could affect interpretation.

Inspect the relevant evidence chain:

- **Measurements:** raw data provenance, calibration or reference behavior, instrument range, drift, missingness, preprocessing, and independence of repeated observations.
- **Observational analysis:** sample selection, timing, dependence, missing data, estimand, model assumptions, and sensitivity to plausible confounding or measurement error.
- **Computation:** input versions, executable code and environment, random seeds when relevant, numerical convergence, baseline correctness, and evaluation leakage.
- **Theory:** definitions, assumptions, each inference, unproved lemmas, and whether numerical checks have been mistaken for proof.

Select checks because they bear on the conclusion. Do not run an unrelated exhaustive audit. If a critical check fails, separate the technical failure from the scientific question it prevents answering.

## Update claims, not just scores

For each claim, compare the observed result with the prior prediction and the assumptions needed to interpret it. Use a compact record when several claims are involved:

| Claim or explanation | Relevant evidence | Assumptions or quality limits | Status | Consequence |
|---|---|---|---|---|
| One claim at a time | Observation, estimate, proof step, or counterexample | What must hold and what remains uncertain | Supported within scope, weakened, excluded within scope, unresolved, or not assessed | What changes in the next decision |

These status labels are judgments to explain, not numerical probabilities. Do not assign posterior probabilities without a defensible model and calculation.

Consider whether the result distinguishes the proposed explanation from a plausible rival or merely agrees with both. Agreement with one prediction is weaker than a result that discriminates among live alternatives. A model can fit accurately while its parameters or mechanism remain nonidentifiable.

Report effect sizes, uncertainty, bounds, and conditions where applicable. A threshold crossing alone does not establish importance, causality, or a unique mechanism. A statistically nonsignificant result is not evidence of no effect unless the design and uncertainty support the relevant bound or equivalence claim.

For a proof, state the proposition established under its assumptions. For a counterexample, state the claim it refutes and its admissibility. For a simulation, distinguish an implication of the chosen model from evidence that the model describes the target system.

## Treat unexpected outcomes as evidence

An unexpected result can reveal a faulty assumption, a deficient measurement, an implementation error, an omitted factor, or a useful new phenomenon. Do not immediately select the most interesting interpretation.

First check the most consequential, plausible defects in the evidence-generating process. If the result survives, revise the explanation set and design a follow-up that distinguishes the new account from remaining alternatives. Preserve the original prediction so the revision is visible.

Exploratory reanalysis is useful when labeled as such. Record consequential analysis choices and seek independent confirmation of a selected pattern. Repeatedly trying analyses until one supports a preferred claim weakens the evidential interpretation, even if every individual analysis can be rerun.

## Recognize unresolved outcomes

Keep a question unresolved when any limitation prevents the intended inference, including:

- Predicted observations overlap under the accessible conditions.
- Precision or coverage cannot exclude differences that matter for the decision.
- A proxy-to-claim assumption is unsupported or an essential causal identification condition is not defensible.
- A required control, calibration, independent test, or proof step is missing.
- Results depend materially on reasonable analytical choices or unstable numerical settings.
- The executed procedure differs from the design in a way that defeats the intended contrast.
- Data or sources required to assess the claim are unavailable.

Name the limiting reason and the smallest action that could remove it. If no feasible action can remove it within the stated constraints, report that boundary instead of filling the gap with a confident conclusion.

## Choose a consequence

| Decision | When justified | What to specify |
|---|---|---|
| Continue | The route is valid and the next unresolved uncertainty has a useful test | The next discriminating action and why it matters |
| Revise | A repairable design or interpretation limitation prevents progress | The specific repair and the check that will establish its adequacy |
| Pivot | The current route cannot answer the question efficiently, or new evidence changes the priority | The new question or route and evidence motivating the change |
| Stop this route | The question is answered within scope, the route is infeasible, or expected benefit no longer justifies further work | What was learned, what remains open, and what future evidence would justify reopening |

Do not equate stopping one route with proving the underlying question unimportant or insoluble. Do not equate continuing with an obligation to collect more data; a source check, derivation, or independent analysis may be the right next action.

## Preserve reproducibility and validity separately

Retain the inputs, versions, procedures, code, analysis settings, and decision record needed to reconstruct the result. Preserve raw data and record transformations; do not replace the original evidence with only a processed figure or summary.

In the terminology used by the [National Academies report](https://www.nationalacademies.org/read/25303/chapter/6), computational reproducibility concerns consistent results from the same data and computational procedure; replication concerns consistent findings from independently obtained data addressing the same question. Terminology differs across disciplines, so state the intended meaning when it matters.

A reproducible computation can faithfully reproduce bias, leakage, an unsuitable model, or an invalid inference. New data can also repeat a shared systematic error. Assess scientific validity through the assumptions, controls, design, scope, and independent evidence relevant to the claim.

## Return a decision-ready result

Lead with the strongest supported conclusion and its scope. Then give the evidence that warrants it, the main unresolved alternative or limitation, and one immediate next action with a completion criterion. Include only additional detail needed to inspect or execute that decision.
