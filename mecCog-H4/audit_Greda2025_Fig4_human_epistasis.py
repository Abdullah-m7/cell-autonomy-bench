#!/usr/bin/env python3
"""Greda et al. Nature Metab 2025 Fig4 author-source posthoc audit.
Actual source values published; numerical reanalysis is NOT de novo biology.
Uses Python standard-library SpreadsheetML read only and fixed source SHA256.
"""
from pathlib import Path
import zipfile,xml.etree.ElementTree as ET,posixpath,hashlib,statistics,itertools,json,datetime,re,random
BASE=Path(__file__).resolve().parent
FILE=BASE/'Greda2025_source_fig4.xlsx'
SOURCE_SHA='875c3afd3c2dd59f69337db6eadcd95d9e6bbda18fec5cdd10d4228ecea8a5be'
assert hashlib.sha256(FILE.read_bytes()).hexdigest()==SOURCE_SHA
N='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
def read_workbook(f):
    with zipfile.ZipFile(f) as z:
        strings=[''.join(y.text or '' for y in s.iter(N+'t')) for s in ET.fromstring(z.read('xl/sharedStrings.xml')).findall(N+'si')] if 'xl/sharedStrings.xml' in z.namelist() else []
        wb=ET.fromstring(z.read('xl/workbook.xml'))
        rels={r.get('Id'):r.get('Target') for r in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
        out={}
        for sheet in wb.findall('.//'+N+'sheet'):
            name=sheet.get('name')
            target=rels[sheet.get(R+'id')]
            path=target.lstrip('/') if target.startswith('/') else posixpath.normpath(posixpath.join('xl',target))
            root=ET.fromstring(z.read(path))
            rows={}
            for row in root.findall('.//'+N+'sheetData/'+N+'row'):
                data={}
                for c in row.findall(N+'c'):
                    s=c.findtext(N+'v')
                    if c.get('t')=='inlineStr':s=''.join(n.text or '' for n in c.iter(N+'t'))
                    if s is None:continue
                    if c.get('t')=='s':s=strings[int(s)]
                    elif c.get('t') not in ('str','e','inlineStr'):
                        try:s=float(s)
                        except:pass
                    cell_col=re.match(r'[A-Z]+',c.get('r')).group()
                    data[cell_col]=s
                rows[int(row.get('r'))]=data
            out[name]=rows
        return out
tables=read_workbook(FILE)
a=tables['Fig 4a-d'];g=tables['Fig 4g']
GROUPS={
'E3WT':('B','C','D'), 'E3KO':('H','I','J'),
'E4WT':('N','O','P'), 'E4KO':('T','U','V')}
assert all(a[4][cols[0]]=='Control' and a[4][cols[1]]=='Etomoxir' and a[4][cols[2]]=='UK5099' for cols in GROUPS.values())
assert all(v in str(a[3][x]).replace(' ','') for v,x in [('E3WT','A'),('E3KO','G'),('E4WT','M'),('E4KO','S')])
source_results={}
for group,cols in GROUPS.items():
    conds={}
    for name,col in zip(('Control','Etomoxir','UK5099'),cols):
        vals=[a[i][col] for i in (5,6,7)]
        assert len(vals)==3 and all(isinstance(v,(int,float)) for v in vals)
        conds[name]={'source_values_normalized_max_OCR_percent':vals,
                     'mean_percent':statistics.mean(vals),
                     'culture_SD_percent':statistics.stdev(vals)}
    assert all(v==100 for v in conds['Control']['source_values_normalized_max_OCR_percent'])
    source_results[group]=conds
    print('GROUP',group,'ETO_MEAN',round(conds['Etomoxir']['mean_percent'],5),
         'UK_MEAN',round(conds['UK5099']['mean_percent'],5),flush=True)

# These are differences in NORMALIZED culture-specific maximal oxygen-consumption response,
# not a factorial randomized APOE allele editing experiment.
interactions={}
for genotype in ('E3','E4'):
    effect=source_results[genotype+'KO']['Etomoxir']['mean_percent']-source_results[genotype+'WT']['Etomoxir']['mean_percent']
    interactions[genotype+'_SORT1_KO_minus_WT_on_etomoxir_OCR_percent_points']=effect
interaction=interactions['E3_SORT1_KO_minus_WT_on_etomoxir_OCR_percent_points']-interactions['E4_SORT1_KO_minus_WT_on_etomoxir_OCR_percent_points']

# Separate E4WT iNeuron astrocyte-media perturbation (n=5 per group).
# We DO NOT assert paired culture indices across groups.
assert 'E4WT' in g[3]['A'] and 'E3WT' in g[3]['B'], g[3]
e4=[g[i]['A'] for i in range(4,9)]
e3=[g[i]['B'] for i in range(4,9)]
assert len(e4)==len(e3)==5
delta=statistics.mean(e3)-statistics.mean(e4)
data=e4+e3
perms=[]
for chosen in itertools.combinations(range(10),5):
    group=set(chosen)
    diff=statistics.mean(data[i] for i in group)-statistics.mean(data[i] for i in range(10) if i not in group)
    perms.append(diff)
p_two_sided=sum(abs(k)>=abs(delta)-1e-12 for k in perms)/len(perms)
rng=random.Random(20261121)
boots=[]
for _ in range(20000):
    boots.append(statistics.mean(e3[rng.randrange(5)] for _ in range(5))-
                 statistics.mean(e4[rng.randrange(5)] for _ in range(5)))
boots.sort()
loo=[statistics.mean([e3[j] for j in range(5) if j!=i])-
     statistics.mean([e4[j] for j in range(5) if j!=k])
     for i in range(5) for k in range(5)]
media={
'E4WT_iAstrocyte_conditioned_medium_five':e4,
'E3WT_iAstrocyte_conditioned_medium_five':e3,
'E4WT_CM_mean':statistics.mean(e4),
'E3WT_CM_mean':statistics.mean(e3),
'E3WT_CM_minus_E4WT_CM_percent_points':delta,
'E3WT_CM_over_E4WT_CM_ratio':statistics.mean(e3)/statistics.mean(e4),
'exploratory_unpaired_exact_two_sided_permutation_p':p_two_sided,
'permutation_count':len(perms),
'exploratory_bootstrap_within_cultures_20000_95percent_interval_pp':[boots[499],boots[19499]],
'leave_one_each_cond_group_range_pp':[min(loo),max(loo)],
'leave_one_each_all_same_direction':all(v*delta>0 for v in loo),
'not_source_author_p_value':True
}
print('E4_NEURON_MEDIA_TEST','E4_CMmean',media['E4WT_CM_mean'],
'E3_CMmean',media['E3WT_CM_mean'],
'delta_pp',delta,'exact_p_posthoc',p_two_sided,
'bootstrap95',media['exploratory_bootstrap_within_cultures_20000_95percent_interval_pp'],flush=True)
print('EPITASIS_DESCRIPTIVE',interactions,'difference_in_differences',interaction,flush=True)
out={
'status':'POSTHOC_SOURCE_REANALYSIS_OF_PUBLISHED_2025_EXPERIMENTS_NOT_NEW_DISCOVERY',
'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
'paper':'Greda et al. Nature Metabolism 2025 DOI 10.1038/s42255-025-01389-5, PMID 41102453',
'source_xlsx_url':'https://static-content.springer.com/esm/art%3A10.1038%2Fs42255-025-01389-5/MediaObjects/42255_2025_1389_MOESM7_ESM.xlsx',
'source_sha256':SOURCE_SHA,
'header_positions_verified':True,'source_Fig4a_d':source_results,
'source_Fig4g_ApoE4_neuron_media_rescue':media,
'descriptive_SORT1_interaction':{**interactions,'E3_minus_E4_difference_in_effect_pp':interaction},
'interpretive_boundaries':[
'Original respiratory OCR effects are normalized to 100% control separately within each genotype, not raw surface receptor recycling.',
'One human APOE3 donor line and one APOE4 line are not an isogenic APOE3-vs-APOE4 edited pair; SORT1 knockout is isogenic only WITHIN each APOE line.',
'Independent APOE3* second-background SORT1 edit is reported in Extended Data Fig6; data not part of this Figure4 source.',
'E4WT iNeurons receiving E3-vs-E4 iAstrocyte media are the same recipient genotype, but conditioned media contain multiple secreted molecules; not a pure ApoE ligand or receptor-affinity intervention.',
'Cells and wells n10-15 per biological culture mean are technical, not independent genetic donors.',
'The independent-label permutation p computed here is posthoc descriptive; not the paper p from Student t test and not a causal mediation estimate.',
'No direct measurement of SORT1 recycling fraction, ApoE4-Sortilin kon or koff, endosomal pH, or same-system adhesion-causal effect here.',
'Published experiment; finding is contextual support for a functional neuronal SORT1-ApoE interaction, not a new Nobel-worthy mechanism.'
]}
dest=BASE/'Greda2025_Fig4_HumanNeuron_SORT1_Media_Audit_20261121.json'
dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('RESULT',dest,flush=True)
