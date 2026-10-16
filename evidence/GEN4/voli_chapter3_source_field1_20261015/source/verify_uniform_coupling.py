#!/usr/bin/env python3
"""Portable exact algebra supporting the uniform-coupling analytic result.

No native session, square-root evaluation or numerical propagation is launched.
The positive square root enters only through the spectral-calculus argument
in UNIFORM_COUPLING_RESPONSE.md.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
def z(n):return [[F(0) for _ in range(n)] for _ in range(n)]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(q,a):return [[q*v for v in row] for row in a]
def mm(a,b):return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*b)] for row in a]
def tr(a):return list(map(list,zip(*a)))
def comm(a,b):return add(mm(a,b),scale(-1,mm(b,a)))
def blocks(a,b,c,d):return [x+y for x,y in zip(a,b)]+[x+y for x,y in zip(c,d)]
def diag(a):return [[F(x) if i==j else F(0) for j in range(len(a))] for i,x in enumerate(a)]
def wire(a):return [[str(v) for v in row] for row in a]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    raw=json.loads((HERE/'EXACT_INPUTS.json').read_text())
    original=json.loads((HERE/'retained/SI29_Q01_RESULT.json').read_text())
    obs=json.loads((HERE/'retained/OBSERVABLE_CLOSURE.json').read_text())
    Q=[list(map(F,row)) for row in raw['Q']]; I=eye(4); Z=z(4)
    K=blocks(Z,Q,I,Z)
    W=blocks(I,Z,Z,Q)
    Pin=blocks(I,Z,Z,Z); Pout=blocks(Z,Z,Z,I)
    B=add(Pin,scale(-1,Pout)); K2=blocks(Q,Z,Z,Q)
    checks=[]
    def ck(name,test):
        if not test:raise AssertionError(name)
        checks.append(name)
    ck('Q is the retained exact actual source',raw['Q']==original['Q'])
    ck('companion generator matches retained closure',all(F(obs['companion_generator'][i][j]['re'])==K[i][j] and F(obs['companion_generator'][i][j]['im'])==0 for i in range(8) for j in range(8)))
    Nin=z(4); Gout=z(4)
    for t in range(3):
        for x in range(8):
            Nin=add(Nin,diag(raw['incoming_number'][t][x]))
            Gout=add(Gout,[list(map(F,row)) for row in raw['coherent_number_gram'][t][x]])
    ck('incoming slot effects sum to eight identities',Nin==scale(8,I))
    ck('outgoing slot Grams sum to eight denQ',Gout==scale(8*raw['gram_denominator'],Q))
    Rin=blocks(scale(F(1,8),Nin),Z,Z,Z)
    Rout=blocks(Z,Z,Z,scale(F(1,8*raw['gram_denominator']),Gout))
    ck('incoming aggregate form is W Pin',Rin==mm(W,Pin))
    ck('outgoing aggregate form is W Pout',Rout==mm(W,Pout))
    ck('aggregate slot form is the physical norm',add(Rin,Rout)==W)
    ck('sector contrast is an involution',mm(B,B)==eye(8))
    ck('incoming projector is exact',mm(Pin,Pin)==Pin)
    ck('outgoing projector is exact',mm(Pout,Pout)==Pout)
    ck('sector projectors are orthogonal',mm(Pin,Pout)==z(8))
    ck('transfer generator is self adjoint in physical companion metric',mm(tr(K),W)==mm(W,K))
    ck('sector contrast is self adjoint in physical companion metric',mm(tr(B),W)==mm(W,B))
    ck('transfer square is diagQ Q',mm(K,K)==K2)
    ck('transfer generator anticommutes with actual sector contrast',add(mm(K,B),mm(B,K))==z(8))
    ck('transfer square commutes with sector contrast',comm(K2,B)==z(8))
    ck('transfer square commutes with transfer generator',comm(K2,K)==z(8))
    ck('sector signal has nonzero transfer derivative operator',comm(K,B)!=z(8))
    double=comm(K,comm(K,B))
    ck('second derivative operator is minus4K2B',double==scale(4,mm(K2,B)))
    ck('incoming e0 signal curvature is minus512',-double[0][0]==-512)
    control_a=F(1,50)
    baseline_curvature=-double[0][0]
    full_scaling_curvature=(1-control_a)*baseline_curvature
    ck('two percent full scaling curvature is minus501 point76',full_scaling_curvature==F(-12544,25))
    ck('two percent scaling control differs from invariant candidate',full_scaling_curvature!=baseline_curvature)
    # A source observable with noncommuting h exists: if [h,N]=0 then [Q,N]=0.
    witness=None
    for t in range(3):
        for x in range(8):
            N=diag(raw['incoming_number'][t][x]); c=comm(Q,N)
            if c!=z(4):
                witness={'species_index':t,'site':x,'N':wire(N),'Q_N_commutator':wire(c)}
                break
        if witness:break
    ck('not every spatial species observable commutes with positive energy',witness is not None)
    source_paths=[HERE/'EXACT_INPUTS.json',HERE/'retained/SI29_Q01_RESULT.json',
                  HERE/'retained/ENERGY_Q01_RESULT.json',HERE/'retained/OBSERVABLE_CLOSURE.json',
                  HERE/'CHECKS.json',ROOT/'GEN4/volii_duck_expansion1/REPORT.md',
                  ROOT/'GEN4/volii_duck_expansion2/REPORT.md']
    result={'schema':'SAM_CH3_UNIFORM_SOURCE_COUPLING_V1','status':'PASS',
            'independent_exact_checks':len(checks),'check_names':checks,
            'execution':'Independent rational source-algebra check only; no fresh native call or time propagation.',
            'source_files_sha256':{str(p.relative_to(ROOT)):sha(p) for p in source_paths},
            'verifier_sha256':sha(Path(__file__)),
            'exact_companion_certificate':{'Q':wire(Q),'K':wire(K),'physical_metric_W':wire(W),
               'P_in':wire(Pin),'P_out':wire(Pout),'B':wire(B),'K_squared':wire(K2),
               'double_commutator':wire(double),'incoming_e0_B_second_derivative':'-512'},
            'positive_square_root_step':'Retained Q is positive definite; H0=sqrt(K^2)=diag(h,h) in the W-inner product. Since K^2 commutes with B and K, so does H0 by functional calculus.',
            'uniform_candidate':'H_phys(a)=eu[Hgen-(a/2)H0]; theta=eu*t/Iu.',
            'exact_response':'B_a(theta)=B_0(theta) for every state and every static a; all incoming/outgoing sector probabilities are unchanged.',
            'incoming_preparation_signal':'<B(theta)>=psi^*cos(2h theta)psi; P_out=psi^*sin(h theta)^2 psi.',
            'full_scaling_comparison':'n(a)Hgen gives B_n(theta)=B_0(n(a)theta), with generically nonzero time-dilation response.',
            'finite_control':{'a':str(control_a),'n':'sqrt(1-a)',
                 'incoming_e0_candidate_B_curvature':str(baseline_curvature),
                 'incoming_e0_full_scaling_B_curvature':str(full_scaling_curvature),
                 'scope':'Algebraic comparison of specified couplings, not an experimental redshift or apparatus precision claim.'},
            'other_observable_witness':witness,
            'scope':'Retained population-transfer signal, not the Chapter I certified phase-clock theorem; other species/site observables need not have zero response. The result distinguishes the proposed positive-energy density coupling from full-generator scaling; no general gravity verdict is assigned.'}
    (HERE/'UNIFORM_COUPLING_RESPONSE.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','independent_exact_checks':len(checks),'e0_B_curvature':-512,
                      'noncommuting_species_site':[witness['species_index'],witness['site']]}))

if __name__=='__main__':main()
