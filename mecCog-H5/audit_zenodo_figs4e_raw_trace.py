#!/usr/bin/env python3
"""Recompute published Zenodo Figure S4e author source kinetic traces.
Exploratory, posthoc, n=recorded traces rather than known biological replicates.
Never conflate derived p with the published dextran-normalized p=0.0098.
"""
import hashlib,io,itertools,statistics as st,urllib.request,zipfile,xml.etree.ElementTree as ET,posixpath,re
URL='https://zenodo.org/records/21177115/files/Figure%20S4%20Raw%20Data.xlsx?download=1'
EXPECTED_MD5='a13200d39a9519bb609c5bfcdffd6342'
EXPECTED_SHA256='802df7826bf3e55f75dc1e32bad9ae9828aac37a5f05c80deef1e62cfa5e1a6a'
data=urllib.request.urlopen(URL,timeout=35).read()
assert hashlib.md5(data).hexdigest()==EXPECTED_MD5
assert hashlib.sha256(data).hexdigest()==EXPECTED_SHA256
z=zipfile.ZipFile(io.BytesIO(data))
M='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
strings=[]
if 'xl/sharedStrings.xml' in z.namelist():
    root=ET.fromstring(z.read('xl/sharedStrings.xml'))
    strings=[''.join((x.text or '') for x in row.iter(M+'t')) for row in root.findall(M+'si')]
work=ET.fromstring(z.read('xl/workbook.xml'))
rels={r.get('Id'):r.get('Target') for r in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
sheets=[s for s in work.iter(M+'sheet') if s.get('name')=='Fig. S4e (Incucyte)']
assert len(sheets)==1
target=rels[sheets[0].get(R+'id')]
path=target.lstrip('/') if target.startswith('/') else posixpath.normpath(posixpath.join('xl',target))
root=ET.fromstring(z.read(path))
rows=[]
for row in root.iter(M+'row'):
    cells={}
    for c in row.findall(M+'c'):
        v=c.find(M+'v');i=c.find(M+'is')
        x=v.text if v is not None else ''.join(i.itertext()) if i is not None else ''
        if c.get('t')=='s' and x:x=strings[int(x)]
        if x is not None and str(x).strip():
            try:cells[c.get('r')]=float(x)
            except ValueError:cells[c.get('r')]=x
    rows.append((int(row.get('r')),cells))
assert len(rows)==14
headers=rows[0][1]
labels=[f'E3 {i}' for i in range(1,5)]+[f'E4 {i}' for i in range(1,5)]
labels+=['E3 + Baf 1','E3 + Baf 2','E4 + Baf 1','E4 + Baf 2','E4 + Baf 3']
for c,l in zip('BCDEFGHIJKLMN',labels):
    assert headers[c+'1']==l
times=[cells['A'+str(rowid)] for rowid,cells in rows[1:]]
assert times==list(range(13))
def auc(values):
    return sum((values[i]+values[i+1])/2*(times[i+1]-times[i]) for i in range(12))
arms={}
for name,cols in [('E3','BCDE'),('E4','FGHI'),('E3+Baf','JK'),('E4+Baf','LMN')]:
    tracks=[]
    for col in cols:
        series=[float(cells[col+str(i)]) for i,cells in rows[1:]]
        assert len(series)==13 and all(x>=0 for x in series)
        tracks.append({'AUC':auc(series),'end':series[-1]})
    arms[name]={'recorded_trajectories':len(tracks),'mean_AUC':st.mean(x['AUC'] for x in tracks),
                'mean_end':st.mean(x['end'] for x in tracks),'raw':tracks}
a=[x['AUC'] for x in arms['E3']['raw']]
b=[x['AUC'] for x in arms['E4']['raw']]
allv=a+b
observed=st.mean(b)-st.mean(a)
perms=[]
for idx in itertools.combinations(range(8),4):
    chosen=set(idx)
    perms.append(st.mean(allv[k] for k in chosen)-
                 st.mean(allv[k] for k in range(8) if k not in chosen))
p=sum(abs(x)>=abs(observed)-1e-9 for x in perms)/len(perms)
assert len(perms)==70
for key,arm in arms.items():
    print(key,'traces',arm['recorded_trajectories'],'AUC_mean',round(arm['mean_AUC'],2),'end_mean',round(arm['mean_end'],2))
print('E4/E3 raw AUC ratio',round(arms['E4']['mean_AUC']/arms['E3']['mean_AUC'],5))
print('Exploratory 4v4 trace-label exact AUC p',p)
print('Author-published dextran-normalized p=0.0098 (not recomputed by this source AUC method).')
print('Trace counts are NOT confirmed independent donors or biological replicates; do not enter n=4 in MecCog.')
