"""Native flow solves for the result-generated conservative transport candidate."""
import argparse,hashlib,json,sqlite3
from pathlib import Path
from fractions import Fraction as F
import sympy as s
from SAM_PROJECT.session import DomainSession
from GEN4.workstation.memory import Memory
P=Path(__file__).resolve().parent
def save(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,default=str)+'\n')
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);ap.add_argument('--parent',type=Path,required=True);a=ap.parse_args();assert not a.out.exists()
 parent=json.loads((a.parent/'RESULTS.json').read_text());assert parent['answers']['lossless_balance']['active_fractions'][0]=='3/4'
 binding={f:hashlib.sha256((P/f).read_bytes()).hexdigest() for f in ['NETWORK_QUESTION.md','NETWORK_METHOD.md','network.py','inputs/MANIFEST.json']};binding['parent_RESULTS.json']=hashlib.sha256((a.parent/'RESULTS.json').read_bytes()).hexdigest()
 mem=Memory(a.out);answers={}
 with mem.db:
  mem.set('root',(P/'NETWORK_QUESTION.md').read_text());mem.set('root_status','OPEN');mem.set('binding',binding);mem.set('source_memory',parent['source_memory']);mem.set('parent',str(a.parent));mem.object('PARENT_NATIVE_RESULT',parent)
  for r in json.loads((P/'inputs/MANIFEST.json').read_text()):mem.object('RETAINED_SOURCE',dict(**r,text=(P/'inputs'/r['file']).read_text()))
 def propose(ident,R,speed,parentid):
  with mem.db:
   mem.db.execute('INSERT INTO tasks VALUES(?,?,?,?,?,NULL)',(ident,'network',parentid,json.dumps(dict(R=R,speed=speed,question='Solve receiver traffic, then read free fractions and boundary correction.')),'PENDING'))
   mem.db.execute('INSERT INTO links VALUES(?,?,?)',(parentid,ident,'RESULT_GENERATED'));mem.event('QUESTION_PROPOSED',dict(id=ident,parent=parentid,R=R,speed=speed))
 propose('radial9',9,1,'parent:lossless_balance')
 ses=DomainSession.start('STARBREAKER',objective='Derive spatial utilization from conservative carrier-work transport',output_root=a.out/'sessions',receipt_storage='gzip')
 try:
  print(ses.announcement(),ses.directory,flush=True);assert ses.manifest['global_slc']=='SLC-GEN4-P1'
  while True:
   row=mem.db.execute("select id,data from tasks where status='PENDING' order by rowid limit 1").fetchone()
   if not row:break
   ident,raw=row;d=json.loads(raw);R=d['R'];speed=d['speed'];L=s.zeros(R-1);J=F(1,2)
   for i in range(1,R):
    left=(i-1)*i;right=i*(i+1);L[i-1,i-1]=left+right
    if i>1:L[i-1,i-2]=-left
    if i<R-1:L[i-1,i]=-right
   payload=dict(strategy='linear',matrix=[[str(speed*v) for v in row] for row in L.tolist()],observed=[str(speed*J)]+['0']*(R-2),source_binding=binding,context=dict(history=dict(mapping='Poisson arrivals, lossless single-server work, conservative isotropic radial routing; free fraction is read after traffic solve'),basis=list(range(1,R))))
   with mem.db:mem.db.execute("update tasks set status='RUNNING' where id=?",(ident,))
   native=ses.execute('GEN2_READOUT_INVERSE',payload,purpose=ident);save(a.out/'calls'/(ident+'.json'),dict(payload=payload,result=native));assert native['unique']
   rho=[F(x) for x in native['particular']];assert all(0<x<1 for x in rho)
   # Analytic comparison after native return; never supplied to the inverse.
   residual=[x-J*(F(1,i)-F(1,R)) for i,x in enumerate(rho,1)];assert not any(residual)
   result=dict(R=R,speed=speed,injection=str(J*speed),utilization=[str(x) for x in rho],free_fraction=[str(1-x) for x in rho],mean_queued_work=[str(x/(1-x)) for x in rho],inverse_radius_formula_residual=[str(x) for x in residual],inner_boundary_correction=str(J-rho[0]))
   save(a.out/'answers'/(ident+'.json'),result);answers[ident]=result
   with mem.db:
    h=mem.object('NATIVE_ANSWER',result);mem.db.execute("update tasks set status='ANSWERED',result=? where id=?",(h,ident));mem.event('ANSWER_RETAINED',dict(id=ident,result_hash=h))
   print(ident,'ANSWERED',flush=True)
   if speed==1 and R<33:propose('radial'+str(2*R-1),2*R-1,1,ident)
   elif speed==1:propose('radial33_fast',R,1000,ident)
  assert answers['radial33']['utilization']==answers['radial33_fast']['utilization']
  save(a.out/'CHECKPOINT.json',ses.execute('GEN3_CHECKPOINT',{},purpose='Retain spatial workload candidate and rate-invariance follow-up'))
  save(a.out/'RESULTS.json',dict(status='COMPLETE_ROOT_OPEN',binding=binding,runtime=ses.manifest,research_calls=len(answers),checkpoints=1,answers=answers,source_memory=parent['source_memory']))
  with mem.db:mem.set('worker_status','COMPLETE');mem.event('PASS_COMPLETED',dict(native_calls=len(answers),root_status='OPEN'))
  mem.db.execute('PRAGMA wal_checkpoint(TRUNCATE)');print('COMPLETE',len(answers),'native network calls',flush=True)
 finally:ses.close();mem.close()
if __name__=='__main__':main()
