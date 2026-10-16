#!/usr/bin/env python3
"""Independent exact energy-difference and inventory checks of physical source law.

All coefficients are rational in (beta,beta*kappa,epsilon,zeta). No native
engine, floating point, transcendental, or Gibbs integration is required.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import gzip,hashlib,json
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
FAMILIES=('R015','R016')+tuple('V%03d'%i for i in range(15))+('V017',)
PATTERNS=tuple(product((-1,1),repeat=4))
MASKS=[0x15556,0x25a59,0x38c5a,0x4c96d,0x52a66,0x6a599,0x7cc6a,0x89a95,0xa5696,0xbc5a9,0xd639a,0xe59a5]
def sigma(mask,i):return 1 if mask&(1<<i) else -1
def parity(p):
 v=1
 for s in p:v*=s
 return v
def magnetization(st,F):
 mask,nf,p,t=st
 return sum(sigma(mask,i) for i in range(20))+F-2*nf+sum((2-2*k)*n for k,n in enumerate(p))+sum((3-2*k)*n for k,n in enumerate(t))
def energy(st,N,F):
 mask,nf,p,t=st;s=[sigma(mask,i) for i in range(20)];M=magnetization(st,F)
 edges=sum(Q((b-2*k)**2-b,2)*n for b,c in ((2,p),(3,t)) for k,n in enumerate(c))
 hidden=[s[4+j]*sum(pp[i]*s[i] for i in range(4)) for j,pp in enumerate(PATTERNS)]
 return [Q(M*M-N,2*N),-2*edges-2*s[0]*s[1]+sum(hidden),sum(parity(pp)*v for pp,v in zip(PATTERNS,hidden)),(s[0]+s[1])*(s[2]+s[3])]
def transitions(st,N,F):
 mask,nf,p,t=st;s=[sigma(mask,i) for i in range(20)];M=magnetization(st,F);out=[]
 for j in range(20):
  sg=s[j]
  if j<4:
   hidden=sum(pp[j]*s[4+k] for k,pp in enumerate(PATTERNS));eh=sum(parity(pp)*pp[j]*s[4+k] for k,pp in enumerate(PATTERNS))
   field=[Q(M-sg,N),hidden-(2*s[1-j] if j<2 else 0),eh,sum(s[2:4]) if j<2 else sum(s[:2])]
  else:
   pp=PATTERNS[j-4];v=sum(pp[k]*s[k] for k in range(4));field=[Q(M-sg,N),v,parity(pp)*v,0]
  out.append((1,sg,field,(mask^(1<<j),nf,p,t)))
 for sg,num,newnf in ((1,F-nf,nf+1),(-1,nf,nf-1)):
  if num:out.append((num,sg,[Q(M-sg,N),0,0,0],(mask,newnf,p,t)))
 for b,c in ((2,p),(3,t)):
  for k,num in enumerate(c):
   if not num:continue
   for sg,nsite,dest in ((1,b-k,k+1),(-1,k,k-1)):
    if not nsite:continue
    cc=list(c);cc[k]-=1;cc[dest]+=1
    new=(mask,nf,tuple(cc),t) if b==2 else (mask,nf,p,tuple(cc))
    out.append((num*nsite,sg,[Q(M-sg,N),-2*(b-2*k-sg),0,0],new))
 return out

def main():
 rows=[];checks=0
 for family in FAMILIES:
  for suffix in ('BASE','H_MINUS','H_PLUS'):
   ident=family+'_'+suffix;p=ROOT/'GEN4/spin_conditional_variance1/sources/original'/(ident+'.json.gz');raw=p.read_bytes();job=json.loads(gzip.decompress(raw))['job']
   N=int(job['N_exact']);F=int(job['free'])-6;P=int(job['pairs'])+3;T=int(job['triangles']);assert F+2*P+3*T+20==N
   local=0
   for mask in MASKS:
    # Exercise occupied positive/negative classes for each original block size.
    initial=(mask,0,(P,0,0),(T,0,0,0))
    perturb=(mask,1,(P-2,1,1),(T-3,1,1,1))
    for st in (initial,perturb):
     a=energy(st,N,F);moves=transitions(st,N,F);assert sum(v[0] for v in moves)==N;local+=1
     for multiplicity,sg,field,new in moves:
      assert multiplicity>0
      delta=[x-y for x,y in zip(a,energy(new,N,F))]
      assert delta==[2*sg*x for x in field],(ident,st,new,delta,field)
      local+=1
   checks+=local
   rows.append(dict(profile_id=ident,checks=local,source=dict(path=str(p.relative_to(ROOT)),sha256=hashlib.sha256(raw).hexdigest())))
 out=dict(schema='SAM_ACTUAL_FINITE_N_SOURCE_LAW_CHECKS_V1',status='PASS',preparations=len(rows),independent_exact_rational_checks=checks,
  coefficient_basis=['beta','beta*kappa','epsilon','zeta'],identity='Phi(x)-Phi(x^i)=2*sigma_i*F_i(x)',
  rate_consequence='r_i(x)=1/(1+exp(Phi(x)-Phi(x^i)))=(1-sigma_i*tanh(F_i(x)))/2',
  normalization_check='Every summed site-class multiplicity adds to original N; original A=N(I-P_transition)',rows=rows)
 (HERE/'SOURCE_LAW_VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:out[k] for k in ('status','preparations','independent_exact_rational_checks')}))
if __name__=='__main__':main()
