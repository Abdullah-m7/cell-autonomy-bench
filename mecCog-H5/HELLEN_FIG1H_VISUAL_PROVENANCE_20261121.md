# MecCog H5 source-figure audit: Hellén et al. 2025, P4.F2

**Date:** 21 November 2026. **Review-only source correction; not a contest submission or a new biological result.**

**Primary manuscript:** Hellén et al., *Journal of Neuroinflammation* (2025), DOI [10.1186/s12974-025-03470-y](https://doi.org/10.1186/s12974-025-03470-y), [PMC12131611](https://pmc.ncbi.nlm.nih.gov/articles/PMC12131611/). Figure 1, panels **G–I**, especially **H**. The original source figure at [NIH PMC CDN](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/afbd/12131611/fcce97e636b8/12974_2025_3470_Fig1_HTML.jpg) was inspected at the original figure resolution. The exact downloaded JPEG SHA256 (Mac research source cache) is `957531333c00df80bd509d245c815312ba75ccdfc8a69538bffdf8515c1e8cb1`.

## What the source actually establishes
- **Figure 1H** has a single asterisk (`*`) over the comparison of lysosomal-substrate fluorescence between APOE3/3 and APOE4/4 human iPSC-derived microglia.
- The **original caption** states that **Figure 1H uses the Mann–Whitney test** and `* p<0.05`, `** p<0.01`. Thus its **source-bound P value is `<0.05`**, provenance **`visual_only`**. It is NOT an author-reported *exact* p value and must not be recorded as one.
- **Figure 1I** has `**` for a distinct **bafilomycin inhibition** comparison in APOE3 control iMGs. Do not use the Figure 1I `p<0.01` threshold as the Figure 1H genotype value.
- The manuscript notes reduced basal pinocytosis in APOE4 microglia, so the lower fluorescent substrate cleavage signal may reflect unequal endocytic uptake, as well as organelle processing. This is not absolute protease flux or lipid-mediated causality.
- Original caption: plotted dots represent iPSC-line means from **1–3 experiments per line**. The article-wide **8 APOE3/3 vs 6 APOE4/4 donor lines** are not necessarily the figure-specific line counts. Independent **P4.F2 sample-size remains `N/A` / `not_found_in_source`** pending panel-specific source audit; never count the imaging dots as independent human donors without verification.

## Recommended exact workbook changes (new candidate only)

| MecCog field for P4.F2 | Prior value | Source-adjudicated new value |
|---|---|---|
| P value (col N) | `N/A` | `<0.05` |
| P value provenance (col O) | `not_found_in_source` | `visual_only` |
| Sample size (col P) | `N/A` | **unchanged** |
| Sample-size provenance (col Q) | `not_found_in_source` | **unchanged** |

The source description, author quote, experimental system, directness class/strength, and all other 21 findings should **remain unchanged**. Any candidate must pin a real Method README commit and be run through the organizer's official `--strict` validator. The original 22-finding user artifact has SHA256 `8d8b2f698e7e9298a299b91eef13039ca30a1a19f1469f99c578e608f51503e1` and remains untouched.

## Separate unresolved scientific rubric review

Independent referee review is still needed for four possible Class2-to-Class4 directness changes (P1.F2, P3.F4, P5.F3, P5.F4) described in [SCIENTIFIC_DIRECTNESS_REDTEAM_22F_20261121.md](SCIENTIFIC_DIRECTNESS_REDTEAM_22F_20261121.md). Do **not** merge those provisional judgments into the source figure p-value correction until adjudicated.

**Not a new disease mechanism, treatment, clinical study, or MecCog upload.**