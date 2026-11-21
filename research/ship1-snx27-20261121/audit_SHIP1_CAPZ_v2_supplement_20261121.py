#!/usr/bin/env python3
"""Read-only source-locked exploratory triangulation of bioRxiv v2 supplement."""
import json,hashlib,zipfile,posixpath,re,xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime,timezone
D=Path.home()/'Research/Mechanism_Atlas_H2/ship1_capz_v2_20261121'
SRC=D/'Terzioglu2026_bioRxiv_v2_supplement_data_original.xlsx'
PROTOCOL=D/'FROZEN_SOURCE_TABLE_TRIANGULATION_20261121.md'
OUT=D/'Terzioglu2026_v2_SHIP1_CAPZ_SOURCE_TRIANGULATION_20261121.json'
assert not OUT.exists(), 'DO NOT overwrite an executed analysis'
LOCKS={SRC:'e6beb43eac6090d8985dbbaefecc6dddcba641968f53c4abfcefdc19e97efdc6',
       PROTOCOL:'995a0b024c611d82e7f81d6c2c31a3aa636115ed381c357c5cc46a1a5122a296'}
for p,h in LOCKS.items():assert hashlib.sha256(p.read_bytes()).hexdigest()==h,(p,'SHA mismatch')
PANEL=['INPP5D','INPPL1','CAPZA2','CAPZA1','CAPZB',
       'RAB5A','RAB5B','RAB5C','RAB7A','RAB11A','RAB11B',
       'TBC1D5','ARF6','RAB35','SNX27','VPS35','PICALM','LRP1',
       'TMEM175','CTSD','LAMP1','ATP6V1A','GPNMB',
       'TREM2','APOE','ABCA1','C1QA','C1QB']
