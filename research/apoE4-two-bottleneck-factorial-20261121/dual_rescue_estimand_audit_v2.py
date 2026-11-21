#!/usr/bin/env python3
"""Scientific-estimand audit of a PROPOSED APOE3/E4 SHIP1 x MbetaCD study.

This is a wrapper around the prior research-data QA script; it does NOT fit
published experimental data or produce p-values. It separates:
  1) recovery of all three functions at pre-chosen thresholds;
  2) whether both interventions are needed to pass that composite;
  3) E4 factorial interaction, potentially on different measurement scales;
  4) E4-vs-E3 initial internalized-dose COMPARABILITY, including the crucial
     opposite-genotype constraint absent from the original checker.
All numeric thresholds here are arbitrary PILOT ENGINEERING controls and cannot
certify a human therapeutic response, biological interaction, or synergy.
"""
from __future__ import annotations
import argparse
import json
import math
from collections import defaultdict
from pathlib import Path

from dual_rescue_factorial_gate import summarize, synthetic_example, FATE_FIELDS

MAX_T0_RELATIVE_DIFFERENCE = 0.10    # illustrative, must be calibrated
RECOVER_BASELINE_DEFICIT = 0.50      # illustrative, cannot establish effect
ARMS = ((0, 0), (1, 0), (0, 1), (1, 1))
OUTCOMES = (
    ('transferrin', 'uptake_5min_pmol'),
    ('transferrin', 'primary_fate_fraction'),
    ('degradable_protein', 'primary_fate_fraction'),
)


def _basic_arm_rows(payload):
    lookup = {}
    for row in payload['observations']:
        key = (row['background'], row['batch'], row['cargo'], row['genotype'],
               row['ship1'], row['cyclodextrin'])
        lookup[key] = row
    return lookup


def _gates_for_arm(block, treatment):
    values = {}
    for cargo, endpoint in OUTCOMES:
        b = block.get(cargo)
        if b is None or not b['usable_for_pilot_comparison']:
            values[f'{cargo}:{endpoint}'] = None
            continue
        data = b['endpoints'][endpoint]
        gap = data['baseline_E3minusE4_gap']
        # Avoid accidental classification when baseline E3/E4 defect is absent.
        floor = 1.0 if endpoint == 'uptake_5min_pmol' else 0.02
        if gap <= floor:
            values[f'{cargo}:{endpoint}'] = None
            continue
        arm_name = { (0,0):'vehicle',(1,0):'ship1_only',
                     (0,1):'cyclodextrin_only',(1,1):'combined'}[treatment]
        start = data['E4']['vehicle']
        gain = data['E4'][arm_name] - start
        values[f'{cargo}:{endpoint}'] = {
            'gap_E3minusE4': gap,
            'gain_E4_vs_vehicle': gain,
            'fraction_of_baseline_gap_recovered': gain/gap,
            'illustrative_half_gap_met': gain/gap >= RECOVER_BASELINE_DEFICIT,
        }
    passed = all(val is not None and val['illustrative_half_gap_met']
                 for val in values.values())
    return {'measurements':values, 'all_three_illustrative_conditions_met':passed}


