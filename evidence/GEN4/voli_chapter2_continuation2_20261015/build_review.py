"""Codex's complete R1 accounting and selected source-bound R2 tasks."""
from pathlib import Path
from copy import deepcopy
import json,hashlib,shutil
BASE=Path(__file__).resolve().parent;ROOT=BASE.parents[1]
RUN=ROOT/'GEN4/duck_gen6_local/runs/chapter2-signature-memory-20261015-01'
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):Path(p).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
def wire(m):return dict(entries=deepcopy(m),row_basis=list(map(str,range(len(m)))),column_basis=list(map(str,range(len(m[0])))),structure='GENERAL')
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def binding(question,**kw):
    files=[BASE/'TARGET.md',BASE/'RUN_POLICY.json',Path(__file__),BASE/'inputs/SIGNATURE_OPERANDS_R2.json',BASE/'memory/SOURCE_OPERANDS.json']
    return dict(campaign=BASE.name,law_namespace='SAM_land',question=question,
        physical_scope='Model predictions; diagnostic calibration and declared receiving controls; no measured SI assignment',
        source_files={str(p.relative_to(ROOT)):digest(p) for p in files},**kw)
def task(key,op,payload,question,lane,target,consumes=None,**kw):
    b=binding(question,**kw)
    t=dict(kind='native',key=key,controller=lane,target_id=target,operation=op,
        payload=dict(payload,source_binding=b),source_binding=b,purpose=question,
        estimated_memory_bytes=402653184)
    if consumes:t['consumes']={x:{'$result':x,'path':['key']} for x in consumes}
    return t
def exact_rank(key,M,lane,target,question,consumes):
    n=len(M);context=dict(basis=list(range(n)),field=dict(radicand=0),units=dict(matrix='exact bound source or receiving coefficient'),
        history=dict(source='Current R1 breadcrumb and authenticated rational operands'),spectral_coordinate='retained source/readout')
    return task(key,'GEN3_SOURCE_OPERATOR_WORD',dict(name=key,context=context,
        data=dict(operators=dict(M=M,I=eye(n)),program=[dict(name='checked_product',op='multiply',inputs=['M','I'])],output='checked_product')),
        question,lane,target,consumes)

packet_path=RUN/'REVIEW_R1.json'
packet=json.loads(packet_path.read_text())
assert json.loads((RUN/'STATUS.json').read_text())['phase']=='NARROW'
shutil.copy2(BASE/'signature/NATIVE_OPERANDS.json',BASE/'inputs/SIGNATURE_OPERANDS_R2.json')
s=json.loads((BASE/'inputs/SIGNATURE_OPERANDS_R2.json').read_text())
tasks=[]
tasks.append(exact_rank('r2_finite_record_rank',s['H3'],'G6_05','FINITE_RECORD',
    'Check the exact nonzero3x3 Hankel minor of the source-calibrated eight-sample protected coherence record', ['web_r1_000','r1_cyclic_g1']))
tasks.append(exact_rank('r2_TLS_control_rank',s['H4_TLS_control'],'G6_06','FINITE_RECORD',
    'Keep an exact autonomous two-level difference-Hankel control of rank two beside the source record', ['web_r1_000']))
tasks.append(task('r2_H3_inverse','GEN3_COMPLEX_SOLVE',dict(precision_bits=1024,data=dict(matrix=wire(s['H3']),rhs=wire(eye(3)))),
    'Receive the exact calibrated Hankel minor into the installed native inverse as a separate finite-record certificate',
    'G6_07','FINITE_RECORD',['r1_cyclic_g1','web_r1_000']))
for placement,lane in [(0,'G6_08'),(1,'G6_09')]:
    question='Inspect original placement'+str(placement)+' at the newly derived exceptional coupling g_H=1/164'
    context=dict(basis=['p0','p1','p2','p3'],field=dict(radicand=0),units=dict(Q='original dimensionless source'),
        history=dict(g_H='1/164',placement=placement,origin='R1 cyclicity breadcrumb'),spectral_coordinate='q')
    tasks.append(task('r2_blind_placement'+str(placement),'GEN3_SOURCE_SUBSPACE',
        dict(name='r2_blind_placement'+str(placement),context=context,data=dict(H=s['Q_placement0_blind'],
            seeds=[[int(i==placement)] for i in range(4)],mode='CLOSURE')),
        question,lane,'PARENT' if placement==0 else 'SOURCE_ACCESS',['r1_cyclic_g0','r1_cyclic_g1','r1_cyclic_g2']))
