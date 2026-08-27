# Stage 002A Controller Review

## Decision

**PASS — structural pre-adjudication gate.**

This PASS means the benchmark is ready to be shown blind to a stem-cell domain expert. It does **not** mean the provisional autonomy labels are biologically validated.

## Evidence

- Stage 001 bank preserved unchanged: 60 cases.
- v0.2 candidate: 100 cases.
- Stable source registry: 11 entries, including an explicit benchmark-extrapolation marker.
- All 100 cases have at least one stable evidence/design source ID.
- 85/100 cases have at least one external source; extrapolations remain explicitly labeled.
- 20 matched counterfactual pairs / 40 variants.
- 0 invalid pair constant-field checks.
- 8 pairs have identical coarse tuples (`family`, consequence, provenance, shift) but different provisional actions.
- 0 unintended exact duplicates.
- 0 unexpected near-duplicates >= 0.92 after exempting intentional pair siblings.
- 11 tests pass.

## Leakage finding

The Stage 001 design contained a meaningful shortcut signal: `consequence_level` alone achieved 0.650 cross-validated provisional-label accuracy.

After matched-counterfactual expansion, the best single coarse feature achieved 0.490 accuracy and the combined four-feature categorical lookup achieved:

- accuracy: **0.560**
- macro-F1: **0.556**

This is above the 0.320 majority baseline but below the predeclared HOLD thresholds. The remaining signal is expected because provenance, shift, and consequence genuinely affect autonomy; the paired design prevents those fields from fully determining the answer.

## Frozen artifact

The blinded expert worksheet contains 100 randomized cases and hides:

- provisional action
- provisional rationale
- family
- pair identity
- source IDs
- origin

Its SHA-256 and row count are pinned in `benchmark/FREEZE_MANIFEST_v0.2.json`.

## Next gate

**DOMAIN EXPERT ADJUDICATION.**

A stem-cell expert should complete the frozen worksheet without seeing author labels. Primary outputs:

1. action agreement with provisional labels;
2. expert confidence;
3. biologically invalid/underspecified cases;
4. `ACT ↔ DEFER`, `CLARIFY ↔ DEFER`, and `ACT ↔ REFUSE` disagreement boundaries;
5. matched-pair consistency after unblinding.

Do not instantiate a real autonomous wet-lab controller from these labels. This remains a research benchmark.
