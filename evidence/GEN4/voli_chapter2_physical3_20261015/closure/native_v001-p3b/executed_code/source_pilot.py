"""Source-bound finite-N Krylov adapter and installed native minor solve."""
from pathlib import Path
import argparse,hashlib,importlib.util,json,shutil,sys
BASE=Path(__file__).resolve().parents[1];ROOT=BASE.parents[1]
sys.path.insert(0,str(ROOT))
from SAM_PROJECT.session import DomainSession
from SAM_PROJECT.gen6_duck_t500.resources import own_cpus
from CURRENT_REVISION.engines.SLC.gen3 import retained
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):Path(p).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
def main():
 p=argparse.ArgumentParser();p.add_argument('--profile',default='V001_BASE');p.add_argument('--power',type=int,default=3)
 p.add_argument('--attempt',required=True);p.add_argument('--precision',type=int,default=1024);a=p.parse_args()
 out=BASE/'closure'/('native_'+a.attempt);out.mkdir(exist_ok=False)
 snap=out/'executed_code';snap.mkdir();shutil.copy2(BASE/'closure/point_source.py',snap/'point_source.py');shutil.copy2(__file__,snap/'source_pilot.py')
 spec=importlib.util.spec_from_file_location('literal_source',snap/'point_source.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 # The frozen script's own directory no longer determines the project root.
 m.ROOT=ROOT
 source=ROOT/'GEN4/spin_conditional_variance1/sources/original'/(a.profile+'.json.gz')
 binding=dict(campaign=BASE.name,question='Does the actual finite-N spin Krylov enlargement have another outgoing direction?',
  profile_id=a.profile,operator='A=N(I-P); original physical heatbath fields, no auxiliary replacement',
  source_files={str(source.relative_to(ROOT)):sha(source)},source_adapter=str(snap.relative_to(ROOT)),
  executed_code={x.name:sha(x)for x in snap.iterdir()},power=a.power,precision_bits=a.precision,
  native_route='Source-bound DomainSession extension followed by installed GEN3_COMPLEX_SOLVE')
 save(out/'SOURCE_BINDING.json',binding)
 with own_cpus([6]):
  with DomainSession.start('STARBREAKER',objective=binding['question'],output_root=out/'sessions') as session:
   print(session.announcement(),flush=True);save(out/'SESSION_POINTER.json',dict(path=str(session.directory),announcement=session.announcement()))
   original=session.consumer;machine=original.ce.runtime_for('STARBREAKER').machine
   class Adapter:
    def __getattr__(self,name):return getattr(original,name)
    def execute(self,op,payload):
     if op!='CHAPTER2_FULL_SOURCE_POINT_KRYLOV_V1':return original.execute(op,payload)
     result=m.calculate(payload['profile_id'],payload['power'],precision=payload['precision_bits'])
     ref=retained.put(machine,'mathematical_result',result,payload,dict(origin=op,source_binding=binding),sorted(retained.nested_refs(result)))
     return dict(result_ref=ref,output=result)
   session.consumer=Adapter()
   got=session.execute('CHAPTER2_FULL_SOURCE_POINT_KRYLOV_V1',dict(profile_id=a.profile,power=a.power,precision_bits=a.precision,source_binding=binding),
    purpose='Evaluate original full-N generator on literal configurations with every background multiplicity retained')
   save(out/'SOURCE_RESULT.json',got);res=got['output']
   print(json.dumps({k:res[k]for k in ['status','profile_id','rank_lower_bound','states_evaluated','seconds']}),flush=True)
   if res['certificate']:
    ids=res['certificate']['row_indices'];n=len(ids)
    mat=dict(entries=[[dict(re=res['evaluation_rows'][i][j],im=0)for j in range(n)]for i in ids],
     row_basis=list(map(str,ids)),column_basis=res['basis'],structure='GENERAL')
    eye=dict(entries=[[int(i==j)for j in range(n)]for i in range(n)],row_basis=list(map(str,ids)),column_basis=list(map(str,ids)),structure='GENERAL')
    inv=session.execute('GEN3_COMPLEX_SOLVE',dict(precision_bits=a.precision,source_binding=binding,data=dict(matrix=mat,rhs=eye)),
     purpose='Certify actual full-source point-minor invertibility in the installed native matrix kernel')
    save(out/'NATIVE_INVERSE.json',inv);print('Native point-minor inverse returned',flush=True)
   save(out/'SESSION_STATUS.json',session.status())
 save(out/'DONE.json',dict(status=res['status'],profile_id=a.profile,power=a.power,rank_lower_bound=res['rank_lower_bound'],native_executions=2 if res['certificate'] else 1))
if __name__=='__main__':main()
