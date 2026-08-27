#!/usr/bin/env python3
"""Build leak-checked clean-room expert review ZIPs.

This script never exports raw internal case IDs or author provisional labels.
"""
from __future__ import annotations
from pathlib import Path
import csv, hashlib, json, sys, zipfile

ROOT=Path(__file__).resolve().parents[1]
BENCH=ROOT/'benchmark'
MATERIALS=ROOT/'expert_materials'
MANIFEST=BENCH/'EXPERT_PACKET_MANIFEST_v0.2.json'

FORBIDDEN_COLUMNS={
    'case_id','pair_id','family','origin','provisional_action','provisional_rationale',
    'evidence_source_ids','evidence_support_type','expert_gold_action','expert_rationale'
}
FORBIDDEN_TEXT=(
    'github.com/Abdullah-m7/cell-autonomy-bench',
    'SRC-BENCH-',
)
ALLOWED_ACTIONS={'','ACT','CLARIFY','DEFER','REFUSE'}

def sha256(path:Path)->str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def audit_csv(path:Path, expected_rows:int, expected_sha:str)->None:
    if sha256(path)!=expected_sha:
        raise SystemExit(f'hash mismatch: {path}')
    with path.open(newline='',encoding='utf-8') as f:
        rows=list(csv.DictReader(f))
        fields=set(f.seek(0) or next(csv.reader(f))) if False else None
    if len(rows)!=expected_rows:
        raise SystemExit(f'row count mismatch: {path}')
    headers=set(rows[0].keys()) if rows else set()
    leaked=headers & FORBIDDEN_COLUMNS
    if leaked:
        raise SystemExit(f'forbidden outbound columns: {sorted(leaked)}')
    if 'review_case_id' not in headers:
        raise SystemExit('missing opaque review_case_id')
    if any(not r['review_case_id'].startswith('ER-') for r in rows):
        raise SystemExit('non-opaque review id found')
    if any(r.get('expert_action','') not in ALLOWED_ACTIONS for r in rows):
        raise SystemExit('unexpected prefilled action')
    # A new packet must be blank before expert use.
    fill_fields=('expert_action','confidence_1_5','rationale','case_valid_y_n','validity_note')
    if any(any(r.get(k,'').strip() for k in fill_fields) for r in rows):
        raise SystemExit('expert response field is prefilled')
    text=path.read_text(encoding='utf-8')
    for token in FORBIDDEN_TEXT:
        if token in text:
            raise SystemExit(f'forbidden text token: {token}')

def build(mode:str='pilot')->Path:
    m=json.loads(MANIFEST.read_text(encoding='utf-8'))
    if mode=='pilot':
        csv_path=ROOT/m['pilot_artifact']; rows=m['pilot_rows']; h=m['pilot_sha256']
        name='Blinded_Living_Cell_Autonomy_Review_Pilot_v0.2.zip'
    elif mode=='full':
        csv_path=ROOT/m['full_cleanroom_artifact']; rows=m['full_rows']; h=m['full_cleanroom_sha256']
        name='Blinded_Living_Cell_Autonomy_Review_Full_v0.2.zip'
    else:
        raise SystemExit('mode must be pilot or full')
    audit_csv(csv_path,rows,h)
    inst=MATERIALS/'EXPERT_REVIEW_INSTRUCTIONS_v0.2.md'
    text=inst.read_text(encoding='utf-8')
    for token in FORBIDDEN_TEXT:
        if token in text:
            raise SystemExit(f'forbidden instruction token: {token}')
    outdir=ROOT/'dist'; outdir.mkdir(exist_ok=True)
    out=outdir/name
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
        z.write(inst,'EXPERT_REVIEW_INSTRUCTIONS_v0.2.md')
        z.write(csv_path,csv_path.name)
        z.writestr('PACKET_SHA256.txt', f'{csv_path.name}  {h}\n')
    print(f'BUILT {out}')
    print(f'WORKSHEET_SHA256 {h}')
    return out

if __name__=='__main__':
    build(sys.argv[1] if len(sys.argv)>1 else 'pilot')
