#!/usr/bin/env python3
"""Strict SpreadsheetML extraction of PXD077344 processed iAstrocyte proteome.
Uses source-provided logFC/P/FDR; no re-estimation or independent test.
APOE3=JIPSC1162, APOE4=JIPSC1150, n=5 culture replicates each,
mapping verified against official metadata workbook.
"""
import xml.etree.ElementTree as ET, pathlib,json,hashlib,re,csv,math,datetime
b=pathlib.Path(__file__).resolve().parent
src=b/'iAstrocytes_Results_Sex_Wilkins_HM.xml'
ns='{urn:schemas-microsoft-com:office:spreadsheet}'
targets={'ARF6','RAB35','ABCA1','PICALM','INPP5D','RAB11A','RAB11B',
         'CLTC','EHD1','EHD3','BIN1','PIP5K1A','CYTH2','GIT1','RAB7A',
         'RAB5A','SLC9A6','LRP1','LRP8'}
names=None;hits=[];nrows=0
def num(s):
    try:return float(s)
    except(TypeError,ValueError):return None
for _,row in ET.iterparse(str(src),events=('end',)):
 if row.tag!=ns+'Row':continue
 vals=[]
 for cell in row.findall(ns+'Cell'):
    idx=int(cell.get(ns+'Index',len(vals)+1))-1
    while len(vals)<idx:vals.append(None)
    d=cell.find(ns+'Data');vals.append(d.text if d is not None else None)
 if names is None:
    names=vals
    assert len(names)==41
    row.clear();continue
 nrows+=1
 v=dict(zip(names,vals))
 sym=v.get('gene_symbol') or ''
 if sym in targets:
    r={k:v.get(k) for k in ['gene_symbol','PG.Genes','PG.UniProtIds','uniprot_id',
       'APOE3_A_num-NA','APOE4_A_num-NA','logFC_APOE4_A_vs_APOE3_A',
       'P.Value_APOE4_A_vs_APOE3_A','adj.P.Val_APOE4_A_vs_APOE3_A',
       'CI.L_APOE4_A_vs_APOE3_A','CI.R_APOE4_A_vs_APOE3_A']}
    r["gene"]=sym
    r["log2fold_APOE4_vs_APOE3"]=num(r['logFC_APOE4_A_vs_APOE3_A'])
    r["fold_ratio"]=2**r["log2fold_APOE4_vs_APOE3"] if r["log2fold_APOE4_vs_APOE3"] is not None else None
    r["source_p"]=num(r["P.Value_APOE4_A_vs_APOE3_A"])
    r["source_FDR"]=num(r["adj.P.Val_APOE4_A_vs_APOE3_A"])
    r["source_logged_values_APOE3"]=[num(v.get('S1162_'+str(i)+'A')) for i in range(1,6)]
    r["source_logged_values_APOE4"]=[num(v.get('S1150_'+str(i)+'A')) for i in range(1,6)]
    r["source_CI95"]=[num(r["CI.L_APOE4_A_vs_APOE3_A"]),num(r["CI.R_APOE4_A_vs_APOE3_A"])]
    r['source_PXD']='PXD077344'
    hits.append(r)
 row.clear()
assert nrows==7108 and sum(r["gene"]=='ARF6' for r in hits)==1
ARF6=next(r for r in hits if r["gene"]=='ARF6')
assert ARF6["source_FDR"] is not None and ARF6["log2fold_APOE4_vs_APOE3"]>0
meta={"run_date_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "study":"Lysaker et al. npj Dementia 2026",
    "doi":"10.1038/s44400-026-00105-8",
    "pride_accession":"PXD077344",
    "primary_processed_file":"iAstrocytes_Results_Sex_Wilkins_HM.xml",
    "primary_processed_file_sha256":hashlib.sha256(src.read_bytes()).hexdigest(),
    "group_metadata_source":"WilkinsHM_APOE_Brain_BrainMito_iNeurons_iAstrocytes_Metadata.xlsx",
    "group_metadata_sha256":hashlib.sha256((b/"WilkinsHM_APOE_Brain_BrainMito_iNeurons_iAstrocytes_Metadata.xlsx").read_bytes()).hexdigest(),
    "sample_info":{"APOE3":"JIPSC1162, 5 culture replicates, male; samples S1162_1A .. S1162_5A",
                   "APOE4":"JIPSC1150, 5 culture replicates, male; samples S1150_1A .. S1150_5A"},
    "important_caveats":["This is third-party published proteomics, not novel proteomics collected here.",
       "Not an ARF6-GTP activity assay; total abundance only.",
       "Single isogenic parental pair; culture replicates are not independent donors.",
       "Proteome and RNA transcript datasets are NOT matched samples; cannot claim within-cell post-transcriptional regulation.",
       "Processed protein differential tests/FDR were performed by the paper authors; not independently recomputed.",
       "Numbers do not prove ARF6 causes disease or H2."],
    "total_detected":nrows, "selected_target_rows":hits}
(b/"pride_protein_panel.json").write_text(json.dumps(meta,ensure_ascii=False,indent=2))
with (b/"pride_protein_panel.csv").open('w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['gene','log2FC_E4_vs_E3','fold_ratio','p_source','FDR_source','CI_lower','CI_upper','APOE3_cultures','APOE4_cultures'])
    for r in hits:
        w.writerow([r['gene'],r['log2fold_APOE4_vs_APOE3'],r['fold_ratio'],
            r['source_p'],r['source_FDR'],*r['source_CI95'],5,5])
print("SOURCE_SHA",meta["primary_processed_file_sha256"])
print("GROUP_SHA",meta["group_metadata_sha256"])
print("TOTAL",nrows,"TARGET_HITS",len(hits))
for g in ['ARF6','RAB35','RAB11A','RAB11B','EHD3','SLC9A6','ABCA1','PICALM','CYTH2','GIT1']:
 for r in hits:
    if r['gene']==g:print("PROTEIN",g,"LOG2FC",r['log2fold_APOE4_vs_APOE3'],
     "RATIO",round(r['fold_ratio'],3),"FDR",r['source_FDR'],
     "CULTURES_E3",r['source_logged_values_APOE3'],
     "CULTURES_E4",r['source_logged_values_APOE4'])
