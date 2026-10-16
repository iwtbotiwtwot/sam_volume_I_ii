"""Portable independent exact kernel identities and frozen-input arithmetic.
This checks the stated Poisson model; it does not run the historical CR004 test.
"""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D,localcontext
import json,hashlib
BASE=Path(__file__).resolve().parents[1];checks=[]
def ok(n,b):assert b,n;checks.append(n)
def derivative(p):return {k-1:v*k for k,v in p.items() if k and v}
def scale(p,s):return {k:v*s for k,v in p.items() if v*s}
def add(p,q):
 z=dict(p)
 for k,v in q.items():z[k]=z.get(k,F(0))+v
 return {k:v for k,v in z.items() if v}
def shift(p,n):return {k+n:v for k,v in p.items()}
def laplacian(p):return add(derivative(derivative(p)),scale(shift(derivative(p),-1),F(2)))
def at(p,x):return sum(v*x**k for k,v in p.items())
def integral01(p):return sum(v/F(k+1) for k,v in p.items())
a_inside={0:F(3),2:F(-1)};a_outside={-1:F(2)}
ok('uniform ball Laplacian exactly minus6',laplacian(a_inside)=={0:F(-6)})
ok('exterior exact vacuum',laplacian(a_outside)=={})
ok('surface value continuous',at(a_inside,F(1))==at(a_outside,F(1))==2)
ok('surface gradient continuous',at(derivative(a_inside),F(1))==at(derivative(a_outside),F(1))==-2)
ok('center potential3',at(a_inside,F(0))==3)
ok('center force zero',at(derivative(a_inside),F(0))==0)
# rho volume weight 3r^2; U/(GM²/b)=−1/4 integral 3r² alpha dr.
ok('uniform ball binding energy exactly minus3/5',-F(1,4)*integral01(scale(shift(a_inside,2),F(3)))==-F(3,5))
for p in range(-3,8):
 trial={-p:F(1)}
 expected={} if p*(p-1)==0 else {-p-2:F(p*(p-1))}
 ok('power Laplacian '+str(p),laplacian(trial)==expected)
for q in [F(0),F(1),F(2),F(5,2),F(3)]:
 ok('cusp mass exponent '+str(q),(2-q>-1)==(q<3))
 ok('cusp potential exponent '+str(q),(1-q>-1)==(q<2))
 ok('cusp field energy exponent '+str(q),(4-2*q>-1)==(q<F(5,2)))
source=BASE/'inputs/CR004_declared_premises.json'
d=json.loads(source.read_text(),parse_float=D,parse_int=D);rows=[]
with localcontext() as ctx:
 ctx.prec=60;c=d['constants']['c']
 for body in d['bodies']:
  mu=body['mu_m3_s2'];b=body['radius_m'];rs=2*mu/(c*c);a=rs/b;g=mu/(b*b);vesc=(2*mu/b).sqrt()
  ok(body['name']+' force range',body['surface_g_range_m_s2'][0]<=g<=body['surface_g_range_m_s2'][1])
  ok(body['name']+' escape range',body['escape_speed_range_m_s'][0]<=vesc<=body['escape_speed_range_m_s'][1])
  ok(body['name']+' dimensionless speed identity',abs(vesc*vesc-c*c*a)<D('1e-40'))
  ok(body['name']+' mass flux normalization',abs(-c*c*b*b*(-rs/(b*b))/(2*mu)-1)<D('1e-55'))
  rows.append(dict(name=body['name'],source_length_m=str(rs),lift=str(a),acceleration_m_s2=str(g),escape_m_s=str(vesc)))
result=dict(schema='SAM_CH3_CORE_AND_FROZEN_ARITHMETIC_V1',status='PASS',checks_passed=len(checks),checks=checks,arithmetic=rows,source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),scope='Exact Laurent-polynomial identities and independent decimal recomputation of retained CR004 premises, no historical runner or physical experiment')
(BASE/'core/RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(dict(status='PASS',checks=len(checks),rows=rows)))
