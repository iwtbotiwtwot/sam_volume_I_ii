"""Final whole-run organization, no further scientific execution."""
from pathlib import Path
import json,hashlib
BASE=Path(__file__).resolve().parents[1];ROOT=BASE.parents[1]
RUN=ROOT/'GEN4/duck_gen6_local/runs/chapter3-source-field-20261015-03'
def read(p):return json.loads(p.read_text())
def save(p,d):p.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
r=read(RUN/'RUNTIME_RESULT.json');assert r['status']=='SCIENCE_COMPLETE_AWAITING_OPERATOR_ORGANIZATION';assert (r['native_returns'],r['research_returns'],r['failures'])==(11,4,0)
rows=[]
for p in sorted((RUN/'native_returns').glob('*.json')):
 d=read(p);assert d['status']=='COMPLETED'
 rows.append(dict(key=d['key'],status=d['status'],task_kind=d['task_kind'],worker=d['id'],cpu=d['worker_cpu'],wrapper=str(p.relative_to(ROOT)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),receipt=d.get('record_file',d.get('receipt')),receipt_sha256=d.get('record_file_sha256',d.get('receipt_sha256'))))
save(BASE/'RAW_OUTCOMES.json',dict(outcomes=rows,native=11,research=4,failures=0))
evidence={
'SOURCE_DENSITY':['r1_si29_outgoing_flatness','r1_si29_incoming_flatness','r1_si29_uniform_coupling_response','r2_cube_rank7_minor_inverse','r2_cube_zero_mode','source/REPORT.md','source/UNIFORM_COUPLING_RESPONSE.md'],
'FINITE_FIELD':['r1_radial_green_inverse','r2_radial_flux_energy_word','radial/REPORT.md','radial/VERIFICATION.json'],
'FIELD_ENERGY':['r2_quadrupole_matching','energy/FIELD_SOURCE.md','energy/FIELD_SOURCE_RESULTS.json'],
'CLOCK_RESPONSE':['chapter3_full_source_clock_energy_commutators','chapter3_full_scaling_epsilon_only_residual','r2_clock_phase_ratios','clock/REPORT.md','clock/RESULTS.json']}
selected=read(BASE/'R2_REVIEW.json')['selected_targets']
org=dict(parent_retained=True,coverage=[dict(id=t['id'],status='COMPLETED',evidence=evidence[t['id']],next_work='Exact physical/source assignments and selected next questions retained in FOLLOW_UP.md') for t in selected],ranking=[dict(id=t['id'],priority=i+1,reason=t['selection_reason']) for i,t in enumerate(selected)],deferred=['Complete localized quantum energy/stress and physical perturbation V','Positive receiving-field packet localization and same-source identification','Physical3D isotropy/G/length/energy/action calibration and causal/spatial completion'],raw_ledger=str(BASE/'RAW_OUTCOMES.json'),report_markdown=(BASE/'REPORT.md').read_text())
save(BASE/'ORGANIZATION.json',org);print(json.dumps(dict(outcomes=len(rows),targets=len(selected))))
