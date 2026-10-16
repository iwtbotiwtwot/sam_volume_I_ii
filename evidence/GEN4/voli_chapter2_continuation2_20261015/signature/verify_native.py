#!/usr/bin/env python3
"""Independent exact readback of eight completed Duck signature returns.

No native execution. Verifies actual payloads, Krylov bases, Gram matrices,
compressed operators, leakage, exact receiving ranks and inverse enclosures.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

from check_signature import det, inv, mul

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RUN_REL = Path('GEN4/duck_gen6_local/runs/chapter2-signature-memory-20261015-01')
RUN = ROOT/RUN_REL
SNAPSHOT = HERE.parent/'inputs/SIGNATURE_OPERANDS_R2.json'
CURRENT = HERE/'NATIVE_OPERANDS.json'
SOURCE = ROOT/'GEN4/duck_chapter1_lane1_20261015/sources/EXACT_INPUTS.json'
checks = []
entries = 0
receipts = []


def require(label, value):
    if not value:
        raise AssertionError(label)
    checks.append(label)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matrix(x):
    return [[F(v) for v in row] for row in x]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return list(map(list,zip(*a)))


def rank(a):
    a = [row[:] for row in a]
    n, m = len(a), len(a[0])
    pivot = 0
    for j in range(m):
        k = next((i for i in range(pivot,n) if a[i][j]),None)
        if k is None:
            continue
        a[k],a[pivot]=a[pivot],a[k]
        v=a[pivot][j]
        a[pivot]=[x/v for x in a[pivot]]
        for i in range(pivot+1,n):
            v=a[i][j]
            a[i]=[x-v*y for x,y in zip(a[i],a[pivot])]
        pivot+=1
        if pivot==n:
            break
    return pivot


def same_matrix(label, actual, expected):
    global entries
    require(label+':rows',len(actual)==len(expected))
    for i,(ar,er) in enumerate(zip(actual,expected)):
        require(label+':columns:'+str(i),len(ar)==len(er))
        for j,(a,e) in enumerate(zip(ar,er)):
            require(f'{label}:{i}:{j}',a==e)
            entries+=1


def load_return(key, operation, bind_snapshot=False):
    path=RUN/'native_returns'/(key+'.json')
    d=json.loads(path.read_text())
    require(key+':receipt_key',d['key']==key)
    require(key+':actual_result',d['kind']=='RESULT')
    require(key+':operation',d['operation']==operation)
    require(key+':native_execution',d['host_domain_arithmetic'] is False)
    require(key+':native_contract',all(c['passed'] for c in d['checks']))
    require(key+':current_generation',d['generation']=='GEN5-COOPERATING-LOG1-20261008-G2-SPIN-CLOCK')
    payload=d['native_payload']
    if bind_snapshot:
        bound=payload['source_binding']['source_files']
        require(key+':snapshot_hash',bound[str(SNAPSHOT.relative_to(ROOT))]==sha(SNAPSHOT))
    else:
        bound=payload['source_binding']['source_files']
        require(key+':original_source_hash',bound[str(SOURCE.relative_to(ROOT))]==sha(SOURCE))
    receipts.append(dict(key=key,path=str(path.relative_to(ROOT)),sha256=sha(path),
                         operation=operation,generation=d['generation']))
    return payload,d['returned']


def verify_subspace(key,g,placement,expected_rank,T,K,snapshot=False):
    p,o=load_return(key,'GEN3_SOURCE_SUBSPACE',snapshot)
    q=[[T[i][j]+g*K[i][j] for j in range(4)]for i in range(4)]
    seed=[[F(i==placement)] for i in range(4)]
    same_matrix(key+':source_payload',matrix(p['data']['H']),q)
    same_matrix(key+':seed_payload',matrix(p['data']['seeds']),seed)
    require(key+':closure_mode',p['data']['mode']=='CLOSURE')
    columns=[]
    v=seed
    for _ in range(expected_rank):
        columns.append([x[0]for x in v])
        v=mul(q,v)
    basis=transpose(columns)
    require(key+':independent_rank',rank(basis)==expected_rank)
    same_matrix(key+':native_basis',matrix(o['basis']),basis)
    gram=mul(transpose(basis),basis)
    same_matrix(key+':native_Gram',matrix(o['Gram']),gram)
    require(key+':Gram_positive_determinant',det(gram)>0)
    compressed=mul(mul(inv(gram),transpose(basis)),mul(q,basis))
    same_matrix(key+':native_compressed_H',matrix(o['compressed_H']),compressed)
    qb=mul(q,basis)
    bc=mul(basis,compressed)
    residual=[[a-b for a,b in zip(ar,br)]for ar,br in zip(qb,bc)]
    require(key+':independent_no_leakage',all(x==0 for row in residual for x in row))
    same_matrix(key+':native_residual',matrix(o['residual']),residual)
    same_matrix(key+':native_nonleaking_coefficients',matrix(o['nonleaking_coefficients']),eye(expected_rank))
    require(key+':native_rank',o['rank']==expected_rank)
    require(key+':native_growth',o['growth']==list(range(1,expected_rank+1)))
    require(key+':native_invariant',o['invariant']is True)
    require(key+':native_backend',o['execution']['backend']=='NATIVE_CPP_GMP_CPU')
    return basis


def verify_word(key,expected,expected_rank):
    p,o=load_return(key,'GEN3_SOURCE_OPERATOR_WORD',True)
    same_matrix(key+':operand',matrix(p['data']['operators']['M']),expected)
    same_matrix(key+':identity',matrix(p['data']['operators']['I']),eye(len(expected)))
    require(key+':program',p['data']['program']==[{'inputs':['M','I'],'name':'checked_product','op':'multiply'}])
    same_matrix(key+':native_matrix',matrix(o['matrix']),expected)
    require(key+':independent_rank',rank(expected)==expected_rank)
    require(key+':native_rank',o['rank']==expected_rank)
    require(key+':native_backend',o['execution']['backend']=='NATIVE_CPP_GMP_CPU')


def main():
    global entries
    snapshot=json.loads(SNAPSHOT.read_text())
    current=json.loads(CURRENT.read_text())
    require('completed_signature_operands_match_R2_snapshot',snapshot==current)
    require('snapshot_original_source_hash',snapshot['source_sha256']==sha(SOURCE))
    T,K=matrix(snapshot['T']),matrix(snapshot['K_response'])
    for g in range(3):
        verify_subspace('r1_cyclic_g'+str(g),F(g),1,4,T,K)
    blind0=verify_subspace('r2_blind_placement0',F(1,164),0,3,T,K,True)
    verify_subspace('r2_blind_placement1',F(1,164),1,4,T,K,True)
    qblind=matrix(snapshot['Q_placement0_blind'])
    vblind=matrix(snapshot['placement0_blind_eigenvector'])
    lam=F(snapshot['placement0_blind_lambda'])
    same_matrix('blind_eigenvector_source_equation',mul(qblind,vblind),[[lam*x[0]]for x in vblind])
    same_matrix('blind_eigenvector_orthogonal_to_placement0_closure',mul(transpose(vblind),blind0),[[F(0)]*3])
    h3=matrix(snapshot['H3'])
    tls=matrix(snapshot['H4_TLS_control'])
    verify_word('r2_finite_record_rank',h3,3)
    verify_word('r2_TLS_control_rank',tls,2)
    require('H3_exact_determinant_matches_independent_operand',det(h3)==F(snapshot['H3_determinant_independent']))
    expected_inverse=inv(h3)
    same_matrix('H3_exact_inverse_matches_independent_operand',matrix(snapshot['H3_inverse_independent']),expected_inverse)
    p,o=load_return('r2_H3_inverse','GEN3_COMPLEX_SOLVE',True)
    same_matrix('inverse_payload_H3',matrix(p['data']['matrix']['entries']),h3)
    same_matrix('inverse_payload_identity',matrix(p['data']['rhs']['entries']),eye(3))
    require('inverse_precision',p['precision_bits']==1024)
    out=o['result']['output']
    require('inverse_native_success',out['status']=='CERTIFIED_SOLVE')
    actual=out['matrix']['entries']
    require('inverse_shape',len(actual)==3 and all(len(r)==3 for r in actual))
    for i,row in enumerate(actual):
        for j,c in enumerate(row):
            require(f'inverse_real_contains_exact:{i}:{j}',F(c['re']['lower'])<=expected_inverse[i][j]<=F(c['re']['upper']))
            require(f'inverse_imag_contains_zero:{i}:{j}',F(c['im']['lower'])<=0<=F(c['im']['upper']))
            entries+=1
    same_matrix('independent_H3_times_inverse',mul(h3,expected_inverse),eye(3))
    report=dict(schema='SAM_CH2_SIGNATURE_NATIVE_READBACK_V1',status='PASS',
        role='Independent exact Fraction readback of completed installed Duck outputs; no new native execution',
        run=str(RUN_REL),native_returns_checked=len(receipts),independent_checks=len(checks),
        matrix_entries_checked=entries,receipts=receipts,
        source_bindings=[dict(path=str(p.relative_to(ROOT)),sha256=sha(p))for p in (SOURCE,SNAPSHOT,CURRENT)],
        conclusions=dict(endpoint_ranks_at_g0_g1_g2=[4,4,4],
            placement0_rank_at_g1_over164=3,placement1_rank_at_g1_over164=4,
            source_Hankel_minor_rank=3,TLS_difference_Hankel_rank=2,
            all_native_Krylov_Grams_compressed_operators_and_leakage_match=True,
            inverse_complex_intervals_contain_independent_exact_inverse=True),
        checks=checks,verifier_sha256=sha(Path(__file__)))
    (HERE/'NATIVE_VERIFICATION.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k]for k in ('status','native_returns_checked','independent_checks','matrix_entries_checked','conclusions')},indent=2))


if __name__=='__main__':
    main()
