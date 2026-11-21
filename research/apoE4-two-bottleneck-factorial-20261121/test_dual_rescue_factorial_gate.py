#!/usr/bin/env python3
"""Only SYNTHETIC schema/QC tests. No human-derived result."""
import copy
from dual_rescue_factorial_gate import summarize,synthetic_example,DataQualityError

def fails(p,needle):
    try:summarize(p)
    except DataQualityError as e:
        assert needle.lower() in str(e).lower(),str(e)
    else:raise AssertionError('Expected QA refusal: '+needle)

base=synthetic_example()
out=summarize(base)
assert out['data_origin']=='SYNTHETIC_DEMO'
assert out['raw_observations_received']==64
assert out['complete_blocks']==8
assert len(out['joint_two_cargo_results'])==4
assert len(out['qa_warnings'])==0
assert all(x['illustrative_combined_early_recycling_degradation_gate'] for x in out['joint_two_cargo_results'])
# The dual-fate gate must NOT require entry improvement of a different degradable
# cargo; the late assay has separate, uptake-matched t0 and verified cleavage.
r=copy.deepcopy(base)
for row in r['observations']:
    if row['cargo']=='degradable_protein' and row['genotype']=='E4':
        row['uptake_5min_pmol']=65.0  # no degradation-cargo entry rescue by either intervention
z=summarize(r)
assert all(x['illustrative_combined_early_recycling_degradation_gate'] for x in z['joint_two_cargo_results'])

r=copy.deepcopy(base)
r['observations'].append(copy.deepcopy(r['observations'][0]))
fails(r,'duplicate arm')

r=copy.deepcopy(base)
r['observations'][0]['degraded_product_pmol']=200
s=summarize(r)
assert any(not x['usable_for_pilot_comparison'] for x in s['block_results'])
assert not all(x['illustrative_combined_early_recycling_degradation_gate'] for x in s['joint_two_cargo_results'])

r=copy.deepcopy(base)
r['observations'][0]['t0_internalized_pmol']=-100
fails(r,'positive')

r=copy.deepcopy(base)
r['observations'][0]['cell_type']='image_frame'
fails(r,'only validated')

r=copy.deepcopy(base)
r['metadata']['data_origin']='EXPERIMENTAL'
fails(r,'requires source_provenance and assay_validation_document')
r['metadata'].update({'source_provenance':'test-lab-notebook-placeholder',
                      'assay_validation_document':'test-calibration-placeholder',
                      'record_unit':'single_cell_image','mass_unit':'pmol_parent_cargo_equivalents',
                      'fate_pool_disjointness_document':'test disjointness placeholder'})
fails(r,'independent_differentiation_batch_summary')
r['metadata']['record_unit']='independent_differentiation_batch_summary'
assert summarize(r)['data_origin']=='EXPERIMENTAL'

r=copy.deepcopy(base)
for row in r['observations']:
    if row['cargo']=='degradable_protein':
        row['degradation_chemically_verified']=False
        row['dq_bsa_fluorescence_secondary']=999999.0
s=summarize(r)
assert s['qa_warnings']
assert all(not x['illustrative_combined_early_recycling_degradation_gate'] for x in s['joint_two_cargo_results'])
assert all(not x['usable_for_pilot_comparison'] for x in s['block_results'] if x['cargo']=='degradable_protein')

r=copy.deepcopy(base)
r['observations'].pop()
s=summarize(r)
assert len(s['block_results'])==7
assert not all(x['illustrative_combined_early_recycling_degradation_gate'] for x in s['joint_two_cargo_results'])

# No baseline APOE3/E4 degradation difference => rescue claim is not estimable.
r=copy.deepcopy(base)
for row in r['observations']:
    if row['cargo']=='degradable_protein' and row['genotype']=='E4':
        row['degraded_product_pmol']=58.0
        row['retained_intact_pmol']=100-row['surface_returned_pmol']-row['released_intact_pmol']-58.0
z=summarize(r)
assert all(not x['illustrative_combined_early_recycling_degradation_gate'] for x in z['joint_two_cargo_results'])
assert all(x['endpoints']['primary_fate_fraction']['combined_recovery_relative_to_baseline_genotype_gap'] is None for x in z['block_results'] if x['cargo']=='degradable_protein')

# An unmatched initial input mass (above +10%) invalidates the full-fate claim.
r=copy.deepcopy(base)
for row in r['observations']:
    if (row['cargo']=='degradable_protein' and row['genotype']=='E4' and row['ship1']==1 and row['cyclodextrin']==1):
        row['t0_internalized_pmol']=135.0
z=summarize(r)
assert all(not x['illustrative_combined_early_recycling_degradation_gate'] for x in z['joint_two_cargo_results'])

r=copy.deepcopy(base)
r['observations'][0]['ship1']=True
fails(r,'integer 0 or 1')

print('PASS: 64 SYNTHETIC records, eight factorial blocks, two separate cargo assays, source-provenance gate, independent batch schema, duplicate/missing arm gate, mass-balance and unverified DQ-BSA rejection.')
