#!/usr/bin/env python3
"""Freeze the exact source-bound native task; parent owns execution."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
from verify_uniform_coupling import z,eye,mm,comm,blocks,tr,scale,add,wire

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    source=json.loads((HERE/'EXACT_INPUTS.json').read_text())
    Q=[list(map(F,row)) for row in source['Q']]; I=eye(4); Z=z(4)
    K=blocks(Z,Q,I,Z); B=blocks(I,Z,Z,scale(-1,I)); W=blocks(I,Z,Z,Q)
    paths=[HERE/'EXACT_INPUTS.json',HERE/'retained/SI29_Q01_RESULT.json',
           HERE/'retained/ENERGY_Q01_RESULT.json',HERE/'retained/OBSERVABLE_CLOSURE.json',
           HERE/'UNIFORM_COUPLING_RESPONSE.md',HERE/'verify_uniform_coupling.py',Path(__file__)]
    binding={'campaign':'voli_chapter3_source_field1_20261015',
             'source_files':{str(p.relative_to(ROOT)):sha(p) for p in paths},
             'model':'Actual Si29 companion generator and sector-resolved incoming/outgoing effects',
             'static_frame':'Uniform prescribed lift in a common external physical time chart; candidate deltaH=-(eu*a/2)H0.',
             'basis':'Eight actual bright companion coordinates; W-inner-product normalization T=diag(I,sqrtQ).',
             'scope':'Exact response of declared positive-excitation coupling; no general gravity verdict or physical coupling selection.'}
    operators={'K':wire(K),'B':wire(B),'W':wire(W)}
    for i in range(3):operators['S'+str(i)]=wire([[F(j==k==i) for k in range(3)] for j in range(3)])
    def step(name,op,*inputs):return {'name':name,'op':op,'inputs':list(inputs)}
    program=[step('K2','multiply','K','K'),step('sqrt_commutator_certificate','commutator','K2','B'),
             step('generator_commutator','commutator','K','B'),step('Kt','transpose','K'),
             step('WK','multiply','W','K'),step('KtW','multiply','Kt','W'),
             step('metric_residual','subtract','WK','KtW')]
    for i,name in enumerate(['sqrt_commutator_certificate','generator_commutator','metric_residual']):
        program.append(step('out'+str(i),'tensor','S'+str(i),name))
    program += [step('out01','add','out0','out1'),step('answer','add','out01','out2')]
    expected=z(24)
    for g,mat in enumerate([comm(mm(K,K),B),comm(K,B),add(mm(W,K),scale(-1,mm(tr(K),W)))]):
        for i,row in enumerate(mat):
            for j,v in enumerate(row):expected[8*g+i][8*g+j]=v
    task={'key':'r1_si29_uniform_coupling_response','operation':'GEN3_SOURCE_OPERATOR_WORD',
          'payload':{'name':'r1_si29_uniform_coupling_response',
                     'context':{'basis':['block%d:bright%d'%(g,j) for g in range(3) for j in range(8)],
                                'field':{'radicand':0},'spectral_coordinate':'actual source companion generator and population contrast',
                                'units':{'K':'retained dimensionless coherent generator','B':'incoming minus outgoing probability','W':'physical companion norm Gram'},
                                'history':{'scope':'uniform static candidate coupling, physical rate eu/Iu assigned separately'}},
                     'data':{'operators':operators,'program':program,'output':'answer'},'source_binding':binding},
          'source_binding':binding,
          'purpose':'Evaluate actual uniform H0-density coupling on retained incoming/outgoing transfer signal: certify sqrt(K²)commutesB whileKdrivesB, retaining physical metric.',
          'expected_matrix':wire(expected),'expected_blocks':['[K²,B]=0','[K,B]=[[0,-2Q],[2I,0]] nonzero','WK-KᵀW=0'],
          'scope':'Functional calculus and exact response derivation in UNIFORM_COUPLING_RESPONSE.md; expected answer is not in payload.'}
    (HERE/'DUCK_UNIFORM_RESPONSE_TASK.json').write_text(json.dumps(task,indent=2)+'\n')
    print(json.dumps({'key':task['key'],'operation':task['operation'],'output_shape':[24,24],
                      'expected_block_nonzero':[False,True,False]}))

if __name__=='__main__':main()
