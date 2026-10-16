"""Source-bound task selection for the qualified installed Duck runtime."""
from pathlib import Path
from copy import deepcopy
import hashlib,json
BASE=Path(__file__).resolve().parent;ROOT=BASE.parents[1]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):Path(p).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
def wire(m):return dict(entries=deepcopy(m),row_basis=list(map(str,range(len(m)))),column_basis=list(map(str,range(len(m[0])))),structure='GENERAL')
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def task(key,op,payload,question,lane,**kw):
 b=dict(campaign=BASE.name,law_namespace='SAM_land',question=question,parent='H002635',
   physical_scope='Original finite-N source and retained continuum calibration; apparatus assumptions separately declared',
   source_files={str(p.relative_to(ROOT)):sha(p) for p in SOURCES},**kw)
 return dict(kind='native',key=key,controller=lane,target_id='PARENT',operation=op,payload=dict(payload,source_binding=b),source_binding=b,purpose=question,estimated_memory_bytes=402653184)
SOURCES=[BASE/'TARGET.md',BASE/'RUN_POLICY.json',Path(__file__),BASE/'closure/native_v001-p4/SOURCE_RAW.json',BASE/'measurement/NATIVE_OPERANDS.json']
tasks=[]
for event,state,orientation,lane,key in [('W1+',[0,0,0],1,'G6_01','r1_forward_duration'),('W1-',[1,0,0],-1,'G6_02','r1_reverse_duration')]:
 tasks.append(task(key,'GEN5_SOURCE_STROKE_INTEGRAL',dict(precision_bits=384,data=dict(law='AN0005_J4_B1_SIGNED_WRITE_V1',state=state,event=event,orientation=orientation,clock_path='LOCAL_DENSITY_INTEGRAL')),
  'Receive the original positive-duration '+event+' source integral, preserving its signed orientation',lane,source_clock='H02/H05 original local density'))
r=json.loads((BASE/'closure/native_v001-p4/SOURCE_RAW.json').read_text());ids=r['certificate']['row_indices'];n=len(ids)
M=[[dict(re=r['evaluation_rows'][i][j],im=0) for j in range(n)] for i in ids]
tasks.append(task('r1_actual_source_rank10','GEN3_COMPLEX_SOLVE',dict(precision_bits=1024,data=dict(matrix=wire(M),rhs=wire(eye(n)))),
 'Certify the actual full-N source rank10 point minor and the two outgoing directions after seven dimensions','G6_03',profile_id=r['profile_id'],N_exact=r['N_exact'],source_minor_sha256=sha(BASE/'closure/native_v001-p4/SOURCE_RAW.json')))
m=json.loads((BASE/'measurement/NATIVE_OPERANDS.json').read_text());O=m['O']
ctx=dict(basis=['protected0','protected1','protected2'],field=dict(radicand=0),units=dict(observable='dimensionless outcomes -sqrt(2),0,sqrt(2)'),history=dict(preparation='Fresh protected-sector source preparations; destructive terminal readout'),spectral_coordinate='declared receiving observable')
tasks.append(task('r1_observable_cube','GEN3_SOURCE_OPERATOR_WORD',dict(name='r1_observable_cube',context=ctx,data=dict(operators=dict(O=O),program=[dict(name='O2',op='multiply',inputs=['O','O']),dict(name='O3',op='multiply',inputs=['O2','O'])],output='O3')),
 'Check the complete physical readout observable algebra used for bounded-outcome shot accounting','G6_04'))
plan=dict(law_namespace='SAM_land',scope='Actual spin closure and physically paid/read records',sources=[dict(path=str(p),sha256=sha(p)) for p in SOURCES],round1=tasks,
 research=dict(mode='connections',index=str(BASE/'inputs/RESEARCH_WEB.sqlite'),depth=2,max_nodes=64,max_results=8,queries=[
  dict(query='source residual invariant memory',seeds=['GEN4/voli_chapter2_continuation2_20261015/memory/DERIVATION.md'],rounds=[1]),
  dict(query='source clock signed Write reference phase',seeds=['GEN4/gen6_spin_clock_successor1_20261014/SOURCE_ACTION.md'],rounds=[1]),
  dict(query='measurement preparation timing coherence',seeds=['GEN4/voli_chapter2_physical3_20261015/measurement/DERIVATION.md'],rounds=[1]),
  dict(query='history counter apparatus work',seeds=['GEN4/voli_chapter2_continuation2_20261015/records/DERIVATION.md'],rounds=[2])]))
save(BASE/'PLAN.json',plan)
save(BASE/'NATIVE_SELECTION.json',dict(route='Qualified installed GEN6 Duck native tasks; source extension separately retained',operations=['GEN5_SOURCE_STROKE_INTEGRAL','GEN3_COMPLEX_SOLVE','GEN3_SOURCE_OPERATOR_WORD','GEN3_COMPLEX_PRODUCT'],round_seconds=[180,180],original_law_preserved=True,native_runtime_replaced=False))
print(json.dumps(dict(tasks=len(tasks),plan=str(BASE/'PLAN.json'))))
