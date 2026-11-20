#!/usr/bin/env python3
"""Audit author-supplied Xia et al. 2024 Nat Commun source data, glial aggregate uptake.
All outcomes published; this is a posthoc independent arithmetic reanalysis, not
a newly generated biological experiment. Read XLSX as original SpreadsheetML only.
"""
from pathlib import Path
import zipfile,xml.etree.ElementTree as E,posixpath,io,re,json,math,statistics,hashlib,itertools,datetime
ROOT=Path(__file__).resolve().parent
F=ROOT/'Xia2024_author_source_MOESM4.xlsx'
EXPECTED_SHA='47d9439f523f58c2e075e0dd853220da9b7971fa3541cfc675913c88db86617e'
assert hashlib.sha256(F.read_bytes()).hexdigest()==EXPECTED_SHA
N='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
def ci(s):
 x=0
 for z in re.match('[A-Z]+',s).group():x=26*x+ord(z)-64
 return x
def letter(x):
 s=''
 while x:
  x,r=divmod(x-1,26);s=chr(65+r)+s
 return s
with zipfile.ZipFile(F) as z:
 shared=E.fromstring(z.read('xl/sharedStrings.xml'))
 strings=[''.join(el.text or '' for el in it.iter(N+'t')) for it in shared.findall(N+'si')]
 workbook=E.fromstring(z.read('xl/workbook.xml'))
 rel={e.get('Id'):e.get('Target') for e in E.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
 def source(sheet_name):
  sheet=next(e for e in workbook.findall('.//'+N+'sheet') if e.get('name')==sheet_name)
  p=rel[sheet.get(R+'id')]
  path=p.lstrip('/') if p.startswith('/') else posixpath.normpath(posixpath.join('xl',p))
  root=E.fromstring(z.read(path));out={}
  for row in root.findall('.//'+N+'sheetData/'+N+'row'):
   n=int(row.get('r'));vals={}
   for c in row.findall(N+'c'):
    addr=c.get('r');v=c.findtext(N+'v')
    if c.get('t')=='inlineStr':
     v=''.join(e.text or '' for e in c.iter(N+'t'))
    if v is None:continue
    if c.get('t')=='s':v=strings[int(v)]
    elif c.get('t') not in ('str','e','inlineStr'):
     try:v=float(v)
     except ValueError:pass
    vals[ci(addr)]=v
   out[n]=vals
  return out
 tab=source('Fig. 4')
 print('FIG4_SOURCE_HEADERS')
 for row in (2,3):
  print('ROW',row,[(letter(k),str(v)[:65]) for k,v in sorted(tab[row].items()) if isinstance(v,str)])
 print('FIG4_GROUP_BY_COL')
 groups={}
 for column in range(3,30):
  label=tab[3].get(column)
  # Row 2 is merged across each lipidation section: use the last preceding labeled section header.
  preceding=[c for c in tab[2] if c<=column and isinstance(tab[2][c],str)]
  phase=tab[2][max(preceding)] if preceding else None
  if isinstance(label,str):
   a=[tab[r].get(column) for r in (4,5,6)]
   b=[tab[r].get(column) for r in (8,9,10)]
   if all(isinstance(x,(int,float)) for x in a+b):
    groups[letter(column)]={'source_lipidation_header':phase,'source_condition':label,
        'microglia_normalized_uptake':a,'astrocytes_normalized_uptake':b,
        'microglia_mean':statistics.mean(a),'astro_mean':statistics.mean(b)}
    print(letter(column),phase,label,'microglia_mean',round(statistics.mean(a),5),
     'astro_mean',round(statistics.mean(b),5))
 assert len(groups)>=13,('groups too small',list(groups))
 src_keys={}
 ambiguity=[]
 for lip,iso in itertools.product(('Non-lipidated apoE','Lipidated apoE'),(2,3,4)):
  matches=[(c,v) for c,v in groups.items() if v['source_lipidation_header']==lip and re.search('apoE'+str(iso),v['source_condition'],re.I) and re.search(r'\bt1\b',v['source_condition'],re.I)]
  if len(matches)!=1:
   ambiguity.append({'lipidation':lip,'isoform':iso,'matching_columns':[c for c,v in matches],
       'status':'NO_GO_FOR_THIS_ISOFORM: duplicate/missing author source condition label'})
   print('SOURCE_LABEL_AMBIGUITY',lip,iso,[c for c,v in matches])
   continue
  src_keys[(lip,iso)]=matches[0]
 contrasts={}
 for cell in ('microglia_normalized_uptake','astrocytes_normalized_uptake'):
  for lip in ('Non-lipidated apoE','Lipidated apoE'):
   if (lip,3) not in src_keys or (lip,4) not in src_keys:
    print('NO_GO_UNRESOLVED_E3_E4_COMPARISON',lip,cell)
    continue
   c3,k3=src_keys[(lip,3)];c4,k4=src_keys[(lip,4)]
   a=k3[cell];b=k4[cell]
   diff=statistics.mean(b)-statistics.mean(a)
   ratio=statistics.mean(b)/statistics.mean(a)
   allx=a+b
   perms=[]
   for choice in itertools.combinations(range(6),3):
    indexes=set(choice)
    perms.append(statistics.mean(allx[i] for i in indexes)-
                 statistics.mean(allx[i] for i in range(6) if i not in indexes))
   exact_p=sum(abs(x)>=abs(diff)-1e-12 for x in perms)/20
   name=('MIC' if cell.startswith('micro') else 'AST')+'_'+('NLP' if lip.startswith('Non') else 'LP')
   contrasts[name]={'E3_source_column':c3,'E4_source_column':c4,'apoE3_three_replicate_values':a,
      'apoE4_three_replicate_values':b,'E3_mean':statistics.mean(a),'E4_mean':statistics.mean(b),
      'E4_over_E3_mean_ratio':ratio,'E4_minus_E3_difference_in_normalized_fluorescence':diff,
      'descriptive_two_sided_3plus3_exact_label_permutation_p':exact_p}
   print('CONTRAST',name,'E4/E3',round(ratio,5),'DELTA',round(diff,5),'PERM_P',exact_p)
 # interaction on relative/absolute scales is exploratory due to already having seen source figure.
 interactions={}
 for cell in ('MIC','AST'):
  if cell+'_NLP' not in contrasts or cell+'_LP' not in contrasts:
   interactions[cell]={'status':'NO_GO: source lipidated E3 or E4 label unresolved'}
   continue
  n=contrasts[cell+'_NLP'];l=contrasts[cell+'_LP']
  interactions[cell]={'E4_vs_E3_abs_effect_NLP_minus_LP':
      n['E4_minus_E3_difference_in_normalized_fluorescence']-
      l['E4_minus_E3_difference_in_normalized_fluorescence'],
   'E4_E3_ratio_NLP':n['E4_over_E3_mean_ratio'],
   'E4_E3_ratio_LP':l['E4_over_E3_mean_ratio']}
  print('EXPLORATORY_INTERACTION',cell,interactions[cell])
 result={'status':'POSTHOC_REANALYSIS_OF_PUBLISHED_EXPERIMENTAL_DATA_NOT_NEW_BIOLOGY',
    'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'source_paper':'Xia et al. Nat Commun 2024 DOI 10.1038/s41467-024-49028-z PMID 38824138',
    'source_xlsx_url':'https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-024-49028-z/MediaObjects/41467_2024_49028_MOESM4_ESM.xlsx',
    'source_xlsx_sha256':EXPECTED_SHA,'source_sheet':'Fig. 4','source_lipidation_group_header_row':2,
    'source_isoform_and_timing_label_row':3,'source_replicate_rows_microglia':[4,5,6],
    'source_replicate_rows_astrocyte':[8,9,10],
    'source_normalization':'fluorescence signal divided by each replicate apoE-free Aβ t1 reference, as published',
    'all_selected_source_columns':groups,'source_label_ambiguity':ambiguity,
    'posthoc_E4_vs_E3_contrasts':contrasts,
    'posthoc_isoform_lipidation_interaction':interactions,
    'limitations':[
      'Original assay includes exogenously prepared APOE+Abeta coaggregates; it does NOT prove APOE4 aggregates de novo inside healthy human endolysosomes',
      'Label row 2 names the lipidation class; row 3 isoform condition uses LP/NLP abbreviations, do not confuse them',
      'Author source represents three biological replicate fluorescence measurements per condition; these may share matched experiment batches; independent-label permutation is only an exploratory sensitivity check not a confirmatory p-value',
      'No independent donor-stratified inference, no newly measured ligand binding, direct intralysosomal fibrillation, or therapeutic efficacy',
      'No source-author statistics or FDRs were recomputed, values are author normalized fluorescence',
      'Posthoc comparisons identified after paper figures were already inspected; no blind holdout'
      ]}
 dest=ROOT/'Xia2024_Fig4_author_source_glia_isoform_lipidation_audit.json'
 dest.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
 print('SAVED',dest)
