# APOE4 dual-bottleneck gate: entry × lysosomal fate

**Mechanism Atlas | 21 November 2026 | Literature-grounded future experiment and executable pilot QA, not original wet-lab findings.** The user has **not** officially submitted a MecCog entry or sent this proposed work to Dr Muaddi Alharbi.

## Actual prior published results — and what they do not establish

| Source | Same parental background names? | What was actually rescued | Assay that is still missing |
|---|---|---|---|
| Gevorgyan *et al.*, NIH-affiliated **bioRxiv preprint**, posted 22 May 2026, DOI [10.64898/2026.05.22.726347](https://doi.org/10.64898/2026.05.22.726347), [PMCID PMC13228211](https://pmc.ncbi.nlm.nih.gov/articles/PMC13228211/) | **AG09173 and KOLF2.1J** human isogenic APOE3/APOE4 iPSC astrocytes | SHIP1/INPP5D or PICALM improved 5-min transferrin uptake. Fig 6J shows published phosphatase-dead SHIP1 rescue too (not ours). RAB11/RAB7 **staining** not measurably rescued by interventions | True receptor surface-return rate and uptake-normalized verified proteolysis under SHIP1 |
| Mesentier-Louro *et al.*, **peer-reviewed Cell Stem Cell 2026**, DOI [10.1016/j.stem.2026.08.001](https://doi.org/10.1016/j.stem.2026.08.001), [PMCID PMC13528747](https://pmc.ncbi.nlm.nih.gov/articles/PMC13528747/) | **AG09173 = Donor 1; KOLF2.1J = Donor 2** in Methods (some other assays use further lines) | APOE4 DQ-BSA deficit persists after normalization to co-internalized dextran (Fig S4e, author p=.0098). Cholesterol-lowering MβCD increased the DQ-BSA signal (Fig5b, author p=.019) and signal replicated under a second-donor condition | For Fig5b drug rescue specifically, uptake-corrected, chemically calibrated cargo breakdown; the figure legend describes 24h **integrated DQ-BSA fluorescence**, without documenting the earlier co-dextran correction for that intervention |

**Same parental line name ≠ same edited clone, same passage, same differentiation batch or matched observations.** These are two different scientific articles and their source p-values cannot be combined to infer synergy or even that the same assay-medium conditions reproduce both baseline deficits.

**Earlier prior art:** PICALM rescue of ApoE4 astrocyte endocytosis appeared in 2020 (*Cell Reports* DOI 10.1016/j.celrep.2020.108224); cholesterol-depletion/lysosomal rescue in human APOE4 astrocytes appeared by 2023 (PMID 37777962). We **do not claim SHIP1 rescue, cholesterol lowering, or dual-pathway dysfunction as first-time discoveries**. Targeted searches have not shown these exact two perturbations used in a single blinded human-iPSC factorial experiment; this is not an exhaustive novelty/patent search.

## A real prospective, **falsifiable** test

- **Pilot stage 0 GO/NO-GO:** Establish the E4-vs-E3 early transferrin uptake defect AND late **dextran/entry-corrected** proteolytic deficit **in the same harmonized iPSC astrocyte culture protocol**. If one disappears, do not claim two independent bottlenecks.
- **Intervention stage 1:** Within APOE3 and APOE4, cross SHIP1-WT 0/1 × validated nontoxic MβCD 0/1 = **eight arms** per independent genetic background and differentiation batch. Both same-parent source names are candidates; exact clone identity, donor age/diagnosis, drug dose/timing and culture identity must be verified before primary assay. Additional parental genetic backgrounds are needed for broader generalization.
- **Matched uptake and true fate:** Use (A) transferrin entry and **normalized returned-to-surface receptor** and (B) **different degradable substrate** with quantified t0 internalized mass + *chemically confirmed* degradation fragments represented as parent-protein-equivalent molar mass. DQ-BSA plus dextran is a secondary proxy, not a chemically complete mass balance. Record retained/released/intact/disjoint pools, membrane cholesterol, early-endosomal and lysosomal pH separately, and viability.
- **Factorial causal question:** Within a verified independent parental background and batch, compute E4 2×2 interaction for each endpoint, and whether the interaction differs from E3. **Synergy cannot be inferred from two studies' separate p-values.**
- **Stop rules:** no replicated baseline deficit, changing uptake without real verified cleavage, no receptor return rescue, low viability, severe pH perturbation, membrane damage, missing true independent batches, or mismatched initial cargo. No strong clinical/cure claims.

See [the source-anchored full evidence and falsifier matrix](SOURCE_EVIDENCE_AND_FALSIFIERS.md).

## Executed software — NOT experimental data

[dual_rescue_factorial_gate.py](dual_rescue_factorial_gate.py) — Python standard library only. It validates an **eight-arm design per culture batch and per cargo**, rejects duplicate/missing and mismatched starting masses, checks viability, mass balance and chemically verified degradation, and computes **descriptive** difference-in-differences. It does **not** calculate inferential p-values or certify treatment success.

[test_dual_rescue_factorial_gate.py](test_dual_rescue_factorial_gate.py) — synthetic-only regression tests covering 64 invented records, no baseline deficit, excessive loss of cargo, lack of chemically verified degradation, unmatched starting mass, invalid culture identifiers, duplicate and missing arms. A real degradable-substrate **uptake improvement is NOT required** for a *fate* gate; the true condition is verified degradation after matching the initial internalized mass.

On the authorized Mac, the script and tests were independently downloaded from immutable GitHub snapshots (script commit `16544217ffc6fc50ec75e3d2bfd580971231ac1e`, tests commit `6797d91877493a88f86c7d2a3ab975db9cf2e7f6`) and **executed successfully (exit 0)**. No wet-lab dataset was loaded.

```bash
python3 test_dual_rescue_factorial_gate.py
python3 dual_rescue_factorial_gate.py --demo --output SYNTHETIC_DEMO_NOT_BIOLOGICAL.json
```

A separate **blank** 64-condition JSON manifest, with NO measurements and unverified clone IDs labeled, was generated in the ChatGPT conversation working files (not claimed to be published here). It includes two *proposed* parental backgrounds × two *proposed* differentiation batches × two different cargos × eight arms, **not 64 independent human donors**.

**Status for MecCog:** This research synthesis **does not add a direct primary paper finding** of ARF6-GTP-driven receptor return (H2), a same-assay lipid-caused lysosomal rate (H5) or de novo APOE self-aggregate formation inside human endolysosomes (H3). Competition Excel drafts remain unsubmitted. Further work requires a human neuroglial laboratory collaborator and independent causal experiments.