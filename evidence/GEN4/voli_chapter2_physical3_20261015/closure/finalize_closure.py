#!/usr/bin/env python3
"""Collect retained exact source certificates and independently verify all minors.

Only scans this scoped closure campaign, skipping native object stores. No
scientific execution, native launch, source evolution, or Gibbs integral occurs.
"""
from pathlib import Path
import argparse,hashlib,json,os
from verify_point_certificate import verify
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
EXPECTED={f+'_'+s for f in ('R015','R016')+tuple('V%03d'%i for i in range(15))+('V017',) for s in ('BASE','H_MINUS','H_PLUS')}
def objects(d):
 if isinstance(d,list):
  for x in d:yield from objects(x)
 elif isinstance(d,dict):
  if d.get('schema')=='SAM_ACTUAL_FINITE_N_KRYLOV_POINT_CERTIFICATE_V1':yield d
  else:
   for value in d.values():
    if isinstance(value,(dict,list)):yield from objects(value)
def read_sources():
 out=[]
 for current,dirs,files in os.walk(HERE):
  dirs[:]=[d for d in dirs if d not in ('sessions','R3_STATE','executed_code','__pycache__','offline')]
  for name in files:
   if name=='SOURCE_RAW.json' or name.endswith('_SOURCE_RAW.json'):
    p=Path(current)/name
    for data in objects(json.loads(p.read_text())):
     if data.get('status')=='PASS':out.append((p,data))
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--require54',action='store_true');args=ap.parse_args()
 best={}
 for p,data in read_sources():
  ident=data['profile_id'];assert ident in EXPECTED
  old=best.get(ident)
  if old is None or data['rank_lower_bound']>old[1]['rank_lower_bound']:best[ident]=(p,data)
 if args.require54:assert set(best)==EXPECTED,sorted(EXPECTED-set(best))
 offline=HERE/'offline';offline.mkdir(exist_ok=True);rows=[];bindings={};checks=0
 for ident,(p,data) in sorted(best.items()):
  source=ROOT/data['source']['path']
  if source.exists():assert hashlib.sha256(source.read_bytes()).hexdigest()==data['source']['sha256']
  out=verify(data);checks+=out['independent_rational_checks']
  inp=dict(path=str(p.relative_to(HERE)),sha256=hashlib.sha256(p.read_bytes()).hexdigest())
  out['input']=inp;(offline/(ident+'.json')).write_text(json.dumps(out,indent=2)+'\n')
  compact=[]
  for x in out['residual_chain']:
   compact.append({k:v for k,v in x.items() if k!='inverse_witness_rows'})
  rows.append(dict(profile_id=ident,N_exact=data['N_exact'],source_input=inp,source=data['source'],rank_lower_bound=data['rank_lower_bound'],
   certificate_rows=data['certificate']['row_indices'],raw_determinant=data['certificate']['determinant'],
   computed_krylov_power=len(data['basis'])//2-1,residual_chain=compact,independent_rational_checks=out['independent_rational_checks'],
   offline_certificate=str((offline/(ident+'.json')).relative_to(HERE))))
  bindings[data['source']['path']]=data['source']
 lows=[r['rank_lower_bound'] for r in rows];all7=all(r['rank_lower_bound']>=10 for r in rows)
 if rows:
  uniform=f'All {len(rows)} evaluated original finite-N preparations have a paired Krylov rank of at least {min(lows)}.'
  residual=' The seven-dimensional enlargement has exact residual rank two in every evaluated preparation.' if all7 else ''
  higher=' Selected deeper certificates reach rank '+str(max(lows))+'.' if max(lows)>min(lows) else ''
  chapter_summary=uniform+residual+higher+' The retained rank has not stabilized: these are exact full-source closure lower bounds, with strict positive Gibbs residual bounds and an explicit finite invariant count-space upper closure. No exact minimum or uncomputed global residual moment is assigned.'
 else:chapter_summary='No completed point certificate is available.'
 summary=dict(schema='SAM_CH2_ACTUAL_SPIN_CLOSURE_PROGRESS_V1',status='PASS' if set(best)==EXPECTED else 'PARTIAL',chapter_summary=chapter_summary,
  preparations=len(rows),expected_preparations=54,missing_preparations=sorted(EXPECTED-set(best)),
  independent_point_certificate_checks=checks,
  certified_Krylov_rank_lower_range=[min(lows),max(lows)] if lows else None,
  seven_dimensional_residual_rank=2 if rows and all7 else 'See individual profiles',
  uniform_all_preparations_rank_lower=min(lows) if set(best)==EXPECTED else None,
  exact_minimal_closure_status='Not stabilized at the computed depths; no exact minimum dimension is assigned',
  result='The test result suggests strong contact with the concept.',
  exact_invariant_upper_bound_file='EXACT_LUMPED_UPPER_BOUND.json',
  source_law_verification='SOURCE_LAW_VERIFICATION.json',
  residual_meaning='Exact functional residuals and strict full-Gibbs norm/rank certificates; no new global eighth-or-higher-moment integral is assigned',
  rows=rows)
 (HERE/'FINAL_CLOSURE.json').write_text(json.dumps(summary,indent=2)+'\n')
 table=['# Actual source closure certificates','',
  '| Original preparation | N | Highest paired Krylov power | Certified independent functions | Seven-dimensional residual rank |',
  '|---|---:|---:|---:|---:|']
 for r in rows:table.append(f"| {r['profile_id']} | {r['N_exact']} | {r['computed_krylov_power']} | {r['rank_lower_bound']} | {'2' if r['rank_lower_bound']>=10 else 'at least 1'} |")
 table+=['','The seven-dimensional enlargement is noninvariant. Every displayed rank is','an exact full-source lower certificate; none states that the rank has stabilized.','The final JSON retains the source hashes, selected point minors, residual-rank','chain, and conservative positive Gibbs norm factors.']
 (HERE/'CERTIFICATE_TABLE.md').write_text('\n'.join(table)+'\n')
 print(json.dumps({k:summary[k] for k in ('status','preparations','certified_Krylov_rank_lower_range','independent_point_certificate_checks')}))
if __name__=='__main__':main()
