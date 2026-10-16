#!/usr/bin/env python3
"""Independent rational check of source-uniform/coherence/calibration results.

This script executes no native operation. Exact source matrices and certified
root enclosures are bound to the retained Chapter I input packet. All numeric
witnesses below are interval/rational arithmetic, including the cosine bound.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = ROOT / 'GEN4/duck_chapter1_lane1_20261015/sources/EXACT_INPUTS.json'
checks = []


def require(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def exact_matrix(record):
    rows = []
    for row in record['entries']:
        cells = []
        for c in row:
            require('source_cell_exact_real', c['re']['lower'] == c['re']['upper']
                    and F(c['im']['lower']) == F(c['im']['upper']) == 0)
            cells.append(F(c['re']['lower']))
        rows.append(cells)
    return rows


def mul(a, b):
    return [[sum(x*y for x, y in zip(r, c)) for c in zip(*b)] for r in a]


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def det(a):
    n = len(a)
    out = F(0)
    for p in permutations(range(n)):
        v = F((-1)**sum(p[i] > p[j] for i in range(n) for j in range(i+1, n)))
        for i in range(n):
            v *= a[i][p[i]]
        out += v
    return out


def inv(a):
    n = len(a)
    aug = [list(row)+[F(i == j) for j in range(n)] for i, row in enumerate(a)]
    for j in range(n):
        k = next(i for i in range(j, n) if aug[i][j])
        aug[j], aug[k] = aug[k], aug[j]
        f = aug[j][j]
        aug[j] = [x/f for x in aug[j]]
        for i in range(n):
            if i != j:
                f = aug[i][j]
                aug[i] = [x-f*y for x, y in zip(aug[i], aug[j])]
    return [r[n:] for r in aug]


def plus(a, b):
    return (a[0]+b[0], a[1]+b[1])


def neg(a):
    return (-a[1], -a[0])


def minus(a, b):
    return plus(a, neg(b))


def times(a, b):
    p = [x*y for x in a for y in b]
    return (min(p), max(p))


def div(a, b):
    require('positive_interval_denominator', b[0] > 0)
    return times(a, (1/b[1], 1/b[0]))


def point(x):
    return (F(x), F(x))


def interval_det(a):
    n = len(a)
    out = point(0)
    for p in permutations(range(n)):
        v = point((-1)**sum(p[i] > p[j] for i in range(n) for j in range(i+1, n)))
        for i in range(n):
            v = times(v, a[i][p[i]])
        out = plus(out, v)
    return out


def floor_decimal(x, places):
    m = 10**places
    return F((x*m).numerator//(x*m).denominator, m)


def ceil_decimal(x, places):
    return -floor_decimal(-x, places)


def compact(a, places=30):
    return (floor_decimal(a[0], places), ceil_decimal(a[1], places))


def encode(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, tuple):
        return {'lower': str(x[0]), 'upper': str(x[1])}
    if isinstance(x, list):
        return [encode(v) for v in x]
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    return x


def arctan_reciprocal(n, terms=80):
    x = F(1, n)
    s = sum((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(terms))
    nxt = (-1)**terms*x**(2*terms+1)/F(2*terms+1)
    return (min(s, s+nxt), max(s, s+nxt))


def cos_interval(a):
    # Taylor at a rational midpoint with an explicit Lagrange remainder,
    # followed by the real-line 1-Lipschitz cosine bound for interval width.
    mid = sum(a)/2
    rad = (a[1]-a[0])/2
    order = 32
    val = sum((-1)**k*mid**(2*k)/factorial(2*k) for k in range(order+1))
    err = abs(mid)**(2*order+2)/factorial(2*order+2)+rad
    return compact((val-err, val+err))


def ratios(q):
    additive = div(minus(q[2], q[1]), minus(q[1], q[0]))
    enhancement = div(plus(plus(q[2], q[1]), point(2)),
                      plus(plus(q[1], q[0]), point(2)))
    return additive, times(additive, enhancement), enhancement


def hankel_det_formula(a,b):
    value = times(point(F(1024,81)), times(minus(point(1),a),minus(point(1),b)))
    value = times(value, times(minus(point(1),times(a,a)),minus(point(1),times(b,b))))
    ab = minus(a,b)
    return times(value,times(times(ab,ab),times(ab,ab)))


def Xi(g):
    return 384+5120*g+1377280*g*g


def inverse_xi_interval(value):
    lo, hi = F(0), F(2)
    require('Xi_bisection_bracket', Xi(lo) <= value <= Xi(hi))
    for _ in range(100):
        mid = (lo+hi)/2
        if Xi(mid) <= value:
            lo = mid
        else:
            hi = mid
    return (lo, hi)


def main():
    d = json.loads(SOURCE.read_text())
    T, K = exact_matrix(d['T']), exact_matrix(d['K'])
    require('source_T', T == [[84,8,8,0],[8,84,0,0],[8,0,84,8],[0,0,8,84]])
    require('source_K', K == [[672,96,32,0],[96,2016,0,0],[32,0,672,32],[0,0,32,672]])
    require('trace_law', (tr(T), tr(K)) == (336, 4032))
    spread = [4*tr(mul(T,T))-tr(T)**2,
              8*tr(mul(T,K))-2*tr(T)*tr(K),
              4*tr(mul(K,K))-tr(K)**2]
    require('Xi_exact_coefficients', spread == [1536,20480,5509120])
    order = [1,0,2,3]
    for i in range(4):
        for j in range(4):
            if abs(i-j) > 1:
                require('Jacobi_structural_zero', T[order[i]][order[j]] == K[order[i]][order[j]] == 0)
    for i in range(3):
        require('Jacobi_positive_link_constant', T[order[i]][order[i+1]] > 0)
        require('Jacobi_positive_link_slope', K[order[i]][order[i+1]] > 0)
    tlo = [T[i][i]-sum(abs(T[i][j]) for j in range(4) if j != i) for i in range(4)]
    klo = [K[i][i]-sum(abs(K[i][j]) for j in range(4) if j != i) for i in range(4)]
    thi = [T[i][i]+sum(abs(T[i][j]) for j in range(4) if j != i) for i in range(4)]
    khi = [K[i][i]+sum(abs(K[i][j]) for j in range(4) if j != i) for i in range(4)]
    require('Gershgorin_uniform_lower', min(tlo) == 68 and min(klo) == 544)
    require('Gershgorin_uniform_upper', max(thi) == 100 and max(khi) == 2112)
    # (8+32g)/(202+4224g) >= 1/132 for every g>=0.
    require('all_g_margin_constant', 132*8 > 202)
    require('all_g_margin_slope', 132*32 == 4224)
    require('compact_margin_monotone', 32*202-8*4224 < 0)
    compact_margin = F(8+32*2,202+4224*2)
    require('compact_margin', compact_margin == F(36,4325))

    q = [compact((F(d['q']['entries'][i][i]['re']['lower']),
                  F(d['q']['entries'][i][i]['re']['upper']))) for i in range(4)]
    for a in range(3):
        require('inherited_root_order', q[a][1] < q[a+1][0])
    add, pair, enhance = ratios(q)
    require('unit_ratio_source_control_separation', pair[0] > add[1])
    require('unit_ratio_pair_distinct_frequencies', pair[0] > 1)
    require('unit_ratio_all_g_margin', enhance[0] > 1+F(1,132))
    pi = compact(minus(times(point(16),arctan_reciprocal(5)),
                       times(point(4),arctan_reciprocal(239))))
    require('pi_Machin_bracket', F(314159,100000) < pi[0] < pi[1] < F(314160,100000))
    theta2 = div(times(pair, pi), point(3))
    b = cos_interval(theta2)
    a = point(F(1,2))
    require('phase_distinct_nonaliased', 0 < b[0] < b[1] < a[0] < 1)
    ta, tb = [point(1),a], [point(1),b]
    for k in range(2,8):
        ta.append(minus(times(times(point(2),a),ta[-1]),ta[-2]))
        tb.append(minus(times(times(point(2),b),tb[-1]),tb[-2]))
    y = [times(point(F(2,3)), plus(x,z)) for x,z in zip(ta,tb)]
    diffs = [minus(y[i+1],y[i]) for i in range(7)]
    h = [[diffs[i+j] for j in range(4)] for i in range(4)]
    dh = compact(interval_det(h),24)
    require('eight_sample_rank4_witness', dh[0] > F(1284,1000000))
    # Independent closed form: detH = (1024/81)(1-a)(1-b)
    # *(1-a*a)*(1-b*b)*(a-b)^4.
    cf = hankel_det_formula(a,b)
    require('Hankel_closed_form_interval_agreement', max(dh[0],cf[0]) <= min(dh[1],cf[1]))
    eta = F(1,10**7)
    two_error_bound = 384*eta*(F(8,3)+4*eta)**3
    require('target_TLS_noise_balls_disjoint', dh[0] > two_error_bound)
    hmid = [[floor_decimal(sum(c)/2+F(1,2*10**12),12) for c in row] for row in h]
    round_radius = max(max(abs(hmid[i][j]-v) for v in h[i][j]) for i in range(4) for j in range(4))
    require('native_operand_rounding_radius', round_radius < F(1,10**12))
    hdet = det(hmid)
    hi = inv(hmid)
    ident = [[F(i==j) for j in range(4)] for i in range(4)]
    require('native_midpoint_exact_inverse', mul(hmid,hi) == ident)
    require('native_midpoint_positive_det', hdet > 0)
    round_det_error = 96*round_radius*(F(8,3)+round_radius)**3
    require('native_midpoint_witness_transfer', hdet-round_det_error > 0)
    # A general exact TLS rank-two witness using nonzero phase and quadrature.
    # cos(theta)=3/5, sin(theta)=4/5; arbitrary dc=7/11, A=2/3, B=-5/7.
    c,s=F(1),F(0)
    tls=[]
    for _ in range(8):
        tls.append(F(7,11)+F(2,3)*c-F(5,7)*s)
        c,s=F(3,5)*c-F(4,5)*s,F(4,5)*c+F(3,5)*s
    td=[tls[i+1]-tls[i] for i in range(7)]
    htls=[[td[i+j] for j in range(4)] for i in range(4)]
    require('TLS_nontrivial_exact_rank_control', det(htls) == 0)
    for p in permutations(range(4),3):
        require('TLS_all_order3_row_minors', det([[htls[i][j] for j in range(3)] for i in p]) == 0)

    xi1 = Xi(F(1))
    require('Xi_unit_value', xi1 == 1382784)
    gl,gh=inverse_xi_interval(xi1-1),inverse_xi_interval(xi1+1)
    gcal=(gl[0],gh[1])
    dg=max(1-gcal[0],gcal[1]-1)
    require('diagnostic_calibration_g', dg < F(1,10**6))
    qradius=2112*dg
    qcal=[(x[0]-qradius,x[1]+qradius) for x in q]
    ca,cp,ce=ratios(qcal)
    require('calibration_uncertainty_preserves_separation', cp[0] > ca[1])
    # Fixed cadence is chosen from the independently calibrated nominal
    # source, without estimating a frequency from these eight measurements.
    # Include a declared relative physical-alpha calibration error as well.
    dnom=F('79355.8477726533875')
    scale_cal=(1-F(1,10**6),1+F(1,10**6))
    edark=[times(plus(x,point(1)),plus(x,point(1))) for x in qcal]
    gap10=minus(edark[1],edark[0])
    gap21=minus(edark[2],edark[1])
    phase_prefactor=div(pi,point(3*dnom))
    phase10=times(times(phase_prefactor,scale_cal),gap10)
    phase21=times(times(phase_prefactor,scale_cal),gap21)
    c10,c21=cos_interval(phase10),cos_interval(phase21)
    require('calibrated_fixed_cadence_no_alias', 0 < c21[0] < c21[1] < c10[0] < c10[1] < 1)
    fixed_det=compact(hankel_det_formula(c10,c21),24)
    require('calibrated_fixed_cadence_robust_TLS_separation', fixed_det[0] > two_error_bound)
    # A selected 3x3 minor uses the same eight samples and tests the TLS
    # rank-two identity with a substantially larger certified noise budget.
    tac,tbc=[point(1),c10],[point(1),c21]
    for k in range(2,8):
        tac.append(minus(times(times(point(2),c10),tac[-1]),tac[-2]))
        tbc.append(minus(times(times(point(2),c21),tbc[-1]),tbc[-2]))
    yc=[times(point(F(2,3)),plus(x,z)) for x,z in zip(tac,tbc)]
    dc=[minus(yc[i+1],yc[i]) for i in range(7)]
    indices=[0,1,3]
    h3=[[hmid[i][j] for j in indices] for i in indices]
    h3c=[[dc[i+j] for j in indices] for i in indices]
    dh3=compact(interval_det(h3c),24)
    eta3=F(1,10**4)
    noise3=72*eta3*(F(8,3)+4*eta3)**2
    require('calibrated_rank3_minor_noise_1e4', dh3[1] < -noise3)
    h3i=inv(h3)
    require('native_H3_exact_inverse',mul(h3,h3i)==[[F(i==j) for j in range(3)] for i in range(3)])
    # Exact placement0 blind mode, distinct from the always-cyclic endpoints.
    blindg=F(1,164)
    blindq=[[T[i][j]+blindg*K[i][j] for j in range(4)] for i in range(4)]
    ba=8+96*blindg
    bb=8+32*blindg
    bd=84+672*blindg
    blindv=[[F(0)],[-bb/ba],[F(1)],[F(1)]]
    blindlambda=bd+bb
    require('placement0_blind_mode_eigenvector',mul(blindq,blindv)==[[blindlambda*x[0]] for x in blindv])
    require('placement0_blind_mode_overlap',blindv[0][0]==0)
    coefficients=[[F(int(i==j))-F(1,4) for j in range(4)] for i in range(4)]
    sensitivity=[sum(abs(row[j]) for j in range(1,4)) for row in coefficients]
    require('root_offset_error_coefficients', sensitivity == [F(3,4),F(5,4),F(5,4),F(5,4)])
    mean=F(84)+1008
    offsets=[minus(x,q[0]) for x in q]
    mean_offsets=times(point(F(1,4)),plus(plus(offsets[0],offsets[1]),plus(offsets[2],offsets[3])))
    recovered=[plus(point(mean),minus(x,mean_offsets)) for x in offsets]
    for i in range(4):
        require('common_offset_reconstruction_root', recovered[i][0] <= q[i][0] <= q[i][1] <= recovered[i][1])
    packet={
      'schema':'SAM_CH2_CONTINUATION_SIGNATURE_V1','status':'PASS',
      'provenance':'New Codex source-bound mathematical derivations and independent rational checks; parent owns native execution.',
      'source':{'path':str(SOURCE.relative_to(ROOT)),'sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest()},
      'scope':{'g_H':'all g_H>=0; [0,2] is a declared diagnostic calibration interval, not a physical fit',
               'sampling':'g_H=1 retained diagnostic; h=pi/(3*omega10); explicit protected preparation/readout',
               'physical_status':'no physical epsilon/g_H assignment, coherent preparation, or experimental measurement performed'},
      'T':T,'K_response':K,'Xi_coefficients':[F(x,4) for x in spread],
      'uniform_spectrum':{'Jacobi_order':order,'q_min_lower':'68+544*g_H','q_max_upper':'100+2112*g_H',
          'q2_minus_q0_lower':'8+32*g_H','ratio_enhancement_lower_all_nonnegative_g':F(1,132),
          'ratio_enhancement_lower_diagnostic_0_2':compact_margin,'K_min_eigenvalue_lower':544,'K_norm_upper':2112},
      'unit_root_intervals':q,'unit_additive_ratio':add,'unit_pair_ratio':pair,'unit_ratio_enhancement':enhance,
      'sampling':{'pi_interval':pi,'theta1_cos':a,'theta2_cos':b,'theta2_interval':theta2,
          'eight_signal_samples':y,'difference_Hankel':h,'determinant_interval':dh,
          'determinant_closed_form_interval':compact(cf,24),'per_sample_error':eta,
          'two_error_determinant_bound':two_error_bound,'target_TLS_noise_balls_disjoint':True},
      'calibration':{'Xi1':xi1,'declared_Xi_error':1,'g_H_interval':gcal,'g_H_error_bound':dg,
          'Weyl_root_error_bound':qradius,'additive_ratio_interval':ca,'pair_ratio_interval':cp,
          'ratio_intervals_disjoint':True,'global_inverse_Lipschitz':'1/5120',
          'fixed_cadence':{'h':'pi/(3*alpha_nominal*D_nominal)','D_nominal':dnom,
              'relative_alpha_interval':scale_cal,'phase10_interval':phase10,'phase21_interval':phase21,
              'cos_phase10_interval':c10,'cos_phase21_interval':c21,
              'Hankel_determinant_interval':fixed_det,
              'target_TLS_noise_balls_disjoint_at_sample_error_1e-7':True,
              'rank3_minor':{'indices':indices,'determinant_interval':dh3,
                  'per_sample_error':eta3,'two_error_determinant_bound':noise3,
                  'target_TLS_noise_balls_disjoint':True}},
          'root_reconstruction_mean':'84+1008*g_H','root_offsets':'s_a=-2*kappa_0a/Delta; s_0=0',
          'root_reconstruction_offset_error_coefficients':sensitivity},
      'native_operand':{'path':'NATIVE_OPERANDS.json','Hankel_midpoint':hmid,
          'maximum_entry_error':round_radius,'determinant_exact':hdet,'determinant_transfer_error_bound':round_det_error},
      'placement0_exception':{'g_H':blindg,'Q':blindq,'lambda':blindlambda,'eigenvector':blindv,
          'statement':'Placement0 misses one eigenmode at g_H=1/164. Jacobi endpoints1 and3 are cyclic for every g_H>=0.'},
      'checks_passed':len(checks),'checks':checks,
      'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    }
    (HERE/'RESULTS.json').write_text(json.dumps(encode(packet),indent=2)+'\n')
    native={'schema':'SAM_CH2_SIGNATURE_NATIVE_OPERANDS_V1','source_sha256':packet['source']['sha256'],
       'purpose':'Parent native exact matrix solve/product check of rational rounded Hankel witness; actual-source transfer bounds in RESULTS.json',
       'H4':hmid,'H4_inverse_independent':hi,'H4_determinant_independent':hdet,
       'H4_entry_error_to_actual':round_radius,'H4_TLS_control':htls,
       'H3_indices':indices,'H3':h3,'H3_inverse_independent':h3i,'H3_determinant_independent':det(h3),
       'Q_placement0_blind':blindq,'placement0_blind_eigenvector':blindv,'placement0_blind_lambda':blindlambda,
       'T':T,'K_response':K,'expected_trace_T':336,'expected_trace_K':4032,
       'expected_spread_coefficients':[1536,20480,5509120]}
    (HERE/'NATIVE_OPERANDS.json').write_text(json.dumps(encode(native),indent=2)+'\n')
    print(json.dumps({'status':'PASS','checks':len(checks),'det_H4_lower':float(dh[0]),
        'noise_bound':float(two_error_bound),'g_H_interval':[float(x) for x in gcal],
        'robust_minor_det_interval':[float(x) for x in dh3],
        'robust_minor_sample_error':float(eta3),'robust_minor_noise_bound':float(noise3),
        'pair_ratio_calibration_interval':[float(x) for x in cp],
        'add_ratio_calibration_interval':[float(x) for x in ca]},indent=2))


if __name__ == '__main__':
    main()
