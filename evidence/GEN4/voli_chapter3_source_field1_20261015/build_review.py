"""Complete shared R1 scientific review and retained source-bound R2 tasks."""
from pathlib import Path
from copy import deepcopy
import json,hashlib
BASE=Path(__file__).resolve().parent;ROOT=BASE.parents[1]
RUN=ROOT/'GEN4/duck_gen6_local/runs/chapter3-source-field-20261015-03'
def read(p):return json.loads(Path(p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):Path(p).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
def wire(a):return dict(entries=deepcopy(a),row_basis=list(map(str,range(len(a)))),column_basis=list(map(str,range(len(a[0])))),structure='GENERAL')
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def task(key,op,payload,question,lane,target,consumes,files):
 p=deepcopy(payload);b=p.get('source_binding',{});b.update(campaign=BASE.name,law_namespace='SAM_land',question=question,source_files={**b.get('source_files',{}),**{str(f.relative_to(ROOT)):sha(f) for f in files+[BASE/'TARGET.md',BASE/'RUN_POLICY.json',Path(__file__)]}});p['source_binding']=deepcopy(b)
 return dict(kind='native',key=key,controller=lane,target_id=target,operation=op,payload=p,source_binding=b,purpose=question,estimated_memory_bytes=268435456,consumes={k:{'$result':k,'path':['key']} for k in consumes})
def main():
 assert read(RUN/'STATUS.json')['phase']=='NARROW'
 packet=read(RUN/'REVIEW_R1.json');accounting=[]
 known={
 'r1_si29_outgoing_flatness':'Actual all-eight outgoing Gram sums return zero residual, fixing each scalar outgoing energy share without discarding species/coherence.',
 'r1_si29_incoming_flatness':'Actual all-eight incoming occupation sums return zero residual; together these establish E_x=H0/8 in the orthonormal source.',
 'r1_radial_green_inverse':'Installed inverse receives the retained finite c_i=i(i+1) source operator; analytic Green, flux and boundary correction are independently derived.',
 'chapter3_full_source_clock_energy_commutators':'Complete sixteen-state source certifies bare current commutator and invisible even/counterterm energy, preserving full-source roles.',
 'chapter3_full_scaling_epsilon_only_residual':'Exact four-term coefficient residual is (0,1/2,0,-1/2), distinguishing complete-H scaling from epsilon-only coupling.',
 'r1_si29_uniform_coupling_response':'Actual eight-coordinate source and physical Gram distinguish positive excitation energy from signed generator; the declared uniform H0 coupling leaves sector-contrast history unchanged.',
 'web_r1_000':'All actual retrieved source/energy excerpts inspected; source location and phase/reference semantics feed finite graph and localized density constructions.',
 'web_r1_001':'All six radial/continuum excerpts inspected; retained conductance and finite-boundary account feed exact field/energy identities. The positive-field receiving sector is recorded as the next localization lead.',
 'web_r1_002':'All actual clock/coupling excerpts inspected; complete generator, time reference and source memory feed the six-lane operational response/precision test.'}
 for row in packet['outcomes']:
  assert row['id'] in known,row['id'];assert row['status']=='COMPLETED',row
  accounting.append(dict(id=row['id'],status=row['status'],disposition='RETAIN_AND_EXTEND',known_work=known[row['id']]))
 tasks=[]
 radial=read(BASE/'radial/DUCK_R2_TASKS.json')[0]
 tasks.append(task('r2_radial_flux_energy_word','GEN3_SOURCE_OPERATOR_WORD',radial['payload'],'Certify incidence/Green/energy identities B^TCB=K, KH=I, HKH=H for the original finite radial receiving law','G6_01','FINITE_FIELD',['r1_radial_green_inverse','web_r1_001'],[BASE/'radial/FIXTURE.json',BASE/'radial/DUCK_R2_TASKS.json']))
 q=read(BASE/'energy/DUCK_R2_TASKS.json')[0]['payload']
 tasks.append(task('r2_quadrupole_matching','GEN3_COMPLEX_SOLVE',dict(precision_bits=384,data=dict(matrix=wire(q['matrix']),rhs=wire([[x] for x in q['observed']]))),'Receive static positive quadrupole free-energy density into its exact Poisson/matching coefficients, retaining exterior source tail and full-account distinction','G6_02','FIELD_ENERGY',['r1_radial_green_inverse','web_r1_000','web_r1_001'],[BASE/'energy/DUCK_R2_TASKS.json',BASE/'energy/CHAPTER_I_MODEL_SOURCE.md',BASE/'energy/FIELD_SOURCE_RESULTS.json']))
 c=read(BASE/'clock/DUCK_R2_TASKS.json')['tasks'][0]
 tasks.append(task('r2_clock_phase_ratios','GEN3_COMPLEX_SOLVE',c['payload'],'Receive all six actual lower/upper phase-rate ratios used in the explicit source-only lift precision criterion','G6_03','CLOCK_RESPONSE',['chapter3_full_source_clock_energy_commutators','chapter3_full_scaling_epsilon_only_residual','r1_si29_uniform_coupling_response','web_r1_002'],[BASE/'clock/RESULTS.json',BASE/'clock/DUCK_R2_TASKS.json',BASE/'clock/chapter1_certificate.json']))
 f=read(BASE/'source/CUBE_GRAPH.json')
 tasks.append(task('r2_cube_rank7_minor_inverse','GEN3_COMPLEX_SOLVE',dict(precision_bits=384,data=dict(matrix=wire(f['minor']),rhs=wire(eye(7)))),'Certify rank seven of the declared closed cube Laplacian with the exact constant null mode retained','G6_04','SOURCE_DENSITY',['r1_si29_outgoing_flatness','r1_si29_incoming_flatness','web_r1_000'],[BASE/'source/CUBE_GRAPH.json']))
 payload=dict(name='r2_cube_zero_mode',context=dict(basis=list(map(str,range(8))),field=dict(radicand=0),units=dict(matrix='declared closed graph conductance'),history=dict(source='Explicit cube embedding; no exterior field discarded'),spectral_coordinate='constant energy-profile mode'),data=dict(operators=dict(L=f['L'],P=f['P']),program=[dict(name='LP',op='multiply',inputs=['L','P'])],output='LP'))
 tasks.append(task('r2_cube_zero_mode','GEN3_SOURCE_OPERATOR_WORD',payload,'Certify that the actual flat source profile lies on the constant closed-graph mode, making an exterior flux account explicit','G6_05','SOURCE_DENSITY',['r1_si29_outgoing_flatness','r1_si29_incoming_flatness','r1_si29_uniform_coupling_response','web_r1_000'],[BASE/'source/CUBE_GRAPH.json']))
 selected=[
 dict(id='SOURCE_DENSITY',from_outcome_ids=['r1_si29_outgoing_flatness','r1_si29_incoming_flatness','r1_si29_uniform_coupling_response','web_r1_000'],known_work='Actual scalar energy fractions are fixed at1/8; explicit finite cube embedding, smoothing and physical coupling retain their assignments.',next_question='Determine exact finite-graph receiving constraint and preserve source-shape and mass/reference information.',selection_reason='First recommended physical source-to-density interface.'),
 dict(id='FINITE_FIELD',from_outcome_ids=['r1_radial_green_inverse','web_r1_001'],known_work='Retained radial source operator has exact analytic inverse and source flux, including finite outer reference.',next_question='Receive its incidence/energy identities and place the full finite example and continuum/boundary bounds in the chapter.',selection_reason='Complete source→field→flux chain.'),
 dict(id='FIELD_ENERGY',from_outcome_ids=['r1_radial_green_inverse','web_r1_000'],known_work='Static source functional and pair force proofs are explicit; actual Chapter I positive free-field sector gives an extended density/tail. The returned positive-field receiving modes remain an explicit additional localization lead.',next_question='Receive exact source-Poisson matching for that sector and preserve its interaction/counterterm completion.',selection_reason='One shared energy/force account and a concrete Chapter I continuation.'),
 dict(id='CLOCK_RESPONSE',from_outcome_ids=['chapter3_full_source_clock_energy_commutators','chapter3_full_scaling_epsilon_only_residual','r1_si29_uniform_coupling_response','web_r1_002'],known_work='Complete-H and epsilon-only couplings have distinct exact responses; actual Si29 population clock provides an additional source-bound control.',next_question='Receive actual six-lane phase precision ratios and state a common perturbation/measurement specification.',selection_reason='Evaluate the proposed coupling and preserve actual phase/energy roles.')]
 save(BASE/'R2_REVIEW.json',dict(selected_by='CODEX_CURRENT_SESSION',parent_retained=True,review_packet_sha256=sha(RUN/'REVIEW_R1.json'),round_one_packet_sha256=sha(RUN/'REVIEW_R1.json'),accounting=accounting,selected_targets=selected,round2=tasks,deferred_targets=[]))
 print(json.dumps(dict(outcomes=len(accounting),selected=len(selected),tasks=len(tasks))))
if __name__=='__main__':main()
