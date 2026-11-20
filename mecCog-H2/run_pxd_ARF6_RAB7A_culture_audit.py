#!/usr/bin/env python3
"""Posthoc H2: exact culture-permutation + bootstrap on author-processed PXD077344.
This is not new laboratory data, author significance or activation measurement.
"""
import json,itertools,statistics,math,hashlib,random,datetime
from pathlib import Path
B=Path.home()/'Research/Mechanism_Atlas_H2'
SRC=B/'biological_discovery_20261120/pride_protein_panel.json'
D=json.loads(SRC.read_text())
assert D['primary_processed_file_sha256']=='340bc2cc7f273c9af06d15d756147d4e9662682db2933d0496032789ba3d2d06'
targets=['ARF6','RAB7A']
results={}
for sym in targets:
 r=next(x for x in D['selected_target_rows'] if x['gene']==sym)
 a=r['source_logged_values_APOE3'];b=r['source_logged_values_APOE4']
 assert len(a)==len(b)==5
 observed=statistics.mean(b)-statistics.mean(a)
 assert abs(observed-r['log2fold_APOE4_vs_APOE3'])<1e-6,(sym,observed,r['log2fold_APOE4_vs_APOE3'])
 pool=a+b
 diffs=[]
 for group_e4 in itertools.combinations(range(10),5):
  s=set(group_e4)
  diffs.append(statistics.mean(pool[i] for i in s)-statistics.mean(pool[i] for i in range(10) if i not in s))
 assert len(diffs)==252
 exact=sum(abs(z)>=abs(observed)-1e-12 for z in diffs)/len(diffs)
 rng=random.Random(20261120+sum(map(ord,sym)))
 boots=[]
 for _ in range(20000):
  aa=[a[rng.randrange(5)] for i in range(5)]
  bb=[b[rng.randrange(5)] for i in range(5)]
  boots.append(statistics.mean(bb)-statistics.mean(aa))
 boots.sort()
 loo=[]
 for exa in range(5):
  for exb in range(5):
   xx=[x for i,x in enumerate(a) if i!=exa]
   yy=[x for i,x in enumerate(b) if i!=exb]
   loo.append(statistics.mean(yy)-statistics.mean(xx))
 results[sym]={
  'source_uniprot':r.get('uniprot_id'),
  'source_log2fc_E4_minus_E3':r['log2fold_APOE4_vs_APOE3'],
  'recomputed_log2fc_from_five_cultures':observed,
  'source_author_p':r['source_p'],'source_author_FDR':r['source_FDR'],
  'posthoc_unpaired_exact_two_sided_culture_label_permutation_p':exact,
  'permutation_count':len(diffs),'min_possible_two_sided_p':2/len(diffs),
  'bootstrap_within_cultures_20000_95pct_interval':[boots[499],boots[19499]],
  'leave_one_each_genotype_25_effect_range':[min(loo),max(loo)],
  'leave_one_each_genotype_all_same_sign':all(z*observed>0 for z in loo),
  'raw_author_logged_source_values_E3':a,'raw_author_logged_source_values_E4':b,
 }
 print('TARGET',sym,'log2FC',round(observed,9),'source_FDR',r['source_FDR'],
       'posthoc_perm',exact,'bootstrap95',results[sym]['bootstrap_within_cultures_20000_95pct_interval'],
       'LOO25_range',list(map(lambda z:round(z,4),results[sym]['leave_one_each_genotype_25_effect_range'])))
out={'status':'POSTHOC_SOURCE_REANALYSIS_ONLY_NOT_ARF6_GTP',
 'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'study':'Lysaker 2026 npj Dementia DOI 10.1038/s44400-026-00105-8',
 'source_processed_file_sha256':D['primary_processed_file_sha256'],
 'source_panel_json_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),
 'n_isogenic_backgrounds':1,'n_culture_replicates_per_genotype':5,'analyzed_proteins':results,
 'limitations':['ARF6 and RAB7A were preselected after author reported effects were known, not blinded external discoveries',
 'A p-value from permuting culture labels does not reestimate author raw mass-spectrometry differential statistics, nor their FDR correction',
 'Isogenic pair means one parental genetic background; n=5 cultures do not equal n=5 independent donor lineages',
 'ARF6 total abundance is not ARF6-GTP activation; RAB7A protein abundance is not retromer recycling flux',
 'Signed shifts of two proteins do NOT establish inverse causal feedback, physical interaction or a therapeutic target',
 'No receiver operating characteristic or diagnosis performance was evaluated.']}
dest=Path(__file__).resolve().parent/'H2_ARF6_RAB7A_source_permutation_sensitivity_20261120.json'
dest.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print('SOURCE_AUDIT_SAVED',dest)
