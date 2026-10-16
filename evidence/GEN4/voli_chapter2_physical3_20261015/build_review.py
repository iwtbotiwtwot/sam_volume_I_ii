"""Complete shared R1 review and selected actual-source R2 tasks."""
from pathlib import Path
from copy import deepcopy
import hashlib,json,shutil
BASE=Path(__file__).resolve().parent;ROOT=BASE.parents[1]
RUN=ROOT/'GEN4/duck_gen6_local/runs/chapter2-physical-protocols-20261015-01'
def read(p):return json.loads(Path(p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):Path(p).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
def wire(m):return dict(entries=deepcopy(m),row_basis=list(map(str,range(len(m)))),column_basis=list(map(str,range(len(m[0])))),structure='GENERAL')
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
SOURCES=[]
def task(key,op,payload,question,lane,target,consumes,**kw):
 b=dict(campaign=BASE.name,law_namespace='SAM_land',question=question,original_law_and_clocks_preserved=True,
  source_files={str(p.relative_to(ROOT)):sha(p) for p in SOURCES},**kw)
 return dict(kind='native',key=key,controller=lane,target_id=target,operation=op,payload=dict(payload,source_binding=b),source_binding=b,
  purpose=question,estimated_memory_bytes=402653184,consumes={k:{'$result':k,'path':['key']} for k in consumes})
def word(key,ops,program,output,question,lane,target,consumes,basis):
 return task(key,'GEN3_SOURCE_OPERATOR_WORD',dict(name=key,context=dict(basis=basis,field=dict(radicand=0),
  units=dict(matrix='source-derived coefficient certificate; original physical units remain in derivation'),
  history=dict(source='Actual source, specified receiving observable or admitted signed event family; no continuum replacement'),spectral_coordinate='declared certificate basis'),
  data=dict(operators=ops,program=program,output=output)),question,lane,target,consumes)
def minor_task(key,data,lane,target,consumes):
 ids=data['certificate']['row_indices'];n=len(ids);M=[[dict(re=data['evaluation_rows'][i][j],im=0) for j in range(n)] for i in ids]
 return task(key,'GEN3_COMPLEX_SOLVE',dict(precision_bits=1024,data=dict(matrix=wire(M),rhs=wire(eye(n)))),
  'Receive the exact actual-source rank'+str(n)+' point minor into the native inverse for '+data['profile_id'],lane,target,consumes,
  profile_id=data['profile_id'],N_exact=data['N_exact'],basis=data['basis'],all_N_sites_retained=True)
def main():
 assert read(RUN/'STATUS.json')['phase']=='NARROW'
 for folder,name in [('measurement','MEASUREMENT_R2.json'),('protocol','PROTOCOL_R2.json')]:
  src=BASE/folder/('NATIVE_OPERANDS.json' if folder=='measurement' else 'NATIVE_PAYLOAD.json');shutil.copy2(src,BASE/'inputs'/name)
 deep_path=BASE/'closure/native_v001_p6/SOURCE_RAW.json'
 if not deep_path.exists():deep_path=BASE/'closure/native_v001_p5b/SOURCE_RAW.json'
 deep=read(deep_path)['profiles'][0];batch=read(BASE/'closure/native_batch_p4b/SOURCE_RAW.json')['profiles'];largest=max(batch,key=lambda x:int(x['N_exact']))
 save(BASE/'inputs/DEEP_SOURCE_R2.json',deep);save(BASE/'inputs/LARGEST_SOURCE_R2.json',largest)
 global SOURCES
 SOURCES=[BASE/'TARGET.md',BASE/'RUN_POLICY.json',Path(__file__),BASE/'inputs/MEASUREMENT_R2.json',BASE/'inputs/PROTOCOL_R2.json',BASE/'inputs/DEEP_SOURCE_R2.json',BASE/'inputs/LARGEST_SOURCE_R2.json']
 m=read(BASE/'inputs/MEASUREMENT_R2.json');H=m['improved_nominal_H3_rounded'];tasks=[]
 tasks.append(word('r2_improved_H3_word',dict(H=H,I=eye(3)),[dict(name='HI',op='multiply',inputs=['H','I'])],'HI',
  'Certify the exact rational minor for the source-selected improved cadence and its finite-shot witness','G6_05','MEASUREMENT',['r1_observable_cube','web_r1_002'],list(map(str,range(3)))))
 tasks.append(task('r2_improved_H3_inverse','GEN3_COMPLEX_SOLVE',dict(precision_bits=1024,data=dict(matrix=wire(H),rhs=wire(eye(3)))),
  'Receive the improved fixed-cadence full-rank Hankel minor into a separate native solve','G6_06','MEASUREMENT',['r1_observable_cube','web_r1_002']))
 p=read(BASE/'inputs/PROTOCOL_R2.json');p.pop('expected_matrix');p.pop('source_binding')
 tasks.append(task('r2_paid_work_coefficients','GEN3_SOURCE_OPERATOR_WORD',p,
  'Receive every switch and continuous reference-drive coefficient, retaining gross positive and negative work separately in the protocol','G6_07','PAID_REFERENCE',['r1_forward_duration','r1_reverse_duration','web_r1_001'],
  formal_work_coefficients_only=True,actual_continuum_energy_replaced=False))
 tasks.append(minor_task('r2_deep_source_inverse',deep,'G6_08','ACTUAL_CLOSURE',['r1_actual_source_rank10','web_r1_000']))
 tasks.append(minor_task('r2_largest_N_inverse',largest,'G6_09','ACTUAL_CLOSURE',['r1_actual_source_rank10','web_r1_000']))
 tasks.append(word('r2_zero_readout_projector',dict(O=m['O'],P0twice=m['P0_twice']),[dict(name='zero',op='multiply',inputs=['O','P0twice'])],'zero',
  'Verify the actual zero-outcome measurement subspace belongs to the specified bounded receiver','G6_10','MEASUREMENT',['r1_observable_cube','web_r1_002'],list(map(str,range(3)))))
 tasks.append(word('r2_min_counter_rank',dict(C=[[1,2],[3,8]],I=eye(2)),[dict(name='CI',op='multiply',inputs=['C','I'])],'CI',
  'Certify the exact rank-two history contrast that requires two linear additive counters through second moments','G6_11','COMPACT_CERTIFICATES',['web_r1_001','web_r1_000'],['S1','S2']))
 packet=read(RUN/'REVIEW_R1.json');known={
 'r1_forward_duration':'Original forward signed Write admitted and both coordinate integrals certified; complete positive source duration retained.',
 'r1_reverse_duration':'Original reverse signed Write admitted with positive duration and reversed path; this is not negative elapsed time.',
 'r1_actual_source_rank10':'Actual full-N point minor certifies the seven-coordinate residual has two outgoing directions; all54 source evaluation certificates retained separately.',
 'r1_observable_cube':'Exact receiver algebra returns O^3=2O, fixing the physical outcome range used in repeated-shot accounting.',
 'web_r1_000':'All retrieved source-memory records inspected; hidden returns, full fields and preserved backgrounds direct the actual closure calculation.',
 'web_r1_001':'All retrieved source-clock records inspected; signed Write, common phase, waiting and work accounts direct the complete reference protocol.',
 'web_r1_002':'All retrieved receiving records inspected; apparatus and calibration remain distinct from source algebra and source-cyclicity access.'}
 accounting=[]
 for x in packet['outcomes']:
  assert x['id'] in known and x['status']=='COMPLETED',x
  accounting.append(dict(id=x['id'],status=x['status'],disposition='RETAIN_AND_EXTEND',known_work=known[x['id']]))
 selected=[
  dict(id='ACTUAL_CLOSURE',from_outcome_ids=['r1_actual_source_rank10','web_r1_000'],known_work='Actual seven-coordinate residual rank two on54 original profiles; deeper full-source certificate retained.',next_question='Certify the reached higher rank and its precise nonstabilization boundary.',selection_reason='First user mathematical target.'),
  dict(id='PAID_REFERENCE',from_outcome_ids=['r1_forward_duration','r1_reverse_duration','web_r1_001'],known_work='Original forward/reverse durations and source energy bound retained; external entry/release and nonzero wait Hamiltonian explicit.',next_question='Receive every reference-work coefficient alongside phase unwrapping and gross exchanged work.',selection_reason='Complete physical protocol requested.'),
  dict(id='MEASUREMENT',from_outcome_ids=['r1_observable_cube','web_r1_002'],known_work='Fresh-copy destructive observable and explicit apparatus budget; improved source-selected cadence lowers sufficient shots.',next_question='Receive the stronger finite-record minor and zero-outcome projector algebra.',selection_reason='Turn expectations into a finite-shot measurement protocol.'),
  dict(id='COMPACT_CERTIFICATES',from_outcome_ids=['web_r1_000','web_r1_001'],known_work='Short block/memory/Gram, event-offset, counter and endpoint certificates independently derived.',next_question='Receive the actual rank-two counter contrast and place all short proofs in the chapter.',selection_reason='Make Chapter II reader-complete for the requested certificates.')]
 save(BASE/'R2_REVIEW.json',dict(selected_by='CODEX_CURRENT_SESSION',parent_retained=True,review_packet_sha256=sha(RUN/'REVIEW_R1.json'),round_one_packet_sha256=sha(RUN/'REVIEW_R1.json'),accounting=accounting,selected_targets=selected,round2=tasks,deferred_targets=[]))
 print(json.dumps(dict(outcomes=len(accounting),selected=len(selected),tasks=len(tasks),deep_rank=deep['rank_lower_bound'])))
if __name__=='__main__':main()