mem=json.loads((BASE/'memory/SOURCE_OPERANDS.json').read_text());ps=mem['profiles'];n=len(ps)
U=[[0]*(2*n) for _ in range(2*n)];W=[[0]*n for _ in range(2*n)];WT=[[0]*(2*n) for _ in range(n)]
for k,p in enumerate(ps):
    for i in range(2):
        for j in range(2):U[2*k+i][2*k+j]=p['U'][i][j]
        W[2*k+i][k]=p['W'][i][0];WT[k][2*k+i]=p['W'][i][0]
tasks.append(task('r2_all54_memory_Usolve','GEN3_COMPLEX_SOLVE',
    dict(precision_bits=1024,data=dict(matrix=wire(U),rhs=wire(W))),
    'Receive all54 completed original spin U/W source blocks for the rank-two initial-memory contraction; no reintegration',
    'G6_10','MEMORY_RANK_TWO',['r1_memory_Usolve','web_r1_001'],
    profiles=[p['profile_id'] for p in ps],source_span='b5',spin_parameters_and_clock='original N,gamma retained'))
pending=task('r2_all54_memory_payment','GEN3_COMPLEX_PRODUCT',
    dict(precision_bits=1024,data=dict(matrix=wire(WT),right={'$result':'r2_all54_memory_Usolve','path':['returned','result','output','matrix']})),
    'Contract the actual all54 native Usolve returns into the original b5 source-action/memory payment',
    'G6_10','MEMORY_RANK_TWO',['r2_all54_memory_Usolve','web_r1_001'])
save(BASE/'PENDING_MEMORY_TASK.json',pending)
shutil.copy2(BASE/'instrument/NATIVE_OPERANDS.json',BASE/'inputs/INSTRUMENT_OPERANDS_R2.json')
shutil.copy2(BASE/'records/NATIVE_OPERANDS.json',BASE/'inputs/RECORD_OPERANDS_R2.json')
ins=json.loads((BASE/'inputs/INSTRUMENT_OPERANDS_R2.json').read_text())
ctx=dict(basis=list(range(4)),field=dict(radicand=0),units=dict(energy='declared finite reference-apparatus diagnostic'),
    history=dict(receiving_status='Finite controlled fixture, not original continuum preparation or physical source assignment'),spectral_coordinate='source plus reference')
ops=dict(Hs=ins['fixture_H_source'],Hr=ins['fixture_H_reference_inverse_write'],
    rs=ins['fixture_density_source'],rr=ins['fixture_density_reference_balanced'],I2=ins['I2'])
program=[dict(name='HsI',op='tensor',inputs=['Hs','I2']),dict(name='IHr',op='tensor',inputs=['I2','Hr']),
    dict(name='Htot',op='add',inputs=['HsI','IHr']),dict(name='rho',op='tensor',inputs=['rs','rr']),
    dict(name='rhoH',op='multiply',inputs=['rho','Htot'])]
tasks.append(task('r2_reference_paid_inverse','GEN3_SOURCE_OPERATOR_WORD',dict(name='r2_reference_paid_inverse',context=ctx,
    data=dict(operators=ops,program=program,output='rhoH')),
    'Receive the explicitly driven reference-apparatus inverse-stroke energy balance; trace is the signed ledger rate',
    'G6_11','PAID_WRITE_CLOCK',['web_r1_000','web_r1_002'],
    declared_fixture=True,original_continuum_energy_assigned=False,operand_sha256=digest(BASE/'inputs/INSTRUMENT_OPERANDS_R2.json')))
rec=json.loads((BASE/'inputs/RECORD_OPERANDS_R2.json').read_text());D=rec['D_endpoint_displacements_18x15'];B=rec['B18_literal']
DT=[list(row) for row in zip(*D)]
tasks.append(task('r2_record_BD','GEN3_COMPLEX_PRODUCT',dict(precision_bits=1024,data=dict(matrix=wire(B),right=wire(D))),
    'Pay all15 actual original-source endpoint displacements using the complete inherited literal B18 energy operator',
    'G6_12','RECORD_ENERGY',['web_r1_002'],operand_sha256=digest(BASE/'inputs/RECORD_OPERANDS_R2.json')))
pending_record=task('r2_record_contact_Gram','GEN3_COMPLEX_PRODUCT',dict(precision_bits=1024,data=dict(matrix=wire(DT),
    right={'$result':'r2_record_BD','path':['returned','result','output','matrix']})),
    'Receive the actual current native energy displacement return into the full endpoint contact Gram',
    'G6_12','RECORD_ENERGY',['r2_record_BD','web_r1_002'])
