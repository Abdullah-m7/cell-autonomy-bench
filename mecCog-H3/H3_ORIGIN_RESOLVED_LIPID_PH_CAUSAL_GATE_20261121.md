# H3 Origin-resolved, lipid-and-pH-gated aggregation programme (21 Nov 2026)

**Status:** Scientific hypothesis + computable assay-identifiability design only. No new wet-lab data, no biological mechanism proven, no MecCog submission.

**Mechanistic question:** Does APOE4 **newly nucleate aggregates inside endolysosomes**, relative to APOE3, after matching initial internalized monomer dose, or are the measured puncta pre-existing imported APOE/Aβ aggregates / retained nonassembled APOE?

## Prior art and unverified boundary

- Kaji et al., *Immunity* 2024, DOI `10.1016/j.immuni.2024.09.014`: purified lipidated ApoE3/E4 showed **no detectable aggregation** under authors' preparation conditions (existing H3 P1.F2). It does not prove lipidated ApoE never aggregates under **different PUFA cargo or acid pH**.
- Xia et al., *Nature Communications* 2024 DOI `10.1038/s41467-024-49028-z`: preformed extracellular APOE–Aβ aggregate uptake measured in human iPSC glia (existing H3 P6); uptake is not **de novo intracellular formation**.
- Guo et al., *Cell* 2024/25 DOI `10.1016/j.cell.2024.10.027`: CE(20:4)-lipidated ApoE4 aggregated more than ApoE3 at 37°C/pH4.5 **in a cell-free centrifugation assay**, with a source-figure E3/E4 `**` bracket `p<0.01`. Without the peroxidizable CE cargo, or with CE(18:1), acidic aggregation was minimal. Conditions explain why different isolated lipidated ApoE results need not contradict. See [exact primary-source audit](GUO_2024_ACIDIC_PUFA_APOE_AGGREGATION_H3_SOURCE_GATE_20261121.md).
- A 2025 *Alzheimer's & Dementia* **meeting abstract**, DOI `10.1002/alz.092614`, measured ApoE4/ApoE3 aggregates with FLIM-FRET in **living BHK cells** and ApoE uptake into human neurons in a separate assay. No direct human endolysosomal in situ assembly finding.
- No one of the 22 findings from our seven-paper H3 candidate fully combines genotype, ApoE-specific aggregate conformation, endolysosomal in-cell site, and qualifying non-aged/non-AD human brain cells. Hence ALL remain **Class5** in the source spreadsheet.

## Prospective causal test (not yet executed)

Use at least two independent isogenic human iPSC backgrounds for **astrocytes and/or microglia**, APOE3 vs APOE4. Establish aggregate-free input purity; synchronize pulse-chase; distinguish imported preformed aggregates (distinct barcode) from de novo ApoE assemblies inside LAMP1/RAB7-positive compartments. Match internalized ApoE concentration across groups.

Factorial perturbations: PUFA-CE(20:4) versus CE(18:1) or equivalent nonperoxidizable cargo; calibrated pH manipulation with viability and fluorophore pH controls. Measure **ApoE-selective FLIM-FRET conformational signal**, orthogonal lysosome-isolated ApoE insolubility/structure, external entry and endosomal retention separately, cargo degradation, pH, damage and viability. Exclude aggregates imported before the pulse. Treat **parental genetic backgrounds and independent differentiations**, not individual imaging fields, as hierarchical biological units.

**Primary discriminating endpoint:** newly formed in-lysosome aggregate-conformation signal per initially internalized monomer and its APOE allele × lipid cargo × pH interaction. Distinguish ApoE aggregates from Aβ aggregates and lipofuscin.

**Stop/falsify:** after matching internal input and imported-seed barcode, no differential newly formed ApoE4 assemblies; only pH-sensitive fluorescence/crowding without structural confirmation; high cell damage or nonisolated compartment; any claim that imaging puncta alone equal protein aggregation.

## Quantitative observation-identifiability gate

If imported aggregate mass is `I` and newly formed aggregate mass `N`, a single aggregate stain measures `Y=I+N`; its observation rank is 1 (two unknowns), so **origin is not identifiable** from fluorescence alone. With a separately calibrated imported barcode `Y_b=I+epsilon*N`, the observation matrix `[[1,1],[1,epsilon]]` has rank 2 if `epsilon != 1`, but becomes poorly conditioned when barcode cross-talk approaches 1: condition number **2.618 at epsilon=0**, **18.145 at epsilon=.8**, **78.037 at epsilon=.95**, and rank1 at epsilon=1. This is a reproducible **mathematical assay-design check**, not biological or Nobel-level evidence.

**Competition decision:** old 6-paper/20-finding H3 passed exact-byte strict validator; new 7-paper/22-finding alternative **also passes strict**, but the two new cell-free Class5 context rows may trigger the organizer's anti-padding preference. Keep the original as the **lean candidate** until independent review or organizer guidance justifies the expansion. NO official upload.