def inspect(payload):
    v1 = summarize(payload)  # preserve old source-provenance and mass QA
    groups = defaultdict(dict)
    for row in v1['block_results']:
        groups[(row['background'],row['batch'])][row['cargo']] = row
    lookup = _basic_arm_rows(payload)
    new_results = []
    for (background, batch), block in sorted(groups.items()):
        complete = set(block) == {'transferrin','degradable_protein'}
        matched_dose = {}
        cross_genotype_failures = []
        for cargo in ('transferrin','degradable_protein'):
            for s,c in ARMS:
                e3 = lookup.get((background,batch,cargo,'E3',s,c))
                e4 = lookup.get((background,batch,cargo,'E4',s,c))
                label=f'{cargo}:S{s}:CD{c}'
                if e3 is None or e4 is None:
                    matched_dose[label] = None
                    cross_genotype_failures.append(label+': missing matched treatment/genotype arm')
                    continue
                t3 = e3['t0_internalized_pmol']
                t4 = e4['t0_internalized_pmol']
                rel=abs(t4-t3)/t3
                matched_dose[label] = {'E3_t0_pmol':t3,'E4_t0_pmol':t4,
                  'relative_difference_to_E3':rel,'within_arbitrary_10pct':rel<=MAX_T0_RELATIVE_DIFFERENCE}
                if rel>MAX_T0_RELATIVE_DIFFERENCE:
                    cross_genotype_failures.append(label+': E3/E4 t0 imbalance')
        dose_ok = complete and not cross_genotype_failures
        all_good = complete and all(b['usable_for_pilot_comparison'] for b in block.values())
        by_arm = {f'S{s}_CD{c}':_gates_for_arm(block,(s,c)) for s,c in ARMS}
        combination=by_arm['S1_CD1']['all_three_illustrative_conditions_met']
        ship_alone=by_arm['S1_CD0']['all_three_illustrative_conditions_met']
        cd_alone=by_arm['S0_CD1']['all_three_illustrative_conditions_met']
        interaction = {}
        for cargo,endpoint in OUTCOMES:
            key=f'{cargo}:{endpoint}'
            if not complete or cargo not in block or not block[cargo]['usable_for_pilot_comparison']:
                interaction[key] = None
                continue
            e=block[cargo]['endpoints'][endpoint]
            arm=e['E4']
            single_best=max(arm['ship1_only'],arm['cyclodextrin_only'])
            interaction[key] = {
              'E4_factorial_interaction_on_this_scale':arm['interaction_difference_of_differences'],
              'E3_factorial_interaction_on_this_scale':e['E3']['interaction_difference_of_differences'],
              'E4_minus_E3_factorial_interaction_on_this_scale':e['genotype_difference_of_interactions'],
              'E4_combined_minus_best_single':arm['combined']-single_best,
              'best_single_value_E4':single_best,
              'combined_E4':arm['combined'],
              'interpretation':'Descriptive interaction only; NOT statistical/biological synergy, depends on outcome scale.'
            }
        full = (all_good and dose_ok and combination)
        need_both = full and not ship_alone and not cd_alone
        if not all_good: status='BLOCKED_INCOMPLETE_OR_FAILED_QC'
        elif not dose_ok: status='BLOCKED_E3_E4_INITIAL_DOSE_MISMATCH'
        elif not combination: status='NO_COMPOSITE_RECOVERY_UNDER_ILLUSTRATIVE_THRESHOLD'
        elif need_both: status='COMPOSITE_MET_AND_NEITHER_SINGLE_MET__NOT_PROVEN_SYNERGY'
        else:status='COMPOSITE_MET_BUT_SINGLE_ARM_ALSO_SUFFICIENT__NO_COMBINATION_NECESSITY'
        new_results.append({
          'background':background,'batch':batch,
          'independent_background_claim':'Only asserted by source metadata; two parental line names do not prove independent biological validation',
          'both_distinct_cargos_present':complete,
          'v1_data_quality_passed':all_good,
          'E3_E4_matched_internalized_initial_dose':dose_ok,
          'cross_genotype_t0_checks':matched_dose,
          'cross_genotype_t0_failures':cross_genotype_failures,
          'per_treatment_composite_check':by_arm,
          'recovery_of_three_distinct_functions_in_combination':full,
          'combination_needed_to_pass_composite_at_illustrative_threshold':need_both,
          'per_endpoint_interactions_and_incremental_comparisons':interaction,
          'status':status
        })
    return {'status':'PROPOSED_FACTORIAL_ESTIMAND_DIAGNOSTICS_NOT_BIOLOGICAL_RESULTS',
      'data_origin':v1['data_origin'],
      'source_paper_DOIs':['10.64898/2026.05.22.726347','10.1016/j.stem.2026.08.001'],
      'preexisting_checker':'dual_rescue_factorial_gate.py (unchanged)',
      'original_summary_num_complete_blocks':v1['complete_blocks'],
      'new_per_background_batch_diagnostics':new_results,
      'n_composites_passed_with_cross_genotype_t0_QA':sum(x['recovery_of_three_distinct_functions_in_combination'] for x in new_results),
      'n_composites_that_require_combination_at_arbitrary_threshold':sum(x['combination_needed_to_pass_composite_at_illustrative_threshold'] for x in new_results),
      'critical_boundaries':[
        'Published studies DID NOT combine SHIP1 and cyclodextrin: this program has no published joint-treatment data.',
        'These quantities are engineering PILOT GATES on in-silico examples, not p-values or population-level causal effect estimates.',
        'The original checker did not compare baseline E3 vs E4 t0 cargo within corresponding treatment arms; this script adds that explicit gate.',
        'Full composite recovery is different from incremental necessity of both interventions, and BOTH differ from positive interaction/synergy.',
        'A factorial interaction depends on outcome scale; positive value has no interpretation as physical pathway synergy without measured uncertainty.',
        'Dose matching is essential for conditional late-fate efficiency; uptake is itself altered by the interventions. Matching by post-treatment selection or statistical conditioning alone can cause bias. Use controlled pulse titration, blocking/wash and calibrated dose-response.',
        'Independent cell-line/batch and donor lineage IDs, predeclared endpoints and pH/viability calibration still needed before biological inference.',
        'No H3 de novo intralysosomal APOE protein self-assembly is measured by this analysis; not a MecCog Step 1 primary finding.'
      ]}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--demo',action='store_true')
    p.add_argument('--input',type=Path)
    p.add_argument('--output',required=True,type=Path)
    a=p.parse_args()
    if a.demo==bool(a.input):p.error('Choose --demo OR --input')
    if a.output.exists():p.error('Refuse overwriting previous output')
    payload=synthetic_example() if a.demo else json.loads(a.input.read_text())
    result=inspect(payload)
    a.output.write_text(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False)+'\n')
    print('ORIGIN',result['data_origin'],'BLOCKS',len(result['new_per_background_batch_diagnostics']))
    print('PILOT COMPOSITES',result['n_composites_passed_with_cross_genotype_t0_QA'])
    print('PILOT COMBINATION REQUIRED',result['n_composites_that_require_combination_at_arbitrary_threshold'])
    print('No real human-cell results and no scientific synergy established.')
    print('OUT',a.output)

if __name__=='__main__':main()
