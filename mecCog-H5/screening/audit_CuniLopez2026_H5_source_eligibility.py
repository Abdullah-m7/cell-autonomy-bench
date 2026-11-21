#!/usr/bin/env python3
"""Posthoc exact source-figure eligibility audit of Nature Communications 2026."""
import zipfile,hashlib,xml.etree.ElementTree as E,posixpath,statistics,json
from pathlib import Path
D=Path.home()/'Research/Mechanism_Atlas_H2/h5_lysosome_20261120'
SOURCE=D/'CuniLopez2026_MOESM6_original_source.xlsx'
FREEZE=D/'FROZEN_POSTHOC_CUNILOPEZ_FIG5_ELIGIBILITY_20261121.md'
OUT=D/'CuniLopez2026_H5_APOE3_vs_APOE4_SourceGate_20261121.json'
assert not OUT.exists()
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()=='b2c21e787d74041f67a8ccee90a14ac83679dd8596948120fd357d2434473ceb'
M='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
def parse(names):
 res={}
 with zipfile.ZipFile(SOURCE) as z:
  ss=[]
  if 'xl/sharedStrings.xml' in z.namelist():
   root=E.fromstring(z.read('xl/sharedStrings.xml'))
   ss=[''.join(t.text or '' for t in x.iter(M+'t')) for x in root.findall(M+'si')]
  w=E.fromstring(z.read('xl/workbook.xml'))
  rel={x.get('Id'):x.get('Target') for x in E.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
  for sh in w.iter(M+'sheet'):
   name=sh.get('name')
   if name not in names:continue
   target=rel[sh.get(R+'id')]
   path=target.lstrip('/') if target.startswith('/') else posixpath.normpath(posixpath.join('xl',target))
   xml=E.fromstring(z.read(path))
   rr=[]
   for row in xml.findall('.//'+M+'sheetData/'+M+'row'):
    entry={'row':int(row.get('r'))}
    for c in row.findall(M+'c'):
     v=c.find(M+'v')
     if v is None:continue
     val=v.text
     if c.get('t')=='s':val=ss[int(val)]
     else:
      try:val=float(val)
      except:pass
     entry[''.join(k for k in c.get('r') if k.isalpha())]=val
    rr.append(entry)
   res[name]=rr
 return res
s=parse({'1C','5C','5F','5L','5N','5P','5R'})
assert set(s)=={'1C','5C','5F','5L','5N','5P','5R'}
rows1={r['row']:r for r in s['1C']}
rows5={r['row']:r for r in s['5C']}
assert rows1[4]['A']=='APOE3' and rows1[5]['A']=='APOE4'
assert [rows5[2][x] for x in ('B','C','D')]==['APOE2','APOE3','APOE4']
def fseq(rows,row,cols):return [float(rows[row][k]) for k in cols if k in rows[row]]
E3vehicle=fseq(rows1,4,'BCDEFG');E4vehicle=fseq(rows1,5,'BCDEFG')
E3OA=fseq(rows1,4,'HIJKLM');E4OA=fseq(rows1,5,'HIJKLM')
E3p62=[float(r['C']) for r in s['5C'] if r['row']>=3 and 'C' in r]
E4p62=[float(r['D']) for r in s['5C'] if r['row']>=3 and 'D' in r]
assert len(E3vehicle)==len(E4vehicle)==len(E3OA)==len(E4OA)==6
assert (len(E3p62),len(E4p62))==(5,4)
def report(a,b,label,unit):
 return {'comparison':label,'unit':unit,'N_E3':len(a),'N_E4':len(b),'E3':a,'E4':b,
  'mean_E3':statistics.mean(a),'mean_E4':statistics.mean(b),
  'ratio_E4_over_E3':statistics.mean(b)/statistics.mean(a),
  'percent_E4_vs_E3':100*(statistics.mean(b)/statistics.mean(a)-1),
  'difference_E4_minus_E3':statistics.mean(b)-statistics.mean(a)}
out={'study':{'doi':'10.1038/s41467-026-76565-6','pmid':'42749735','published':'2026-08-19','human_iPSC_isogenic_backgrounds':['KOLF2.1J original donor age57','BIONi037A original donor age77, diagnosed disease not recorded in source line registry'],'paper_status':'PEER_REVIEWED'},
 'source':{'url':'https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-026-76565-6/MediaObjects/41467_2026_76565_MOESM6_ESM.xlsx','sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'posthoc_freeze_sha256':hashlib.sha256(FREEZE.read_bytes()).hexdigest()},
 'fig1C_vehicle':report(E3vehicle,E4vehicle,'APOE4/4 vs APOE3/3 basal lipid droplet #/cell area','6 independently treated cultures/group, NOT donors'),
 'fig1C_oleic_acid':report(E3OA,E4OA,'APOE4/4 vs APOE3/3 after 80 uM oleic acid','6 independent treatments/group, NOT donors'),
 'fig5C_p62':report(E3p62,E4p62,'APOE4/4 vs APOE3/3 % droplet volume overlapping SQSTM1/p62','5 and 4 imaged frames from KOLF2.1J only, NOT independent genetic donors'),
 'fig5C_source_author_reported_E3_E4_p':0.000038,
 'fig5C_p_provenance':'printed_in_Figure5_caption author ANOVA Tukey posthoc comparison; DO NOT calculate new p from nested fields',
 'Fig5A_E3_vs_E4':'NOT SIGNIFICANT (Figure5A original image shows ns; proteomic p62 abundance in buoyant LD fraction)',
 'Fig5F_J_L_N_P_R_genotype_warning':'APOE2 versus APOE4 comparisons, NOT APOE3 versus APOE4 direct evidence',
 'complete_H5_causal_conjunction':'NOT measured directly in E3 vs E4 same-system: Fig1C only lipid droplet abundance (A part); Fig5C p62/droplet overlap proxy, no direct lysosomal cargo degradation flux. Strong lipophagy flux experiments focus E2 vs E4.',
 'recommendation':'HOLD OUT of H5 submission pending strict relevance review: the pairwise E3/E4 readouts contextual and add little beyond current P1/P5 direct lysosome assays; do not count E2/E4 rescue as E3/E4.',
 'nonaged_origin_uncertainty':'BIONi original donor aged 77 and KOLF donor aged 57; donor clinical disease vs reprogrammed cell state qualifiers unresolved.',
 'limitations':['Originally reviewed Figures 1 and 5 before freeze; this is POSTHOC source reconstruction.','No p-values recomputed, although author E3/E4 Figure5C p cited.','n from Figure5C are nested frames, not independent human donors.','Source Fig5A protein-abundance E3/E4 ns is not absolute evidence of equivalent p62.','No wet-lab experiments or novel causality by Mechanism Atlas.','No MecCog submission updated.']}
OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2))
for key in ['fig1C_vehicle','fig1C_oleic_acid','fig5C_p62']:
 q=out[key]
 print(key,'E3',round(q['mean_E3'],6),'E4',round(q['mean_E4'],6),'E4/E3',round(q['ratio_E4_over_E3'],5),'N',q['N_E3'],q['N_E4'])
print('FILE',OUT,hashlib.sha256(OUT.read_bytes()).hexdigest(),'POSTHOC_H5_P6_HOLD')