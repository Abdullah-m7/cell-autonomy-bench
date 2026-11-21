#!/usr/bin/env python3
"""H3 twofold structural non-identifiability of aggregate-only pulse-chase.
Exclusively analytical/synthetic: NOT fitting biological measurements.
"""
from __future__ import annotations
from math import exp, isfinite
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, random

D = Path(__file__).resolve().parent
OUT=D/'H3_AggregateOnly_Twofold_Identifiability_20261121.json'
assert not OUT.exists(), 'Do not overwrite prior research run'
PROTO = D/'FROZEN_STRUCTURAL_IDENTIFIABILITY_20261121.md'
M0=100.0

def state(t:float, kf:float, km:float, kc:float):
    assert all(x>0 for x in (kf,km,kc))
    lam=kf+km
    M=M0*exp(-lam*t)
    A= kf*M0*t*exp(-lam*t) if abs(kc-lam)<1e-12 else kf*M0*(exp(-lam*t)-exp(-kc*t))/(kc-lam)
    D_removed=M0-M-A
    assert min(M,A,D_removed)>-1e-8,(t,M,A,D_removed)
    assert abs(M+A+D_removed-M0)<1e-9
    return {'M':M,'A':A,'removed':D_removed}

def alter(kf:float, km:float, kc:float):
    assert kc>kf and km>0
    return (kf,kc-kf,kf+km)

base=(.08,.12,.30)
alternative=alter(*base)
assert all(z>0 for z in alternative)
assert alternative==(.08,.21999999999999997,.2) or all(abs(a-b)<1e-15 for a,b in zip(alternative,(.08,.22,.20)))
data=[]
maxdiff=0
for i in range(72*8+1):
    t=i/8
    a=state(t,*base);b=state(t,*alternative)
    dif=abs(a['A']-b['A']);maxdiff=max(maxdiff,dif)
    assert dif<1e-11,(t,a,b)
    if t in (0,2,4,8,12,24,48,72):
        data.append({'hours':t,'base':a,'alternate':b,'A_difference':dif})
assert len(data)==8
for t in (12.,24.):
    x=next(r for r in data if r['hours']==t)
    assert abs(x['base']['M']-x['alternate']['M'])>0.1
    assert abs(x['base']['removed']-x['alternate']['removed'])>0.1
rng=random.Random(20261121)
checked=0
for i in range(250):
    kf=rng.uniform(.005,.3)
    km=rng.uniform(.005,.5)
    kc=rng.uniform(kf+.005, .9)
    alt=alter(kf,km,kc)
    for t in [0,.1,.5,1,3,8,16,24,72]:
        assert abs(state(t,kf,km,kc)['A']-state(t,*alt)['A'])<5e-11
    checked+=1
report={
  'research_label':'ANALYTICAL_SYNTHETIC_ONLY_NOT_BIOLOGICAL_DATA',
  'time_utc':datetime.now(timezone.utc).isoformat(),
  'protocol_sha256':hashlib.sha256(PROTO.read_bytes()).hexdigest(),
  'model':'dM/dt=-(kf+km)M; dA/dt=kf*M-kc*A; D=100-M-A',
  'observable':'A(t) alone (ideal, all time points)',
  'closed_form':'A(t)=M0*kf*(exp(-lambda*t)-exp(-kc*t))/(kc-lambda), lambda=kf+km',
  'ambiguous_transformation':'(kf, km, kc) -> (kf, kc-kf, kf+km), if kc>kf',
  'base_rates_per_h':{'kf':base[0],'km':base[1],'kc':base[2]},
  'alternative_rates_per_h':{'kf':alternative[0],'km':alternative[1],'kc':alternative[2]},
  'aggregate_curves_max_abs_diff_0_to_72h':maxdiff,
  'observed_sample_times':data,
  'random_positive_parameter_models_passing':checked,
  'scientific_conclusion':'Aggregate-only observation cannot discriminate monomer disappearance rate and aggregate clearance rate even with dense noiseless sampling in this minimal two-state model.',
  'resolution':'Orthogonal M(t) or independently measured degraded/exported mass plus initial M0, and origin-labelled seed controls, are needed; qualify pH and cell system.',
  'not_done':['no real APOE measurements fitted','no matched human iPSC experiment','no donor level p-values','no MecCog source finding','no clinical treatment'] 
}
OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2))
print('TWO_DISTINCT_POSITIVE_RATE_TRIPLES',base,alternative)
print('PERFECT_AGGREGATE_CURVE_AGREEMENT_MAX_ERROR',maxdiff)
for r in data:
    if r['hours'] in (12,24):
        print('AT_HOUR',r['hours'],
              'A_base',round(r['base']['A'],5),'A_alt',round(r['alternate']['A'],5),
              'M_base',round(r['base']['M'],5),'M_alt',round(r['alternate']['M'],5),
              'removed_base',round(r['base']['removed'],5),'removed_alt',round(r['alternate']['removed'],5))
print('RANDOM_PARAMETER_TRANSFORM_PASS',checked)
print('OUTPUT',str(OUT),'SHA',hashlib.sha256(OUT.read_bytes()).hexdigest())