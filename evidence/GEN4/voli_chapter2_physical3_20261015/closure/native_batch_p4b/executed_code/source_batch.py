"""Bounded, source-bound batch; the installed matrix kernel receives real minors."""
from pathlib import Path
import argparse,hashlib,importlib.util,json,shutil,sys
BASE=Path(__file__).resolve().parents[1];ROOT=BASE.parents[1];sys.path.insert(0,str(ROOT))
from SAM_PROJECT.session import DomainSession
from SAM_PROJECT.gen6_duck_t500.resources import own_cpus
from CURRENT_REVISION.engines.SLC.gen3 import retained
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):Path(p).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
def main():
 p=argparse.ArgumentParser();p.add_argument('--attempt',required=True);p.add_argument('--power',type=int,default=4);p.add_argument('--precision',type=int,default=1024);p.add_argument('--profile');a=p.parse_args()
 out=BASE/'closure'/('native_'+a.attempt);out.mkdir(exist_ok=False);snap=out/'executed_code';snap.mkdir()
 for f in [BASE/'closure/point_source.py',Path(__file__)]:shutil.copy2(f,snap/f.name)
 spec=importlib.util.spec_from_file_location('original_source',snap/'point_source.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);m.ROOT=ROOT
 profiles=[a.profile] if a.profile else [x['profile_id'] for x in json.loads((ROOT/'GEN4/voli_chapter2_continuation2_20261015/memory/SOURCE_OPERANDS.json').read_text())['profiles']]
 binding=dict(campaign=BASE.name,question='Calculate actual full-N residual after seven dimensions and certify the next exact Krylov ranks',
  operator='A=N(I-P); every original physical field and all N sites',power=a.power,precision_bits=a.precision,
  executed_code={x.name:sha(x) for x in snap.iterdir()},profile_ids=profiles,
  source_files={str((ROOT/'GEN4/spin_conditional_variance1/sources/original'/(x+'.json.gz')).relative_to(ROOT)):sha(ROOT/'GEN4/spin_conditional_variance1/sources/original'/(x+'.json.gz')) for x in profiles})
 save(out/'SOURCE_BINDING.json',binding);results=[]
 with own_cpus([6]):
  with DomainSession.start('STARBREAKER',objective=binding['question'],output_root=out/'sessions') as session:
   save(out/'SESSION_POINTER.json',dict(path=str(session.directory)));original=session.consumer;machine=original.ce.runtime_for('STARBREAKER').machine
   class Adapter:
    def __getattr__(self,k):return getattr(original,k)
    def execute(self,op,payload):
     if op!='CHAPTER2_FULL_SOURCE_POINT_KRYLOV_V1':return original.execute(op,payload)
     r=m.calculate(payload['profile_id'],a.power,precision=a.precision);r['seconds']=str(r['seconds'])
     save(out/(payload['profile_id']+'_RAW.json'),r)
     ref=retained.put(machine,'mathematical_result',r,payload,dict(origin=op,source_binding=binding),sorted(retained.nested_refs(r)))
     return dict(result_ref=ref,output=r)
   session.consumer=Adapter()
   for index,profile in enumerate(profiles):
    got=session.execute('CHAPTER2_FULL_SOURCE_POINT_KRYLOV_V1',dict(profile_id=profile,source_binding=binding),purpose='Literal full-source Krylov evaluation with exact exchangeable-background multiplicities')
    save(out/(profile+'_RETURN.json'),got);r=got['output'];results.append(r)
    print(json.dumps(dict(profile=profile,status=r['status'],rank=r['rank_lower_bound'],seconds=r['seconds'])),flush=True)
    if r['certificate'] and index in {0,len(profiles)-1}:
     ids=r['certificate']['row_indices'];n=len(ids);basis=list(map(str,range(n)))
     mat=dict(entries=[[dict(re=r['evaluation_rows'][i][j],im=0) for j in range(n)] for i in ids],row_basis=basis,column_basis=r['basis'],structure='GENERAL')
     eye=dict(entries=[[int(i==j) for j in range(n)] for i in range(n)],row_basis=basis,column_basis=basis,structure='GENERAL')
     inv=session.execute('GEN3_COMPLEX_SOLVE',dict(source_binding=binding,precision_bits=a.precision,data=dict(matrix=mat,rhs=eye)),purpose='Native certification of an actual full-source point minor')
     save(out/(profile+'_NATIVE_INVERSE.json'),inv)
    for method in [m.OriginalSource.value,m.OriginalSource.info,m.OriginalSource.transitions]:method.cache_clear()
    save(out/'SOURCE_RAW.json',dict(profiles=results))
   save(out/'SESSION_STATUS.json',session.status())
 save(out/'DONE.json',dict(status='PASS' if all(x['status']=='PASS' for x in results) else 'UNRESOLVED',profiles=len(results),power=a.power,rank_lower_bounds=[x['rank_lower_bound'] for x in results]))
if __name__=='__main__':main()
