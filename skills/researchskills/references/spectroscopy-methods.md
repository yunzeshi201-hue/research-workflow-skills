# Spectroscopy interpretation guide

Read only the relevant method sections. Use the actual signal definition and experiment metadata; an acronym does not specify normalization, sample or geometry. The checks below support interpretation and manuscript claims. They are not replacements for instrument-specific preprocessing, calibration or approved analysis pipelines.

## TAS: transient absorption

Identify DeltaA, DeltaOD, mOD, DeltaT/T, or DeltaR/R from the figure or metadata. For a transmission measurement defined as DeltaT/T = (T_pumped - T_unpumped)/T_unpumped, DeltaA = -log10(1 + DeltaT/T); only in the small-signal limit is DeltaA approximately -(DeltaT/T)/ln(10). mOD is 10^-3 OD. Do not apply this conversion to reflectance or an unspecified differential signal.

In the usual DeltaA convention, ground-state bleach (GSB) and stimulated emission (SE) contribute negatively, and excited-state absorption (ESA) positively; signs reverse in the corresponding DeltaT/T convention. Observed bands can overlap. Product absorption, electroabsorption, spectral shifts, scattering or coherent artifacts can also contribute. GSB can overlap SE, and a derivative-shaped response should not be treated as a new positive species band by default. These distinctions are illustrated in [a primary pump-dump-probe study](https://pmc.ncbi.nlm.nih.gov/articles/PMC1304590/).

Compare GSB candidates with sample absorption and SE with emission under compatible conditions. Treat PIA/ESA as an observable category until singlet, triplet, charge or other species is supported by controls. Preserve peak center versus kinetic probe versus integration range. Check chirp/time-zero treatment and instrument response before interpreting early dynamics; identify pump scatter, saturation, annihilation, heating and sample damage where the data bear on them. A long-lived signal alone is not proof of free charges, and bleach recovery is not always the population decay of one state.

## FSRS: femtosecond stimulated Raman spectroscopy

Read the spectral axis as Raman shift, normally in cm^-1, rather than an optical absorption wavelength. Identify the actinic pump, Raman pump, probe, their delays and resonance conditions, and whether the plot is Raman gain, loss, an excited-minus-ground-state spectrum or another difference. The conventional three-pulse method and the effect of Raman pump conditions are described in [McCamant et al.'s apparatus paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC1712672/).

Record mode positions, widths, shapes and relative changes with their calibration and spectral resolution. A differential negative band can reflect depletion or a shift; dispersive line shapes and electronic backgrounds are not automatically new vibrational modes. Keep baseline subtraction and any removal of transient-absorption background traceable. Raman intensity depends on resonance enhancement and cross section as well as population, so do not infer concentration directly from uncalibrated intensity.

Link structural assignments to available ground/excited-state controls, isotope substitution, polarization, known modes or calculations; distinguish a calculated mode assignment from an experimentally isolated structural coordinate. Peak shifts alone do not uniquely determine bond length, temperature, charge localization or a reaction pathway. No universal time or wavenumber resolution may be assumed from the technique name.

## THz: terahertz spectroscopy and optical-pump THz-probe

Distinguish the sampled THz electric-field time coordinate from the optical-pump delay. Read frequency in THz separately from angular frequency, omega = 2*pi*f. Identify whether the figure shows E, DeltaE/E, transmission amplitude, phase, dielectric response, or complex conductivity. Electric-field change is not identical to optical intensity transmission. Extraction of real and imaginary conductivity requires the relevant field/reference data and propagation model; see [a primary time-resolved THz study](https://www.nature.com/articles/ncomms8903).

Keep real and imaginary components and the Fourier sign convention together. Record film thickness, substrate/reference, penetration profile and the use of sheet conductance (S) versus bulk conductivity (S/m or S/cm). Do not fit a conductivity model to a field-amplitude trace as if it were a frequency spectrum, or infer complex conductivity from one pump-delay curve alone.

Under a simple free-carrier model, sigma = e*(n_e*mu_e + n_h*mu_h); the response therefore weights density and mobility. Photoconductivity changes can reflect either quantity, heating, scattering or other excitations. Normalizing to absorbed photons may yield a generation-yield-times-mobility quantity, not mobility alone. A drop in THz amplitude is not automatically recombination. [Combined THz and TA measurements](https://www.nature.com/articles/ncomms8558) demonstrate why population-sensitive evidence is useful for this distinction.

Require density/yield or model assumptions before reporting mobility. Compare both conductivity components across the available bandwidth when testing Drude, Drude-Smith or other models. State parameter identifiability and alternatives; a satisfactory fit alone does not prove a unique microscopic localization mechanism or a long-range device mobility.

## PPP: pump-push-probe

Confirm that PPP means pump-push-probe in this task. Identify the pump, push and probe, their wavelengths/energies, fluences, polarization and sequence. Define pump-push and push-probe delays and which delay is scanned or fixed; a label “delay” alone is insufficient.

Write the measured difference from the actual chopping/reference scheme. Common observables include push-induced Delta(DeltaA) or Delta(DeltaT/T), comparing a pump-excited sample with and without the push after appropriate background subtraction. Do not assume PPP has the same sign or physical meaning as ordinary pump-probe spectra. Verify push-only/direct ground-state excitation, pump-only, negative-delay and pulse-overlap controls where relevant, including whether the stated subtraction has already removed them. The differential definition is illustrated in [a primary PPP study](https://www.nature.com/articles/s41467-017-02457-5).

The push perturbs an existing population and can change absorption, state occupation, temperature, annihilation, mobility or separation. A larger signal does not by itself measure the original bound-state population or an absolute dissociation yield. Assign push-induced separation using spectral references and controls that distinguish electroabsorption and charge signals from competing effects. Preserve the delay after the push when comparing dynamics; do not call it the original population lifetime without a justified model. Do not confuse optical PPP with pump-push-photocurrent measurements.

## PL and time-resolved PL

Read PL as an emission measurement. Record wavelength or photon-energy axis, excitation wavelength/fluence or power, collection geometry, spectral-response correction, integration range and normalization. Do not equate a PL maximum with a TAS bleach or ESA. If converting a spectral density between wavelength and energy, account for the Jacobian; relabeling the axis alone does not preserve integrated intensity.

Separate absolute PL quantum yield from detector counts and normalized emission. Compare quenching only after accounting for absorption, thickness/concentration, inner-filter effects, reabsorption and collection differences where relevant. Lower emission can indicate transfer, trapping or another nonradiative process, but does not by itself establish productive charge separation.

For TRPL, record the instrument response, repetition rate, time window, acquisition mode and convolution treatment. A fitted decay time is not automatically a radiative lifetime or the lifetime of all charges. For multiexponential fits, retain amplitudes, fit range and the defined average; amplitude-weighted and intensity-weighted lifetimes differ. Do not report absent replicate statistics or a unique mechanism from a fit alone.

In a verified single-population first-order model, lifetime and absolute PLQY can constrain radiative and nonradiative rates. Do not apply that reduction indiscriminately to mixed populations, energy transfer, time-varying rates, bimolecular recombination or strong reabsorption. Interpret PL alongside complementary absorption/transport evidence when assigning charge generation or recombination.

## Cross-method claims

Match sample, preparation, temperature, absorbed excitation density, polarization and time resolution before combining datasets. Keep observations, source interpretations and our inferences separate using [evidence-records.md](evidence-records.md). A matching time scale across methods is a consistency check, not proof of a shared species. For actual figure analysis and drafting, continue with [figure-to-manuscript.md](figure-to-manuscript.md).