assert len(PANEL)==28 and len(set(PANEL))==28
M='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
def workbook_reader(path,names):
 result={}
 with zipfile.ZipFile(path) as z:
  ss=[]
  if 'xl/sharedStrings.xml' in z.namelist():
   rr=ET.fromstring(z.read('xl/sharedStrings.xml'))
   ss=[''.join((t.text or '') for t in v.iter(M+'t')) for v in rr.findall(M+'si')]
  w=ET.fromstring(z.read('xl/workbook.xml'))
  rel={v.get('Id'):v.get('Target') for v in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
  for sh in w.iter(M+'sheet'):
   name=sh.get('name')
   if name not in names:continue
   target=rel[sh.get(R+'id')]
   full=target.lstrip('/') if target.startswith('/') else posixpath.normpath(posixpath.join('xl',target))
   root=ET.fromstring(z.read(full))
   rows=[]
   for row in root.iter(M+'row'):
    values={}
    for cell in row.findall(M+'c'):
     key=re.match(r'^[A-Z]+',cell.get('r',''))
     if not key:continue
     raw=cell.find(M+'v')
     inl=cell.find(M+'is')
     v=raw.text if raw is not None else ''.join(inl.itertext()) if inl is not None else ''
     if cell.get('t')=='s' and v is not None:v=ss[int(v)]
     values[key.group(0)]=v
    rows.append({'source_row':int(row.get('r')),'values':values})
   result[name]=rows
 return result
names=[f'Supplementary Table {i}' for i in [1,9,10,12]]
tab=workbook_reader(SRC,names)
assert len(tab)==4
def records(name,heads):
 rows=tab[name]
 header=next((r for r in rows if r['source_row']==3),None)
 assert header is not None and all(header['values'].get(k)==v for k,v in heads.items()),(name,header)
 return [r for r in rows if r['source_row']>3 and r['values'].get('A')]
r1=records('Supplementary Table 1',{'A':'Protein ID','B':'Protein Names','C':'Log2FC (WT vs KO)','D':'p-value'})
r9=records('Supplementary Table 9',{'A':'Protein','B':'Pearson r','C':'pval'})
r12=records('Supplementary Table 12',{'A':'Protein','B':'beta','C':'pval'})
r10=records('Supplementary Table 10',{'A':'pathway','B':'pval','C':'padj','D':'NES','E':'leadingEdge'})
aliases={'INPP5D':'SHIP1','INPPL1':'SHIP2','CAPZA2':'CAZA2','CAPZA1':'CAZA1','CAPZB':'CAPZB'}
out={'status':'REAL_SOURCE_AUDIT_EXPLORATORY_NOT_NEW_BIOLOGY',
     'date_utc':datetime.now(timezone.utc).isoformat(),
     'primary_publication':'Terzioglu et al. bioRxiv v2, posted 21 Jun 2026, 10.1101/2025.10.27.684632',
     'source_url':'https://www.biorxiv.org/content/10.1101/2025.10.27.684632v2',
     'supp_source_url':'https://www.biorxiv.org/content/biorxiv/early/2026/06/21/2025.10.27.684632/DC3/embed/media-3.xlsx?download=true',
     'original_supplement_sha256':LOCKS[SRC],
     'pre_numeric_protocol_sha256':LOCKS[PROTOCOL],
     'selected_targets':PANEL,'tables_counts':{'IPMS':len(r1),'donor_correlation':len(r9),'genotype_association':len(r12),'KEGG':len(r10)},
     'target_results':{}}
def numeric(x):
 try:return float(x)
 except:return None
def matches(table,gene,ix='A'):
 return [row for row in table if str(row['values'].get(ix,'')).strip().upper()==gene]
for gene in PANEL:
 key=aliases.get(gene,gene)
 ip=[row for row in r1 if str(row['values'].get('B','')).strip().upper().split('_')[0]==key]
 cor=matches(r9,gene)
 snp=matches(r12,gene)
 out['target_results'][gene]={
  'IPMS_WT_vs_KO': [{'row':row['source_row'],'uniprot_protein_name':row['values'].get('B'),
                   'log2FC':numeric(row['values'].get('C')),'nominal_p':numeric(row['values'].get('D'))} for row in ip],
  'donor_SHIP1_correlation': [{'row':row['source_row'],'pearson_r':numeric(row['values'].get('B')),
                       'nominal_p':numeric(row['values'].get('C'))} for row in cor],
  'rs10933431_protein_association': [{'row':row['source_row'],'source_beta':numeric(row['values'].get('B')),
                       'nominal_p':numeric(row['values'].get('C'))} for row in snp],
  'appearance':{'IPMS':'LISTED' if ip else 'NOT_LISTED','donor_correlation':'LISTED' if cor else 'NOT_LISTED',
                'rs10933431':'LISTED' if snp else 'NOT_LISTED'}
 }
lys=[row for row in r10 if str(row['values']['A']).strip().upper()=='KEGG_LYSOSOME']
assert len(lys)==1
out['author_KEGG_lysosome']={'source_row':lys[0]['source_row'],'nominal_p':numeric(lys[0]['values']['B']),
    'author_adjusted_p':numeric(lys[0]['values']['C']),'NES':numeric(lys[0]['values']['D']),
    'leading_edge_proteins':lys[0]['values']['E']}
out['scientific_limits']=[
 'All rows are source author-processed statistics; not a new independent 75-donor reanalysis.',
 'No raw 75-donor individual protein abundance matrix supplied in this workbook; cannot recompute Pearson, adjust donor covariates, or prove genotype effect.',
 'Source tables may be filtered; NOT_LISTED is not a measured zero correlation.',
 'Nominal p values are not an invented FDR. No new BH q computed on potentially filtered source tables.',
 'Co-IP/PLA establishes physical association or proximity, not causal interface necessity nor cargo handoff regulation.',
 'Variant-domain abundance is prior art from authors; no functional catalytic-vs-scaffold rescue from this source.',
 'No direct APOE4-to-APOE3 paired human receptor recycling experiment in these tables.',
 'No wetlab test, therapy, clinical claim, award, or MecCog upload.'
]
OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print('SOURCE_AND_PROTOCOL_SHA_PASS',out['tables_counts'],'28_TARGETS')
for gene in PANEL:
 v=out['target_results'][gene]
 if any(v['appearance'][x]=='LISTED' for x in v['appearance']):
  print(gene,'ip',[(z['log2FC'],z['nominal_p']) for z in v['IPMS_WT_vs_KO']],
        'corr',[(z['pearson_r'],z['nominal_p']) for z in v['donor_SHIP1_correlation']],
        'snp',[(z['source_beta'],z['nominal_p']) for z in v['rs10933431_protein_association']])
print('LYSOSOME',out['author_KEGG_lysosome']['NES'],out['author_KEGG_lysosome']['author_adjusted_p'])
print('OUTPUT',OUT,'SHA256',hashlib.sha256(OUT.read_bytes()).hexdigest())