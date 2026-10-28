# Designing the Next Research Action

Read the route relevant to the question. These fields are a design aid, not a form that every project must fill in completely.

## Start with a decision, then choose an action

Write the question in operational terms: a specified system or population, conditions, quantity or proposition, comparison, and scope. State what would change if the answer were different. If no plausible result changes the research decision, reconsider the question or the action.

Before a new study, check whether existing evidence can settle the uncertainty. A targeted search can test a novelty claim; a reanalysis can locate an inconsistency; a derivation can expose an impossible parameter regime. Do not treat these as mandatory stages when the user has already supplied adequate evidence.

Compare feasible actions on:

- Which competing answers they distinguish, and under which assumptions.
- Whether the expected difference is observable or the formal claim is decidable by the proposed approach.
- Time, cost, access, irreversibility, and the value of learning even if the preferred explanation fails.
- The chance that an outcome would remain ambiguous because of an avoidable limitation.

Avoid decimal rankings built from unsupported estimates. If two actions exchange cost for discrimination, state the tradeoff and the condition that would change the recommendation.

## The bridge from observation to claim

Record this chain explicitly where interpretation is nontrivial:

`raw observation -> processing or estimation -> observable -> model or inference -> claim`

For each link, name the necessary assumptions and a plausible failure. For example, a change in a proxy can reflect a change in the intended quantity, the measurement process, or an uncontrolled variable. An accurate fit to a proxy does not make that interpretation unique.

Distinguish scientific rivals from nuisance explanations. Scientific rivals propose different accounts of the phenomenon; nuisance explanations concern how the apparent result could arise without the proposed phenomenon or through a study defect. Both can require checks, but they need not receive equal prior plausibility.

Use a prediction table when it clarifies the design:

| Candidate explanation or account | Predicted observation under specified conditions | Distinguishing comparison | Necessary assumptions | What would remain compatible |
|---|---|---|---|---|
| Each live alternative | Direction, pattern, range, or formal consequence with justification | Intervention, contrast, boundary case, or validation set | Assumptions required to interpret that comparison | Residual ambiguity |

Do not force numerical predictions when theory only supports qualitative ones. Do not present the candidate set as exhaustive. If all candidates predict the same accessible observation, change the conditions, add an independent observable, or acknowledge that this approach cannot distinguish them.

## Routes

### Mechanism or intervention study

Identify the intervention, comparator, measured response, conditions, and independent experimental unit. Explain why the contrast distinguishes mechanisms rather than merely showing an association.

Use controls for the actual alternative explanations: a blank may address background; a reference may establish calibration; randomization may reduce allocation confounding; an independent measurement may constrain interpretation. Explain each control's purpose rather than accumulating controls by habit.

Check perturbation specificity, measurement range, resolution, drift, carryover, saturation, and confounding where relevant. A strong intervention that changes several relevant properties can be less informative than a weaker, more selective contrast. Separate repeated measurements of one unit from independent units or independent preparations.

### Exploratory study

State what space is being explored, which measurements are trustworthy, and what would count as a useful pattern or anomaly. Exploration can precede a precise mechanism hypothesis.

Record the search space and major analytical choices. Identify how a candidate finding would be checked on new data, a held-out portion when appropriate, a different method, or a planned follow-up. Do not describe a pattern selected after inspection as a prediction made beforehand.

Distinguish absence of a detected pattern from evidence that no pattern exists. Report what the sampling and measurement coverage can support.

### Observational study

Define the target population, selection process, exposure or predictor, outcome, and estimand. Identify missingness, measurement error, confounding, time ordering, and sources of dependence that could change the interpretation.

For a causal claim, state the identification assumptions and the design or evidence supporting them. Adjustment, matching, or a predictive model does not automatically remove confounding. If a causal interpretation is not supported, frame the output as an association, prediction, or descriptive estimate.

Use sensitivity checks tied to plausible violations. Do not promise that a single diagnostic proves an untestable assumption.

### Theory, proof, or counterexample

State definitions, assumptions, the target proposition, and relevant limiting or boundary cases. Identify the missing lemma, reduction, construction, or contradiction needed to advance the argument.

Use small cases, dimensional reasoning, or numerical exploration to locate errors and guide a proof. A finite computational search does not prove a general statement unless its coverage is itself justified. A valid counterexample can refute a universal claim within its stated scope; it need not explain every observed case.

Record which statements are proved, conjectured, numerically supported, or conditional. If a full proof is not tractable, consider a bound, restricted theorem, necessary condition, or explicit counterexample.

### Simulation or computational model

Separate implementation verification from validation of the model as a representation of the target system. Check known limits, conservation relations, exact cases, convergence, or an independent implementation as appropriate.

