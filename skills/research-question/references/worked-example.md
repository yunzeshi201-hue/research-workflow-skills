# Worked Example: A Sensor-Network Anomaly

This is a wholly synthetic teaching example. Its system, observations, constraints, and possible outcomes are illustrative. It makes no claim about a real dataset, current literature, or research novelty. Proposed tasks have not been performed.

In the four-stage workflow, use this as a stage-2 question and feasibility example after accepting the subfield. Its proposed audits, calibration, and experimental branches do not authorize executing a study or skipping the question-set, website, and review checkpoints.

## Start with an aim

An imagined team wants a building-monitoring system to distinguish persistent local overheating from sensor faults. It has noticed occasional temperature excursions in stored readings and has a small calibration chamber available.

"Use a new anomaly detector" is a possible implementation. The research-relevant uncertainty is whether the available observations can distinguish local heating from measurement artifacts under the intended deployment conditions.

The consequence matters: a detector that cannot separate the causes may trigger unnecessary inspections or miss real events. Whether this is a publishable research gap remains unassessed. The team first needs to examine the nearest work on sensor drift, environmental monitoring, and fault diagnosis under comparable conditions.

## Decompose the question

`reliable event decision -> distinguish physical change from artifact -> define temperature excursion and sensor error -> identify the source of the observed excursions -> obtain predictions that differ -> choose a corrective action`

Define a physical excursion as a local temperature change relative to a calibrated reference over a stated interval. Define sensor error as disagreement with the reference after accounting for the reference's uncertainty and response time. Duration and magnitude thresholds must follow the intended decision and calibration performance; none is assumed here.

The bounded question is:

> Under the intended operating conditions, can local temperature excursions be distinguished from sensor-specific drift or logging artifacts using the available measurements?

The following dependencies are relevant:

| Micro-question | Why it matters | First useful task |
|---|---|---|
| Are timestamps and transformations trustworthy? | Misaligned records can imitate disagreement between sensors. | Reconstruct the logging and processing path for an existing event. |
| Does sensor response remain stable under controlled conditions? | Unstable calibration undermines interpretation of field anomalies. | Compare sensors with a reference in a shared controlled environment. |
| Does the anomaly follow a device or a location? | These outcomes imply different candidate causes. | Design a controlled device-location swap if the first checks are adequate. |
| Can the remaining causes be distinguished within attainable uncertainty? | An apparently useful pattern may be too small or ambiguous to classify. | Estimate uncertainty and compare rival predicted patterns. |

Each answer changes the parent plan. A timestamp failure makes pipeline repair the next step. A stable device calibration permits a stronger field test. Ambiguous location effects require another observable or a narrower claim.

## Audit the inference before training a model

| Step | Proposed inference | What could break it |
|---|---|---|
| Raw voltage to logged temperature | Calibration converts the measured response to temperature. | Offset, drift, conversion mistakes, or response lag. |
| Logged temperature to anomaly score | Processing identifies an unusual departure from baseline. | Resampling, missing values, timestamp errors, or baseline mismatch. |
| Anomaly score to local overheating | The departure reflects a physical change at that location. | Device fault, airflow differences, placement changes, or shared interference. |
| Local overheating to maintenance decision | The event exceeds a meaningful operating limit. | An arbitrary threshold or a consequence model unsupported by the intended use. |

A high anomaly score establishes unusual data relative to a model. It does not establish the cause of the unusual data.

## Compare possible explanations

- **Physical local change:** A calibrated independent reference should register a compatible change at the location after accounting for response differences.
- **Device-specific drift:** Disagreement may follow the device into a controlled environment or another location.
- **Logging artifact:** Reconstructed raw records and processed records may diverge in a way that explains the apparent event.

These predictions are conditional. A device-location swap could also alter contact, airflow, or orientation, and a common environmental interference could affect both devices. Record these alternatives rather than treating a single swap as definitive proof.

## Choose the next action

First audit one existing event from raw record to processed trace, retaining timestamps, units, transformation settings, and missing-value treatment. This can eliminate an avoidable ambiguity before collecting more data.

If that audit finds no explanatory defect, use the chamber to compare the devices with a calibrated reference across the operating conditions relevant to the question. Plan independent runs sufficient to estimate repeatability. Choose the acceptance tolerance from the required decision and the combined measurement uncertainty; a convenient sample count or arbitrary score is not a substitute.

The pilot's purpose is to learn whether the proposed field test can be informative. It is not yet evidence that the monitoring system works in deployment.

## Branch on the result

| Possible result | Supported conclusion | Next decision |
|---|---|---|
| A processing error reproduces the apparent excursion | This event is explained by the identified transformation defect. | Repair and reprocess, then reassess whether a residual scientific question remains. |
| A stable device-specific bias appears in controlled comparisons | The device needs calibration or replacement under the tested conditions. | Correct the bias and ask whether field excursions persist. |
| No meaningful disagreement is found, with uncertainty small enough for the stated tolerance | The tested calibration defect is bounded under those conditions. Other artifacts remain possible. | Proceed to the controlled field comparison. |
| No disagreement is detected, but uncertainty is too large | The comparison cannot discriminate the candidate causes. | Improve the reference, repeatability, or operating-range design before drawing a null conclusion. |
| Both devices track a location-dependent change | A physical local change is supported, subject to shared interference and placement controls. | Test the remaining alternatives before attributing the event to overheating. |
| Outcomes overlap across device and location changes | The current design is inconclusive. | Add an independent observable, narrow the operating conditions, or stop if no attainable test can separate the causes. |

## What became smaller

The original aim was a reliable monitoring system. The immediate task is an inspectable audit of one event, followed conditionally by calibration. Both tasks directly affect whether a later detector study would answer the real question.

A separate literature search must determine whether any unresolved contribution remains after these checks. It is a valid outcome to discover that the problem is a known engineering defect rather than a new research question.
