# From supplied figures to a scientific manuscript

Start with the figures and the user's intended question. A manuscript is not required for analysis. A request to develop supplied results into an article authorizes building the evidence map, investigating literature support, and drafting supported sections; do not stop at proposing a plan. “Submission-oriented” describes the work product, not a promise of acceptance or proof that the evidence is complete.

## Inspect and identify what the figures contain

Open every relevant image or rendered page. For multi-panel figures, identify each panel, sample labels, axis quantities and units, linear/log scales, color scale, time windows, normalization, offsets, annotations, and plotted uncertainty. Read accompanying captions and metadata. Preserve the original assets; use readable crops only as inspection aids, without altering scientific content.

Establish whether each figure is the user's measurement, a simulation, a published figure, or an illustrative schematic. Published results can support background or comparison; they must not be presented as new experiments. A schematic does not establish the mechanism it depicts.

Read the relevant section of [spectroscopy-methods.md](spectroscopy-methods.md). Record unclear labels as unknown. Do not infer sample identity, pump wavelength/fluence, film thickness, substrate, acquisition geometry, normalization, repeated measurements, statistics, instrument response, or preprocessing from visual resemblance or common practice. Look for existing metadata and source files first, then ask for only the missing information that changes interpretation. Continue with observations and text that do not depend on that answer.

## Build a figure evidence map

Use [evidence-records.md](evidence-records.md), with three visibly separate layers:

1. **Figure observations:** directly visible feature, order of changes, approximate position/range, or relative trend. Qualify estimates by the displayed resolution and scaling. A smoother curve is not evidence of lower experimental noise or more replicates.
2. **Reported interpretations:** claims in a caption, source paper, user note, or prior fit. Preserve attribution; a state label or fit curve is not independent validation.
3. **Our inferences:** what follows from the observations and controls, plausible alternatives, and the smallest test or missing record that would distinguish them.

Quantitative comparisons require compatible units, normalization, excitation conditions, and samples. Independently normalized curves can show shape or kinetics but generally not absolute population or yield. A cropped axis can conceal an unresolved maximum. Digitized image values are approximate derived data, never raw measurements; disclose extraction and uncertainty. Do not generate fitted lifetimes, error bars, replicate counts, or statistical significance from appearance alone.

If fitting or reanalysis is requested, use original arrays and the applicable analysis workflow when available. Report the model, instrument-response treatment, window, weighting, residuals and uncertainty actually used. If only an image is available, state the limits of any explicitly requested exploratory digitization. Distinguish reproduced author fit parameters from newly estimated ones. A fit does not by itself identify a chemical species or causal mechanism.

## Combine spectroscopy with the literature

Search the external library using sample composition, state, structural family, processing, measurement mode and conditions. Retrieve the primary evidence behind decisive assignments; do not assign a feature merely because its position resembles a literature value. Keep conflicts visible.

Build a claim-to-panel map before composing a single mechanism narrative. Complementary methods constrain different quantities: TAS reports overlapping optical responses, FSRS vibrational structure, THz transport-weighted response, PPP the response to an added excitation, and PL emissive pathways. Agreement in time constants can motivate a link but does not establish identical species. Compare samples, excitation density and temporal resolution before linking processes across instruments.

For each proposed central claim, identify the strongest observation, the supporting control, the inference still needed, and the relevant source. Prefer a narrower supported claim over an elaborate mechanism whose indispensable steps are unmeasured. Do not invent a missing Results section, Methods detail, computation, control experiment, citation, or supplementary dataset to complete the story.

## Draft the article progressively

Use [write-with-evidence.md](write-with-evidence.md) for the immediate figure-analysis and provisional-drafting stage. Produce requested observations, captions and evidence-supported paragraphs without waiting for a target journal, template, or separate story approval. For a full manuscript, use the available paper-writer skill's planning and quality checks, adapting its workflow to the user's current intent and established choices. A writing request already authorizes drafting; do not convert a supporting skill's default venue or narrative checkpoint into a repeated permission request. If an unresolved choice would materially change the manuscript, ask that substantive question while continuing independent supported sections. Record a provisional format or narrative assumption when appropriate; never replace missing facts with assumptions.

Preserve any source `a.u.` axis and describe what its normalization does and does not permit. A preference for physical units does not justify inventing a calibration, silently renormalizing a figure, or withholding an otherwise defensible description. Quantitative replotting requires adequate source data and the applicable analysis workflow.

Prepare concise panel observations and provisional captions first, then supported Results and Discussion paragraphs. Use wording that separates measurements from assignment: an observed change can be reported directly, whereas a mechanism with incomplete discrimination should remain conditional and attributed. Methods may include verified procedures; retain a separate missing-information ledger for unprovided procedures. Do not fill omissions using a “typical” laser, fluence, sample preparation, fitting model or statistical test.

Keep drafting gaps explicit and local. Missing repeat statistics may prevent a significance claim without preventing a descriptive trend paragraph. Missing sample identity may prevent mechanistic attribution without preventing axis-level description. If the central claim cannot yet be supported, deliver the defensible analysis and draft portions together with the concrete evidence needed to finish that claim; do not call the entire article submission-ready.

## Deliver and check readiness

Match scope to the request: figure analysis can be a concise annotated explanation; an article task should include an editable manuscript, figure/caption mapping, resolved bibliography, and a short list of unresolved evidence or methods gaps. Use the requested venue template when known and document any missing required sections. Keep internal extraction scripts out of the manuscript.

Before describing a draft as ready for submission, verify that its main claims are supported, Methods are factual, figure labels/captions match the assets, cited sources support the text, uncertainty and replication are accurately described, and required format checks actually pass. Report limitations when any of these remain unresolved. Scientific plausibility and polished prose are not substitutes for missing experiments, and publication is an editorial decision.
