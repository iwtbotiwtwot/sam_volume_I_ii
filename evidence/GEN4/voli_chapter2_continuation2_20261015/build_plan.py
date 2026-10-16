"""Assemble source-bound native tasks for the installed Duck; no mathematics runs."""
from pathlib import Path
from copy import deepcopy
from fractions import Fraction
import hashlib,json

BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[1]
def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d): Path(p).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
def wire(m):
    return dict(entries=deepcopy(m),row_basis=[str(i) for i in range(len(m))],
        column_basis=[str(i) for i in range(len(m[0]))],structure='GENERAL')
def integer_matrix(m):
    rows=[]
    for row in m['entries']:
        result=[]
        for x in row:
            assert x['im']==dict(lower='0',upper='0') and x['re']['lower']==x['re']['upper']
            f=Fraction(x['re']['lower']); assert f.denominator==1
            result.append(int(f))
        rows.append(result)
    return rows

def binding(question,**kw):
    return dict(campaign=BASE.name,law_namespace='SAM_land',question=question,
        construction_author='Codex; installed GEN6 Duck execution',
        parent='H002634 Chapter II source-bound development',
        original_law_and_clocks_preserved=True,physical_epsilon='symbolic, not fitted',
        signed_response='Original K_response in Q=T+g_H K_response',
        source_files={str(p.relative_to(ROOT)):digest(p) for p in SOURCES},**kw)

def task(key,operation,payload,question,lane,**extra):
    b=binding(question,**extra);payload=dict(payload,source_binding=b)
    return dict(kind='native',key=key,controller=lane,target_id='PARENT',
        operation=operation,payload=payload,source_binding=b,purpose=question,
        estimated_memory_bytes=402653184)

source=ROOT/'GEN4/duck_chapter1_lane1_20261015/sources/EXACT_INPUTS.json'
SOURCES=[source,BASE/'TARGET.md',BASE/'RUN_POLICY.json',Path(__file__).resolve(),
    ROOT/'GEN4/voli_chapter2_bridge1/comparison/DERIVATION.md',
    ROOT/'GEN4/voli_chapter2_bridge1/MEMORY_DERIVATION.md',
    BASE/'memory/SOURCE_OPERANDS.json']
raw=json.loads(source.read_text());T=integer_matrix(raw['T']);K=integer_matrix(raw['K'])
tasks=[]
for index,g in enumerate([0,1,2],1):
    Q=[[T[i][j]+g*K[i][j] for j in range(4)] for i in range(4)]
    context=dict(basis=['p0','p1','p2','p3'],field=dict(radicand=0),
        units=dict(Q='original dimensionless source; physical epsilon separate'),
        history=dict(source='Original placement basis and signed response',g_H=g),
        spectral_coordinate='q')
    tasks.append(task('r1_cyclic_g'+str(g),'GEN3_SOURCE_SUBSPACE',
        dict(name='chapter2_endpoint_cyclic_g'+str(g),context=context,
             data=dict(H=Q,seeds=[[0],[1],[0],[0]],mode='CLOSURE')),
        'Determine the exact source modes reached from endpoint placement p1 at diagnostic g_H='+str(g),
        'G6_%02d'%index,diagnostic_g_H=g,physical_calibration_claimed=False))
mem=json.loads((BASE/'memory/SOURCE_OPERANDS.json').read_text())
p=next((p for p in mem['profiles'] if p.get('id')=='V000_BASE'),mem['profiles'][0])
U=p['U'];W=p['W']
tasks.append(task('r1_memory_Usolve','GEN3_COMPLEX_SOLVE',
    dict(precision_bits=1024,data=dict(matrix=wire(U),rhs=wire([[W[0][0]],[W[1][0]]]))),
    'Receive the completed original spin U and W columns for the exact b5 memory residual; no source reintegration',
    'G6_04',spin_profile=p.get('id',p.get('profile')),spin_basis='b5=(d,e,u_d,u_e,w_d)'))
plan=dict(law_namespace='SAM_land',scope='Chapter II signature -> memory -> paid Write clock; active breadcrumb exploration',
    sources=[dict(path=str(p),sha256=digest(p)) for p in SOURCES],round1=tasks,
    research=dict(mode='connections',index=str(BASE/'inputs/RESEARCH_WEB.sqlite'),
        depth=2,max_nodes=64,max_results=8,queries=[
            dict(query='coherence source clock',seeds=['GEN4/voli_chapter2_bridge1/comparison/DERIVATION.md'],rounds=[1]),
            dict(query='source action residual',seeds=['GEN4/duck_spin_upper1_20261014/REPORT.md'],rounds=[1]),
            dict(query='phase history reference',seeds=['GEN4/voli_chapter2_bridge1/bridge/DERIVATION.md'],rounds=[1]),
            dict(query='memory retained source',seeds=['GEN4/voli_chapter2_bridge1/MEMORY_DERIVATION.md'],rounds=[2])]))
save(BASE/'PLAN.json',plan)
save(BASE/'NATIVE_SELECTION.json',dict(route='Installed Duck native tasks through DomainSession',
    operations=['GEN3_SOURCE_SUBSPACE','GEN3_COMPLEX_SOLVE','GEN3_COMPLEX_PRODUCT','GEN3_COMPLEX_RANK'],
    discovery='Current dynamic254-operation capability catalogue; SOURCE_OPERATORS.md and MODULAR.md',
    mathematical_roles='Exact cyclicity, original-source residual contraction, robust finite-record and controlled-reference checks',
    round_seconds=[180,180],native_runtime_replaced=False))
print(json.dumps(dict(plan=str(BASE/'PLAN.json'),tasks=len(tasks),source_count=len(SOURCES))))
