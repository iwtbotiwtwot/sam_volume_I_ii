#!/usr/bin/env python3
"""Reconstruct Chapter 2 algebra. Does not run any original repository code."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import sympy as s

root = Path(__file__).resolve().parents[1]
checks = []
def require(name, condition):
    if not bool(condition):
        raise AssertionError(name)
    checks.append(name)

h, d = 2, 3
radix = h*h*d
grid = [(a,b,h**a*d**b) for a in range(d+1) for b in range(d)]
retained = sorted(v for a,b,v in grid if v <= radix)
overflow = sorted(v for a,b,v in grid if v > radix)
require('radix', radix == 12)
require('complete_bounded_grid_size', len(grid) == 12)
require('retained_values', retained == [1,2,3,4,6,8,9,12])
require('overflow_values', overflow == [18,24,36,72])
require('sixteen_excluded', 16 not in [v for a,b,v in grid])
require('sixteen_is_unrestricted_counterexample', 12 < 2**4 < min(overflow))
require('first_admitted_overflow', min(overflow) == h*d*d == 18)
require('closure', d**(d-1) == h**d+1 == 9)
# Regression checks supplement the analytical full-domain proof in the chapter.
require('fixed_binary_closure_scan', [n for n in range(2,101) if n**(n-1)==2**n+1] == [3])
require('fixed_binary_inequality_scan', all(n**(n-1)>=4**(n-1)==2**(2*n-2)>=4*2**n>2**n+1 for n in range(4,101)))
require('minimal_exchange_scan', min(n for n in range(1,101) if n>1 and n%2==0)==2)
require('declared_dimension_predicates', [n for n in range(1,101) if n>=2 and n>=3 and n<=3]==[3])
require('full_phase_return', s.exp(2*s.pi*s.I)==1)
require('half_phase_not_return', s.exp(s.pi*s.I)==-1)
require('double_phase_return', s.exp(4*s.pi*s.I)==1)
N=radix**2; theta=min(overflow); nret=N-theta
require('square_capacity', N==144)
require('carrier_fraction', F(theta,N)==F(1,8)==F(1,2**d))
require('retained_fraction', nret==126 and F(nret,N)==F(7,8))
require('carrier_units', (F(nret,theta),F(N,theta))==(7,8))
ledger=h*d**(d+1)
require('closed_ledger', ledger==162 and ledger-theta==N and nret+theta==N)
require('shares', 2*F(1,2*radix)==F(1,radix))
A0=1/(12*s.pi)
require('compact_cycle_floor', s.simplify(1/(2*s.pi*h*d)-A0)==0)
require('radix_floor', s.simplify(1/(s.pi*radix)-A0)==0)
require('spherical_projection', s.simplify(1/(4*s.pi*d)-A0)==0)
require('radix_floor_product', s.simplify(radix*A0-1/s.pi)==0)
hh,dd=s.symbols('h d',positive=True)
require('binary_factor_equivalence_only_at_two', s.factor(hh**2-2*hh)==hh*(hh-2))
b,a1,a2=s.symbols('b a1 a2', real=True)
require('linear_difference', s.expand((b+a2)-(b+a1))==a2-a1)
raw=(1-b-a2)/(1-b-a1)
scaled=(1-a2/(1-b))/(1-a1/(1-b))
lift=(1-a2)/(1-a1)
require('nonlinear_factorization_squared', s.simplify(raw-scaled)==0)
example={b:s.Rational(1,4),a1:s.Rational(1,8),a2:s.Rational(1,4)}
require('raw_ratio_counterexample_squared', raw.subs(example)==s.Rational(4,5))
require('lift_ratio_counterexample_squared', lift.subs(example)==s.Rational(6,7))
require('nonlinear_non_cancellation', s.simplify(raw-lift)!=0)
x=s.symbols('x'); f=s.Function('f')
require('uniform_gradient', s.diff(b+f(x),x)==s.diff(f(x),x))

manifest=json.loads((root/'sources/source_manifest.json').read_text())
custody=[]
for item in manifest['sources']:
    path=root/'sources'/item['filename']
    data=path.read_bytes()
    digest=hashlib.sha256(data).hexdigest()
    require('sha256:'+item['filename'],digest==item['sha256'])
    blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    expected=item.get('git_blob_sha_returned')
    if expected: require('git_blob:'+item['filename'],blob==expected)
    custody.append({'file':item['filename'],'sha256':digest,'git_blob_verified':bool(expected)})
print(json.dumps({'status':'PASS','assertions_passed':len(checks),'checks':checks,
    'bounded_grid':grid,'retained':retained,'overflow':overflow,
    'floor_decimal_display':str(s.N(A0,40)), 'source_custody':custody,
    'scope':['Independent algebra reconstruction, not an original GEN6 campaign.',
             'Finite scans are regression controls; analytical proofs are in the manuscript.',
             'No physical premise necessity, topological exhaustiveness, or empirical agreement is proved.',
             'Hash matches establish snapshot integrity, not scientific validity.'],
    'sympy_version':s.__version__},indent=2))
