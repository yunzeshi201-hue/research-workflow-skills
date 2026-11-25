# External evidence records and registry

Use an existing equivalent schema if available. Otherwise a JSONL/CSV table plus Markdown notes is sufficient; do not build a database service unless requested.

## Library registry

`library-registry.json` has `schema_version` and a `libraries` array. Each entry may contain:

- `id`, `title`, `scope`: stable library identity and topics.
- `root`: external library root, supplied by the user or established project context.
- `catalog`, `index`, `notes_dir`, `evidence_table`, `bibliography`: paths relative to `root` where practical.
- `project_match`: optional project/context match for selection.
- `methods`: optional routing tags such as TAS, FSRS, THz, PPP, PL, and TRPL. Tags describe intended scope, not verified coverage; consult the catalog for actual access and reading status.

Store only routing metadata in the registry. Researcher publications, extracted facts, numerical spectra, manuscripts, and learning progress belong in the external library. Do not place secrets in registry entries. Preserve existing entries when adding a library.

## Catalog fields

At minimum: `paper_id`, `title`, `authors`, `year`, `doi_or_stable_id`, `versions`, `source_urls`, `inclusion_reason`, `scope_status`, `main_access`, `si_access`, `reading_status`, `note_path`, `unresolved_items`, `last_checked`.

Keep main/SI access separate. `reading_status` should distinguish catalog-only, limited stub, distilled, and evidence-checked. Link preprint and journal versions rather than counting them twice.

## Evidence fields

| Field | Meaning |
|---|---|
| `record_id`, `paper_id`, `note_path` | Stable route back to the note and catalog |
| `origin`, `figure_id`, `panel`, `source_asset`, `raw_data_ref` | User experiment, published source, or derived analysis; link the inspected figure and available original arrays. Published figures are not the user's new results |
| `source_locator`, `source_version`, `access_level` | Figure/panel/table/section/SI page and accessible evidence |
| `method`, `measurement_mode` | TAS, FSRS, THz, PPP, PL/TRPL, with actual acquisition mode; method labels alone do not define the measured quantity |
| `material`, `sample`, `structure`, `composition` | Chemical identity and actual studied system; unknown stays unknown |
| `preparation`, `conditions` | Processing, environment, excitation, time range, and relevant measurement settings |
| `observable`, `signal_definition`, `unit` | What was measured and the convention used |
| `axes`, `time_definitions`, `normalization`, `offsets` | Axis quantities, scales, delay origins and pulse sequence; reference subtraction, scaling and vertical offsets |
| `instrument_response`, `resolution`, `calibration` | Time/spectral response and calibration actually provided; mark unknown explicitly |
| `replicates`, `error_definition`, `statistics` | Independent samples versus repeated scans, meaning of error bars, statistical procedure; none may be inferred from a plotted line |
| `value`, `value_kind`, `uncertainty` | Center, range, shoulder, monitor, integration window, bound, or other quantity type |
| `value_origin` | Author-reported, digitized, or derived; include derivation when applicable |
| `observation` | The measured or calculated result before mechanistic assignment |
| `author_assignment`, `author_reasoning` | What the paper concludes and its evidence chain |
| `controls`, `alternatives`, `conflicts` | Tests performed, unresolved interpretations, and source disagreements |
| `our_evaluation`, `transfer_limits` | Defensible inference strength and conditions for reuse |
| `verification_status` | Checked against source, provisional extraction, conflict, or unresolved |
| `missing_metadata`, `fit_provenance`, `identifiability_limits` | Unprovided methods, source of reported or newly fitted parameters, and alternative models the observable cannot resolve |

Use qualitative, explained confidence rather than an invented probability. A well-verified number can still have an ambiguous physical assignment. Track these two uncertainties separately. Do not overwrite the observation with the preferred mechanism.

For figure-led work, explicitly separate `figure_observation` (visible feature), `reported_interpretation` (caption/author/user assertion), and `our_inference` (reasoned conclusion with alternatives). `observation` may map to `figure_observation` in an existing schema. A label on a graph is reported metadata, not independent verification of its physical assignment.

Method-specific fields are conditional, not compulsory empty columns:

- TAS: DeltaA/DeltaOD/mOD versus DeltaT/T or DeltaR/R, sign, pump wavelength/fluence, probe or integration window, GSB/SE/ESA/EA candidates.
- FSRS: Raman shift in cm^-1, Raman pump and actinic pump, gain/loss/difference definition, resonance condition, mode assignment and structural controls.
- THz: electric-field versus intensity response, detection time versus pump delay, frequency versus angular frequency, real/imaginary conductivity, sheet/bulk units, substrate/thickness model, density/yield/mobility assumptions.
- PPP: pump/push/probe identities and fluences, pump-push and push-probe delays, differential formula, chopping/reference states, push-only and overlap controls.
- PL/TRPL: emission axis, excitation and collection conditions, spectral correction, PLQY calibration, time response, decay model, lifetime convention, reabsorption and quenching controls.

## Claim-to-source links for writing

A compact claim ledger can use `claim_id`, `draft_location`, `claim_text`, `claim_type` (observation / interpretation / comparison / prediction), `record_ids`, `citation_keys`, `support_status`, and `scope_limit`. Preserve the source locator even when the final manuscript citation is only a paper-level reference.
