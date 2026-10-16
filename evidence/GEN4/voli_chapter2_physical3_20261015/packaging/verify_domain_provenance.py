#!/usr/bin/env python3
"""Offline hash/source/snapshot audit of the actual finite-source native sessions.

Native inverse outputs are additionally checked against the literal returned
source point minors by independent dyadic interval multiplication. No engine is
loaded and no native science is executed. Incomplete attempts remain explicit.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,sys
HERE=Path(__file__).resolve().parent;BASE=HERE.parent;ROOT=BASE.parents[1]
sys.path.insert(0,str(BASE/'closure'));from verify_point_certificate import I
checks=0
def ok(v,label):
 global checks
 assert v,label
 checks+=1
def read(p):return json.loads(Path(p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def points(d):return d['profiles'] if 'profiles' in d else [d]
def main():
 records=[];incomplete=[];code=[];scientific=solves=0
 for folder in sorted((BASE/'closure').glob('native_*')):
  bp=folder/'SOURCE_BINDING.json'
  if not bp.is_file():continue
  binding=read(bp)
  for name,digest in binding['executed_code'].items():
   p=folder/'executed_code'/name;ok(sha(p)==digest,'executed-code snapshot '+str(p));code.append(dict(path=str(p.relative_to(ROOT)),sha256=digest))
  for name,digest in binding['source_files'].items():ok(sha(ROOT/name)==digest,'literal source bytes '+name)
  raw=read(folder/'SOURCE_RAW.json') if (folder/'SOURCE_RAW.json').is_file() else None
  candidates=points(raw) if raw else []
  for call in sorted(folder.glob('sessions/*/calls/*')):
   inp=call/'INPUT.json';rp=call/'RECEIPT.json'
   if inp.is_file():
    request=read(inp);ok(request['payload']['source_binding']==binding,'frozen input binding '+str(call))
   else:request={}
   if not rp.is_file():
    incomplete.append(dict(path=str(call.relative_to(ROOT)),input_present=inp.is_file(),receipt_present=False,scientific_return_assigned=False));continue
   receipt=read(rp);ok(receipt['status']=='RETURNED','returned session call '+str(call))
   outp=call/'OUTPUT.json';ok(sha(inp)==receipt['input_sha256'],'input receipt digest '+str(call));ok(sha(outp)==receipt['output_sha256'],'output receipt digest '+str(call))
   output=read(outp);operation=receipt['operation']
   ok(operation==request['operation'],'operation identity '+str(call))
   if operation=='CHAPTER2_FULL_SOURCE_POINT_KRYLOV_V1':
    scientific+=1;r=output['output'];same=next((x for x in candidates if x['profile_id']==r['profile_id']),None)
    ok(same is not None,'returned source has retained raw '+r['profile_id'])
    for name in ('source','basis','configurations','evaluation_rows','certificate','rank_lower_bound'):
     ok(r[name]==same[name],'retained scientific field '+r['profile_id']+' '+name)
   elif operation=='GEN3_COMPLEX_SOLVE':
    solves+=1;m=request['payload']['data']['matrix'];n=len(m['entries']);candidate=None
    for r in candidates:
     if r['basis']!=m['column_basis']:continue
     ids=r['certificate']['row_indices']
     if len(ids)!=n:continue
     if all(m['entries'][i][j]==dict(re=r['evaluation_rows'][ids[i]][j],im=0) for i in range(n) for j in range(n)):
      candidate=r;break
    ok(candidate is not None,'native inverse uses an actual source minor '+str(call))
    result=output['result'];ok(result['source_binding']==binding,'native inverse binding '+str(call))
    inverse=result['output'];ok(inverse['status']=='CERTIFIED_SOLVE','native certified inverse '+str(call))
    x=inverse['matrix']['entries'];ok(len(x)==n and all(len(row)==n for row in x),'native inverse shape')
    a=[[I.make(v['re']) for v in row] for row in m['entries']];b=[]
    for row in x:
     br=[]
     for v in row:
      ok(F(v['im']['lower'])<=0<=F(v['im']['upper']),'inverse real source imaginary enclosure');br.append(I.make(v['re']))
     b.append(br)
    for i in range(n):
     for j in range(n):
      value=sum((a[i][k]*b[k][j] for k in range(n)),I.make(0));ok(value.lo<=F(i==j)<=value.hi,'independent native inverse product identity')
   else:raise AssertionError('Unexpected finite-source operation: '+operation)
   records.append(dict(operation=operation,receipt_path=str(rp.relative_to(ROOT)),receipt_sha256=sha(rp),
    input_path=str(inp.relative_to(ROOT)),input_sha256=receipt['input_sha256'],output_path=str(outp.relative_to(ROOT)),output_sha256=receipt['output_sha256']))
 out=dict(schema='SAM_CH2_ACTUAL_SOURCE_DOMAIN_PROVENANCE_V1',status='PASS',checks=checks,returned_source_evaluations=scientific,
  native_source_minor_inverses=solves,returned_calls=len(records),incomplete_attempts=incomplete,
  scientific_return_scope='Incomplete attempts are preserved without assigning a source return; all recorded successful outputs are hash-authenticated.',
  native_executions_from_this_script=0,executed_code_snapshots=code,records=records)
 (HERE/'DOMAIN_PROVENANCE_VERIFICATION.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({k:out[k] for k in ('status','checks','returned_source_evaluations','native_source_minor_inverses','returned_calls')}))
if __name__=='__main__':main()
