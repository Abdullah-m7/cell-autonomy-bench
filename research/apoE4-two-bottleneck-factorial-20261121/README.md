# APOE4 dual-bottleneck gate: entry × lysosomal fate

**Mechanism Atlas | 21 November 2026 | Literature-grounded future experiment and executable pilot QA, not original wet-lab findings.** The user has **not** officially submitted a MecCog entry or sent this proposed work to Dr Muaddi Alharbi.

## V2: source-locked intervention interaction and dose comparability gate

We reviewed the source Fig5b/S4e methods and discovered a **differential drug exposure caveat**. The 2026 peer-reviewed human-APOE4 astrocyte study treated cells with **100 µM MβCD over several days**; acute historical **10 mM/15 min MβCD** experiments in other cells impaired clathrin-mediated transferrin uptake, but this is a *different concentration (100×), duration and cell system*, **not a direct refutation of the 2026 result**. Sources: [Mesentier-Louro 2026 Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC13528747/) and [Rodal et al. 1999](https://pmc.ncbi.nlm.nih.gov/articles/PMC25220/). The 2026 study also reports **increased α-synuclein uptake** with MβCD; increased DQ-BSA signal without treatment-matched uptake correction alone cannot identify **per-internalized-dose chemical degradation**. Its *baseline* DQ-BSA/dextran control is a distinct experiment from treated Fig5b.

Two previously missed **data-QA / scientific interpretation** cases were found by adversarial synthetic counterexamples:

1. The earlier schema checked t0-mass matching **within each genotype across arms**, but could still label a restored genotype gap after E3/E4 starting cargo differed by 30% within the same treatment. The new [estimand audit v2](dual_rescue_estimand_audit_v2.py) *blocks genotype cross-comparison* when the declared source t0 differs beyond the arbitrary engineering tolerance; the natural genotype entry deficit should still be measured in a separate untitrated pulse, and matched t0 must be achieved by a valid experimental design rather than merely statistical adjustment.
2. The original composite-success indicator did not distinguish a treatment pair that rescued three endpoints from a **single intervention already sufficient** to rescue those endpoints. V2 reports both **full composite recovery** and **incremental necessity of both treatments**, and separately computes the E4 factorial interaction and its E4–E3 contrast **on explicitly named measurement scales**. None of these computer outputs constitutes population-level statistical synergy.

The [six adversarial tests](test_dual_rescue_estimand_audit_v2.py) all passed: ordinary synthetic example, cross-genotype dose mismatch, redundant single-treatment efficacy, mass-balance violation, incomplete block, and fluorescence-only degradation. The original v1 QA also still passes. The original synthetic readouts intentionally show **opposite-signed interactions on different endpoints** (E4: transferrin uptake −2 toy units, receptor recycling +0.09 fraction, verified degradation +0.06 fraction); this proves the **software distinguishes endpoint scales**, not any human biological response.

**Mac clean-room test actually completed:** downloaded the four exact files from pinned GitHub commit `0d56b65603ad5b09be23c7cf06c161d68aeecab8` (original v1, v2, v2 tests, Arabic research gate) into a *new* research directory and verified their SHA256 values against the conversation-generated originals. Ran all six adversarial tests, exit 0, and reproduced the 64-record synthetic output with **byte-exact SHA256 `94cd02be9b860607a5a7fff386cfc89634f7fdae1dc156401a08b26c11d120b0`**. This is independent *code execution*, not independently collected human biological evidence.

The [full Arabic primary-source & causal protocol](DUAL_RESCUE_V2_SOURCE_AND_CAUSAL_GATE_20261121.md) specifies the most important **future primary contrast**: whether SHIP1+MβCD improves **chemically verified degradation per experimentally matched internalized t0** beyond MβCD **alone**, while preserving transferrin entry/recycling and viable, calibrated organellar pH. Complementarity, additive interaction and synergy are different estimands; no unmeasured lab effects are asserted. Two parental backgrounds alone are not a population inference; prospective additional donor backgrounds and independent differentiation batches are required for generalizability.

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