#!/usr/bin/env python3
"""Exact source-bound measurement budgets and finite-shot certificates.

Standard library only. No native execution, no fitted experimental data and no
physical preparation is performed. All certificate calculations use fractions.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SIGNATURE = ROOT / 'GEN4/voli_chapter2_continuation2_20261015/signature'
PRIMARY = ROOT / 'GEN4/duck_chapter1_lane1_20261015/sources/EXACT_INPUTS.json'
checks = []


def require(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def point(x):
    return F(x), F(x)


def plus(a, b):
    return a[0]+b[0], a[1]+b[1]


def minus(a, b):
    return a[0]-b[1], a[1]-b[0]


def times(a, b):
    v = [x*y for x in a for y in b]
    return min(v), max(v)


def floor_decimal(v, places=30):
    scale = 10**places
    return F((v*scale).numerator//(v*scale).denominator, scale)


def compact(a, places=30):
    return floor_decimal(a[0], places), -floor_decimal(-a[1], places)


def det(a):
    n = len(a)
    result = F(0)
    for p in permutations(range(n)):
        term = F((-1)**sum(p[i] > p[j] for i in range(n) for j in range(i+1, n)))
        for i in range(n):
            term *= a[i][p[i]]
        result += term
    return result


def interval_det(a):
    n = len(a)
    result = point(0)
    for p in permutations(range(n)):
        term = point((-1)**sum(p[i] > p[j] for i in range(n) for j in range(i+1, n)))
        for i in range(n):
            term = times(term, a[i][p[i]])
        result = plus(result, term)
    return compact(result, 24)


def mul(a, b):
    return [[sum(x*y for x, y in zip(r, c)) for c in zip(*b)] for r in a]


def arctan_reciprocal(n, terms=80):
    x = F(1, n)
    s = sum((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(terms))
    nxt = (-1)**terms*x**(2*terms+1)/F(2*terms+1)
    return min(s, s+nxt), max(s, s+nxt)


def pi_interval():
    return compact(minus(times(point(16), arctan_reciprocal(5)),
                         times(point(4), arctan_reciprocal(239))))


def cos_interval(a, pi):
    # Exact range reduction by an integer multiple of the certified 2*pi.
    midpoint = sum(a)/2
    turns_estimate = midpoint/sum(pi)
    q = turns_estimate+F(1, 2)
    turns = q.numerator//q.denominator
    reduced = minus(a, times(point(2*turns), pi))
    mid, rad = sum(reduced)/2, (reduced[1]-reduced[0])/2
    val = sum((-1)**k*mid**(2*k)/factorial(2*k) for k in range(33))
    remainder = abs(mid)**66/factorial(66)+rad
    return compact((val-remainder, val+remainder))


def make_record(q, relative_alpha, cadence_factor, nominal_gap, pi, indices):
    energy = [times(plus(x, point(1)), plus(x, point(1))) for x in q]
    gap = [times(relative_alpha, minus(energy[i+1], energy[i])) for i in range(2)]
    phases = [times(times(x, pi), point(cadence_factor/nominal_gap)) for x in gap]
    cosines = [cos_interval(x, pi) for x in phases]
    sequences = []
    for c in cosines:
        sequence = [point(1), c]
        for k in range(2, 8):
            sequence.append(compact(minus(times(times(point(2), c), sequence[-1]), sequence[-2])))
        sequences.append(sequence)
    samples = [times(point(F(2, 3)), plus(a, b)) for a, b in zip(*sequences)]
    differences = [minus(samples[i+1], samples[i]) for i in range(7)]
    minor = [[differences[i+j] for j in indices] for i in indices]
    return {'gap_over_alpha_nominal': gap, 'phases': phases, 'cosines': cosines,
            'samples': samples, 'minor': minor, 'determinant': interval_det(minor),
            'maximum_minor_entry': max(abs(v) for row in minor for x in row for v in x)}


def log_interval_integer(r, terms=128):
    x = F(r-1, r+1)
    lower = 2*sum(x**(2*k+1)/F(2*k+1) for k in range(terms))
    upper = lower+2*x**(2*terms+1)/F((2*terms+1)*(1-x*x))
    return lower, upper


def ceil_fraction(x):
    return -((-x.numerator)//x.denominator)


def encode(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, tuple):
        return {'lower': str(x[0]), 'upper': str(x[1])}
    if isinstance(x, list):
        return [encode(y) for y in x]
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    return x


def protocol(name, eta, indices, factor, record, B, pi, Dnom, log1600, L):
    require(name+'_bound_on_source_entries', record['maximum_minor_entry'] < B)
    determinant = record['determinant']
    require(name+'_determinant_sign', determinant[0]*determinant[1] > 0)
    absolute_lower = min(abs(x) for x in determinant)
    single = 36*eta*(B+2*eta)**2
    two = 72*eta*(B+4*eta)**2
    threshold_upper = 36*eta*(B+4*eta)**2
    require(name+'_two_noise_balls_disjoint', absolute_lower > two)
    require(name+'_direct_empirical_rejection', absolute_lower-single > threshold_upper)
    stat = F(3, 5)*eta
    sys = eta/F(10)
    require(name+'_budget_sum', 4*sys+stat == eta)
    shots_interval = times(point(4/stat**2), log1600)
    shots = ceil_fraction(shots_interval[1])
    require(name+'_ceil_certified', shots-1 < shots_interval[0] < shots_interval[1] <= shots)
    return {'eta': eta, 'indices': list(indices), 'cadence_factor_pi_over_alpha_D': factor,
            'h_times_alpha_nominal': times(pi, point(factor/Dnom)),
            'source_minor_entry_bound': B, 'source_minor_determinant_interval': determinant,
            'source_minor_maximum_entry_enclosure': record['maximum_minor_entry'],
            'single_error_determinant_bound': single,
            'two_error_determinant_bound': two,
            'empirical_absolute_determinant_lower': absolute_lower-single,
            'empirical_rejection_threshold_upper': threshold_upper,
            'decision_margin_lower': absolute_lower-single-threshold_upper,
            'confidence_sampling_only': '99/100', 'joint_failure_bound': '1/100',
            'each_systematic_bias_budget': sys, 'statistical_error_budget': stat,
            'd_prep_max': 'eta/(20*sqrt(2))',
            'd_prep_squared_max': sys**2/8,
            'evolution_path_integral_max': 'eta/(20*sqrt(2))',
            'readout_operator_error_max': sys,
            'leakage_probability_max_if_conditional_state_exact': sys**2/8,
            'leakage_probability_max_equal_prep_split': sys**2/32,
            'delta_t_times_alpha_nominal_max': sys/L,
            'shots_logarithm_interval': shots_interval,
            'shots_per_time': shots, 'total_measurement_shots': 8*shots}


def main():
    s = json.loads((SIGNATURE/'RESULTS.json').read_text())
    primary_hash = hashlib.sha256(PRIMARY.read_bytes()).hexdigest()
    require('primary_source_hash_binding', primary_hash == s['source']['sha256'])
    require('retained_signature_pass', s['status'] == 'PASS')
    q0 = [(F(x['lower']), F(x['upper'])) for x in s['unit_root_intervals']]
    err = F(s['calibration']['Weyl_root_error_bound'])
    qcal = [(a-err, b+err) for a, b in q0]
    cal = s['calibration']['fixed_cadence']
    relative_alpha = tuple(F(cal['relative_alpha_interval'][k]) for k in ['lower', 'upper'])
    Dnom = F(cal['D_nominal'])
    pi = pi_interval()
    require('Machin_pi_contains_retained_pi',
            pi[0] <= F(s['sampling']['pi_interval']['lower']) <=
            F(s['sampling']['pi_interval']['upper']) <= pi[1])
    O = [[F(x) for x in row] for row in [[0,1,0],[1,0,1],[0,1,0]]]
    O2, O3 = mul(O,O), mul(mul(O,O),O)
    require('observable_spectral_polynomial', O3 == [[2*x for x in row] for row in O])
    require('observable_trace_zero', sum(O[i][i] for i in range(3)) == 0)
    require('observable_squared_trace_four', sum(O2[i][i] for i in range(3)) == 4)
    P0twice = [[2*F(i==j)-O2[i][j] for j in range(3)] for i in range(3)]
    require('zero_outcome_projector_scaled', mul(P0twice,P0twice) == [[2*x for x in row] for row in P0twice])
    require('zero_outcome_annihilates_observable', mul(O,P0twice) == [[0]*3 for _ in range(3)])
    baseline = make_record(qcal, relative_alpha, F(1,3), Dnom, pi, (0,1,3))
    olddet = tuple(F(cal['rank3_minor']['determinant_interval'][k]) for k in ['lower','upper'])
    require('baseline_interval_replayed', baseline['determinant'] == olddet)
    improved = make_record(qcal, relative_alpha, F(5,2), Dnom, pi, (0,2,3))
    require('improved_minor_positive_lower', improved['determinant'][0] > F(5318,1000))
    require('improved_four_exponentials_nonaliased',
            -1 < improved['cosines'][1][0] < improved['cosines'][1][1] <
            improved['cosines'][0][0] < improved['cosines'][0][1] < 1)
    # Prespecified finite source-only scan. No measured target values are inputs.
    candidates = []
    for factor, indices in [(F(1,3),(0,1,3)), (F(2,3),(0,1,3)),
                            (F(4,3),(0,1,3)), (F(5,2),(0,2,3)), (F(3),(0,1,3))]:
        r = make_record(qcal, relative_alpha, factor, Dnom, pi, indices)
        candidates.append({'factor':factor,'indices':list(indices),'determinant_interval':r['determinant'],
                           'maximum_minor_entry':r['maximum_minor_entry']})
    nominal = make_record(q0, point(1), F(5,2), Dnom, pi, (0,2,3))
    rounded = [[floor_decimal(sum(x)/2+F(1,2*10**12),12) for x in row] for row in nominal['minor']]
    rounding = max(abs(rounded[i][j]-v) for i in range(3) for j in range(3) for v in nominal['minor'][i][j])
    Bround = max(abs(x) for row in rounded for x in row)
    nominal_det = det(rounded)
    rounding_det = 18*rounding*(Bround+rounding)**2
    require('native_minor_rounding', rounding < F(1,10**12))
    require('native_minor_positive_transfer', nominal_det-rounding_det > 5)
    # ln1600 = 6 ln2 + 2 ln5, each from an exact atanh series.
    log1600 = plus(times(point(6), log_interval_integer(2)), times(point(2), log_interval_integer(5)))
    require('logarithm_bracket', F(73777589,10**7) < log1600[0] < log1600[1] < F(73777590,10**7))
    L = F(2,3)*sum(x[1] for x in baseline['gap_over_alpha_nominal'])
    require('derivative_source_bound', L < F(114081396605,10**6))
    original = protocol('baseline',F(1,10**4),(0,1,3),F(1,3),baseline,F(8,3),pi,Dnom,log1600,L)
    better = protocol('improved',F(1,100),(0,2,3),F(5,2),improved,F(2),pi,Dnom,log1600,L)
    require('baseline_shot_count', original['shots_per_time'] == 8197509899)
    require('improved_shot_count', better['shots_per_time'] == 819751)
    require('shot_reduction_better_than_9999', F(original['shots_per_time'],better['shots_per_time']) > 9999)
    operands = {'schema':'SAM_CH2_MEASUREMENT_NATIVE_OPERANDS_V1',
                'meaning':'Exact observable identities and rational midpoint minor; not detector data or native evolution.',
                'O':O,'O_squared':O2,'P0_twice':P0twice,
                'improved_nominal_H3_rounded':rounded,'improved_nominal_H3_det_exact':nominal_det,
                'maximum_nominal_entry_error':rounding,'determinant_transfer_error':rounding_det}
    (HERE/'NATIVE_OPERANDS.json').write_text(json.dumps(encode(operands),indent=2)+'\n')
    result = {'schema':'SAM_CH2_PHYSICAL_MEASUREMENT_V1','status':'PASS',
              'physical_status':'Mathematical receiver and sufficient error/shot requirements; no physical apparatus or precision claimed.',
              'sources':[{'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
                         for p in [PRIMARY,SIGNATURE/'RESULTS.json',SIGNATURE/'DERIVATION.md']],
              'source_calibration':{'Xi':s['calibration']['Xi1'],'Xi_error':1,
                                    'g_H_interval':s['calibration']['g_H_interval'],
                                    'relative_alpha_interval':relative_alpha,'D_nominal':Dnom},
              'observable':{'O':O,'eigenvalues':['-sqrt(2)','0','sqrt(2)'],
                            'outcome_range':'[-sqrt(2),sqrt(2)]','field_status':'full protected source-plus-vacuum ideal state'},
              'derivative_upper_over_alpha_nominal':L,
              'baseline':original,'improved':better,
              'improved_record':improved,'source_only_cadence_candidates':candidates,
              'nominal_native_operand':operands,
              'log_1600_interval':log1600,'checks_passed':len(checks),'checks':checks,
              'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'RESULTS.json').write_text(json.dumps(encode(result),indent=2)+'\n')
    print(json.dumps({'status':'PASS','checks':len(checks),
                      'baseline_shots_per_time':original['shots_per_time'],
                      'improved_shots_per_time':better['shots_per_time'],
                      'improved_total_shots':better['total_measurement_shots'],
                      'improved_minor_interval':[float(x) for x in improved['determinant']],
                      'improved_decision_margin':float(better['decision_margin_lower'])},indent=2))


if __name__ == '__main__':
    main()
