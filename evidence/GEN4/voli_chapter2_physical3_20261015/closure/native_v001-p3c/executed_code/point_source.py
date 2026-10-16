#!/usr/bin/env python3
"""Literal finite-N heatbath Krylov evaluations; no auxiliary field or Gibbs integration.

The background is lumped by exchangeable block occupancies. Every site appears
with its exact integer multiplicity. Core sites remain individually labelled.
"""
from __future__ import annotations
from pathlib import Path
from functools import lru_cache
import gzip,hashlib,json,time,argparse
from flint import arb,arb_mat,ctx
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PATTERN=tuple(tuple(2*((p>>(3-j))&1)-1 for j in range(4)) for p in range(16))
def read(p):
 b=Path(p).read_bytes();return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)
def exact(v):
 a,b=str(v).split('/') if '/' in str(v) else (str(v),'1');return arb(int(a))/int(b)
def wire(x):
 # Endpoints of Arb enclosures are exact dyadics, serialized as rationals.
 def f(v):
  a,b=v.man_exp();return str(int(a)*(2**int(b))) if b>=0 else str(int(a))+'/'+str(2**(-int(b)))
 return dict(lower=f(x.lower()),upper=f(x.upper()))
def spin(mask,j):return 2*((mask>>j)&1)-1
class OriginalSource:
 def __init__(self,job):
  self.job=job;self.N=int(job['N_exact']);self.F=int(job['free'])-6;self.P=int(job['pairs'])+3;self.T=int(job['triangles'])
  assert self.F+2*self.P+3*self.T+20==self.N
  self.beta=exact(job['beta']);self.a=self.beta/self.N;self.kap=arb(3).log()*15/128
  self.g=2*self.beta*self.kap;self.ep=exact(job['epsilon_exact']);self.zeta=exact(job['zeta_exact'])
  self.t=tuple(self.beta*self.kap+self.ep*((-1)**p.bit_count()) for p in range(16))
  self.count_calls=0
 def initial(self,core_mask,negative_free=0,pair_minus=None,triangle_minus=None):
  # Occupancy k denotes the number of negative spins in an exchangeable block.
  return (core_mask,negative_free,tuple(pair_minus or (self.P,0,0)),tuple(triangle_minus or (self.T,0,0,0)))
 @lru_cache(maxsize=None)
 def info(self,state):
  mask,nf,np,nt=state;s=tuple(spin(mask,j) for j in range(20))
  M=sum(s)+self.F-2*nf+sum((2-2*k)*n for k,n in enumerate(np))+sum((3-2*k)*n for k,n in enumerate(nt))
  fields=[]
  for j in range(4):
   short=sum((self.t[p]*PATTERN[p][j]*s[4+p] for p in range(16)),arb(0))
   short+=self.zeta*(s[2]+s[3] if j<2 else s[0]+s[1])
   if j<2:short-=self.g*s[1-j]
   fields.append(self.a*(M-s[j])+short)
  for p in range(16):fields.append(self.a*(M-s[4+p])+self.t[p]*sum(PATTERN[p][j]*s[j] for j in range(4)))
  return s,M,tuple(fields)
 def rate(self,s,field):return (1-s*field.tanh())/2
 @lru_cache(maxsize=None)
 def transitions(self,state):
  mask,nf,np,nt=state;s,M,fields=self.info(state);out=[]
  for j in range(20):out.append((self.rate(s[j],fields[j]),(mask^(1<<j),nf,np,nt)))
  for sg,count,newnf in ((1,self.F-nf,nf+1),(-1,nf,nf-1)):
   if count:out.append((count*self.rate(sg,self.a*(M-sg)),(mask,newnf,np,nt)))
  for size,counts in ((2,np),(3,nt)):
   for k,num in enumerate(counts):
    if not num:continue
    for sg,nsite,dest in ((1,size-k,k+1),(-1,k,k-1)):
     if not nsite:continue
     field=self.a*(M-sg)-self.g*(size-2*k-sg)
     changed=list(counts);changed[k]-=1;changed[dest]+=1
     new=(mask,nf,tuple(changed),nt) if size==2 else (mask,nf,np,tuple(changed))
     out.append((num*nsite*self.rate(sg,field),new))
  return tuple(out)
 @lru_cache(maxsize=None)
 def value(self,power,state):
  self.count_calls+=1
  mask=state[0];d=spin(mask,1)-spin(mask,0);e=d*spin(mask,2)*spin(mask,3)
  if power==0:return arb(d),arb(e)
  if power==1:
   # Only the four ports change d/e, eliminating exactly-zero other terms.
   s,M,fields=self.info(state);v=[arb(0),arb(0)]
   for j in range(4):
    r=self.rate(s[j],fields[j]);post=mask^(1<<j)
    dp=spin(post,1)-spin(post,0);ep=dp*spin(post,2)*spin(post,3)
    v[0]+=r*(d-dp);v[1]+=r*(e-ep)
   return tuple(v)
  old=self.value(power-1,state);v=[arb(0),arb(0)]
  for rate,new in self.transitions(state):
   post=self.value(power-1,new)
   for c in range(2):v[c]+=rate*(old[c]-post[c])
  return tuple(v)
 def feature(self,state,max_power):
  return [v for power in range(max_power+1) for v in self.value(power,state)]

