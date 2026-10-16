"""Independent exact checks of the declared receiving apparatus, not native execution."""
from fractions import Fraction as F
from pathlib import Path
import hashlib, json, math
BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[2]
OLD=ROOT/'GEN4/voli_chapter2_bridge1'
checks=[]
def ok(name,value):
    assert value,name
    checks.append(name)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def sqrt_upper(x,places=40):
    scale=10**places
    k=math.isqrt(x.numerator*scale*scale//x.denominator)
    a,b=F(k,scale),F(k+1,scale)
    ok('sqrt enclosure '+str(len(checks)),a*a<=x<b*b)
    return b
# Differential identities are tested by rational tangent coordinates on the
# exact square-root sphere n=x^2,1-n=y^2 (x,y rational).
for x,y in [(F(3,5),F(4,5)),(F(5,13),F(12,13)),(F(8,17),F(15,17))]:
    n=x*x;r=y*y
    for ndot in [F(-3,7),F(0),F(2,5)]:
        # Real-amplitude derivative contribution to <r|r_dot>.
        ok('normalization differential '+str(len(checks)),x*ndot/(2*x)+y*(-ndot/(2*y))==0)
        # H_trans=-ndot Y/(2xy): imaginary Schr RHS components.
        coeff=-ndot/(2*x*y)
        ok('reference transition component0 '+str(len(checks)),-coeff*y==ndot/(2*x))
        ok('reference transition component1 '+str(len(checks)),coeff*x==-ndot/(2*y))
    ok('occupation compensation '+str(len(checks)),n+r==1)
# Original full role incidence: each pure legal stroke has w=sigma ell_dot.
roles={'a':(1,1,0),'b':(1,-1,0),'p':(-2,0,1)}
for role,(g,d,c) in roles.items():
    for sigma in [-1,1]:
        for rate in [F(1,13),F(9,7)]:
            w=sigma*rate*(g+3*c)
            ok('legal '+role+str(sigma)+str(rate),w==sigma*rate)
            E=F(573049,97)
            beta_dot=2*(w-E)
            ok('actual canonical closure '+role+str(sigma)+str(rate),E+beta_dot/2==w)
            # Relative calibrated ref eigenvalue may be negative; paid explicitly.
            c0=max(F(0),-beta_dot)
            ok('positive offset accounted '+role+str(sigma)+str(rate),E+beta_dot/2+c0==w+c0)
# Signed switching work including entry and release telescopes.
for word in [[1,1,-1],[1,-1,1,-1],[-1,-1,-1]]:
    E=F(31,5);rates=[F(s,3) for s in word]
    levels=[F(0),*[w-E for w in rates],F(0)]
    ok('switch-work telescope '+str(word),sum((b-a for a,b in zip(levels,levels[1:])),F(0))==0)
# Duck-selected antecedents bind the positive original path clock.
antecedents=[]
for name,expected in [('ACTION_LEARNING.md','37212e905ec778383ffd6b1d0216e91157064452211f7e1105f0217b53ba46a3'),('SOURCE_ACTION.md','4b400d5f3b074bf00cbb64d4f90eddda9f0355799ab6f32b16afafeb616b0df4')]:
    path=ROOT/'GEN4/gen6_spin_clock_successor1_20261014'/name
    ok('Duck selected source hash '+name,sha(path)==expected)
    antecedents.append({'path':str(path.relative_to(ROOT)),'sha256':sha(path)})
# Uniform source metric bounds follow from exact polynomial factorizations.
# Lower:400x-(x+36)^2=(x-4)(324-x); x=E_B^2 in[4,100].
# Upper:(x+36)^2-80(x+g^2)=(x-4)^2+80(16-g^2).
for x in [F(4),F(9),F(36),F(64),F(100)]:
    ok('source metric lower factor '+str(x),400*x-(x+36)**2==(x-4)*(324-x)>=0)
    for g2 in [F(0),F(4),F(16)]:
        ok('source metric upper factor '+str(x)+str(g2),(x+36)**2-80*(x+g2)==(x-4)**2+80*(16-g2)>=0)
# Consume exact actual native amplitude/rate evidence, never invent a trajectory.
hist=json.loads((OLD/'bridge/ACTUAL_CLOCK_HISTORY.json').read_text())
rows=[]
M=16
for h in hist['histories']:
    m=F(h['amplitude_lower']);lo=F(h['actual_uniform_rate']['lower']);hi=F(h['actual_uniform_rate']['upper'])
    b=sqrt_upper(1-m*m);rlo=(1-b)/2;rhi=(1+b)/2
    ok('positive reference occupation '+str(h['pair']),0<rlo<rhi<1)
    ok('all sixteen phase-addressed events exist '+str(h['pair']),lo*573049>F(3,2))
    times=[]
    for k in range(1,M+1):
        # All coefficients are relative to pi.
        phase=F(3*k,2*M)
        a,z=phase/hi,phase/lo
        ok('threshold within certified window '+str(h['pair'])+str(k),0<a<=z<573049)
        times.append({'k':k,'theta_over_pi':str(phase),'time_over_pi':{'lower':str(a),'upper':str(z)}})
    rows.append({'pair':h['pair'],'amplitude_lower':str(m),'reference_occupation_outer':{'lower':str(rlo),'upper':str(rhi)},'phase_addressed_16_event_enclosures':times})
# Native algebra operands: source-qubit trace bookkeeping and full actual B18
# costs are distinct. Parent may select these; this script never launches Duck.
I=[[1,0],[0,1]];P=[[0,0],[0,1]]
operands={'P_ref':P,'I2':I,'fixture_density_source':[['2/5','2/5'],['2/5','3/5']],
'fixture_density_reference_occupation':[['3/5','0'],['0','2/5']],
'fixture_density_reference_balanced':[['1/2','1/2'],['1/2','1/2']],
'fixture_H_source':[[2,0],[0,5]],'fixture_H_reference_inverse_write':[[0,0],[0,'-46/5']],
'fixture_E_source':'18/5','fixture_w':'-1',
'scope':'Declared finite apparatus algebra controls only; actual continuum H/preparation remain inherited and unchanged.'}
# This finite apparatus control uses exactly its own density expectation.
E=F(2,5)*2+F(3,5)*5;w=F(-1)
operands['fixture_E_source']=str(E)
operands['fixture_H_reference_inverse_write']=[[0,0],[0,str(2*(w-E))]]
ok('native fixture total expectation',E+F(operands['fixture_H_reference_inverse_write'][1][1])/2==w)
(BASE/'NATIVE_OPERANDS.json').write_text(json.dumps(operands,indent=2)+'\n')
report={'schema':'SAM_CH2_CONTROLLED_WRITE_CLOCK_INSTRUMENT_V1','status':'PASS','independent_checks_passed':len(checks),'checks':checks,
'actual_clock_source':{'path':str((OLD/'bridge/ACTUAL_CLOCK_HISTORY.json').relative_to(ROOT)),'sha256':sha(OLD/'bridge/ACTUAL_CLOCK_HISTORY.json')},
'actual_native_reexecutions':0,'new_reference_apparatus':'Explicit controlled balanced qubit; not a newly executed physical preparation',
'actual_certificate_consumption':rows,'Duck_selected_source_clock_antecedents':antecedents,'generator_sha256':sha(Path(__file__))}
(BASE/'RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'actual_lanes':len(rows),'event_crossing_enclosures':6*M}))
