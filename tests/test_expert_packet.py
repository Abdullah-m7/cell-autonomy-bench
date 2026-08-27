import csv, hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BENCH=ROOT/'benchmark'
FORBIDDEN={'case_id','pair_id','family','origin','provisional_action','provisional_rationale','evidence_source_ids','evidence_support_type','expert_gold_action','expert_rationale'}

def _rows(name):
    with (BENCH/name).open(newline='',encoding='utf-8') as f:
        return list(csv.DictReader(f))

def test_cleanroom_packet_has_no_structural_label_leakage():
    for name,n in [('expert_review_pilot_v0.2_cleanroom.csv',24),('expert_review_full_v0.2_cleanroom.csv',100)]:
        rows=_rows(name); assert len(rows)==n
        assert not (set(rows[0]) & FORBIDDEN)
        assert all(r['review_case_id'].startswith('ER-') for r in rows)
        assert all(r['expert_action']=='' and r['confidence_1_5']=='' and r['rationale']=='' for r in rows)

def test_manifest_hashes_cleanroom_artifacts():
    m=json.loads((BENCH/'EXPERT_PACKET_MANIFEST_v0.2.json').read_text())
    for artifact,key in [(m['pilot_artifact'],'pilot_sha256'),(m['full_cleanroom_artifact'],'full_cleanroom_sha256')]:
        got=hashlib.sha256((ROOT/artifact).read_bytes()).hexdigest()
        assert got==m[key]

def test_pilot_uses_24_unique_opaque_ids():
    rows=_rows('expert_review_pilot_v0.2_cleanroom.csv')
    ids=[r['review_case_id'] for r in rows]
    assert len(ids)==len(set(ids))==24
