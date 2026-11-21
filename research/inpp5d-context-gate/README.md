# Mechanism Atlas — INPP5D context reversal gate (21 November 2026)

**Research status: completed retrospective source-reanalysis.** This is *not* a discovery of a new Alzheimer mechanism, not an inference about independent human donors, and not a MecCog competition submission.

## Question

An existing hypothesis proposed that APOE4 should elevate microglial **INPP5D / SHIP1** mRNA in all tested human isogenic microglial contexts. We already had a within-lineage directional match in GSE102956 (+0.284 log2FC) and GSE305481 (+0.249887; new differentiation of the **same** original iPSC ancestry). The independent-publication expression source **GSE286874** generated a **negative** APOE4−APOE3 INPP5D contrast (−0.630976 log2FC), invalidating the assumption of an invariant positive sign across these data sets.

The two source articles differ in iPSC genetics, differentiation, protocol, library quantification and possible batch/cell-state composition; the *reason* for the sign change remains unidentified.

## Input and provenance

| Cohort | Author source / study | Nature of six samples | Analysis input | Within-study E4−E3 log2FC |
|---|---|---|---|---:|
| GSE305481 | [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE305481), processed original featureCounts, source SHA256 `ddd7d96f13ca2d163f316472cb537ac35436b0e2e2c2eefdc7a67e763a53d1f1` | 3 E3 + 3 E4 culture libraries; same original ancestry as Lin GSE102956 | log2(CPM+0.5) from integer gene counts | +0.249887 |
| GSE286874 | [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286874), [Stephenson et al. *Cell Reports* 2025](https://doi.org/10.1016/j.celrep.2025.115961), original GSE286874_RAW.tar SHA256 `e0018a54a10def3011facbea4579cc66222698ad203b08019a1da69ae165a6d8` | 3 untreated E3 + 3 untreated E4 culture libraries; sample-specific parental origin unresolved | log2(CPM+0.5) from author Salmon gene-length-normalized estimates, **not raw integer counts** | −0.630976 |

The Stephenson article describes **two Coriell parental genetic backgrounds** across its work. The specific 6 source library names do not establish which donor line is represented by each sample. Do not interpret 3 culture measurements as 3 independent genetic donors.

## Results — tested on the connected Mac, source-hash locked

A previous **frozen** protocol prescribed the individual targets before numerical inspection; their 3 vs 3 exact two-sided genotype-label permutation `p=0.10` in each cohort does not provide conventional significance. The joint contextual comparison below was specified **after the signs were known** (posthoc), so is not a new blind holdout.

- Cross-study difference of separately normalized log2FC: **+0.880864** (GSE305481 minus GSE286874).
- Genotype-relative fold-change ratio across studies: **1.84148**. This is *not* a ratio of unnormalized expression between studies.
- Leave-one-from-each-genotype sensitivity: positive in **9/9** reduced GSE305481 subsets (effect range **+0.120 to +0.334**); negative in **9/9** reduced GSE286874 subsets (effect range **−0.734 to −0.552**). All **81/81** cross-pairs retain sign separation.
- Alternate *posthoc* median-of-ratios normalization: **+0.292155** for GSE305481 versus **−0.796577** for GSE286874.
- Previously frozen intervention contrast of **DGAT1/2 inhibition** in GSE286874: INPP5D log2 delta E4 treatment −0.2183, E3 treatment −0.0476; difference-in-differences **−0.1707**. Within-source 700 exact permutations for treatment genotype interaction yielded **p=0.2086**. It cannot explain the inter-study sign change or demonstrate an INPP5D-specific drug mechanism.

This source reanalysis was actually executed on the Mac, using an independent script to re-derive the 20 exact possible genotype-label assignments *within each study*. Six intermediate source-derived output files were SHA256 locked; no original manuscript or GEO data were modified.

## Conclusions that follow — and those that do not

**Supported:** The already-tested universal increase-of-INPP5D transcription assumption fails for the published GSE286874 culture set. It is not driven by any one culture library under the tested leave-one sensitivity and the reversal remains under two normalization approaches.

**Not supported:** A statistically proven APOE genotype×state interaction across *independent donors*, a mechanism involving INPP5D catalytic activity or SHIP1–CapZ scaffolding, receptor return-to-surface kinetics, restoration of lysosomal clearance, or a Nobel-caliber therapeutic discovery. No direct SHIP1 protein, CapZ binding, ARF6-GTP or cargo recycling endpoint exists in these six-sample source vectors. Separate labs and genetic backgrounds remain confounded.

## Next empirical discriminator — not yet run

In at least **two separately derived isogenic human iPSC parental backgrounds**, cross **APOE allele (E3/E4)**, **matched maturation state / differentiation protocol**, and **TG-lipid/DGAT intervention**. Hold initial uptake and batch conditions fixed; assay INPP5D transcripts, SHIP1 protein/catalytic activity, interaction with CAPZA2, uptake-corrected proteolytic flux, functional receptor recycling, cytokines, and healthy synapse clearance. A strictly transcriptional explanation predicts that receptor-flux rescue will track INPP5D RNA; a proposed noncatalytic scaffold model instead predicts functional rescue at comparable phosphatase output only if an experimentally verified interaction surface is intact. These are *hypotheses to falsify*, not tested outcomes.

## Local reproducibility

Full locked-source protocol on connected Mac:
`~/Research/Mechanism_Atlas_H2/external_holdout_20261120/FROZEN_POSTHOC_INPP5D_CONTEXT_HETEROGENEITY_20261121.md`; SHA256 `4707dcd7c01ba19886bcb67ad7371d45b02c2df950c247f8709c5a9516cebdd5`.

Execution script: `run_INPP5D_context_heterogeneity_gate_20261121.py`, output JSON `INPP5D_CROSS_CONTEXT_HETEROGENEITY_RESULT_20261121.json`, SHA256 `1efc927c5bd8dddde572d562bd08221b249c5431d411c580c1ece76b429a420c`. Companion minimal `recompute_aggregate_signs.py` in this branch reconstructs the published **normalized per-culture vectors only**; it does not independently download GEO or identify donor mapping.

**Competition boundary:** This is a distinct Mechanism Atlas research memo. Do **not** enter its simulated or cross-study observations as newly published primary experimental findings in any of MecCog's five Step-1 submissions.