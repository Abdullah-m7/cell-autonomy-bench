#!/usr/bin/env python3
"""Adversarial tests on SYNTHETIC 64-row records. No biological validation."""
from __future__ import annotations
from copy import deepcopy
from dual_rescue_factorial_gate import summarize, synthetic_example, FATE_FIELDS
from dual_rescue_estimand_audit_v2 import inspect


def replace_e4_cd_only_with_combined(payload):
    """Make CD single-arm as effective as combination, preserving mass balance."""
    arm_by_key = {(x['background'],x['batch'],x['cargo'],x['genotype'],
                   x['ship1'],x['cyclodextrin']):x for x in payload['observations']}
    for x in payload['observations']:
        if (x['genotype'],x['ship1'],x['cyclodextrin']) != ('E4',0,1):
            continue
        y=arm_by_key[(x['background'],x['batch'],x['cargo'],'E4',1,1)]
        x['uptake_5min_pmol']=y['uptake_5min_pmol']
        for key in FATE_FIELDS:x[key]=y[key]


def test_baseline():
    d=inspect(synthetic_example())
    assert d['data_origin']=='SYNTHETIC_DEMO'
    assert d['n_composites_passed_with_cross_genotype_t0_QA']==4
    assert d['n_composites_that_require_combination_at_arbitrary_threshold']==4
    assert len(d['new_per_background_batch_diagnostics'])==4
    x=d['new_per_background_batch_diagnostics'][0]
    assert x['E3_E4_matched_internalized_initial_dose']
    interactions=x['per_endpoint_interactions_and_incremental_comparisons']
    assert interactions['transferrin:uptake_5min_pmol']['E4_factorial_interaction_on_this_scale']==-2
    assert abs(interactions['transferrin:primary_fate_fraction']['E4_factorial_interaction_on_this_scale']-.09)<1e-12
    assert abs(interactions['degradable_protein:primary_fate_fraction']['E4_factorial_interaction_on_this_scale']-.06)<1e-12


def test_cross_genotype_t0_under_v1_radar():
    d=deepcopy(synthetic_example())
    for x in d['observations']:
        if x['genotype']=='E4':
            x['t0_internalized_pmol']*=.7
            for key in FATE_FIELDS:x[key]*=.7
    old=summarize(d)
    assert all(x['illustrative_combined_early_recycling_degradation_gate'] for x in old['joint_two_cargo_results'])
    new=inspect(d)
    assert new['n_composites_passed_with_cross_genotype_t0_QA']==0
    assert new['n_composites_that_require_combination_at_arbitrary_threshold']==0
    assert all(x['status']=='BLOCKED_E3_E4_INITIAL_DOSE_MISMATCH'
               for x in new['new_per_background_batch_diagnostics'])
    assert all(len(x['cross_genotype_t0_failures'])==8
               for x in new['new_per_background_batch_diagnostics'])


def test_combination_not_needed_even_when_composite_restored():
    d=deepcopy(synthetic_example())
    replace_e4_cd_only_with_combined(d)
    old=summarize(d)
    assert all(x['illustrative_combined_early_recycling_degradation_gate'] for x in old['joint_two_cargo_results'])
    new=inspect(d)
    assert new['n_composites_passed_with_cross_genotype_t0_QA']==4
    assert new['n_composites_that_require_combination_at_arbitrary_threshold']==0
    for x in new['new_per_background_batch_diagnostics']:
        assert x['status']=='COMPOSITE_MET_BUT_SINGLE_ARM_ALSO_SUFFICIENT__NO_COMBINATION_NECESSITY'
        assert x['per_treatment_composite_check']['S0_CD1']['all_three_illustrative_conditions_met']
        assert all(abs(z['E4_combined_minus_best_single'])<1e-10
                   for z in x['per_endpoint_interactions_and_incremental_comparisons'].values())


def test_mass_balance_required():
    d=deepcopy(synthetic_example())
    for x in d['observations']:
        if x['genotype']=='E4' and x['ship1']==1 and x['cyclodextrin']==1:
            x['degraded_product_pmol']+=30
    new=inspect(d)
    assert new['n_composites_passed_with_cross_genotype_t0_QA']==0
    assert all(x['status']=='BLOCKED_INCOMPLETE_OR_FAILED_QC'
               for x in new['new_per_background_batch_diagnostics'])


def test_missing_arm():
    d=deepcopy(synthetic_example())
    d['observations']=[x for x in d['observations'] if not (
        x['background']=='SYNTHETIC_PARENT_B' and x['batch']=='SYNTHETIC_BATCH_2'
        and x['cargo']=='degradable_protein' and x['genotype']=='E4'
        and x['ship1']==1 and x['cyclodextrin']==1)]
    new=inspect(d)
    assert new['n_composites_passed_with_cross_genotype_t0_QA']==3
    assert len(new['new_per_background_batch_diagnostics'])==4
    assert any(x['status']=='BLOCKED_INCOMPLETE_OR_FAILED_QC'
               for x in new['new_per_background_batch_diagnostics'])


def test_unverified_degradation_cannot_be_credited():
    d=deepcopy(synthetic_example())
    for x in d['observations']:
        if x['cargo']=='degradable_protein':
            x['degradation_chemically_verified']=False
            x['dq_bsa_fluorescence_secondary']=1e12
    new=inspect(d)
    assert new['n_composites_passed_with_cross_genotype_t0_QA']==0


if __name__=='__main__':
    tests=[test_baseline,test_cross_genotype_t0_under_v1_radar,
           test_combination_not_needed_even_when_composite_restored,
           test_mass_balance_required,test_missing_arm,
           test_unverified_degradation_cannot_be_credited]
    for test in tests:
        test()
        print('PASS',test.__name__)
    print(f'ALL {len(tests)} SYNTHETIC LOGIC TESTS PASSED; NO human iPSC experiment or inferential p-values.')