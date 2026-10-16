#!/usr/bin/env python3
"""Portable independent readback of the Chapter III Duck native returns.

No engine, worker or network call is made. Source operands are reconstructed
from the frozen scientific fixtures. Fraction algebra checks complete native
word outputs; exact elimination and rational interval products check certified
solves. Retained helper paths are accepted only through both custody manifests.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import argparse
import hashlib
import json

BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[1]
DEFAULT_RUN=ROOT/'GEN4/duck_gen6_local/runs/chapter3-source-field-20261015-03'


def read(p):return json.loads(Path(p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def matrix(a):return [[scalar(v) for v in r] for r in a]
def scalar(v):
    if isinstance(v,dict):
        if 're' in v and 'im' in v:
            if F(v['im'])!=0:raise ValueError('This campaign uses exact real source operands')
            return F(v['re'])
        raise ValueError('An uncertain operand needs a separately defined source certificate')
    if isinstance(v,float):raise ValueError('Machine float is not an exact source operand')
    return F(v)
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def zeros(n,m=None):return [[F(0)]*(n if m is None else m) for _ in range(n)]
def diag(v):return [[F(x) if i==j else F(0) for j in range(len(v))] for i,x in enumerate(v)]
def scale(a,s):return [[F(s)*v for v in r] for r in a]
def add(a,b):
    if len(a)!=len(b) or any(len(r)!=len(s) for r,s in zip(a,b)):raise ValueError('Addition shape')
    return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def sub(a,b):return add(a,scale(b,-1))
def transpose(a):return [list(c) for c in zip(*a)]
def mul(a,b):
    if not a or not b or len(a[0])!=len(b):raise ValueError('Product shape')
    return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def tensor(a,b):return [[x*y for x in r for y in s] for r in a for s in b]
def block(*arrays):
    out=zeros(sum(len(a) for a in arrays));off=0
    for a in arrays:
        for i,r in enumerate(a):out[off+i][off:off+len(r)]=r
        off+=len(a)
    return out
def rank(a):
    a=[r[:] for r in a];i=0
    for j in range(len(a[0]) if a else 0):
        p=next((k for k in range(i,len(a)) if a[k][j]),None)
        if p is None:continue
        a[i],a[p]=a[p],a[i];v=a[i][j];a[i]=[x/v for x in a[i]]
        for k in range(i+1,len(a)):
            v=a[k][j];a[k]=[x-v*y for x,y in zip(a[k],a[i])]
        i+=1
        if i==len(a):break
    return i
def solve(a,b):
    n=len(a)
    if any(len(r)!=n for r in a) or len(b)!=n:raise ValueError('Solve shape')
    aug=[r[:]+s[:] for r,s in zip(a,b)]
    for j in range(n):
        p=next((i for i in range(j,n) if aug[i][j]),None)
        if p is None:raise ValueError('Exact singular matrix')
        aug[j],aug[p]=aug[p],aug[j];v=aug[j][j];aug[j]=[x/v for x in aug[j]]
        for i in range(n):
            if i!=j:
                v=aug[i][j];aug[i]=[x-v*y for x,y in zip(aug[i],aug[j])]
    return [r[n:] for r in aug]


class Checks:
    def __init__(self):self.labels=[];self.entries=0
    def ok(self,label,condition):
        if not condition:raise AssertionError(label)
        self.labels.append(label)
    def same(self,label,a,b):
        self.ok(label+'_shape',len(a)==len(b) and all(len(r)==len(s) for r,s in zip(a,b)))
        for i,(r,s) in enumerate(zip(a,b)):
            for j,(x,y) in enumerate(zip(r,s)):
                self.ok(label+'_%d_%d'%(i,j),x==y);self.entries+=1


def word(data):
    """Small independent rational evaluator; no installed operator implementation."""
    env={k:matrix(v) for k,v in data['operators'].items()}
    for step in data['program']:
        args=[env[k] for k in step['inputs']];op=step['op']
        if step['name'] in env:raise ValueError('Word overwrites an operand')
        if op=='add':
            ans=args[0]
            for a in args[1:]:ans=add(ans,a)
        elif op in ('multiply','tensor','subtract','commutator'):
            if len(args)!=2:raise ValueError('Binary operation arity')
            if op=='commutator':ans=sub(mul(args[0],args[1]),mul(args[1],args[0]))
            else:ans={'multiply':mul,'tensor':tensor,'subtract':sub}[op](*args)
        elif op in ('transpose','adjoint'):
            if len(args)!=1:raise ValueError('Transpose arity')
            ans=transpose(args[0])
        elif op=='scale':
            if len(args)!=1:raise ValueError('Scale arity')
            ans=scale(args[0],scalar(step['factor']))
        else:raise ValueError('Unsupported independent word operation: '+op)
        env[step['name']]=ans
    return env[data['output']]


class Receipts:
    def __init__(self,run,checks):
        self.run=run;self.c=checks;self.rows=[];self.helper_rows=[]
        self.config=read(run/'CONFIG.json')
        self.oldroot=Path(self.config['prepared_run']).parents[3]
        self.c.ok('run_name_matches_prepared_run',Path(self.config['prepared_run']).name==run.name)
        self.custody=None

    def mapped_source(self,path):
        p=Path(path)
        rel=p.relative_to(self.oldroot) if p.is_absolute() else p
        self.c.ok('safe_literal_source_'+p.name,not rel.is_absolute() and '..' not in rel.parts)
        mapped=ROOT/rel
        self.c.ok('source_stays_in_portable_root_'+p.name,mapped.resolve().is_relative_to(ROOT.resolve()))
        return mapped

    def kept_helper(self,pointer,digest):
        if self.custody is None:
            cp=self.run/'helper_custody/RAM_CUSTODY.json';hp=self.run/'HELPER_READBACK.json'
            custody,helper=read(cp),read(hp)
            cm={r['path']:r for r in custody['files']};hm={r['path']:r for r in helper['files']}
            self.c.ok('custody_manifests_PASS',custody['status']==helper['status']=='PASS')
            self.c.ok('custody_manifest_digest',hm['RAM_CUSTODY.json']['sha256']==sha(cp))
            self.c.ok('custody_manifest_unique_paths',len(cm)==len(custody['files']) and len(hm)==len(helper['files']))
            self.custody=(custody,cm,hm)
        custody,cm,hm=self.custody
        rel=Path(pointer).relative_to(Path(custody['original_scratch']))
        self.c.ok('safe_manifest_relative_helper',not rel.is_absolute() and '..' not in rel.parts)
        original=rel.as_posix();kept='retained_ram/'+original
        self.c.ok('helper_path_explicitly_listed',original in cm and kept in hm)
        self.c.ok('helper_original_retained_digest',cm[original]['sha256']==hm[kept]['sha256']==digest)
        path=self.run/'helper_custody'/kept
        self.c.ok('helper_path_stays_in_retention',path.resolve().is_relative_to((self.run/'helper_custody/retained_ram').resolve()))
        self.c.ok('helper_retained_bytes',path.stat().st_size==cm[original]['bytes'])
        self.helper_rows.append({'original':original,'kept':str(path.relative_to(ROOT)),'sha256':digest})
        return path

    def authenticate(self,wrapper_path):
        w=read(wrapper_path);key=w['key'];pointer=w.get('record_file',w.get('receipt'))
        digest=w.get('record_file_sha256',w.get('receipt_sha256'))
        self.c.ok(key+'_receipt_pointer_and_digest',isinstance(pointer,str) and isinstance(digest,str) and len(digest)==64)
        # A helper path is resolved only from the original scratch declared by
        # custody, never by basename, guessed suffix or arbitrary filesystem search.
        if w.get('task_kind')=='research_web':path=self.kept_helper(pointer,digest)
        else:
            path=self.mapped_source(pointer)
            self.c.ok(key+'_native_receipt_inside_this_run',path.resolve().is_relative_to(self.run.resolve()))
        self.c.ok(key+'_record_file_SHA256',sha(path)==digest)
        receipt=read(path)
        self.c.ok(key+'_completed_identity',receipt['key']==key and receipt['status']==w['status']=='COMPLETED')
        if 'returned' in w:self.c.ok(key+'_wrapper_return_matches',w['returned']==receipt['returned'])
        if 'native_payload' in w:self.c.ok(key+'_wrapper_payload_matches',w['native_payload']==receipt.get('native_payload'))
        if 'record_file' in w:self.c.ok(key+'_large_wrapper_byte_count',w['bytes']==path.stat().st_size)
        row={'key':key,'task_kind':w.get('task_kind'),'wrapper_path':str(wrapper_path.relative_to(ROOT)),
             'wrapper_sha256':sha(wrapper_path),'receipt_path':str(path.relative_to(ROOT)),'receipt_sha256':digest}
        if w.get('task_kind')=='research_web':
            self.rows.append(row);return key,None,None,None
        rp=self.run/'native_requests'/(key+'.json');request=read(rp)
        task=request['task'];payload=receipt['native_payload'];binding=payload['source_binding']
        self.c.ok(key+'_request_identity',request['key']==task['key']==key)
        self.c.ok(key+'_same_native_operation',receipt['operation']==task['operation']==w['operation'])
        self.c.ok(key+'_accepted_exact_payload',task['payload']==payload)
        self.c.ok(key+'_source_binding_preserved',task['source_binding']==receipt['source_binding']==binding)
        self.c.ok(key+'_arithmetic_not_host',receipt['host_domain_arithmetic'] is False)
        for check in receipt.get('checks',[]):self.c.ok(key+'_native_contract_'+str(check.get('predicate',check.get('name','check'))),check['passed'] is True)
        self.c.ok(key+'_source_binding_nonempty',bool(binding))
        for source,expected in binding.get('source_files',{}).items():self.c.ok(key+'_source_SHA256_'+source,sha(self.mapped_source(source))==expected)
        # R1 retains the derivation that actually supplied its operands. An
        # explicit, hash-bound historical path prevents later manuscript edits
        # from being silently substituted for that source. R2's separately
        # named response_derivation_sha256 still binds its current derivation.
        if 'derivation_sha256' in binding:
            declared=binding.get('derivation_source_path')
            self.c.ok(key+'_explicit_derivation_source_path',isinstance(declared,str))
            source=self.mapped_source(declared)
            allowed={(BASE/'clock/DERIVATION.md').resolve(),(BASE/'clock/DERIVATION_R1.md').resolve()}
            self.c.ok(key+'_retained_clock_derivation_whitelist',source.resolve() in allowed)
            self.c.ok(key+'_derivation_in_source_manifest',binding.get('source_files',{}).get(declared)==binding['derivation_sha256'])
            self.c.ok(key+'_declared_derivation_SHA256',sha(source)==binding['derivation_sha256'])
        special={'frozen_source_sha256':BASE/'clock/chapter1_certificate.json',
                 'actual_clock_input_sha256':BASE/'clock/chapter1_certificate.json',
                 'response_derivation_sha256':BASE/'clock/DERIVATION.md',
                 'source_snapshot_sha256':BASE/'energy/CHAPTER_I_MODEL_SOURCE.md'}
        for field,source in special.items():
            if field in binding:self.c.ok(key+'_'+field,sha(source)==binding[field])
        row.update(operation=task['operation'],request_path=str(rp.relative_to(ROOT)),request_sha256=sha(rp))
        self.rows.append(row)
        return key,task['operation'],payload,receipt['returned']


def independent_expectations(c):
    """Scientific operands and expected outputs, independent of native requests."""
    s=read(BASE/'source/EXACT_INPUTS.json');q=matrix(s['Q']);den=F(s['gram_denominator'])
    out={}
    for label,operators in [
        ('outgoing',{**{'G'+str(t):block(*(matrix(s['coherent_number_gram'][t][x]) for x in range(8))) for t in range(3)},'negative_denQ':block(*(scale(q,-den) for _ in range(8)))}),
        ('incoming',{**{'N'+str(t):block(*(diag(s['incoming_number'][t][x]) for x in range(8))) for t in range(3)},'negative_I':scale(eye(32),-1)})]:
        out['r1_si29_'+label+'_flatness']={'kind':'word','operators':operators,'expected':zeros(32)}
    # The source-positive energy sqrt(K^2) commutes with the actual sector
    # contrast B, while K itself does not. The middle block deliberately retains
    # the nonzero generator witness, rather than reducing every test to zero.
    K=([r+s for r,s in zip(zeros(4),q)]+
       [r+s for r,s in zip(eye(4),zeros(4))])
    contrast=block(eye(4),scale(eye(4),-1));W=block(eye(4),q)
    selectors={'S'+str(k):diag([int(i==k) for i in range(3)]) for k in range(3)}
    witness=([r+s for r,s in zip(zeros(4),scale(q,-2))]+
             [r+s for r,s in zip(scale(eye(4),2),zeros(4))])
    out['r1_si29_uniform_coupling_response']={
        'kind':'word','operators':{'K':K,'B':contrast,'W':W,**selectors},
        'expected':block(zeros(8),witness,zeros(8))}
    c.ok('uniform_response_nonzero_generator_witness_rank',rank(witness)==8)
    c.same('uniform_response_companion_square',mul(K,K),block(q,q))
    c.same('uniform_response_square_root_commutator',sub(mul(mul(K,K),contrast),mul(contrast,mul(K,K))),zeros(8))
    c.same('uniform_response_physical_metric',mul(W,K),mul(transpose(K),W))
    cert=read(BASE/'clock/chapter1_certificate.json');q=matrix(cert['matrices']['Q']);I=eye(4)
    ql,qr=tensor(q,I),tensor(I,q);S=[[F(j==4*(i%4)+i//4) for j in range(16)] for i in range(16)]
    D=sub(ql,qr);Z=mul(sub(eye(16),S),D);E=add(add(ql,qr),mul(ql,qr));ct=scale(mul(D,D),2)
    out['chapter3_full_source_clock_energy_commutators']={'kind':'word','operators':{'A':block(S,E,ct),'Z':block(Z,Z,Z),'K':block(scale(Z,2),zeros(16),zeros(16))},'expected':zeros(48)}
    out['chapter3_full_scaling_epsilon_only_residual']={'kind':'word','operators':{'PARTIAL':diag([F(-1,2),0,F(-1,2),-1]),'NEG_FULL':diag([F(1,2)]*4)},'expected':diag([0,F(1,2),0,F(-1,2)])}
    f=read(BASE/'radial/FIXTURE.json');n=f['n'];K=matrix(f['K']);H=[[F(1,max(i,j))-F(1,f['L']) for j in range(1,n+1)] for i in range(1,n+1)]
    c.same('radial_fixture_Green_analytic',matrix(f['Green_H']),H)
    out['r1_radial_green_inverse']={'kind':'solve','matrix':K,'rhs':eye(n),'expected':H}
    radial=read(BASE/'radial/DUCK_R2_TASKS.json')[0]['payload']['data']['operators']
    radial={k:matrix(v) for k,v in radial.items()}
    c.same('radial_word_K_matches_fixture',radial['K'],K);c.same('radial_word_H_matches_analytic',radial['H'],H)
    c.same('radial_incidence_matches_fixture',radial['B'],matrix(f['incidence_B']))
    c.same('radial_conductance_matches_fixture',radial['C'],matrix(f['conductance_C']))
    out['r2_radial_flux_energy_word']={'kind':'word','operators':radial,'expected':zeros(24)}
    A=matrix([[0,20,0,0],[0,0,0,30],[1,1,-1,-1],[0,4,1,6]])
    b=matrix([[-2],[-3],[0],[0]]);coeff=matrix([[1],[F(-1,10)],[1],[F(-1,10)]])
    out['r2_quadrupole_matching']={'kind':'solve','matrix':A,'rhs':b,'expected':coeff}
    cube=read(BASE/'source/CUBE_GRAPH.json');coords=cube['coordinates']
    L=[[F(3) if i==j else F(-1) if sum((a-b)**2 for a,b in zip(coords[i],coords[j]))==4 else F(0) for j in range(8)] for i in range(8)]
    c.same('cube_declared_L_from_geometry',matrix(cube['L']),L)
    c.ok('cube_exact_rank_seven',rank(L)==cube['rank']==7)
    P=[[F(1,8)]*8 for _ in range(8)];c.same('cube_uniform_projector',matrix(cube['P']),P)
    minor=[r[:7] for r in L[:7]];c.same('cube_minor',matrix(cube['minor']),minor)
    out['r2_cube_rank7_minor_inverse']={'kind':'solve','matrix':minor,'rhs':eye(7),'expected':solve(minor,eye(7))}
    out['r2_cube_zero_mode']={'kind':'word','operators':{'L':L,'P':P},'expected':zeros(8)}
    c.same('cube_uniform_zero_mode',mul(L,P),zeros(8))
    result=read(BASE/'clock/RESULTS.json');rates=[r['actual_rate_enclosure'] for r in result['lanes']]
    upper=[F(r['upper']) for r in rates];lower=[F(r['lower']) for r in rates]
    expected=diag([a/b for a,b in zip(lower,upper)])
    out['r2_clock_phase_ratios']={'kind':'solve','matrix':diag(upper),'rhs':diag(lower),'expected':expected}
    for i,(row,lane) in enumerate(zip(expected,result['lanes'])):
        c.ok('clock_threshold_from_ratio_'+str(i),1-row[i]**2==F(lane['full_scaling_sufficient_lift_for_disjoint_phase_bands']))
    return out


def bound(value):
    if not isinstance(value,dict) or set(value)!={'lower','upper'}:raise ValueError('Expected explicit certified interval endpoints')
    lo,hi=F(value['lower']),F(value['upper'])
    if lo>hi:raise ValueError('Reversed interval')
    return lo,hi
def iadd(a,b):return a[0]+b[0],a[1]+b[1]
def iscale(a,s):return (s*a[0],s*a[1]) if s>=0 else (s*a[1],s*a[0])


def check_word(c,key,payload,returned,expected):
    c.ok(key+'_rational_field',payload['context']['field']=={'radicand':0})
    operands=payload['data']['operators'];c.ok(key+'_operator_names',set(operands)==set(expected['operators']))
    for name,a in expected['operators'].items():c.same(key+'_source_operand_'+name,matrix(operands[name]),a)
    computed=word(payload['data']);c.same(key+'_independent_source_identity',computed,expected['expected'])
    c.same(key+'_complete_native_matrix',matrix(returned['matrix']),expected['expected'])
    c.ok(key+'_returned_program',returned['ordered_program']==payload['data']['program'])
    c.ok(key+'_returned_output',returned['output']==payload['data']['output'])
    c.ok(key+'_output_basis',len(payload['context']['basis'])==len(computed))
    c.ok(key+'_native_exact_rank',returned['rank']==rank(computed))
    c.ok(key+'_native_GMP_arithmetic',returned['execution']['backend']=='NATIVE_CPP_GMP_CPU')


def check_solve(c,key,payload,returned,expected):
    A=matrix(payload['data']['matrix']['entries']);B=matrix(payload['data']['rhs']['entries'])
    c.same(key+'_source_matrix',A,expected['matrix']);c.same(key+'_source_rhs',B,expected['rhs'])
    exact=solve(A,B);c.same(key+'_independent_exact_solution',exact,expected['expected'])
    c.same(key+'_exact_equations',mul(A,exact),B)
    c.ok(key+'_precision',isinstance(payload['precision_bits'],int) and payload['precision_bits']>=384)
    output=returned['result']['output'];c.ok(key+'_certified_native_solve',output['status']=='CERTIFIED_SOLVE')
    entries=output['matrix']['entries'];c.ok(key+'_certified_matrix_shape',len(entries)==len(exact) and all(len(r)==len(s) for r,s in zip(entries,exact)))
    real=[];imag=[]
    for i,row in enumerate(entries):
        rr=[];ii=[]
        for j,cell in enumerate(row):
            r,z=bound(cell['re']),bound(cell['im']);rr.append(r);ii.append(z)
            c.ok(key+'_exact_solution_enclosed_%d_%d'%(i,j),r[0]<=exact[i][j]<=r[1])
            c.ok(key+'_imaginary_zero_enclosed_%d_%d'%(i,j),z[0]<=0<=z[1]);c.entries+=1
        real.append(rr);imag.append(ii)
    # A is exact and real. The whole returned interval solution must satisfy
    # every real and imaginary equation as an enclosure, not only its midpoint.
    for i,j in product(range(len(A)),range(len(B[0]))):
        re=im=(F(0),F(0))
        for k in range(len(A)):
            re=iadd(re,iscale(real[k][j],A[i][k]));im=iadd(im,iscale(imag[k][j],A[i][k]))
        c.ok(key+'_interval_equation_real_%d_%d'%(i,j),re[0]<=B[i][j]<=re[1])
        c.ok(key+'_interval_equation_imag_%d_%d'%(i,j),im[0]<=0<=im[1])
    if 'residual_norm_upper' in output:
        residual=bound(output['residual_norm_upper']);c.ok(key+'_native_residual_bound_nonnegative',0<=residual[0]<=residual[1])


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--run',type=Path,default=DEFAULT_RUN)
    parser.add_argument('--output',type=Path,default=BASE/'NATIVE_VERIFICATION.json');args=parser.parse_args()
    run=args.run.resolve();c=Checks();final=read(run/'COMPLETE.json')
    c.ok('actual_run_complete',final['status']=='COMPLETE' and final['failed_returns']==0)
    reader=Receipts(run,c);expected=independent_expectations(c);seen=set();web=0
    for path in sorted((run/'native_returns').glob('*.json')):
        key,operation,payload,returned=reader.authenticate(path)
        if operation is None:web+=1;continue
        c.ok(key+'_no_duplicate_native_key',key not in seen);seen.add(key)
        c.ok(key+'_independent_scientific_target_known',key in expected)
        target=expected[key]
        if target['kind']=='word':
            c.ok(key+'_operation_word',operation=='GEN3_SOURCE_OPERATOR_WORD');check_word(c,key,payload,returned,target)
        else:
            c.ok(key+'_operation_solve',operation=='GEN3_COMPLEX_SOLVE');check_solve(c,key,payload,returned,target)
    c.ok('every_expected_native_target_returned',seen==set(expected))
    c.ok('complete_native_count',len(seen)==final['native_returns'])
    c.ok('complete_research_receipt_count',web==final['research_returns'])
    c.ok('complete_return_accounting',len(reader.rows)==final['total_returns']==len(seen)+web)
    report={'schema':'SAM_CH3_NATIVE_INDEPENDENT_READBACK_V1','status':'PASS','run':str(run.relative_to(ROOT)),
            'native_outputs_verified':len(seen),'research_receipts_authenticated':web,
            'matrix_entries_checked':c.entries,'independent_checks':len(c.labels),'checks':c.labels,
            'native_receipts':reader.rows,'retained_helper_receipts':reader.helper_rows,
            'verifier_sha256':sha(Path(__file__)),'native_executions_from_this_script':0,
            'scope':'Complete exact source-word matrices and ranks; exact rational solves enclosed by certified native intervals and full interval equations; source/request/receipt custody authenticated.'}
    args.output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:report[k] for k in ['status','native_outputs_verified','research_receipts_authenticated','matrix_entries_checked','independent_checks']}))


if __name__=='__main__':main()
