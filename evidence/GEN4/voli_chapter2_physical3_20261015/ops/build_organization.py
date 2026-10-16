"""Organize every actual outcome without launching another calculation."""
from pathlib import Path
import hashlib,json
BASE=Path(__file__).resolve().parents[1];ROOT=BASE.parents[1]
RUN=ROOT/'GEN4/duck_gen6_local/runs/chapter2-physical-protocols-20261015-01'
def read(p):return json.loads(Path(p).read_text())
def save(p,d):Path(p).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
def main():
 rows=[]
 for p in sorted((RUN/'native_returns').glob('*.json')):
  d=read(p);assert d['status']=='COMPLETED'
  rows.append(dict(key=d['key'],status=d['status'],task_kind=d['task_kind'],receipt=d.get('record_file',d.get('receipt')),receipt_sha256=d.get('record_file_sha256',d.get('receipt_sha256'))))
 save(BASE/'RAW_OUTCOMES.json',dict(outcomes=rows,native=sum(x['task_kind']=='native' for x in rows),research=sum(x['task_kind']=='research_web' for x in rows)))
 evidence={
 'ACTUAL_CLOSURE':['r1_actual_source_rank10','r2_deep_source_inverse','r2_largest_N_inverse','closure/FINAL_CLOSURE.json','closure/DERIVATION.md'],
 'PAID_REFERENCE':['r1_forward_duration','r1_reverse_duration','r2_paid_work_coefficients','protocol/DERIVATION.md','protocol/RESULTS.json'],
 'MEASUREMENT':['r1_observable_cube','r2_improved_H3_word','r2_improved_H3_inverse','r2_zero_readout_projector','measurement/DERIVATION.md','measurement/RESULTS.json'],
 'COMPACT_CERTIFICATES':['r2_min_counter_rank','web_r2_003','certificates/SHORT_PROOFS.md','certificates/COMPACT_CERTIFICATES.json']}
 review=read(BASE/'R2_REVIEW.json');targets=review['selected_targets']
 coverage=[dict(id=t['id'],status='COMPLETED',evidence=evidence[t['id']],next_work='Exact reached boundary or physical assignments explicitly retained in FOLLOW_UP.md; no automatic continuation') for t in targets]
 org=dict(parent_retained=True,coverage=coverage,ranking=[dict(id=t['id'],priority=i+1,reason=t['selection_reason']) for i,t in enumerate(targets)],
  deferred=['Exact smallest invariant spin dimension and new global high residual norm moments','Implemented source preparation, physical epsilon/K calibration and detector tolerances','Autonomous material controller and complete thermodynamic apparatus costs'],
  raw_ledger=str(BASE/'RAW_OUTCOMES.json'),report_markdown=(BASE/'REPORT.md').read_text())
 save(BASE/'ORGANIZATION.json',org);print(json.dumps(dict(outcomes=len(rows),coverage=len(coverage))))
if __name__=='__main__':main()
