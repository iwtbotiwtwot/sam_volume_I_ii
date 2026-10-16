"""Choose installed native capabilities for retained source-to-field operands."""
from pathlib import Path
from copy import deepcopy
import json,hashlib
BASE=Path(__file__).resolve().parent;ROOT=BASE.parents[1]
def read(p):return json.loads(Path(p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):Path(p).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
def wire(a):return dict(entries=a,row_basis=list(map(str,range(len(a)))),column_basis=list(map(str,range(len(a[0])))),structure='GENERAL')
def wrap(t,lane):
 t=deepcopy(t);t.pop('expected_matrix',None);t.pop('expected_blocks',None);t.setdefault('source_binding',deepcopy(t['payload'].get('source_binding',{})));t.setdefault('key',t['payload'].get('name',''));t.setdefault('purpose',t['source_binding'].get('question','Exact interacting source clock coupling certificate'));t.update(kind='native',controller=lane,target_id='PARENT',estimated_memory_bytes=402653184)
 b=t['source_binding'];b.update(law_namespace='SAM_land',parent='Chapter III localized source and finite receiving field',campaign=BASE.name)
 if 'clock' in t['key'] or 'scaling' in t['key']:
  b.setdefault('source_files',{})[str((BASE/'clock/chapter1_certificate.json').relative_to(ROOT))]=sha(BASE/'clock/chapter1_certificate.json')
  if 'derivation_sha256' in b:
   old=BASE/'clock/DERIVATION_R1.md';assert sha(old)==b['derivation_sha256'];b['derivation_source_path']=str(old.relative_to(ROOT));b['source_files'][str(old.relative_to(ROOT))]=sha(old)
 b.setdefault('source_files',{}).update({str(p.relative_to(ROOT)):sha(p) for p in [BASE/'TARGET.md',BASE/'RUN_POLICY.json']})
 t['payload']['source_binding']=deepcopy(b)
 return t

def main():
 tasks=[]
 for i,t in enumerate(read(BASE/'source/DUCK_R1_TASKS.json')):tasks.append(wrap(t,'G6_'+str(i+1).zfill(2)))
 f=read(BASE/'radial/FIXTURE.json');b=f['source_binding'];b['source_files'][str((BASE/'radial/FIXTURE.json').relative_to(ROOT))]=sha(BASE/'radial/FIXTURE.json')
 t=dict(key='r1_radial_green_inverse',operation='GEN3_COMPLEX_SOLVE',payload=dict(precision_bits=384,data=dict(matrix=wire(f['K']),rhs=wire([[int(i==j) for j in range(f['n'])] for i in range(f['n'])]))),source_binding=b,purpose='Receive the exact finite shell stiffness inverse and compare to H_ij=1/max(i,j)-1/L')
 tasks.append(wrap(t,'G6_03'))
 ct=read(BASE/'clock/DUCK_R1_TASKS.json')['tasks']
 for i,t in enumerate(ct):tasks.append(wrap(t,'G6_'+str(i+4).zfill(2)))
 uniform=read(BASE/'source/DUCK_UNIFORM_RESPONSE_TASK.json');uniform.pop('expected',None);tasks.append(wrap(uniform,'G6_06'))
 queries=[
 dict(query='positive source energy spatial shell density',seeds=['GEN4/volii_duck_expansion2/REPORT.md','GEN4/native_energy_source1/RESULT.md'],rounds=[1]),
 dict(query='radial Laplacian conductance source continuum',seeds=['GEN4/native_energy_source1/RESULT.md','manuscripts/volume_I/02_spherical_sources/DERIVATIONS.md'],rounds=[1]),
 dict(query='interacting source clock common energy coupling',seeds=['GEN4/voli_chapter2_physical3_20261015/REPORT.md','GEN4/native_coupling_scale1/REPORT.md'],rounds=[1]),
 dict(query='source spatial response memory clock road',seeds=['GEN4/source_spatial_response1/REPORT.md','GEN4/joint_source_clock_road1/REPORT.md'],rounds=[2])]
 sources=[BASE/'TARGET.md',BASE/'RUN_POLICY.json',BASE/'source/EXACT_INPUTS.json',BASE/'radial/FIXTURE.json',BASE/'clock/DUCK_R1_TASKS.json']
 plan=dict(law_namespace='SAM_land',scope='Chapter III retained source-energy map, finite static receiving field and actual clock response',sources=[dict(path=str(p),sha256=sha(p)) for p in sources],round1=tasks,research=dict(mode='connections',index=str(BASE/'inputs/RESEARCH_WEB.sqlite'),depth=2,max_nodes=48,max_results=6,queries=queries))
 save(BASE/'PLAN.json',plan)
 save(BASE/'NATIVE_SELECTION.json',dict(operations=sorted(set(t['operation'] for t in tasks)),generation=read(BASE/'inputs/CAPABILITIES.json')['generation'],duck_version=read(BASE/'inputs/DUCK_CAPABILITIES.json')['controller_version'],core=read(BASE/'inputs/DUCK_CAPABILITIES.json')['core']['version'],round_seconds=[180,180],route='Installed GEN6 Duck Connections; analytic derivations and explicitly independent Fraction readback accompany source-bound native execution',source_semantics_preserved=True,no_new_runtime=True))
 print(json.dumps(dict(tasks=len(tasks),keys=[t['key'] for t in tasks])))
if __name__=='__main__':main()