def calculate(profile='V001_BASE',max_power=3,masks=None,precision=1024):
 ctx.prec=precision;ctx.threads=1;start=time.monotonic()
 p=ROOT/'GEN4/spin_conditional_variance1/sources/original'/(profile+'.json.gz');raw=read(p);source=OriginalSource(raw['job'])
 # Fixed, declared actual configurations; no fitted test state or thermodynamic limit.
 masks=masks or [0x15556,0x25a59,0x38c5a,0x4c96d,0x52a66,0x6a599,0x7cc6a,0x89a95,0xa5696,0xbc5a9,0xd639a,0xe59a5]
 n=2*(max_power+1);rows=[];configs=[]
 for mask in masks:
  state=source.initial(mask);row=source.feature(state,max_power);rows.append(row)
  configs.append(dict(core_mask=mask,free_minus=0,pair_minus=list(state[2]),triangle_minus=list(state[3])))
 # Independent columns require one nonzero square minor. Deterministic combinations.
 from itertools import combinations
 cert=None
 for selected in combinations(range(len(rows)),n):
  m=arb_mat([[rows[i][j] for j in range(n)] for i in selected]);det=m.det()
  if not det.contains(0):cert=dict(row_indices=list(selected),determinant=wire(det));break
 return dict(schema='SAM_ACTUAL_FINITE_N_KRYLOV_POINT_CERTIFICATE_V1',status='PASS' if cert else 'UNRESOLVED',profile_id=profile,N_exact=str(source.N),
  source=dict(path=str(p.relative_to(ROOT)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),job=raw['job']),
  source_law='A=sum_i r_i(s)[f(s)-f(s^i)]=N(I-P_transition); physical self-excluded fields; all N sites retained',
  basis=[('d' if c==0 else 'e') if power==0 else f'A^{power}'+('d' if c==0 else 'e') for power in range(max_power+1) for c in range(2)],
  configurations=configs,evaluation_rows=[[wire(v) for v in row] for row in rows],certificate=cert,
  rank_lower_bound=n if cert else None,precision_bits=precision,states_evaluated=source.count_calls,seconds=time.monotonic()-start,
  full_background_multiplicities=True,auxiliary_20_site_replacement=False,
  seven_dimension_residual='Nonzero because A^3 e is not in V7=span(d,e,Ad,Ae,A^2d,A^2e,A^3d)' if cert and max_power>=3 else 'UNRESOLVED',
  closure_status='Only the displayed rank lower bound is certified. Invariant rank stabilization is not asserted.')

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--profile',default='V001_BASE');ap.add_argument('--power',type=int,default=3);ap.add_argument('--precision',type=int,default=1024);ap.add_argument('--output',type=Path);args=ap.parse_args()
 out=calculate(args.profile,args.power,precision=args.precision)
 if args.output:args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:out[k] for k in ('status','profile_id','rank_lower_bound','states_evaluated','seconds')}),flush=True)
if __name__=='__main__':main()
