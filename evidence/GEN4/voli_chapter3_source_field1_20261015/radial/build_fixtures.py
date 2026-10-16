#!/usr/bin/env python3
"""Compile source-bound exact operands; native execution is parent-owned."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCES = [
    'GEN4/native_energy_source1/RADIAL_METHOD.md',
    'GEN4/native_energy_source1/RADIAL_ANALYSIS.md',
    'GEN4/vol_i_activation_selection1/NETWORK_METHOD.md',
    'GEN4/vol_i_activation_selection1/network.py',
]

def wire(a):
    return [[str(v) for v in row] for row in a]

def main():
    L = 9
    n = L - 1
    mass = list(map(F, ['0', '1/5', '0', '3/10', '1/10', '0', '2/5', '0']))
    kappa = F(1, 50)
    B = [[F(i == j) - F(j == i + 1) for j in range(n)] for i in range(n)]
    C = [[F((i+1)*(i+2) if i == j else 0) for j in range(n)] for i in range(n)]
    K = [[F(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        K[i][i] = F((i+1)*(i+2) + i*(i+1))
        if i + 1 < n:
            K[i][i+1] = K[i+1][i] = F(-(i+1)*(i+2))
    H = [[F(1, max(i+1, j+1)) - F(1, L) for j in range(n)] for i in range(n)]
    q = [kappa*m for m in mass]
    expected = [sum(H[i][j]*q[j] for j in range(n)) for i in range(n)]
    binding = {
        'model': 'retained c_i=i(i+1) isotropic-monopole receiver; explicit thin-shell density extension',
        'source_files': {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in SOURCES},
        'builder_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope': 'static conditional shell receiving law; physical source-to-mass map and angular isotropy are not inferred',
    }
    fixture = {
        'schema': 'SAM_CHAPTER3_RADIAL_EXACT_V1',
        'L': L, 'n': n, 'kappa': str(kappa),
        'mass': list(map(str, mass)), 'q': list(map(str, q)),
        'incidence_B': wire(B), 'conductance_C': wire(C),
        'K': wire(K), 'Green_H': wire(H),
        'expected_a': list(map(str, expected)),
        'source_binding': binding,
        'units': {
            'r_i': 'i*h', 'outer_radius': 'L*h',
            'kappa': '2*G*M_unit/(c^2*h); masses are in M_unit',
            'a': 'dimensionless source lift',
            'energy_unit': 'G*M_unit^2/h',
            'energy': 'U_L/energy_unit = -sum_ij m_i H_ij m_j/2',
        },
    }
    (HERE/'FIXTURE.json').write_text(json.dumps(fixture, indent=2)+'\n')
    def context(n):
        return {'basis': list(range(n)), 'field': {'radicand': 0},
                'history': {'mapping': 'finite radial shell Poisson source, explicit absorbing outer boundary'},
                'units': fixture['units'], 'spectral_coordinate': 'dimensionless static radial source lift'}
    tasks = [{
        'id': 'CH3_RADIAL_SOURCE_INVERSE', 'domain': 'STARBREAKER',
        'operation': 'GEN2_READOUT_INVERSE',
        'payload': {'strategy': 'linear', 'matrix': wire(K), 'observed': list(map(str, q)),
                    'context': context(n), 'source_binding': binding},
        'question': 'What field does the retained c_i=i(i+1) receiver return for this declared extended shell source?',
        'expected': {'a': fixture['expected_a']},
        'source_mapping': 'K=B^T C B; q_i=kappa*m_i; no desired inverse-radius field enters the right-hand side',
    }]
    sel = lambda i: [[str(int(j == k == i)) for k in range(3)] for j in range(3)]
    ops = {'B': wire(B), 'C': wire(C), 'K': wire(K), 'H': wire(H),
           'I': wire([[F(i == j) for j in range(n)] for i in range(n)])}
    ops.update({'S'+str(i): sel(i) for i in range(3)})
    def s(name, op, *inputs): return {'name': name, 'op': op, 'inputs': list(inputs)}
    prog = [s('Bt','transpose','B'),s('BtC','multiply','Bt','C'),
            s('BtCB','multiply','BtC','B'),s('incidence_residual','subtract','BtCB','K'),
            s('KH','multiply','K','H'),s('green_residual','subtract','KH','I'),
            s('HK','multiply','H','K'),s('HKH','multiply','HK','H'),
            s('energy_residual','subtract','HKH','H')]
    for i, name in enumerate(['incidence_residual','green_residual','energy_residual']):
        prog.append(s('o'+str(i),'tensor','S'+str(i),name))
    prog += [s('o01','add','o0','o1'),s('answer','add','o01','o2')]
    tasks.append({
        'id': 'CH3_RADIAL_FLUX_ENERGY_IDENTITIES','domain':'STARBREAKER',
        'operation':'GEN3_SOURCE_OPERATOR_WORD',
        'payload':{'name':'CH3_RADIAL_FLUX_ENERGY_IDENTITIES',
                   'data':{'operators':ops,'program':prog,'output':'answer'},
                   'context':context(3*n),'source_binding':binding},
        'question':'Do source conductances, telescoping Green kernel and discrete energy form give one exact receiving operator?',
        'source_mapping':'Three native blocks: B^T C B-K; KH-I; HKH-H. Analytic Green candidate supplied independently of native inverse.',
        'expected':{'zero_matrix_shape':[3*n,3*n]},
    })
    (HERE/'NATIVE_TASKS.json').write_text(json.dumps(tasks,indent=2)+'\n')
    print(json.dumps({'fixture':'FIXTURE.json','tasks':[t['id'] for t in tasks]}))

if __name__ == '__main__':
    main()
