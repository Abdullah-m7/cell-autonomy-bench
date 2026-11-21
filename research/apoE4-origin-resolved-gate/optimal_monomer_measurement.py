#!/usr/bin/env python3
"""Design an orthogonal measurement to split a TWO-FOLD aggregate-only ambiguity.
POSTHOC + ALL SYNTHETIC, constant absolute Gaussian monomer-readout noise model.
Structural parameter-symmetry is classical compartment-model prior art, NOT novel math.
"""
from math import exp, log, sqrt, erfc
from pathlib import Path
import json, hashlib
D=Path(__file__).resolve().parent
BASE=D/'H3_AggregateOnly_Twofold_Identifiability_20261121.json'
DEST=D/'H3_Optimal_Monomer_Checkpoint_SyntheticDesign_20261121.json'
assert BASE.exists() and not DEST.exists()
d=json.loads(BASE.read_text())
assert d['random_positive_parameter_models_passing']==250
kf=.08
rate1=.08+.12 # monomer disappearance, baseline
rate2=.08+.22 # alternate
M0=100.
assert abs(rate1-.2)<1e-13 and abs(rate2-.3)<1e-13
t_best=log(rate2/rate1)/(rate2-rate1)
def mon(t,lam):return M0*exp(-lam*t)
def sep(t):return abs(mon(t,rate1)-mon(t,rate2))
peak=sep(t_best)
# For equal prior probabilities + independent readout Gaussian errors N(0,sigma^2),
# Bayes-optimal pair discrimination threshold is the midpoint of predicted M(t).
def error_rate(t,sigma):return .5*erfc(sep(t)/(2*sqrt(2)*sigma))
assert 0<t_best<24
grid=[(i/100,sep(i/100)) for i in range(2401)]
best_grid=max(grid,key=lambda x:x[1])
assert abs(best_grid[0]-t_best)<.012 and abs(best_grid[1]-peak)<.001
rows=[]
for t in (0.,1.,2.,4.,t_best,8.,12.,24.):
 rows.append({'hour':t,'M_base':mon(t,rate1),'M_alternative':mon(t,rate2),
              'absolute_M_difference':sep(t),'toy_error_probability_sigma3':error_rate(t,3)})
report={
 'scope':'SYNTHETIC_POSTHOC_DESIGN_NOT_BIOLOGICAL_DATA',
 'source_theorem_type':'classical two-compartment global identifiability symmetry, here mapped to ApoE hypothesized assembly vs clearance',
 'prior_model_file_sha256':hashlib.sha256(BASE.read_bytes()).hexdigest(),
 'two_mononer_disappearance_rates_h': [rate1,rate2],
 'optimal_single_additional_M_readout_hours_when_noise_sd_constant':t_best,
 'maximum_absolute_M_difference_arbitrary_units':peak,
 'noise_model':'Known hypothetical sigma=3 absolute monomer units, equal class priors and Gaussian independently distributed errors. Not inferred from assay.',
 'grid_best_time':best_grid[0],
 'rows':rows,
 'interpretation':'Measure monomeric/intact ApoE mass at ~4h in addition to aggregate burden, not only after 24h, when THESE hypothetical rates and constant absolute assay noise apply.',
 'critical_limits':['not verified for true ApoE rates or real pH','ratio-dependent or heteroscedastic measurement noise may change optimal time',
 'two-state homogeneous pulse model omits uptake, export, seed import, aggregation reversibility, antibody/sensor physics and cell toxicity',
 'need truly orthogonal quantitative monomer and aggregate-specific assays and lysosomal mass balance',
 'no biological experiments or clinical results performed']
}
DEST.write_text(json.dumps(report,ensure_ascii=False,indent=2))
print('MODEL_INPUT_SHA_PASS',hashlib.sha256(BASE.read_bytes()).hexdigest())
print('OPTIMAL_HOUR',round(t_best,6),'MAX_MONOMER_SEPARATION',round(peak,6))
for r in rows:
 print('t',round(r['hour'],3),'M1',round(r['M_base'],3),'M2',round(r['M_alternative'],3),
       'DELTA',round(r['absolute_M_difference'],3),'THEORETICAL_ERROR_SIGMA3',round(r['toy_error_probability_sigma3'],5))
print('OUT',DEST,'SHA',hashlib.sha256(DEST.read_bytes()).hexdigest())