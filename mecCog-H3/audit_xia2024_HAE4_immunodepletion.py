#!/usr/bin/env python3
"""Author-source HAE-4 immunodepletion vs isotype in Xia Nat Commun 2024 Fig 7.
POSTHOC numeric audit, not new biological data or causal mediation proof.
"""
import zipfile,xml.etree.ElementTree as ET,posixpath,re,hashlib,json,statistics,itertools,datetime
from pathlib import Path
B=Path(__file__).resolve().parent
SRC=B/'Xia2024_author_source_MOESM4.xlsx'
assert hashlib.sha256(SRC.read_bytes()).hexdigest()=='47d9439f523f58c2e075e0dd853220da9b7971fa3541cfc675913c88db86617e'
N='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
def parse_sheet(z):
    ss=[''.join(t.text or '' for t in s.iter(N+'t')) for s in ET.fromstring(z.read('xl/sharedStrings.xml')).findall(N+'si')]
    wb=ET.fromstring(z.read('xl/workbook.xml'))
    rel={x.get('Id'):x.get('Target') for x in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
    sheet=next(x for x in wb.findall('.//'+N+'sheet') if x.get('name')=='Fig. 7')
    target=rel[sheet.get(R+'id')]
    path=target.lstrip('/') if target.startswith('/') else posixpath.normpath(posixpath.join('xl',target))
    root=ET.fromstring(z.read(path))
    table={}
    for row in root.findall('.//'+N+'sheetData/'+N+'row'):
        vals={}
        for cell in row.findall(N+'c'):
            value=cell.findtext(N+'v')
            if value is None:continue
            if cell.get('t')=='s':value=ss[int(value)]
            elif cell.get('t') not in ('str','e'):
                try:value=float(value)
                except ValueError:pass
            letter=re.match('[A-Z]+',cell.get('r')).group()
            vals[letter]=value
        table[int(row.get('r'))]=vals
    return table
def stats(a,b):
    assert len(a)==len(b)==3 and all(isinstance(v,(int,float)) for v in a+b)
    v=a+b
    actual=statistics.mean(b)-statistics.mean(a)
    perms=[]
    for c in itertools.combinations(range(6),3):
        ix=set(c)
        perms.append(statistics.mean(v[i] for i in ix)-statistics.mean(v[i] for i in range(6) if i not in ix))
    return {
      'isotype_original_three':a,'HAE4_original_three':b,
      'isotype_mean':statistics.mean(a),'HAE4_mean':statistics.mean(b),
      'HAE4_minus_isotype':actual,'HAE4_div_isotype':statistics.mean(b)/statistics.mean(a),
      'source_values_unpaired_ranges':{'isotype':[min(a),max(a)],'HAE4':[min(b),max(b)]},
      'exact_unpaired_two_sided_p_posthoc':sum(abs(x)>=abs(actual)-1e-12 for x in perms)/20,
      'complete_separation':max(b)<min(a) or max(a)<min(b)
    }
with zipfile.ZipFile(SRC) as z:sheet=parse_sheet(z)
SOURCE_FIELDS=[
 ('uptake','F','G','H'),
 ('MCP-1','J','K','L'),
 ('IL-1β','N','O','P'),
 ('IL-6','R','S','T'),
 ('TNF-α','V','W','X')
]
MODELS={
 'microglia':{'header':4,'rows':[5,6,7]},
 'astrocytes':{'header':11,'rows':[12,13,14]}
}
ret={
 'status':'POSTHOC_PUBLISHED_SOURCE_IMMUNODEPLETION_NOT_CAUSAL_MEDIATION',
 'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'source_article':'Xia et al. Nature Communications 2024 DOI 10.1038/s41467-024-49028-z',
 'source_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),
 'source_fig':'Fig. 7 C–L, human glial recipient cultures',
 'intervention':'HAE-4 immunoprecipitation depletion of nonlipidated extracellular ApoE4–Aβ aggregates (pre-exposure), NOT a receptor inhibitor',
 'groups':{},'limitations':[
    'Figure 7 involves immunodepletion of preformed extracellular aggregates, which changes the amount and composition of the ligand stimulus.',
    'A decrease in uptake and cytokine secretion after depletion cannot distinguish cell surface recognition, intracellular uptake or lysosomal retention.',
    'The source may not pair uptake and secreted cytokines in same cells. No mediation/covariance analysis across assays is justified.',
    'Every group n=3; exact independent-label 3+3 two-sided p has minimum 0.10 and is a posthoc sensitivity only, not author-reported p.',
    'Eight cytokine effects are correlated and not eight independent discoveries, nor proof of disease treatment.',
    'Original paper was published 2024. Findings are already published.'
 ] }
for model,meta in MODELS.items():
    header=sheet[meta['header']]
    rownos=meta['rows']
    outputs={}
    for name,original,isotype,treated in SOURCE_FIELDS:
        for c,want in ((original,'Aβ +apoE4'),(isotype,'isotype'),(treated,'HAE-4')):
            value=header.get(c,'')
            if not isinstance(value,str) or want.lower() not in value.lower().replace(' ','') and want.lower().replace(' ','') not in value.lower().replace(' ',''):
                raise ValueError(f'BAD_SOURCE_GROUP_LABEL {model} {name} {c} {value!r}, expected {want!r}')
        a=[sheet[row][isotype] for row in rownos]
        b=[sheet[row][treated] for row in rownos]
        zero=[sheet[row][original] for row in rownos]
        result=stats(a,b)
        result['unprocessed_Aβ_APOE4_original_three']=zero
        result['unprocessed_mean']=statistics.mean(zero)
        result['isotype_div_unprocessed_mean']=statistics.mean(a)/statistics.mean(zero)
        outputs[name]=result
        print('TREATMENT',model,name,'HAE4/isotype',round(result['HAE4_div_isotype'],6),
              'unprocessed/isotype',round(result['isotype_mean']/result['unprocessed_mean'],6),
              'posthoc_exact_p',result['exact_unpaired_two_sided_p_posthoc'],
              'all_3_complete_separation',result['complete_separation'],flush=True)
    ret['groups'][model]=outputs
summary=[]
for model,data in ret['groups'].items():
    uptake=data['uptake']['HAE4_div_isotype']
    for name,value in data.items():
        if name=='uptake':continue
        summary.append({'cell_type':model,'marker':name,'uptake_HAE4_over_isotype':uptake,
            'cytokine_HAE4_over_isotype':value['HAE4_div_isotype'],
            'cytokine_suppression_smaller_magnitude_than_uptake_suppression':
             value['HAE4_div_isotype']>uptake,
            'unprocessed_control_isotype_relative':value['isotype_div_unprocessed_mean']})
ret['descriptive_cross_endpoint_suppression']=summary
print('CYTOKINES_DECREASE_LESS_THAN_UPTAKE',
      sum(x['cytokine_suppression_smaller_magnitude_than_uptake_suppression'] for x in summary),
      'OUT_OF',len(summary),flush=True)
dst=B/'Xia2024_Fig7_HAE4_Immunodepletion_Audit_20261121.json'
dst.write_text(json.dumps(ret,indent=2,ensure_ascii=False)+'\n')
print('SOURCE_RESULT',dst,flush=True)
