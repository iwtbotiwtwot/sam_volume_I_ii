#!/usr/bin/env python3
"""Read back the actual Duck memory solve/payment; launch no computation.

Native receipt matrices are checked against the original interval operands
with independent exact rational arithmetic. This is separate provenance from
the installed GEN3_COMPLEX_SOLVE and GEN3_COMPLEX_PRODUCT executions.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

from exact_memory import I, HERE, ROOT, read, sha

RUN_NAME = 'chapter2-signature-memory-20261015-01'
DEFAULT_RUN = ROOT/'GEN4/duck_gen6_local/runs'/RUN_NAME
COUNTS = Counter()


def require(category, condition):
    if not condition:
        raise AssertionError(category)
    COUNTS[category] += 1


def overlap(a, b):
    return max(a.lo,b.lo) <= min(a.hi,b.hi)


def literal(x):
    """Read an original wire scalar, retaining the exact real intervals."""
    return I.make(x)


def source_relative(path):
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def native(run, key, operation):
    wrapper_path = run/'native_returns'/(key+'.json')
    wrapper = read(wrapper_path)
    require('completed_native_returns', wrapper['status'] == 'COMPLETED')
    require('native_operation_binding', wrapper['operation'] == operation)
    pointer = wrapper.get('record_file',wrapper.get('receipt'))
    # Map only the exact original run suffix. The recorded hash remains
    # mandatory; this supports portable copies without reading another run.
    anchor = '/runs/'+RUN_NAME+'/'
    require('native_pointer_run_binding', anchor in pointer)
    suffix = pointer.split(anchor,1)[1]
    require('native_pointer_path_safe', not Path(suffix).is_absolute() and '..' not in Path(suffix).parts)
    record_path = run/suffix
    expected_sha = wrapper.get('record_file_sha256',wrapper.get('receipt_sha256'))
    require('native_record_hash', sha(record_path) == expected_sha)
    record = read(record_path)
    require('completed_native_record', record['status'] == 'COMPLETED')
    require('record_operation_binding',record['operation'] == operation)
    result = record['returned']['result']
    require('returned_operation_binding',result['operation'] == operation)
    matrix = result['output']['matrix']
    require('native_precision',matrix['precision_bits'] == 1024)
    binding = record['source_binding']['source_files']
    rel = str((HERE/'SOURCE_OPERANDS.json').relative_to(ROOT))
    require('native_original_source_operand_hash',binding[rel] == sha(HERE/'SOURCE_OPERANDS.json'))
    provenance = [dict(role='native_return_wrapper',path=source_relative(wrapper_path),sha256=sha(wrapper_path)),
                  dict(role='native_complete_record',path=source_relative(record_path),sha256=sha(record_path))]
    return record,matrix,provenance


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--run',type=Path,default=DEFAULT_RUN)
    args = parser.parse_args()
    operand_path = HERE/'SOURCE_OPERANDS.json'
    operands = read(operand_path)
    profiles = operands['profiles']
    n = len(profiles)
    require('original_preparation_count',n == 54)
    solve_record,xmatrix,sources1 = native(args.run,'r2_all54_memory_Usolve','GEN3_COMPLEX_SOLVE')
    product_record,pmatrix,sources2 = native(args.run,'r2_all54_memory_payment','GEN3_COMPLEX_PRODUCT')
    require('native_preparation_order',solve_record['source_binding']['profiles'] == [p['profile_id'] for p in profiles])
    X, P = xmatrix['entries'], pmatrix['entries']
    require('native_solve_matrix_shape',len(X) == 2*n and all(len(row) == n for row in X))
    require('native_payment_matrix_shape',len(P) == n and all(len(row) == n for row in P))
    srcu = solve_record['native_payload']['data']['matrix']['entries']
    srcrhs = solve_record['native_payload']['data']['rhs']['entries']
    srcwt = product_record['native_payload']['data']['matrix']['entries']
    srcright = product_record['native_payload']['data']['right']['entries']
    for i,row in enumerate(srcu):
        for j,cell in enumerate(row):
            expected = profiles[i//2]['U'][i%2][j%2] if i//2 == j//2 else 0
            require('native_literal_source_U_entries',literal(cell) == literal(expected))
    for i,row in enumerate(srcrhs):
        for j,cell in enumerate(row):
            expected = profiles[j]['W'][i%2][0] if i//2 == j else 0
            require('native_literal_source_W_entries',literal(cell) == literal(expected))
    for i,row in enumerate(srcwt):
        for j,cell in enumerate(row):
            expected = profiles[i]['W'][j%2][0] if i == j//2 else 0
            require('native_literal_source_W_transpose_entries',literal(cell) == literal(expected))
    for i,row in enumerate(srcright):
        for j,cell in enumerate(row):
            require('native_payment_consumes_actual_solve_entries',cell == X[i][j])

    # Independent exact2x2 source solves, not a call to native runtime code.
    independent = []
    for p in profiles:
        u = [[literal(x) for x in row] for row in p['U']]
        w = [[literal(x) for x in row] for row in p['W']]
        detu = u[0][0]*u[1][1]-u[0][1]*u[1][0]
        require('independent_U_positive_determinant',detu.lo > 0)
        xx = [(u[1][1]*w[0][0]-u[0][1]*w[1][0])/detu,
              (u[0][0]*w[1][0]-u[1][0]*w[0][0])/detu]
        payment = w[0][0]*xx[0]+w[1][0]*xx[1]
        independent.append((u,w,xx,payment))

    max_solve_zero_radius = F(0)
    max_payment_zero_radius = F(0)
    for i,row in enumerate(X):
        for j,cell in enumerate(row):
            value = literal(cell) # also checks the imaginary interval is exactly0
            if i//2 == j:
                require('native_nonzero_solve_entry_overlaps_independent',overlap(value,independent[j][2][i%2]))
            else:
                require('native_solve_structural_zero_contained',value.lo <= 0 <= value.hi)
                max_solve_zero_radius = max(max_solve_zero_radius,abs(value.lo),abs(value.hi))
    for i,row in enumerate(P):
        for j,cell in enumerate(row):
            value = literal(cell)
            if i == j:
                require('native_payment_entry_overlaps_independent',overlap(value,independent[i][3]))
            else:
                require('native_payment_structural_zero_contained',value.lo <= 0 <= value.hi)
                max_payment_zero_radius = max(max_payment_zero_radius,abs(value.lo),abs(value.hi))

    old = read(HERE/'INDEPENDENT_RESULTS.json')
    old_results = {r['profile_id']:r for r in old['results']}
    rows = []
    for k,p in enumerate(profiles):
        u,w,xx,qind = independent[k]
        nx = [literal(X[2*k+i][k]) for i in range(2)]
        for i in range(2):
            residual = u[i][0]*nx[0]+u[i][1]*nx[1]-w[i][0]
            require('native_solve_equation_residual_contains_zero',residual.lo <= 0 <= residual.hi)
        nq = literal(P[k][k])
        qfromnative = w[0][0]*nx[0]+w[1][0]*nx[1]
        require('native_payment_matches_actual_solve_contraction',overlap(nq,qfromnative))
        j11,j21,f11 = (literal(p[key]) for key in ('J11','J21','F11'))
        delta = w[1][1]-w[1][0].square()/w[0][0]
        s = j21-w[1][0]*j11/w[0][0]
        r5 = f11-nq-j11.square()/w[0][0]
        determinant = delta*r5-s.square()
        r6 = r5-s.square()/delta
        require('native_based_delta_positive',delta.lo > 0)
        require('native_based_R5_positive',r5.lo > 0)
        require('native_based_memory_block_determinant_positive',determinant.lo > 0)
        require('native_based_R6_positive',r6.lo > 0)
        previous = old_results[p['profile_id']]
        require('native_based_R5_overlaps_independent',overlap(r5,literal(previous['R5'])))
        require('native_based_R6_overlaps_independent',overlap(r6,literal(previous['R6'])))
        rows.append(dict(profile_id=p['profile_id'],native_projection_payment=nq.wire(),
            R5_from_native_payment=r5.wire(),R6_from_native_payment=r6.wire(),delta=delta.wire(),s=s.wire(),
            initial_memory_block_determinant=determinant.wire(),initial_memory_rank=2,
            minimum_invariant_extension_dimension_at_least=7))

    result = dict(schema='SAM_CH2_MEMORY_NATIVE_READBACK_V1',status='PASS',
        provenance='Readback of actual installed GEN6 Duck native solve/product; independent rational source contractions and zero-containment checks. No new native execution or source integration.',
        native_run=str(args.run),native_operations=['GEN3_COMPLEX_SOLVE','GEN3_COMPLEX_PRODUCT'],
        native_returns=2,native_matrix_entries_checked=2*n*n+n*n,
        nonzero_solve_entries_checked=2*n,native_projection_payments_checked=n,
        structural_zero_entries_checked=(2*n*n-2*n)+(n*n-n),
        preparations=n,positive_rank_two_initial_memory_blocks=n,
        exact_invariant_extension_dimension_at_least=7,
        maximum_solve_zero_enclosure_radius=str(max_solve_zero_radius),
        maximum_payment_zero_enclosure_radius=str(max_payment_zero_radius),
        checks_by_category=dict(COUNTS),total_independent_readback_checks=sum(COUNTS.values()),
        sources=[dict(role='original_source_operand_packet',path=source_relative(operand_path),sha256=sha(operand_path)),
                 dict(role='independent_rational_results',path=source_relative(HERE/'INDEPENDENT_RESULTS.json'),sha256=sha(HERE/'INDEPENDENT_RESULTS.json'))]+sources1+sources2,
        R5_range=dict(lower=str(min(F(r['R5_from_native_payment']['lower']) for r in rows)),upper=str(max(F(r['R5_from_native_payment']['upper']) for r in rows))),
        R6_range=dict(lower=str(min(F(r['R6_from_native_payment']['lower']) for r in rows)),upper=str(max(F(r['R6_from_native_payment']['upper']) for r in rows))),
        results=rows)
    result['verifier_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (HERE/'NATIVE_VERIFICATION.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(status=result['status'],native_returns=2,
        native_matrix_entries_checked=result['native_matrix_entries_checked'],
        nonzero_solve_entries_checked=2*n,native_projection_payments_checked=n,
        structural_zero_entries_checked=result['structural_zero_entries_checked'],
        positive_rank_two_blocks=n,total_independent_readback_checks=result['total_independent_readback_checks'],
        R5_range=[float(F(result['R5_range'][key])) for key in ('lower','upper')],
        max_zero_radius=float(max(max_solve_zero_radius,max_payment_zero_radius))),indent=2))


if __name__ == '__main__':
    main()
