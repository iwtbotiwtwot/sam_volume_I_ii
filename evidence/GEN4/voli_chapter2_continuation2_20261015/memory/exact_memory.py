#!/usr/bin/env python3
"""Independent, standard-library checks of source-bound initial memory.

No source integration or native execution is performed. Complete source
enclosures are reduced with exact rational interval arithmetic. This is an
independent contraction check, separate from the parent's native arithmetic.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import gzip
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
FAMILIES = ('R015', 'R016') + tuple('V%03d' % i for i in range(15)) + ('V017',)
PROFILES = tuple(f + '_' + s for f in FAMILIES for s in ('BASE', 'H_MINUS', 'H_PLUS'))


@dataclass(frozen=True)
class I:
    lo: F
    hi: F

    @staticmethod
    def make(x):
        if isinstance(x, I):
            return x
        if isinstance(x, dict):
            if 're' in x:
                assert F(x['im']['lower']) == F(x['im']['upper']) == 0
                x = x['re']
            return I(F(x['lower']), F(x['upper']))
        return I(F(x), F(x))

    def __add__(self, other):
        b = I.make(other)
        return I(self.lo + b.lo, self.hi + b.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -I.make(other)

    def __rsub__(self, other):
        return I.make(other) + -self

    def __mul__(self, other):
        b = I.make(other)
        v = (self.lo*b.lo, self.lo*b.hi, self.hi*b.lo, self.hi*b.hi)
        return I(min(v), max(v))

    __rmul__ = __mul__

    def __truediv__(self, other):
        b = I.make(other)
        assert b.lo > 0 or b.hi < 0
        return self * I(1/b.hi, 1/b.lo)

    def square(self):
        if self.lo <= 0 <= self.hi:
            return I(F(0), max(self.lo*self.lo, self.hi*self.hi))
        return I(min(self.lo*self.lo, self.hi*self.hi), max(self.lo*self.lo, self.hi*self.hi))

    def wire(self):
        return dict(lower=str(self.lo), upper=str(self.hi))

    def approx(self):
        return [float(self.lo), float(self.hi)]


def read(path):
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract():
    sources = {}
    profiles = []

    def bind(path, role):
        rel = str(path.relative_to(ROOT))
        sources[rel] = dict(path=rel, original_path=str(path), sha256=sha(path), bytes=path.stat().st_size, role=role)
        return read(path)

    for ident in PROFILES:
        family = ident.split('_')[0]
        oldp = ROOT/'GEN4/spin_difference_fifth1/native1'/family/(ident+'_RESULT.json.gz')
        newp = ROOT/'GEN4/spin_upper_source1_20261014'/('pilot3' if family == 'V000' else 'native1')/family/(ident+'_RESULT.json.gz')
        prep = ROOT/'GEN4/spin_conditional_variance1/sources/original'/(ident+'.json.gz')
        gp = ROOT/'GEN4/duck_spin_connections1/field_gamma'/(family+'.json')
        old = bind(oldp, 'completed G5,D5,W original source')['output']
        new = bind(newp, 'completed J21,F11 original source')['output']
        source = bind(prep, 'original N and preparation')
        gamma = bind(gp, 'original odd-sector gap')
        assert old['profile_id'] == new['profile_id'] == source['profile_id'] == ident
        assert ident in [x['profile_id'] for x in gamma['covered_preparations']]
        G, D, W = old['G5']['entries'], old['D5']['entries'], old['projected_matrices']['W']['entries']
        assert old['G5']['row_basis'] == ['d','e','u_d','u_e','g1']
        assert old['G5']['column_basis'] == old['G5']['row_basis']
        # g1 is exactly w_d in the completed fifth-direction source.
        for i in range(5):
            for j in range(5):
                if (i < 2) != (j < 2) or (i == 4) != (j == 4):
                    assert I.make(G[i][j]) == I.make(0)
        profiles.append(dict(profile_id=ident, N_exact=source['job']['N_exact'], gamma_lower=gamma['gamma_lower'],
            U=[[G[i][j] for j in (2,3)] for i in (2,3)], W=W,
            J11=D[4][4], J21=new['J21'], F11=new['F11'],
            source_paths=[str(p.relative_to(ROOT)) for p in (oldp,newp,prep,gp)]))
    return dict(schema='SAM_CH2_INITIAL_MEMORY_OPERANDS_V1', basis5=['d','e','u_d','u_e','w_d'],
        basis6=['d','e','u_d','u_e','w_d','w_e'], sources=list(sources.values()), profiles=profiles,
        meaning='Exact selected enclosures from completed source; no reintegration, eigenvalue fit, or native launch')


def contract(p):
    u = [[I.make(x) for x in row] for row in p['U']]
    w = [[I.make(x) for x in row] for row in p['W']]
    j11, j21, f11 = (I.make(p[k]) for k in ('J11','J21','F11'))
    detu = u[0][0]*u[1][1] - u[0][1]*u[1][0]
    assert detu.lo > 0 and w[0][0].lo > 0
    # k^T G4^-1 k, exploiting only the exactly retained block orthogonality.
    qproj = (u[1][1]*w[0][0].square() -(u[0][1]+u[1][0])*w[0][0]*w[1][0] +u[0][0]*w[1][0].square())/detu
    r5 = f11 - qproj - j11.square()/w[0][0]
    delta = w[1][1] - w[1][0].square()/w[0][0]
    s = j21 - w[1][0]*j11/w[0][0]
    gain = s.square()/delta
    r6 = r5 - gain
    assert delta.lo > 0
    assert r5.lo > 0 and r6.lo > 0
    determinant = delta*r5-s.square()
    assert determinant.lo > 0
    normalized = r5/w[0][0]
    # Nonzero spectrum of G5^-1 K0: the u_e,w_d inverse-Gram block is
    # diag(U11/det(U),1/W11), not diag(1/U22,1/W11).
    a, b = u[0][0]/detu, I.make(1)/w[0][0]
    trace = a*delta+b*r5
    norm_lower = max((a*delta).lo, (b*r5).lo)
    norm_upper = trace.hi
    assert normalized.lo > 0 and norm_lower <= norm_upper
    return dict(profile_id=p['profile_id'], R5=r5.wire(), R6=r6.wire(), delta=delta.wire(), s=s.wire(),
        projection_cost_b4=qproj.wire(), norm_wd=w[0][0].wire(), b6_extra_payment=gain.wire(),
        K0_block_determinant=determinant.wire(), normalized_wd_memory=normalized.wire(),
        K0_norm_bounds=dict(lower=str(norm_lower), upper=str(norm_upper)),
        compressed_scalar_second_order_coefficient=(normalized/I.make(2)).wire(),
        N_exact=p['N_exact'], gamma_lower=p['gamma_lower'],
        approximations={k:v.approx() for k,v in [('R5',r5),('R6',r6),('delta',delta),('s',s),('normalized_wd_memory',normalized)]},
        native_requested=dict(solve_U_rhs=[p['W'][0][0],p['W'][1][0]], contractions=['projection_cost_b4','R5','delta','s','R6']))


def run(operands):
    results = [contract(p) for p in operands['profiles']]
    checks = 0
    # Additional source-specific agreement with the six completed b6 floor
    # pilots; these are the original native Fexcess enclosures, not our output.
    split_path = ROOT/'GEN4/duck_spin_upper1_20261014/SOURCE_ACTION_SPLIT.json'
    if split_path.exists():
        split = read(split_path)
    else:
        split = read(HERE/'INHERITED_B6_FEXCESS.json')
    by_profile = {r['profile_id']:r for r in results}
    inherited = []
    for ident in sorted({r['profile'] for r in split}):
        r = next(x for x in split if x['profile'] == ident)
        x = I(F(r['Fexcess'][0]), F(r['Fexcess'][1]))
        own = I.make(by_profile[ident]['R6'])
        assert max(x.lo,own.lo) <= min(x.hi,own.hi)
        inherited.append(dict(profile_id=ident, Fexcess=x.wire()))
        checks += 1
    # Each profile: exact-zero retained block structure is checked on extract;
    # 8 numerical positivity/nonclosure and source-pilot checks follow here.
    checks += 8*len(results)
    return dict(schema='SAM_CH2_INITIAL_MEMORY_CHECKS_V1', status='PASS', independent_checks=checks,
        preparations=len(results), nonzero_b5_initial_memory=len(results), nonzero_b6_wd_residual=len(results),
        initial_memory_block_rank=2, minimum_invariant_extension_dimension_at_least=7,
        numerical_role='Independent exact rational interval contraction; parent native run has separate provenance',
        R5_range=dict(lower=str(min(F(r['R5']['lower']) for r in results)),upper=str(max(F(r['R5']['upper']) for r in results))),
        R6_range=dict(lower=str(min(F(r['R6']['lower']) for r in results)),upper=str(max(F(r['R6']['upper']) for r in results))),
        inherited_b6_pilots=inherited, results=results)


def main():
    operand_path = HERE/'SOURCE_OPERANDS.json'
    if operand_path.exists():
        operands = read(operand_path)
    else:
        operands = extract()
        operand_path.write_text(json.dumps(operands,indent=2,sort_keys=True)+'\n')
    for item in operands['sources']:
        path = ROOT/item['path']
        if path.exists():
            assert sha(path) == item['sha256'], str(path)
    result = run(operands)
    result['source_operands_sha256'] = sha(operand_path)
    split_path = ROOT/'GEN4/duck_spin_upper1_20261014/SOURCE_ACTION_SPLIT.json'
    if split_path.exists():
        # Retain only actual pilot scalar enclosures for self-contained replay.
        selected = []
        rows = read(split_path)
        for ident in sorted({r['profile'] for r in rows}):
            selected.append(next(r for r in rows if r['profile'] == ident))
        (HERE/'INHERITED_B6_FEXCESS.json').write_text(json.dumps(selected,indent=2,sort_keys=True)+'\n')
        result['inherited_b6_source'] = dict(path=str(split_path.relative_to(ROOT)),sha256=sha(split_path))
    (HERE/'INDEPENDENT_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:result[k] for k in ('status','independent_checks','preparations','nonzero_b5_initial_memory','initial_memory_block_rank','R5_range','R6_range')}))


if __name__ == '__main__':
    main()