save(BASE/'PENDING_RECORD_TASK.json',pending_record)

known={
 'r1_cyclic_g0':'Endpoint placement1 reaches all4 source modes at g_H=0; exact invariant growth1,2,3,4.',
 'r1_cyclic_g1':'Endpoint placement1 reaches all4 source modes at g_H=1; exact source basis and zero leakage retained.',
 'r1_cyclic_g2':'Endpoint placement1 reaches all4 source modes at g_H=2; motivates analytic all-g endpoint access and exceptional interior placement search.',
 'r1_memory_Usolve':'Native original R015_BASE Usolve completed. Profile metadata was null due to an id-field lookup; literal payload and SOURCE_OPERANDS identify R015_BASE unambiguously. All54 R2 tasks correct the explicit profile label.',
 'web_r1_000':'Eight source-linked records inspected; original action-learning/source-action constructions preserve signed phase, positive reverse duration and paid reference.',
 'web_r1_001':'Eight records inspected; completed J21/F11/T5 source-action remainder supplies actual b5/b6 residuals and two-dimensional initial memory.',
 'web_r1_002':'Eight records inspected; complete history work and moving-reference accounts supply useful source and endpoint-work analogues; numerical receiving application retained separately.'}
account=[]
for o in packet['outcomes']:
    k=o['id'];assert k in known
    account.append(dict(id=k,status=o.get('status'),disposition='RETAIN_AND_EXTEND' if not k.endswith('002') else 'RETAIN_SOURCE_CONNECTIONS',known_work=known[k]))
selected=[
 dict(id='FINITE_RECORD',from_outcome_ids=['r1_cyclic_g1','web_r1_000'],known_work='Protected ratio and source eigenmodes retained; exact rational source-bound sample packet developed during R1.',next_question='Does a finite noisy record select the multilevel protected signal under independently fixed calibration?',selection_reason='General signature becomes an explicit finite receiving test.'),
 dict(id='SOURCE_ACCESS',from_outcome_ids=['r1_cyclic_g0','r1_cyclic_g1','r1_cyclic_g2'],known_work='Endpoint is cyclic at all three tested couplings; analytic continuation locates a different interior-placement blind point.',next_question='What source access changes at g_H=1/164 for placement0 versus endpoint1?',selection_reason='A useful exception directs the physical receiving preparation.'),
 dict(id='MEMORY_RANK_TWO',from_outcome_ids=['r1_memory_Usolve','web_r1_001'],known_work='Completed actual source contractions supply two nonzero unresolved directions.',next_question='Receive all54 source payments and quantify the exact minimum invariant extension.',selection_reason='Connect existing spin residuals to dynamical memory without another source integration.'),
 dict(id='PAID_WRITE_CLOCK',from_outcome_ids=['web_r1_000','web_r1_002'],known_work='Original source action and reverse-path timing located; explicit controlled reference construction is being derived.',next_question='Join legal signed role strokes to positive actualclock intervals with complete reference work.',selection_reason='Closes the concrete receiving construction selected after the two theorem developments.'),
 dict(id='RECORD_ENERGY',from_outcome_ids=['web_r1_002'],known_work='Complete source-history work retains all reference/endpoints; original B18 source displacements are available.',next_question='Compute the complete actual endpoint Gram and physical-feasible record payment beside its ambient bound.',selection_reason='Connects the operational record to its complete source energy.')]
review=dict(selected_by='CODEX_CURRENT_SESSION',parent_retained=True,
    review_packet_sha256=digest(packet_path),round_one_packet_sha256=digest(packet_path),accounting=account,
    selected_targets=selected,round2=tasks,deferred_targets=[])
save(BASE/'R2_REVIEW.json',review)
save(BASE/'R1_SOURCE_METADATA_CLARIFICATION.json',dict(task='r1_memory_Usolve',actual_profile='R015_BASE',
    field_issue='Source binding spin_profile is null because extractor used id/profile rather than profile_id',
    scientific_operands_unchanged=True,source_operands_sha256=digest(BASE/'memory/SOURCE_OPERANDS.json'),
    correction='R2 binds each original profile_id explicitly; no original result is edited or replayed'))
print(json.dumps(dict(outcomes=len(account),selected=len(selected),tasks=len(tasks),pending='PENDING_MEMORY_TASK.json')))
