#!/usr/bin/env python3
"""Independent dyadic rational verification of the retained source evaluations.

Checks invertibility and interpolation residual certificates without native
engines, flint, or floating point. Source-transcendental evaluation has its own
native receipt; this is independent certificate arithmetic, not a new integral.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,argparse
BITS=256;SCALE=1<<BITS
@dataclass(frozen=True)
class I:
 lo:F
 hi:F
 @staticmethod
 def make(v):
  if isinstance(v,I):return v
  if isinstance(v,dict):return I(F(v['lower']),F(v['upper']))
  return I(F(v),F(v))
 @staticmethod
 def rounded(lo,hi):
  return I(F((lo*SCALE).__floor__(),SCALE),F((hi*SCALE).__ceil__(),SCALE))
 def __add__(a,b):
  b=I.make(b);return I.rounded(a.lo+b.lo,a.hi+b.hi)
 __radd__=__add__
 def __neg__(a):return I(-a.hi,-a.lo)
 def __sub__(a,b):return a+-I.make(b)
 def __rsub__(a,b):return I.make(b)+-a
 def __mul__(a,b):
  b=I.make(b);v=[a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi];return I.rounded(min(v),max(v))
 __rmul__=__mul__
 def __truediv__(a,b):
  b=I.make(b);assert not b.contains0();return a*I(1/b.hi,1/b.lo)
 def contains0(a):return a.lo<=0<=a.hi
 def abs_upper(a):return max(abs(a.lo),abs(a.hi))
 def wire(a):return dict(lower=str(a.lo),upper=str(a.hi))

def inverse(a):
 n=len(a);rows=[[I.make(v) for v in row]+[I.make(i==j) for j in range(n)] for i,row in enumerate(a)]
 det=I.make(1);swaps=0
 for k in range(n):
  choices=[j for j in range(k,n) if not rows[j][k].contains0()];assert choices,('undecided interval pivot',k)
  p=max(choices,key=lambda j:min(abs(rows[j][k].lo),abs(rows[j][k].hi)))
  if p!=k:rows[k],rows[p]=rows[p],rows[k];swaps+=1
  pivot=rows[k][k];det*=pivot
  rows[k]=[v/pivot for v in rows[k]]
  for i in range(n):
   if i==k:continue
   factor=rows[i][k];rows[i]=[v-factor*w for v,w in zip(rows[i],rows[k])]
  # Known exact symbolic elimination entries prevent interval identity drift.
  for i in range(n):rows[i][k]=I.make(i==k)
 if swaps%2:det=-det
 assert not det.contains0()
 return det,[row[n:] for row in rows]

def verify(data):
 assert data['status']=='PASS' and data['full_background_multiplicities'] is True
 assert data['auxiliary_20_site_replacement'] is False
 rows=[[I.make(v) for v in row] for row in data['evaluation_rows']];cert=data['certificate'];selected=cert['row_indices'];n=len(data['basis'])
 m=[[rows[i][j] for j in range(n)] for i in selected]
 det,inv=inverse(m)
 assert max(det.lo,F(cert['determinant']['lower']))<=min(det.hi,F(cert['determinant']['upper']))
 # The true interval-enclosed inverse defines the exact interpolating functional.
 lam=inv[-1];norm_upper=sum(v.abs_upper()**2 for v in lam)
 assert norm_upper>0
 residual_chain=[]
 for dim in range(5,n,2):
  # V_dim uses the first dim polynomial columns. The next two operator
  # directions are exactly columns dim,dim+1; only the first is present at
  # the last odd stage n-1. Inverse rows annihilate the full retained span.
  targets=list(range(dim,min(dim+2,n)))
  denominator=sum(inv[j][i].abs_upper()**2 for j in targets for i in range(n))
  residual_chain.append(dict(retained_dimension=dim,
   operator_residual_rank_lower=len(targets),operator_residual_rank_upper=2,
   next_Krylov_dimension_lower=dim+len(targets),
   exact_rank=len(targets) if len(targets)==2 else None,
   positive_Gibbs_Gram_factor='exp(-N*log(2)-2*L)/witness_squared_Frobenius_norm_upper',
   witness_squared_Frobenius_norm_upper=str(denominator),
   target_columns=[data['basis'][j] for j in targets],
   inverse_witness_rows={str(j):[v.wire() for v in inv[j]] for j in targets}))
 # Endpoints/labels are actual literal configurations, not hypothetical probabilities.
 assert len(selected)==n and len(set(selected))==n
 job=data['source']['job'];N=int(job['N_exact']);assert int(job['free'])-6+2*(int(job['pairs'])+3)+3*int(job['triangles'])+20==N
 # Functional verification in interval arithmetic: exact target e_n is included.
 for j in range(n):
  value=sum((lam[i]*m[i][j] for i in range(n)),I.make(0));target=F(j==n-1)
  assert value.lo<=target<=value.hi
 return dict(schema='SAM_CH2_POINT_RANK_OFFLINE_VERIFICATION_V1',status='PASS',profile_id=data['profile_id'],
  rank_lower_bound=n,columns=data['basis'],independent_rational_checks=n+5+len(residual_chain),residual_chain=residual_chain,
  determinant=det.wire(),last_coordinate_annihilator=[v.wire() for v in lam],
  annihilator_squared_norm_upper=str(norm_upper),
  literal_Gibbs_residual_lower_bound='exp(-N*log(2)-2*L)/annihilator_squared_norm_upper',
  L='beta*(N+1)/2+g*(P_background+3*T)+4*sum_p(abs(t_p))+g+4*abs(zeta)',
  physical_meaning='Strictly positive exact full-source Gibbs residual; conservative bound uses full support, not a reweighted auxiliary source',
  closure_status='Displayed Krylov rank reached; invariance/stabilization not asserted',rational_precision_bits=BITS)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('certificate',type=Path);ap.add_argument('--output',type=Path);args=ap.parse_args()
 data=json.loads(args.certificate.read_text());out=verify(data);out['input']=dict(path=str(args.certificate),sha256=hashlib.sha256(args.certificate.read_bytes()).hexdigest())
 if args.output:args.output.write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:out[k] for k in ('status','profile_id','rank_lower_bound','independent_rational_checks')}))
if __name__=='__main__':main()
