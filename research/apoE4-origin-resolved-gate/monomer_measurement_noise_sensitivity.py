#!/usr/bin/env python3
"""Sensitivity of a toy ApoE monomer-only measurement schedule to noise models.
POSTHOC, SYNTHETIC; no sample sizes, no wetlab rates or p-values are inferred.
"""
import json, hashlib
from pathlib import Path
from math import exp, sqrt
D=Path(__file__).resolve().parent
base=D/'H3_Optimal_Monomer_Checkpoint_SyntheticDesign_20261121.json'
assert base.exists()
source=json.loads(base.read_text())
assert 4.05<source['optimal_single_additional_M_readout_hours_when_noise_sd_constant']<4.06
output=D/'H3_ApoE_Monomer_Readout_Noise_Sensitivity_20261121.json'
assert not output.exists()
lam1,lam2=.2,.3
M0=100.0
def m(t,rate):return M0*exp(-rate*t)
def z(t,sigma0,cv):
    x,y=m(t,lam1),m(t,lam2)
    return abs(x-y)/sqrt((sigma0**2+(cv*x)**2)+(sigma0**2+(cv*y)**2))
regimes={
  'absolute_SD_3':(3.,0.),
  'floor_2_CV10pct':(2.,.10),
  'floor_3_CV20pct':(3.,.20),
  'floor_1_CV5pct':(1.,.05)
}
result={'status':'POSTHOC_SYNTHETIC_NO_ASSAY_VALIDATION','prior_file_sha256':hashlib.sha256(base.read_bytes()).hexdigest(),
        'definition':'score=abs(M1-M2)/sqrt(var1+var2); var_i=sigma_floor**2+(CV*M_i)**2',
        'rate_sets_per_hour':[lam1,lam2],'M0_arbitrary_units':M0,'noise_regimes':{}}
for label,(floor,cv) in regimes.items():
  series=[(i/100,z(i/100,floor,cv)) for i in range(2401)]
  t,score=max(series,key=lambda p:p[1])
  result['noise_regimes'][label]={'floor':floor,'CV':cv,'optimal_hour_0_to_24':t,'max_standardized_difference':score,
                                 'score_at_h4':z(4,floor,cv),'score_at_h8':z(8,floor,cv),
                                 'score_at_h24':z(24,floor,cv)}
  print(label,'t*',t,'score',round(score,5),'z4',round(z(4,floor,cv),5),
        'z8',round(z(8,floor,cv),5),'z24',round(z(24,floor,cv),5))
assert result['noise_regimes']['absolute_SD_3']['optimal_hour_0_to_24']==4.05
assert result['noise_regimes']['floor_2_CV10pct']['optimal_hour_0_to_24']==7.12
assert result['noise_regimes']['floor_3_CV20pct']['optimal_hour_0_to_24']==7.87
result['no_go']='Cannot choose a real iPSC ApoE assay sampling time before obtaining pilot ApoE rates, assay detection limit and measurement variance, and confirming biological donor/experiment unit.'
output.write_text(json.dumps(result,indent=2))
print('OUTPUT',output,'SHA',hashlib.sha256(output.read_bytes()).hexdigest())