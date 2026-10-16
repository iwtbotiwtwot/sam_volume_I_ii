#!/usr/bin/env python3
"""Exact finite ambient upper bounds for the original-source invariant closure.

No generator or scientific source integral is executed. Integer combinatorics
bounds the existing exchangeable source representation from literal inventories.
"""
from pathlib import Path
from math import comb
import gzip,hashlib,json
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
FAMILIES=('R015','R016')+tuple('V%03d'%i for i in range(15))+('V017',)
def main():
 rows=[]
 for family in FAMILIES:
  for suffix in ('BASE','H_MINUS','H_PLUS'):
   ident=family+'_'+suffix;p=ROOT/'GEN4/spin_conditional_variance1/sources/original'/(ident+'.json.gz');raw=p.read_bytes();job=json.loads(gzip.decompress(raw))['job']
   N=int(job['N_exact']);F=int(job['free'])-6;P=int(job['pairs'])+3;T=int(job['triangles']);assert F+2*P+3*T+20==N
   # Individual core spin assignments; number of multisets of block occupancies.
   D=(1<<20)*(F+1)*comb(P+2,2)*comb(T+3,3)
   assert D<2**(20+6*N.bit_length()) # coarse integer-only sanity bound, not scientific estimate
   rows.append(dict(profile_id=ident,N_exact=str(N),free_blocks=str(F),pair_blocks=str(P),triangle_blocks=str(T),
    explicit_invariant_lumped_dimension_upper=str(D),decimal_digits=len(str(D)),
    source=dict(path=str(p.relative_to(ROOT)),sha256=hashlib.sha256(raw).hexdigest())))
 out=dict(schema='SAM_CH2_EXACT_SOURCE_LUMPED_CLOSURE_UPPER_V1',status='PASS',preparations=len(rows),
  meaning='Explicit exact invariant exchangeable source space, not a claim that every state is reached by d/e',
  dimension_formula='2^20*(F_b+1)*binomial(P_b+2,2)*binomial(T_b+3,3)',
  follows_from='Uniform physical heatbath is equivariant under permutations of free sites, complete pair blocks and complete triangle blocks; d/e are fixed by these permutations',
  independence_from_Gibbs='The full generator includes exact site multiplicities and physical self-excluded field; Gibbs orthogonality is needed only when forming projected residual norms',rows=rows)
 (HERE/'EXACT_LUMPED_UPPER_BOUND.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(dict(status='PASS',preparations=len(rows),dimension_digit_range=[min(r['decimal_digits'] for r in rows),max(r['decimal_digits'] for r in rows)])))
if __name__=='__main__':main()
