#!/usr/bin/env python3
"""Portable independent rational check; no new native or transcendental run."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
checks = []

def check(name, test):
    if not test:
        raise AssertionError(name)
    checks.append(name)

def dot(x, y): return sum((a*b for a,b in zip(x,y)), F(0))
def mv(a, x): return [dot(row, x) for row in a]
def mm(a, b): return [[dot(row,col) for col in zip(*b)] for row in a]
def transpose(a): return list(map(list,zip(*a)))
def matrix(raw): return [list(map(F,row)) for row in raw]

def solve(a,b):
    """Exact elimination, independent of the candidate Green kernel."""
    n=len(b)
    work=[list(row)+[b[i]] for i,row in enumerate(a)]
    for j in range(n):
        k=next(i for i in range(j,n) if work[i][j])
        work[j],work[k]=work[k],work[j]
        p=work[j][j]
        work[j]=[x/p for x in work[j]]
        for i in range(n):
            if i!=j:
                p=work[i][j]
                work[i]=[x-p*y for x,y in zip(work[i],work[j])]
    return [row[-1] for row in work]

def shell_u(mass, radii, outer=None):
    return [[1/max(r,s)-(F(0) if outer is None else 1/outer)
             for s in radii] for r in radii]

def shell_energy(mass,radii,outer=None):
    return -dot(mass,mv(shell_u(mass,radii,outer),mass))/2

def main():
    f=json.loads((HERE/'FIXTURE.json').read_text())
    n,L=f['n'],f['L']
    kappa=F(f['kappa']); mass=list(map(F,f['mass'])); q=list(map(F,f['q']))
    K,H,B,C=map(matrix,[f['K'],f['Green_H'],f['incidence_B'],f['conductance_C']])
    a=solve(K,q)
    I=[[F(i==j) for j in range(n)] for i in range(n)]
    check('independent exact elimination agrees with retained solution',a==list(map(F,f['expected_a'])))
    check('source mass is one',sum(mass)==1)
    check('incidence conductance form equals K',mm(mm(transpose(B),C),B)==K)
    check('analytic telescoping Green matrix is exact inverse',mm(K,H)==I)
    check('inverse energy identity HKH=H',mm(mm(H,K),H)==H)
    closed=[row[:] for row in K]
    closed[-1][-1]-=F((L-1)*L)
    check('removing exterior exit leaves the conservative zero mode',mv(closed,[F(1)]*n)==[F(0)]*n)
    check('positive source violates closed graph solvability',sum(q)>0 and all(sum(row)==0 for row in closed))
    check('positive field and negative binding have opposite signs',dot(q,a)>0)
    check('field q dot a equals weighted edge gradient',dot(q,a)==dot(mv(B,a),mv(C,mv(B,a))))
    check('finite field is nonnegative for nonnegative source',all(x>=0 for x in a))
    full_a=a+[F(0)]
    enclosed=F(0)
    for i in range(1,L):
        enclosed+=mass[i-1]
        check('flux edge '+str(i),F(i*(i+1))*(full_a[i-1]-full_a[i])==kappa*enclosed)
    a_inf=[kappa*sum(mass[j]/max(i+1,j+1) for j in range(n)) for i in range(n)]
    check('outer boundary correction is one common constant',all(x-y==kappa/L for x,y in zip(a_inf,a)))
    u=[x/kappa for x in a]
    j=lambda v: dot(v,mv(K,v))/2-dot(mass,v)
    U_L=j(u); U_inf=-dot(mass,[x/kappa for x in a_inf])/2
    check('on-shell binding is half the source coupling',U_L==-dot(mass,u)/2)
    check('whole-space exterior tail energy retained',U_inf==U_L-F(1,2*L))
    perturb=[F((-1)**i*(i+1),13) for i in range(n)]
    check('minimum identity for signed nontrivial perturbation',j([x+y for x,y in zip(u,perturb)])-j(u)==dot(perturb,mv(K,perturb))/2)
    check('positive second variation for nonzero perturbation',dot(perturb,mv(K,perturb))>0)
    wrong=[[x+F(1,L) for x in row] for row in H]
    check('omitting outer boundary correction fails the declared finite inverse',mm(K,wrong)!=I)
    wrongK=[row[:] for row in K]; wrongK[0][0]+=F(1)
    check('invented central sink changes operator and flux',mm(wrongK,H)!=I)
    mass1=[x if i<4 else F(0) for i,x in enumerate(mass)]
    mass2=[x-y for x,y in zip(mass,mass1)]
    U=lambda m:-dot(m,mv(H,m))/2
    cross=-dot(mass1,mv(H,mass2))
    check('two source interaction appears exactly once',U(mass)==U(mass1)+U(mass2)+cross)
    # Shell radius work: vary one shell while preserving all radial ordering.
    radii=list(map(F,range(1,L))); jidx=3; r=radii[jidx]; delta=F(1,7)
    coeff=mass[jidx]*(sum(mass[:jidx])+mass[jidx]/2)
    rp=radii[:]; rm=radii[:]; rp[jidx]+=delta; rm[jidx]-=delta
    Uplus=shell_energy(mass,rp,F(L)); Uminus=shell_energy(mass,rm,F(L))
    force_fd=-(Uplus-Uminus)/(2*delta)
    force_exact=-coeff/r**2
    check('shell virtual work has the inward sign',force_exact<0)
    check('shell work includes half self-field and all inner mass',force_fd==-coeff/(r*r-delta*delta))
    check('finite-difference force error is exactly controlled',abs(force_fd-force_exact)==coeff*delta**2/(r*r*(r*r-delta*delta)))
    check('external finite reference does not alter shell force',
          (shell_energy(mass,rp)-shell_energy(mass,rm))/(2*delta)==-force_fd)
    # Uniform ball sampled by outer-endpoint shells: analytic source-shell error.
    continuum=[]
    for cells in [2,4,8,16,32,64]:
        masses=[F(j**3-(j-1)**3,cells**3) for j in range(1,cells+1)]
        rs=[F(j,cells) for j in range(1,cells+1)]
        harmonic=sum((F(1,j) for j in range(1,cells+1)),F(0))
        err=F(3,cells)-F(2,cells*cells)*harmonic
        central=2*sum(m/r for m,r in zip(masses,rs))
        check('uniform central shell error '+str(cells),3-central==err)
        check('uniform strict O(h) potential bound '+str(cells),0<err<F(3,cells))
        for i in range(cells+1):
            x=F(i,cells)
            sampled=2*sum(m/max(x,r) for m,r in zip(masses,rs))
            exact=3-x*x
            check('uniform potential node '+str(cells)+':'+str(i),0<=exact-sampled<=err)
            if i:
                enclosed=sum(masses[:i])
                check('uniform outer node force '+str(cells)+':'+str(i),enclosed/x**2==x)
        energy=shell_energy(masses,rs)
        check('uniform binding convergence enclosure '+str(cells),0<=energy+F(3,5)<=err/2)
        # R=2b stays fixed: refining h cannot remove its finite-boundary bias.
        finite=shell_energy(masses,rs,F(2))
        check('fixed outer radius leaves fixed binding bias '+str(cells),finite-energy==F(1,4))
        continuum.append({'cells':cells,'max_reduced_lift_error':str(err),
                          'binding_in_GM2_over_b':str(energy),'fixed_R_over_b':2,
                          'finite_boundary_reduced_lift_offset':'1'})
    result={'status':'PASS','checks':len(checks),'check_names':checks,
            'finite_example':{'L':L,'kappa':str(kappa),'mass':list(map(str,mass)),
              'field_a':list(map(str,a)),'infinite_boundary_field_a':list(map(str,a_inf)),
              'U_L_in_GMunit2_over_h':str(U_L),'U_infinity_in_GMunit2_over_h':str(U_inf),
              'tail_binding_correction':'-1/18',
              'moving_shell_index':jidx+1,'moving_shell_force_in_GMunit2_over_h2':str(force_exact)},
            'uniform_ball_continuum':continuum,
            'scope':'Independent rational verification of the declared static shell receiver; no microscopic localization or angular isotropy is inferred.',
            'inputs':{'FIXTURE.json':hashlib.sha256((HERE/'FIXTURE.json').read_bytes()).hexdigest()}}
    (HERE/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','checks':len(checks),'U_L':str(U_L),'U_infinity':str(U_inf)}))

if __name__=='__main__': main()
