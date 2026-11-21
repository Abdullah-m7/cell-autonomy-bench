#!/usr/bin/env python3
"""Read author DESeq2 Ribo-seq transcription-normalized translation efficiency.
No invented p-values, no synthesis-rate or causal claims.
"""
from pathlib import Path
import openpyxl,hashlib,json,math
from datetime import datetime,timezone
D=Path(__file__).resolve().parent
SOURCE=D/'Krogsaeter2026_Translation_Riboseq_S2_original.xlsx'
FREEZE=D/'FROZEN_KROGSAETER_S2_RIBOSEQ_TE_TARGETS_20261121.md'
OUT=D/'Krogsaeter2026_Riboseq_TE_PreselectedPanel_REPRO.json'
assert not OUT.exists()
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()=='9e297d2643179e01b537a227d3551297645e5c97bdb8a277fc48ee1d10303e5f'
assert hashlib.sha256(FREEZE.read_bytes()).hexdigest()=='14379068fa2000dd93e4682422d1d7f3e06242133ab95156d93aac5e753055c5'
targets=['APOE','MAPT','APP','CLU','CTSD','CTSB','LAMP1','TMED5','LGALS3BP',
'PICALM','SNX27','RAB5A','RAB7A','ABCA1','INPP5D','CAPZA2','PSMB5','PSME1','GAPDH','ACTB']
assert len(targets)==len(set(targets))==20
s=openpyxl.load_workbook(SOURCE,read_only=True,data_only=True)['S2B']
head=list(next(s.iter_rows(min_row=2,max_row=2,values_only=True)))
col={k:head.index(k) for k in ['transcript','gene_id','gene_name','baseMean','log2FoldChange','lfcSE','pvalue','padj','APOE3_RNA','APOE3_RPF','APOE4_RNA','APOE4_RPF']}
def num(v):
 try:
  z=float(v)
  return z if math.isfinite(z) else None
 except:return None
panel={g:[] for g in targets}
alln=0
for rownum,row in enumerate(s.iter_rows(min_row=3,values_only=True),3):
 g=str(row[col['gene_name']] or '')
 alln+=1
 if g not in panel:continue
 r={k:row[col[k]] if k in ('transcript','gene_id','gene_name') else num(row[col[k]])
    for k in col}
 r['source_row']=rownum
 panel[g].append(r)
res={'status':'REAL_AUTHORED_SOURCE_DESEQ2_TRANSLATIONAL_EFFICIENCY_AUDIT_PREPRINT',
 'audit_context_date_fixed':'2026-11-21',
 'doi':'10.64898/2026.07.15.738801','original_source':'S2B sheet, internally captioned Table S2C TE DESeq2',
 'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
 'pre_numeric_freeze_sha256':hashlib.sha256(FREEZE.read_bytes()).hexdigest(),
 'n_source_TE_transcripts':alln,'per_gene':panel,
 'critical_limits':['TE is RPF / mRNA model, NOT absolute translation protein synthesis rate.',
 'Ribo-seq samples from 4 differentiation replicates/genotype are not 4 independent human donors.',
 'Gene-level TE may be transcript-specific; no arbitrary isoform consolidation or cherry-picked directions.',
 'Authors own p and adjusted FDR retained unmodified; no custom statistical p.',
 'No direct ApoE protein aggregates or within lysosome conformation measured.',
 'Study is preprint; not peer reviewed. No original wet-lab or MecCog submission.']}
OUT.write_text(json.dumps(res,ensure_ascii=False,indent=2))
print('SOURCE_SHA_LOCKS_PASS')
for g in targets:
 vals=panel[g]
 print('TE',g,'TRANSCRIPTS',len(vals))
 for t in vals:
  print('  ID',t['transcript'],'log2TEFC',t['log2FoldChange'],'source_FDR',t['padj'],'p',t['pvalue'],
       'E3_RNA',t['APOE3_RNA'],'E4_RNA',t['APOE4_RNA'],
       'E3_RPF',t['APOE3_RPF'],'E4_RPF',t['APOE4_RPF'])
print('OUTPUT',OUT,'SHA',hashlib.sha256(OUT.read_bytes()).hexdigest())