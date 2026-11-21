# Mechanism Atlas — from early uptake rescue to verified cargo fate (2026-11-21)

**Status:** Research-stage prior-art correction and laboratory analysis gate, **NOT** a novel biology finding, medical treatment, conference acceptance, or MecCog submission.

## A major May 2026 source we must not claim as ours

**Gevorgyan A. S. et al.**, [*APOE4 and INPP5D converge on membrane mechanics to regulate endocytosis in human astrocytes*](https://doi.org/10.64898/2026.05.22.726347). **bioRxiv PREPRINT**, originally posted 22 May 2026; PMID 42239208, PMCID [PMC13228211](https://pmc.ncbi.nlm.nih.gov/articles/PMC13228211/). This work, from NIH-affiliated laboratories, used **human APOE3/APOE4 isogenic iPSC astrocytes derived from two parental backgrounds, KOLF2.1J and AG09173**, assayed under serum-free conditions.

**Directly published source observations:**

1. **APOE4 baseline:** Fewer mature clathrin-coated pits, reduced 5-minute fluorescent-transferrin uptake and EEA1 intensity, and reduced immunofluorescent RAB11, RAB7, and LAMP1 compartment markers relative to APOE3 (Figs 1–2). There were multiple wells/flow runs in two backgrounds, **not 18–23 independent donors**.
2. **INPP5D/SHIP1 and PICALM overexpression:** Both increased early transferrin entry and EEA1 (Fig 5A–D). **Neither** measurably restored **RAB11** or **RAB7** immunofluorescence signal in the reported comparison (Fig 5E–H). INPP5D decreased LAMP1 signal (Fig 5I–J). *Marker intensity is neither the rate of receptor recycling nor the rate of lysosomal cargo proteolysis.* Thus “no detectable change in RAB11/RAB7 staining” must **not** be equated to experimentally proven absence of late functional rescue.
3. **Distinct early mechanics:** PICALM reduced measured membrane tension; INPP5D did not, but altered clathrin dome/sphere maturation (Fig 6).
4. **CRUCIAL PRIOR ART:** Overexpressing a **phosphatase-dead SHIP1/INPP5D variant (P668A/D672A/R673G)** also improved transferrin uptake (Fig 6J; six independent flow-cytometry runs pooled across two isogenic lines). The authors say the rescue **may be independent of phosphatase activity**. This does **NOT** establish an endogenous, expression-matched, direct scaffold-specific mechanism or identify a requisite SHIP1–SNX27/CapZ interface.
5. **Other endpoints:** Increasing INPP5D reduced lipid-droplet accumulation and cytokine-associated NF-κB nuclear translocation (Fig 7), already author prior art. It does **not** establish a non-diseased human therapy or prevention of neuronal degeneration.

**Additional known prior art:** Terzioglu et al., [bioRxiv v2 21 June 2026 DOI 10.1101/2025.10.27.684632v2](https://www.biorxiv.org/content/10.1101/2025.10.27.684632v2), already report SHIP1/CapZ physical interaction and partial TREM2-associated functional rescue in their own systems. Prasad & Rao, [PNAS 2018 DOI 10.1073/pnas.1801612115](https://doi.org/10.1073/pnas.1801612115) and Xian et al., [eLife 2018 DOI 10.7554/eLife.40048](https://doi.org/10.7554/eLife.40048) have **opposite-direction NHE6/endosomal pH interventions** in *different rodent-derived cell lineages and receptor/cargo contexts*; no universal pH treatment is inferred.

## A narrow remaining gap: does rescue *propagate* after entry?

No cited Gevorgyan source assay directly demonstrates that the SHIP1 or catalytic-dead intervention restores:

- **Time-resolved receptor surface return** after initial, uptake-matched internalization;
- **Verified proteolytic cargo mass balance** inside lysosomes or release/egress fractions;
- **New ApoE protein assembly** within an endolysosome rather than import of existing seeds; or
- **Synapse/viability safety** of the downstream rescue across independent parental human backgrounds.

**Candidate hypothesis to falsify**, not observed biology: SHIP1 rescues clathrin-mediated **entry** without necessarily rescuing **receptor-specific downstream recycling and/or lysosomal degradation**; catalysis and scaffold-like mechanisms may differ at that late stage. PICALM is a useful comparator because it rescues early uptake through measurably distinct membrane mechanics. A full-fate rescue could instead be present but invisible to RAB11/RAB7 marker staining; direct functional experiments must settle it.

### Minimal causal intervention layout (prospective human iPSC lab, NOT performed)

- **Cell units**: At least two genuinely distinct parental human iPSC backgrounds with isogenic APOE3/E4 astrocytes, independent differentiation batches and blinded assays; verify true donor origin and permissible non-aged/non-AD interpretation.
- **Arms**: E3 vehicle, E4 vehicle, E4+SHIP1-WT, E4+SHIP1-catalytic-dead, E4+PICALM. These intervention constructs are previous author technology, **not our invention**. Optionally add SHIP1×PICALM factorial interaction only after pilot power and controls are fixed.
- **Stage A**: 5-min calibrated uptake and clathrin-state readouts.
- **Stage B**: Synchronized uptake, surface strip/wash, **matched quantified internalized dose**, time-resolved transferrin receptor return; calculate *surface-returned / internalized-at-t0*, not fluorescence only.
- **Stage C**: A **separate valid degradable substrate**, biochemically verified degradation fragments / t0, plus intact released and remaining peptide. DQ-BSA fluorescence alone is **not** direct mass balance; RAB11/RAB7/LAMP1 intensity alone is **not** k_rec/k_deg.
- **Physiology and safety**: Calibrated compartment-specific endosomal vs lysosomal pH (do not interchange), validated cell viability, independent donor and culture batch variance. Compare cargo categories separately; do not demand physiological transferrin degradation or recycling of degradable peptides as the main endpoint.
- **Research gate**: A treatment that rescues entry but not direct late cargo fate is an **early-only rescue**, not complete recovery. If apparent late improvement vanishes after uptake matching, favor the entry explanation. Any catalytic-dead outcome requires expression/localization, substrate and PIP3/PI(3,4)P2 controls before claiming a scaffold-specific molecular route.

## A functional, conservative **pilot data-quality** analyzer

An offline Python *research engineering* tool was created and tested in this ChatGPT research session: `fate_rescue_gate.py` (SHA256 **`cd4c0690bbada050218008f2e81456e60e9286fcdbef606e8eb326fc120fe4ee`**). It expects independent differentiation-batch **summary** records with both genotype controls and the three E4 intervention arms for each background/cargo. It records five-minute uptake, baseline-entry-normalized receptor return, verified degradation fragments, recovered intact/released cargo, independent early/late pH and viability; it flags missing experiments, double-counting, incomplete mass recovery, and no baseline deficit.

The analyzer explicitly **does not calculate p-values, estimate a human treatment effect, prove molecular catalysis-independence or certify clinical efficacy**. Its gates use arbitrary pilot-design thresholds that collaborators must prespecify and calibrate. A 40-record example has `data_origin=SYNTHETIC_DEMO` and no full dual-cargo fate rescue; it is **not** a result from human iPSC experiments. Mechanical QA tests were executed on duplicate records, unsupported image-level provenance, changed cargo identity and mass-closure errors.

**Artifact location:** Available to the researcher as a direct ChatGPT conversation attachment, not pushed as a public GitHub code file in this commit; copy it to the laboratory analysis environment once a collaboration is agreed. Thus this README is a **source/audit provenance record**, not a representation that the Python code is already in GitHub.

## MecCog decision gate

The preprint is highly relevant human APOE3/APOE4 **early endocytosis** evidence and SHIP1 prior art, but it does not measure a direct **ARF6-GTP→receptor recycling** H2 chain, nor direct **lipid-metabolism→late lysosomal degradation** H5 chain in the same intervention assay, nor ApoE4 de novo within-lysosome aggregation H3. No **new direct** Class1–4 Step-1 experimental finding was generated by our secondary analysis, and source padding may penalize accuracy-first judging. **Do not append speculative "proof of recycling/degradation restoration" rows to H2/H5**, and do not upload an official competition entry without explicit user direction.

## Collaboration brief status

A **new two-page English discussion PDF** corrects the earlier draft to acknowledge the published catalytic-dead SHIP1 rescue and restrict novelty to downstream fate and verified mass balance. It is prepared **only in the researcher's ChatGPT workspace**, not sent to Dr Muaddi Alharbi. The original LinkedIn interest-check message was sent by the researcher, and no follow-up was initiated here.

**Novel claim status**: We have a falsifiable *experimental design* and a reproducible software QA method. We do not yet have independent human-cell biochemical results, a patentable cure, or a proven Nobel-scale contribution.