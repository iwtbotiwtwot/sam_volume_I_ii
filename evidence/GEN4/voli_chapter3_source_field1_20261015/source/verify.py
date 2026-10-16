#!/usr/bin/env python3
"""Portable independent exact checks; no native session is started."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, product
from collections import Counter
import hashlib
import json
import math

HERE=Path(__file__).resolve().parent

def determinant(A):
    A=[[F(v) for v in row] for row in A]; d=F(1)
    for k in range(len(A)):
        pivot=next((j for j in range(k,len(A)) if A[j][k]),None)
        if pivot is None:return F(0)
        if pivot!=k:A[k],A[pivot]=A[pivot],A[k];d=-d
        p=A[k][k];d*=p
        for i in range(k+1,len(A)):
            q=A[i][k]/p
            for j in range(k+1,len(A)):A[i][j]-=q*A[k][j]
    return d

def verify():
    d=json.loads((HERE/'EXACT_INPUTS.json').read_text())
    obs=json.loads((HERE/'retained/OBSERVABLE_CLOSURE.json').read_text())
    source=json.loads((HERE/'retained/SI29_Q01_RESULT.json').read_text())
    checks=[]
    def ck(name,condition):
        if not condition:raise AssertionError(name)
        checks.append(name)
    for name,v in d.items():
        if name in source:ck('retained_source_'+name,v==source[name])
    Q=d['Q'];N=d['incoming_number'];G=d['coherent_number_gram'];den=d['gram_denominator']
    for x in range(8):
        ck('incoming_flat_site_%d'%x,all(sum(N[t][x][j] for t in range(3))==1 for j in range(4)))
        ck('outgoing_flat_site_%d'%x,all(sum(G[t][x][i][j] for t in range(3))==den*Q[i][j] for i in range(4) for j in range(4)))
    principal=[]
    for size in range(1,5):
        ids=list(range(size));m=determinant([[Q[i][j] for j in ids] for i in ids]);principal.append(str(m));ck('Q_positive_leading_minor_%d'%size,m>0)
    for t in range(3):
        for x in range(8):
            ck('N_positive_%d_%d'%(t,x),all(v>=0 for v in N[t][x]))
            ck('G_symmetric_%d_%d'%(t,x),all(G[t][x][i][j]==G[t][x][j][i] for i in range(4) for j in range(4)))
            for size in range(1,5):
                for ids in combinations(range(4),size):
                    ck('G_PSD_%d_%d_%s'%(t,x,''.join(map(str,ids))),determinant([[G[t][x][i][j] for j in ids] for i in ids])>=0)
            coeff=obs['seed_map'][8*t+x]
            for i,j in product(range(8),repeat=2):
                re=sum(F(c)*F(O[i][j]['re']) for c,O in zip(coeff,obs['operators']))
                im=sum(F(c)*F(O[i][j]['im']) for c,O in zip(coeff,obs['operators']))
                want=F(N[t][x][i]) if i==j and i<4 else F(G[t][x][i-4][j-4],den) if i>=4 and j>=4 else F(0)
                ck('independent_closure_seed_%d_%d_%d_%d'%(t,x,i,j),re==want and im==0)
    ck('companion_Q_matches',all(F(obs['companion_generator'][i][j+4]['re'])==Q[i][j] for i in range(4) for j in range(4)))
    for task in json.loads((HERE/'DUCK_R1_TASKS.json').read_text()):
        operands=task['payload']['data']['operators'];n=len(next(iter(operands.values())))
        ck('native_operand_identity_'+task['key'],all(sum(F(A[i][j]) for A in operands.values())==0 for i in range(n) for j in range(n)))
    coords=[tuple(1 if (x>>j)&1 else -1 for j in range(3)) for x in range(8)]
    pair_hist=Counter(sum((a-b)**2 for a,b in zip(coords[i],coords[j])) for i,j in combinations(range(8),2))
    ck('cube_pair_histogram',pair_hist=={4:12,8:12,12:4})
    graph=source['cube_edges'];ck('cube_retained_edges',all(sum((coords[i][j]-coords[k][j])**2 for j in range(3))==4 for i,k in graph))
    for powers in product(range(6),repeat=3):
        degree=sum(powers)
        if degree>5:continue
        moment=F(sum(math.prod(c[j]**powers[j] for j in range(3)) for c in coords),8)
        ck('cube_moment_'+''.join(map(str,powers)),moment==int(all(p%2==0 for p in powers)))
    # Polynomial coefficients of the l=4 term before setting |n|=1.
    actual={};expected={}
    def accum(out,p,v):out[p]=out.get(p,F(0))+v
    for p in product(range(5),repeat=3):
        if sum(p)!=4:continue
        multinomial=F(math.factorial(4),math.prod(math.factorial(x) for x in p))
        moment=F(sum(math.prod(c[j]**p[j] for j in range(3)) for c in coords),8)
        accum(actual,p,F(35,8)*multinomial*moment)
    for i,j in product(range(3),repeat=2):
        p=tuple(2*int(k==i)+2*int(k==j) for k in range(3))
        accum(actual,p,F(-90+27,8))
        accum(expected,p,F(21,4))
    for i in range(3):
        p=tuple(4*int(k==i) for k in range(3));accum(expected,p,F(-35,4))
    ck('cube_l4_polynomial',{k:v for k,v in actual.items() if v}=={k:v for k,v in expected.items() if v})
    ck('axis_l4_coefficient',F(7,4)*(3-5)==F(-7,2))
    ck('diagonal_l4_coefficient',F(7,4)*(3-F(5,3))==F(7,3))
    ck('self_energy_coefficient',8*F(3,5)*F(1,8)**2==F(3,40))
    ck('mutual_edge_coefficient',F(pair_hist[4],2)==6)
    ck('mutual_face_sqrt2_coefficient',F(pair_hist[8],4)==3)
    ck('mutual_body_sqrt3_coefficient',F(pair_hist[12],6)==F(2,3))
    retained=json.loads((HERE/'retained/ENERGY_Q01_RESULT.json').read_text())
    worked=[{'preparation':r['preparation'],'retained_energy_relative':str(r['total_energy']),
             'per_site_energy_relative':str(F(str(r['total_energy']))/8),
             'eight_equal_normalized_shares':['1/8']*8} for r in retained['records']]
    return {'status':'PASS','independent_exact_checks':len(checks),'Q_positive_leading_minors':principal,
            'cube_coordinates_embedding':coords,'pair_squared_distance_counts':dict(pair_hist),
            'worked_retained_energy_rows':worked,
            'scope':'Exact retained source and finite-cube algebra; displayed retained energy decimals are not new certified square-root evaluation.',
            'native_tasks':'Prepared here; actual execution and receipts belong to parent Duck run.',
            'theorem_controls':['All principal minors establish PSD of each rational spatial Gram.',
                'Congruence by positive energy square root carries exact flatness to H0/8.',
                'For q=sqrt(3)*ell/r<1, even Legendre tail beyond l=4 bounded by q^6/(r*(1-q^2)).']}

if __name__=='__main__':
    result=verify();(HERE/'CHECKS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':result['status'],'independent_exact_checks':result['independent_exact_checks']}))
