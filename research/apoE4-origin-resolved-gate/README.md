# Origin-resolved ApoE aggregation: formation vs clearance
**Mechanism Atlas | 21 November 2026 | Experiment-design research, not original wet-lab biology.**

## Purpose
Distinguish (i) import of preformed aggregates, (ii) de novo formation inside the endolysosome, and (iii) degradation/egress. A single late aggregate burden does NOT identify the relative rates.

## Literature triangulation: an apparent pH-direction tension, not a contradiction
1. **Guo et al., Cell (published online 2024, issue 2025)** [DOI 10.1016/j.cell.2024.10.027](https://doi.org/10.1016/j.cell.2024.10.027) report increased cell-free pelleting of CE(20:4)-lipidated ApoE at pH 4.5 versus pH 7.4, and stronger ApoE4 than ApoE3 acidic pelleting. The assay uses **purified synthetic lipoprotein particles** (not intact lysosomes), and lipid chemistry matters.
2. **Kerstein et al., Autophagy (2025)** [DOI 10.1080/15548627.2025.2576613](https://doi.org/10.1080/15548627.2025.2576613) report *human-APOE-expressing mouse Neuro-2a* cells with lysosomal pH **5.86 (E4)** vs **4.30 (E3)**, and lower cathepsin-related fluorescence in E4. This does **not** measure intra-lysosomal ApoE aggregation in human iPSC-derived glia; E3/E4 lysosomal pH values are specific to that model.
3. **Xia et al., Nature Communications (2024)** [DOI 10.1038/s41467-024-49028-z](https://doi.org/10.1038/s41467-024-49028-z) measure human microglia and astrocyte uptake of preformed ApoE–Aβ coaggregates; uptake is not evidence of new ApoE self-assembly in those endolysosomes.
4. **Mesentier-Louro et al., Cell Stem Cell (2026)** [DOI 10.1016/j.stem.2026.08.001](https://doi.org/10.1016/j.stem.2026.08.001) report an ApoE4-associated lower dextran-normalized DQ-BSA signal in isogenic human iPSC astrocytes (Fig S4e, reported p=.0098). Panel-specific independent biological n remains unresolved in our source audit, so do not treat 4 instrument traces as 4 independent donors.

**Scientific insight:** acidic conditions may increase ApoE assembly capacity, **and independently** increase lysosomal removal efficiency. Hence an E4 model with a larger *residual aggregate pool* could have a **slower new-assembly rate** and a more seriously impaired clearance rate. Cross-study observations are not a paired confirmation of this mechanism.

## Computational result (100% SYNTHETIC)
A monomer pulse of 100 arbitrary units is followed in two hypothetical states:

dM/dt = -(k_form + k_mclear) * M
dA/dt = k_form * M - k_aclear * A

At t=0: M=100 and A=0. Both fates are measured in arbitrary units. **Rate constants were selected illustratively, not estimated from sources, not linked by a measured pH-rate relationship.**

| State | k_form/h | k_mclear/h | k_aclear/h | New aggregate A at 2h | A at 24h |
|---|---:|---:|---:|---:|---:|
| More acidic (illustrative) | .08 | .12 | .30 | 9.721 | 0.599 |
| Less acidic (illustrative) | .02 | .025 | .015 | 3.768 | 23.872 |

The curves cross at **6.371 hours**. At 12 hours, exact script results are **A=5.072** versus **A=16.835**, respectively. The key is **structural ambiguity**, not the numerical size or biological likelihood of these arbitrary examples. Mass conservation (monomer + new aggregate + cleared fraction =100) is checked.

Run [the executable Python script](formation_vs_clearance_synthetic.py) using only the Python standard library.

## Minimum causal experiment (not executed)
- In **at least two independent** human iPSC donor backgrounds, generate APOE3/APOE4 isogenic microglia or astrocytes in independent differentiation batches, with donor clinical/age provenance.
- Deliver conformation-verified, **aggregate-free** ApoE3/ApoE4 monomer under matched initial internalized quantity, plus a distinct positive-control arm of **preformed, differentially labeled aggregates**. Exclude external aggregates by surface washing, media sampling and validated baseline controls.
- Vary CE(20:4) vs CE(18:1) with calibrated lysosomal pH and matched cellular viability. Avoid assuming that the cell-free pH sensitivity transfers unchanged to cells.
- At 0,1,4,8,24 hours assay ApoE-specific conformation (validated FLIM-FRET or orthogonal protein conformational readout), lysosomal compartment location (LAMP1/RAB7 + fractionation), aggregate mass, initial uptake/retention and **proteolytic clearance** independently.
- Include non-ApoE lipid peroxidation controls and pH sensitivity calibrations for each fluorophore. If assembly signals are fully accounted for by seed import/uptake, or have no orthogonal protein confirmation, **reject de novo formation**.
- Independently normalize/reproduce across donor backgrounds; images and wells do not constitute independent patients. No p-values or therapeutic efficacy are claimed.

## Global structural identifiability check — two equally valid biological fates (21 November 2026)

**New work in our ApoE design model; the underlying mathematics is prior art.** A two-compartment system with one measured output can possess an exact parameter-exchange ambiguity (see [Godfrey & Chapman, 1990](https://doi.org/10.1016/0378-4754(90)90185-L), [Zhang, Collins & King, 1991](https://doi.org/10.1016/0025-5564(91)90092-W), and a [2026 structural-identifiability tutorial](https://doi.org/10.1007/s11538-026-01779-0)). Our contribution is an **application to an assay-design question**, not the invention of the mathematical theorem.

Let initial monomer M(0)=100, initial newly formed aggregates A(0)=0, rates kf for assembly, km for monomer removal, and kc for aggregate removal:

`dM/dt = -(kf+km)*M`; `dA/dt = kf*M-kc*A`.

The exact aggregate signal is `A(t) = M0*kf*(exp[-(kf+km)t]-exp[-kc*t])/(kc-(kf+km))`. **The transformation** `(kf,km,kc) -> (kf,kc-kf,kf+km)` leaves the *ENTIRE continuous aggregate curve* unchanged whenever both alternatives remain biologically admissible. The measured A(t) is **not globally unique** in these parameters even for noiseless dense measurements. This does NOT assert that all parameters are locally unidentifiable in the formal mathematical sense.

| Hypothetical parameter set | kf (/h) | monomer removal km (/h) | aggregate removal kc (/h) | A(12h) | M(12h) | already removed D(12h) |
|---|---:|---:|---:|---:|---:|---:|
| Interpretation 1 | 0.08 | 0.12 | 0.30 | **5.0715** | **9.0718** | **85.8567** |
| Interpretation 2 | 0.08 | 0.22 | 0.20 | **5.0715** | **2.7324** | **92.1961** |

At 24 hours both A(24h)=0.59865 again, but M differs markedly. The **maximum aggregate-curve absolute mismatch over 577 points from 0–72h was exactly zero in double precision**, and 250 randomly generated feasible positive-parameter transformations passed numerical checks. Code [structural identifiability](structural_identifiability_twofold.py), backed by SHA-locked local results `H3_AggregateOnly_Twofold_Identifiability_20261121.json` on the researcher Mac. **No biological data were fit.**

### What one orthogonal monomer assay would change

Under **these artificial two rate sets**, the absolute monomer difference `|100*exp(-0.20t)-100*exp(-0.30t)|` peaks at **t = ln(0.30/0.20)/(0.30-0.20) ≈ 4.05465 hours** (14.8148 arbitrary units). At 24 hours the monomer difference is only **0.7483**. Thus if measurement noise has the **same absolute SD at each time** (one *assumed* Gaussian SD=3 units), a single 4.05h monomer readout can theoretically distinguish the two fixed models much more reliably than a 24h readout (toy equal-prior misclassification risks ≈0.00677 vs ≈0.45037). This is **not a real power calculation or experimentally established optimal time**, and heterogeneous/relative fluorescence noise would change the choice. The timing must be optimized in new human-cell pilot data, not blindly used.

Executable code: [optimal monomer measurement](optimal_monomer_measurement.py). The important general result is that **an orthogonal monomeric intact-ApoE measurement and measured degradation/exit mass break this particular symmetry**, while extra images of aggregate-only fluorescence do not.

### Measurement-noise sensitivity — this is not an optimal 4-hour claim

The analytic ~4.05-hour maximizer above **assumes constant absolute measurement error**. Under an explicitly **different** toy error model, each monomer readout has independent variance \(σ0²+(CV·M)²\). Maximizing the standardized separation of the same **two hypothetical kinetic rate sets** over 0–24 hours produces:

| Assumed monomer instrument error | Best toy checkpoint | Standardized difference (peak) |
|---|---:|---:|
| Constant absolute SD=3, CV=0% | **4.05h** | 3.492 |
| Absolute SD floor=2, CV=10% | **7.12h** | 3.146 |
| Absolute SD floor=3, CV=20% | **7.87h** | 1.814 |
| Absolute SD floor=1, CV=5% | **7.12h** | 6.292 |

This standardized score is a **design contrast, not a biological test statistic or claim of clinical/experimental power**. The optimum is **noise-model-dependent** and may change further with limits of detection, actual rates, cell heterogeneity, uptake errors, lysosomal losses, and reporter pH sensitivity. We therefore propose pilot samples near 0,1,4,8 and 24h and a locked confirmatory schedule based on real assay variance. The code [noise sensitivity](monomer_measurement_noise_sensitivity.py) reads the prior source-locked synthetic result and reproduces these values on the Mac. Its JSON SHA256 is `43492cd6be03e84828a3a003ac2a2522dbed46a5087cdf21ca83a9c763081bf4`.

### Source-data sufficiency: why we have NOT claimed a real kinetic estimate

| Existing curated source | What is actually measured | Missing to identify new ApoE assembly and clearance |
|---|---|---|
| Xia et al., *Nature Communications* (2024), doi 10.1038/s41467-024-49028-z, author Figure1A | 241-timepoint Thioflavin T reporter of **Aβ42 fibrillation**, perturbed by APOE isoforms; processed worksheet has **one trajectory per condition**, not complete biological replicates | ApoE self-aggregate specificity, intracellular organelle, ApoE monomer, degradation and seeded-input origin |
| Guo et al., *Cell* (2024/25), doi 10.1016/j.cell.2024.10.027, Fig5O-Q | Endpoint pelleting of purified CE(20:4)-ApoE isoforms at pH4.5 / pH7.4, not a live-cell time-course | In situ ApoE conformational flux, monomer and export, independently defined cell donor backgrounds |
| Kerman et al., *Alzheimer's & Dementia* (2024 meeting abstract, 2025 indexed), doi 10.1002/alz.092614 | ApoE FLIM-FRET/aggregate detection in **living BHK nonbrain cells**; separate tagged-ApoE uptake in human neurons | Same human-cell compartment APOE aggregate formation assay with lysosomal localization, new vs imported conformations |
| Hellén et al., *J Neuroinflammation* (2025), doi 10.1186/s12974-025-03470-y | Human iPSC microglial uptake and lysosomal enzyme-surrogate fluorescence | Direct ApoE aggregate identity and formation/clearance rates |

**This is a screened set of four relevant public sources, not a systematic proof that no such dataset exists anywhere.** Continue source search and seek experimental collaborators. Do not fit the H3 ApoE formation-vs-clearance model to an *Aβ reporter* and call the parameters biological ApoE rates. No new human wet-lab experiment has occurred.

### Independent clean-room code reproduction (21 Nov 2026)

We fetched the **four exact source text files** (the frozen protocol and three scripts) from immutable GitHub commit `63a7b76493ce2a369cb6005bccb9cd5764edbab6` into a **new empty directory** on the authorized Mac and ran all three scripts sequentially under Python without third-party packages. All three returned **exit 0**, and the test suite confirmed 250 admissible parameter symmetries, the 4.05h checkpoint, and the 7.12h time under a 10% CV noise model. The JSON output files include a run timestamp, so their SHA256 values differ across runs despite identical numerical checks. This establishes **computational reproducibility only**, not a replicated human cell experiment.

## Competition and collaboration boundary
MecCog H3 (existing 6-paper/20-finding and 7-paper/22-finding candidate workbooks) **still lacks a published finding measuring all components of direct de novo ApoE4 endolysosomal aggregation in eligible human cells**. This model is a research-design instrument and **must not** be inserted into Step 1 as a source experimental finding. No MecCog entry has been uploaded.

The proposed discussion with Dr. Muaddi Alharbi is a request for interest/expert feedback or referral to an appropriate human neuroglial biology laboratory, **not** an agreed collaboration, signed-off experiment or a claim of Nobel-prize-level original discovery. A separate two-page discussion brief is held privately by the researcher pending a reply.
