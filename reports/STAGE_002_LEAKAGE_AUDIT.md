# Stage 002 Leakage & Structure Audit

> Provisional labels only. This report does **not** convert them into expert gold labels.

## Stage 001 v0.1

- cases: **60**
- action distribution: `{'CLARIFY': 14, 'DEFER': 23, 'REFUSE': 14, 'ACT': 9}`
- exact duplicate groups: **0**
- unexpected near-duplicate pairs (>=0.92; matched pair siblings exempt): **0**

| baseline | features | accuracy | macro-F1 |
|---|---|---:|---:|
| majority | none | 0.383 | 0.139 |
| family | family | 0.583 | 0.627 |
| consequence_level | consequence_level | 0.650 | 0.592 |
| provenance_state | provenance_state | 0.383 | 0.273 |
| shift_state | shift_state | 0.383 | 0.139 |
| coarse_combined | family, consequence_level, provenance_state, shift_state | 0.517 | 0.478 |

## Stage 002 v0.2 candidate

- cases: **100**
- action distribution: `{'CLARIFY': 18, 'DEFER': 32, 'REFUSE': 21, 'ACT': 29}`
- exact duplicate groups: **0**
- unexpected near-duplicate pairs (>=0.92; matched pair siblings exempt): **0**

| baseline | features | accuracy | macro-F1 |
|---|---|---:|---:|
| majority | none | 0.320 | 0.121 |
| family | family | 0.470 | 0.457 |
| consequence_level | consequence_level | 0.490 | 0.404 |
| provenance_state | provenance_state | 0.410 | 0.317 |
| shift_state | shift_state | 0.360 | 0.304 |
| coarse_combined | family, consequence_level, provenance_state, shift_state | 0.560 | 0.556 |

## Matched-counterfactual structure

- pair count: **20**
- invalid pair-constant checks: **0**
- pairs with identical coarse feature tuple but different provisional actions: **8**
- such pair IDs: `P001, P007, P009, P011, P012, P014, P015, P020`

## Evidence coverage

- candidate cases with >=1 mapped source/design-evidence ID: **100/100**
- cases with at least one external source: **85/100**
- missing source mappings: **0**

## Predeclared structural gate

- max single coarse-feature CV accuracy must be < 0.65
- combined coarse-feature CV accuracy must be < 0.75
- combined coarse-feature macro-F1 must be < 0.70
- >=20 valid matched pairs
- >=8 matched pairs must have identical coarse tuples but different labels
- 100% evidence-ID coverage
- no unintended exact duplicates

**Result: PASS**

The v0.2 candidate passes the structural pre-adjudication gate. This does not validate the biological labels; blinded expert adjudication is still required.