Document inputs, parameter provenance, numerical choices, initial and boundary conditions, randomness, and sensitivity to relevant assumptions. Use resolution or tolerance checks when numerical error could change the conclusion.

A simulation can establish consequences of a model under its assumptions. To make claims about a real system, identify the independent empirical evidence that supports those assumptions and predictions. Fitting and validating on the same observations limits the strength of that evidence.

### Algorithm or method benchmark

Define the task, dataset or test instances, target metric, relevant baselines, and resource constraints. Match comparisons on the factors that matter for the claim, such as available information, tuning effort, compute, or operating conditions.

Keep evaluation data independent of development where feasible. Check leakage, duplicate or dependent cases, tuning on the test set, and hidden changes in task definition. Report variability across seeds or instances when that variability affects conclusions.

Use ablations or targeted cases to test why a method behaves differently. A better average score alone does not establish the proposed mechanism or performance outside the tested distribution. Include meaningful costs and failure cases.

### Feasibility pilot

Name the feasibility uncertainty: acquisition quality, stability, recruitment, protocol delivery, computational scaling, access, or another practical bottleneck. Define a progression criterion related to the requirements of the larger study.

Separate feasibility conclusions from scientific efficacy or mechanism conclusions. A small pilot may expose a major problem without having enough precision to establish the final scientific effect. Do not base the larger study solely on an unstable effect estimate from the pilot.

The [NCCIH pilot-study guidance](https://www.nccih.nih.gov/grants/pilot-studies-common-uses-and-misuses) makes this distinction for clinical intervention research. Its specific restrictions are not universal rules for every scientific pilot.

## Detectability, uncertainty, and size

Derive the resolution required from the question. Use the route's appropriate basis: a practically meaningful effect, desired interval width, measurement detection limit, model-separation requirement, numerical tolerance, coverage criterion, or proof obligation.

For empirical studies, identify the independent unit, variability sources, dependence, plausible effect or contrast range, and intended analysis. Justify sample size using precision, power, design simulation, or feasibility objectives as appropriate. Account for multiplicity, attrition, clustering, or sequential decisions when they materially affect the design. If required quantities are unknown, provide conditional scenarios or a plan to estimate them; do not invent a definitive number.

Measurement uncertainty can include calibration, environmental, processing, and model contributions as well as repeat variability. More repeats may reduce some components while leaving others unchanged. [NIST Technical Note 1297](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-2-classification-components-uncertainty) distinguishes statistical and other methods of evaluating measurement uncertainty; those categories are not synonyms for random and systematic effects.

For observational or computational studies, a large dataset does not remove bias, nonindependence, leakage, or model misspecification. For theory, resource estimates concern the proposed proof or search, not an invented statistical sample.

## Outcome-dependent decisions

Write the decision rule before executing a confirmatory study when feasible. Keep exploratory work flexible and record when criteria change.

| Possible outcome | Interpretation allowed by this design | Remaining uncertainty | Next action |
|---|---|---|---|
| Result favors one candidate over another | State the contrast actually supported and its assumptions | Other compatible accounts | Validate independently or test the next unresolved implication |
| Result is precise enough to exclude a relevant range | Report the bound or excluded range | Effects or regimes outside that bound | Redirect or narrow the claim |
| No clear contrast with insufficient precision | Inconclusive | Relevant alternatives remain | Improve the limiting precision only if doing so can change the decision |
| Quality, identification, or implementation checks fail | The planned inference is not justified | Scientific question remains open | Repair the failed check or change the design |
| Result conflicts with all current predictions | Candidate set or assumptions may be inadequate | Artifact and new explanation remain possible | Check integrity, then revise the candidate set |
| Feasibility criterion is not met | The proposed larger study is not ready | The underlying scientific claim is unresolved | Modify the approach, obtain a prerequisite, or stop this route |

Use only rows that fit the actual study. Define the evidence or resource limit that triggers a review, pivot, or stop. Do not schedule indefinite repetition of an uninformative action.

## Compact study record

For an experimental plan, include the [prior-experiment comparison and step-to-source mapping](experiment-precedents.md), with verified reference links in the deliverable. Preserve which work was already completed, which observations were inspected, and which steps remain proposals. Report absent parameters and transfer assumptions explicitly.

Record enough for execution and later interpretation:

- Question, scope, current uncertainty, and decision.
- Evidence basis with source links or supplied data identifiers.
- Candidate explanations, assumptions, and discriminating prediction or formal target.
- Chosen route, strongest alternative, and reason for the choice.
- Inputs, prerequisites, procedure, independent unit where relevant, and quality checks.
- Analysis or proof strategy, uncertainty basis, and resource justification.
- Outcome-dependent decisions, unresolved criteria, and review boundary.
- Immediate action and its observable completion criterion.

Keep this record with the project, outside the installed skill. Retain the original plan alongside dated revisions and executed procedures.
