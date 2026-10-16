#!/usr/bin/env python3
"""Independent rational Laurent-polynomial check of the static field source."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent
checks=[]
def check(name,test):
    if not test: raise AssertionError(name)
    checks.append(name)
def clean(p): return {k:v for k,v in p.items() if v}
def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items(): out[k]=out.get(k,F(0))+v
    return clean(out)
def scale(a,p): return clean({k:a*v for k,v in p.items()})
def mul(p,q):
    out={}
    for i,a in p.items():
        for j,b in q.items(): out[i+j]=out.get(i+j,F(0))+a*b
    return clean(out)
def der(p): return clean({k-1:k*v for k,v in p.items()})
def lap(p): return add(der(der(p)),scale(2,mul({-1:F(1)},der(p))))
def at(p,x): return sum((v*x**k for k,v in p.items()),F(0))
def integ01(p):
    if any(k<=-1 for k in p): raise ValueError('divergent lower endpoint')
    return sum((v/F(k+1) for k,v in p.items()),F(0))
def integ1inf(p):
    if any(k>=-1 for k in p): raise ValueError('divergent upper endpoint')
    return -sum((v/F(k+1) for k,v in p.items()),F(0))
def integ(p,a,b):
    if -1 in p: raise ValueError('log term outside rational scope')
    return sum((v*(b**(k+1)-a**(k+1))/F(k+1) for k,v in p.items()),F(0))
def anti(p):
    if -1 in p: raise ValueError('log primitive outside rational scope')
    return {k+1:v/F(k+1) for k,v in p.items()}
def wire(p): return {str(k):str(v) for k,v in sorted(p.items())}
def solve(a,b):
    w=[list(map(F,row))+[F(b[i])] for i,row in enumerate(a)]
    n=len(b)
    for j in range(n):
        i=next(i for i in range(j,n) if w[i][j]); w[i],w[j]=w[j],w[i]
        q=w[j][j]; w[j]=[x/q for x in w[j]]
        for i in range(n):
            if i!=j:
                q=w[i][j]; w[i]=[x-q*y for x,y in zip(w[i],w[j])]
    return [r[-1] for r in w]

def main():
    kappa=F(4,5)
    phi_in={2:F(1)}; phi_out={-3:F(1)}
    e=lambda p:scale(kappa/4,add(mul({2:F(1)},mul(der(p),der(p))),scale(6,mul(p,p))))
    uin=e(phi_in); uout=e(phi_out)
    Uin=integ01(uin); Uout=integ1inf(uout); U=Uin+Uout
    check('field is continuous at physical source interface',at(phi_in,F(1))==at(phi_out,F(1)))
    check('derivative jump retains the source forcing',at(der(phi_out),F(1))-at(der(phi_in),F(1))==-5)
    check('positive free field inside density from derivative and angular terms',uin=={4:F(2)})
    check('positive free field outside density from derivative and angular terms',uout=={-6:F(3)})
    check('inside energy fraction',Uin==F(2,5))
    check('outside energy fraction',Uout==F(3,5))
    check('positive total free energy is X2/R for kappa4/5',U==1)
    eps=F(1,7); currents=[F(2,3),F(-5,4)]; Rstatic=F(3,8)
    xs=[eps*j/2 for j in currents]
    Ufree=sum(x*x for x in xs)/Rstatic
    Uint=-eps*sum(j*x for j,x in zip(currents,xs))/Rstatic
    Uct=eps**2*sum(j*j for j in currents)/(4*Rstatic)
    check('commuting-current static boundary jump',all(5*x==2*eps*j/kappa for j,x in zip(currents,xs)))
    check('commuting static interaction is minus twice positive free energy',Uint==-2*Ufree)
    check('commuting static counterterm equals positive free energy',Uct==Ufree)
    check('commuting three term static package cancels',Ufree+Uint+Uct==0)
    rhoin=mul(uin,{-2:F(1)})  # 4pi R^3 rho/Mf
    rhoout=mul(uout,{-2:F(1)})
    muin=anti(uin)
    # Match cumulative mass at 1; primitive outside is -(3/5)x^-5.
    muout=add(anti(uout),{0:Uin-at(anti(uout),F(1))})
    check('inside enclosed mass coefficient',muin=={5:F(2,5)})
    check('outside enclosed mass coefficient',muout=={0:F(1),-5:F(-3,5)})
    check('enclosed mass continuous',at(muin,F(1))==at(muout,F(1)))
    # Integrate the actual shell kernel: alpha=mu/x+integral_x^infinity dmu/s.
    tail_out=scale(-1,anti(mul(uout,{-1:F(1)})))
    alphout=add(mul(muout,{-1:F(1)}),tail_out)
    pin=anti(mul(uin,{-1:F(1)}))
    alphin=add(mul(muin,{-1:F(1)}),{0:at(pin,F(1))+at(tail_out,F(1))},scale(-1,pin))
    check('inside potential derived from full source kernel',alphin=={0:F(1),4:F(-1,10)})
    check('outside potential derived from full source kernel',alphout=={-1:F(1),-6:F(-1,10)})
    check('inside Poisson equation with angular averaged density',lap(alphin)==scale(-1,rhoin))
    check('outside is sourced rather than vacuum',lap(alphout)==scale(-1,rhoout) and bool(rhoout))
    check('potential continuous at interface',at(alphin,F(1))==at(alphout,F(1)))
    check('acceleration continuous at interface',at(der(alphin),F(1))==at(der(alphout),F(1)))
    check('central potential finite and nonzero',at(alphin,F(0))==1)
    check('central acceleration zero',at(der(alphin),F(0))==0)
    check('inside mass flux',scale(-1,mul({2:F(1)},der(alphin)))==muin)
    check('outside mass flux',scale(-1,mul({2:F(1)},der(alphout)))==muout)
    Wsource=-(integ01(mul(alphin,uin))+integ1inf(mul(alphout,uout)))/2
    Wmass=-(integ01(mul(mul(muin,uin),{-1:F(1)}))+integ1inf(mul(mul(muout,uout),{-1:F(1)})))
    Wgradient=-(integ01(mul({2:F(1)},mul(der(alphin),der(alphin))))+
                integ1inf(mul({2:F(1)},mul(der(alphout),der(alphout)))))/2
    check('binding source integral',Wsource==F(-421,990))
    check('binding enclosed mass integral',Wmass==Wsource)
    check('binding whole-space gradient integral',Wgradient==Wsource)
    finite=[]
    for Lam in map(F,[2,3,4,8]):
        q=Lam**-5
        # Actual finite Dirichlet phi(L)=0 changes the outside profile.
        p=add(scale(-q/(1-q),{2:F(1)}),scale(1/(1-q),{-3:F(1)}))
        check('finite Dirichlet inner trace '+str(Lam),at(p,F(1))==1)
        check('finite Dirichlet outer trace '+str(Lam),at(p,Lam)==0)
        actual=Uin+integ(e(p),F(1),Lam)
        check('finite Dirichlet energy '+str(Lam),actual==1/(1-q))
        removed=F(3,5)*Lam**-5
        check('original field tail energy '+str(Lam),-at(anti(uout),Lam)==removed)
        miss_potential=F(1,2)*Lam**-6
        check('tail source interior potential is constant '+str(Lam),at(tail_out,Lam)==miss_potential)
        gravtail=-F(1,2)*Lam**-1+F(1,10)*Lam**-6-F(9,550)*Lam**-11
        gradtail=-(at(anti(mul({2:F(1)},mul(der(alphout),der(alphout)))),Lam))
        check('gravitational gradient tail '+str(Lam),gradtail==-2*gravtail)
        finite.append({'L_over_R':str(Lam),'original_free_energy_tail_fraction':str(removed),
                       'finite_Dirichlet_total_free_energy_ratio':str(actual),
                       'missing_tail_reduced_lift_inside_L':str(miss_potential),
                       'negative_gravitational_gradient_tail_in_GMf2_over_R':str(gravtail)})
    # Native matching inverse solves coefficients, rather than inserting alpha.
    A=[[0,20,0,0],[0,0,0,30],[1,1,-1,-1],[0,4,1,6]]
    rhs=[-2,-3,0,0]; coeff=solve(A,rhs)
    check('boundary and Poisson coefficient solve independently matches kernel integral',coeff==[1,F(-1,10),1,F(-1,10)])
    result={'status':'PASS','checks':len(checks),'check_names':checks,'kappa':str(kappa),
            'normalization':'R=1, sum x_alpha^2=1, Uf=1; Mf=Uf/c^2; alpha=a/(2GMf/(c^2R))',
            'phi_in':wire(phi_in),'phi_out':wire(phi_out),'dUf_dx_inside':wire(uin),'dUf_dx_outside':wire(uout),
            'rho_4piR3_over_Mf_inside':wire(rhoin),'rho_4piR3_over_Mf_outside':wire(rhoout),
            'M_over_Mf_inside':wire(muin),'M_over_Mf_outside':wire(muout),
            'alpha_inside':wire(alphin),'alpha_outside':wire(alphout),
            'g_in_GMf_over_R2_inside':wire(der(alphin)),'g_in_GMf_over_R2_outside':wire(der(alphout)),
            'inside_free_energy_fraction':str(Uin),'outside_free_energy_fraction':str(Uout),
            'Ugrav_in_GMf2_over_R':str(Wsource),'finite_boundary_examples':finite,
            'commuting_static_example':{'epsilon':str(eps),'currents':list(map(str,currents)),
                  'R':str(Rstatic),'boundary_coordinates':list(map(str,xs)),
                  'positive_free_energy':str(Ufree),'signed_interaction_energy':str(Uint),
                  'counterterm_energy':str(Uct),'sum':'0',
                  'scope':'Classical simultaneous c-number currents; not noncommuting quantum D,C.'},
            'scope':'Classical static positive free-field angular average under conditional rho=energy/c^2; not a full quantum interacting/counterterm source density.'}
    (HERE/'FIELD_SOURCE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    context={'basis':list(range(4)),'field':{'radicand':0},'history':{'mapping':'static positive free-field angular-average source; radial Poisson matching'},
             'units':{'x':'r/R','alpha':'a/(2GMf/(c^2R))'},'spectral_coordinate':'piecewise radial potential coefficients (A,B,C,D)'}
    task={'id':'CH3_QUADRUPOLE_FIELD_SOURCE_MATCHING','domain':'STARBREAKER','operation':'GEN2_READOUT_INVERSE',
          'payload':{'strategy':'linear','matrix':[[str(x) for x in row] for row in A],
                     'observed':list(map(str,rhs)),'context':context,
                     'source_binding':{'model':'Chapter I static quadrupole free-field angular average',
                                       'source_snapshot_sha256':hashlib.sha256((HERE/'CHAPTER_I_MODEL_SOURCE.md').read_bytes()).hexdigest(),
                                       'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                                       'scope':result['scope']}},
          'question':'What potential follows from the actual static quadrupole positive free-field density and matching conditions?',
          'source_mapping':'alpha_in=A+B x^4; alpha_out=C/x+D/x^6. Two source-Poisson rows plus continuity of alpha and its derivative atx=1.',
          'expected':{'coefficients':list(map(str,coeff))}}
    (HERE/'DUCK_R2_TASKS.json').write_text(json.dumps([task],indent=2)+'\n')
    print(json.dumps({'status':'PASS','checks':len(checks),'Ugrav':str(Wsource),'native_task':task['id']}))

if __name__=='__main__':main()
