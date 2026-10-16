#!/usr/bin/env python3
"""Exact source/response checks. Offline; no worker launch or PDF authoring."""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json

HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(a,c):return [[F(c)*x for x in r] for r in a]
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def kron(a,b):return [[x*y for x in r for y in s] for r in a for s in b]
def comm(a,b):return sub(mul(a,b),mul(b,a))
def block(*a):
    sizes=[len(v) for v in a]; n=sum(sizes); out=[[F(0) for _ in range(n)] for _ in range(n)];k=0
    for v in a:
        for i,r in enumerate(v):
            for j,x in enumerate(r):out[k+i][k+j]=x
        k+=len(v)
    return out
def wire(a):return [[str(x) for x in r] for r in a]
def interval(row):return F(row['lower']),F(row['upper'])
def show(iv):return {'lower':str(iv[0]),'upper':str(iv[1]),'display_lower':format(float(iv[0]),'.17g'),'display_upper':format(float(iv[1]),'.17g')}

def run():
    p=json.loads((HERE/'chapter1_certificate.json').read_text())
    bindings=json.loads((HERE/'SOURCE_BINDINGS.json').read_text())
    checks=[]
    def ok(n,t):
        if not t:raise AssertionError(n)
        checks.append(n)
    for row in bindings['frozen_inputs']:ok('frozen '+row['path'],sha(HERE/row['path'])==row['sha256'])
    q=[[F(x) for x in row] for row in p['matrices']['Q']];I=eye(4)
    QL,QR=kron(q,I),kron(I,q)
    S=[[F(j==4*(i%4)+i//4) for j in range(16)] for i in range(16)]
    D=sub(QL,QR);Z=mul(sub(eye(16),S),D)
    E=add(add(QL,QR),mul(QL,QR));CT=scale(mul(D,D),2)
    zero=[[F(0)]*16 for _ in range(16)]
    residuals=[add(comm(S,Z),scale(Z,2)),comm(E,Z),comm(CT,Z)]
    for k,r in enumerate(residuals):
        for i,row in enumerate(r):
            for j,x in enumerate(row):ok(f'full16 commutator {k} {i},{j}',x==0)
    for name,a in [('S',S),('D',D),('C_over_i',mul(S,D))]:
        ok('even energy commutes '+name,comm(E,a)==zero)
    ok('counterterm commutes source H',comm(CT,add(S,E))==zero)
    ok('signed source clock nonzero',any(x for r in Z for x in r))
    eps=F(1,573049);Delta=2*eps;kappa=F(4,5);lam=64*Delta
    pi_lo=F('3.14159265358979323846264338327950288419716939937510')
    pi_hi=pi_lo+F(1,10**50)
    b_lo,b_hi=1/(6*kappa*pi_hi),1/(6*kappa*pi_lo)
    Rlo,Rhi=interval(p['lanes'][0]['clock']['R'])
    Jlo=b_lo-Rhi**4*lam**4/(450*kappa*pi_lo)
    r=F(1,64**2);Jhi=b_hi/(1-r)
    ok('positive complete continuum J bound',0<Jlo<Jhi)
    qs=[interval(x) for x in p['q']]
    diag=[((1+a)**2*eps,(1+b)**2*eps) for a,b in qs]
    ok('four distinct current-dark source energies',all(diag[i][1]<diag[i+1][0] for i in range(3)))
    lanes=[]
    for lane in p['lanes']:
        a,b=lane['pair']; d=(qs[a][0]-qs[b][1],qs[a][1]-qs[b][0])
        ok(f'{a}{b} signed difference',d[1]<0)
        g2=(eps**2*d[1]**2,eps**2*d[0]**2)
        xlo,xhi=4*g2[0]*Jlo,4*g2[1]*Jhi
        ok(f'{a}{b} perturbative positive gap',0<xlo<xhi<1)
        corrlo=2*xlo/(1-xlo)
        corrhi=2*xhi/((1-r)*(1-xhi))
        slope=(1-corrhi,1-corrlo)
        ok(f'{a}{b} epsilon-only slope below one',0<slope[0]<slope[1]<1)
        rate=interval(lane['certificate']['actual_uniform_rate'])
        threshold=1-(rate[0]/rate[1])**2
        ok(f'{a}{b} full-scale phase-band threshold',0<threshold<1)
        lanes.append({'pair':[a,b],'d_squared':show((d[1]**2,d[0]**2)),'g_squared':show(g2),'J':show((Jlo,Jhi)),'second_order_fractional_delay':show((xlo,xhi)),'epsilon_log_gap_derivative':show(slope),'actual_rate_enclosure':show(rate),'full_scaling_sufficient_lift_for_disjoint_phase_bands':str(threshold),'lift_threshold_display':format(float(threshold),'.17g'),'scope':'Fixed hard split; second-order branch diagnostic; phase-band result conditional on declared full-H scale; not full-field finite-a perturbation certification'})
    order=sorted(lanes,key=lambda x:F(x['epsilon_log_gap_derivative']['lower']))
    for a,b in zip(order,order[1:]):ok('disjoint second-order lane response '+str(a['pair'])+' '+str(b['pair']),F(a['epsilon_log_gap_derivative']['upper'])<F(b['epsilon_log_gap_derivative']['lower']))
    A0=(1/(12*pi_hi),1/(12*pi_lo))
    fac=(1/(1-A0[0]),1/(1-A0[1]))
    ok('raw background sensitivity remains',1<fac[0]<fac[1])
    # Four terms ordered Hs,Hf,Hint,Hct. Coefficients are response, not states.
    full=[F(-1,2)]*4;partial=[F(-1,2),F(0),F(-1,2),F(-1)]
    residual=[x-y for x,y in zip(partial,full)]
    ok('epsilon-only full Hamiltonian residual',residual==[0,F(1,2),0,F(-1,2)])
    def diagm(x):return [[x[i] if i==j else F(0) for j in range(len(x))] for i in range(len(x))]
    r1_derivation=HERE/'DERIVATION_R1.md'
    if not r1_derivation.exists():r1_derivation=HERE/'DERIVATION.md'
    sb={'campaign':'voli_chapter3_source_field1_20261015','source':'Chapter I exact finite source and complete continuum receiving law','frozen_source_sha256':sha(HERE/'chapter1_certificate.json'),'derivation_sha256':sha(r1_derivation),'physical_scope':'Exact algebra and declared perturbation controls; no microscopic gravity map or measured SI redshift'}
    contexts=lambda basis,semantic:{'basis':basis,'field':{'radicand':0},'units':{'coordinate':'dimensionless original model source coefficients'},'history':{'semantic_class':semantic},'spectral_coordinate':'original placement pair basis; no source eigenvalue fit'}
    task1={'operation':'GEN3_SOURCE_OPERATOR_WORD','payload':{'name':'chapter3_full_source_clock_energy_commutators','context':contexts([f'{tag}:{a},{b}' for tag in ['bare','even','counter'] for a in range(4) for b in range(4)],'Three block copies of complete original16-state source; exact commutator certificate'),'source_binding':sb,'data':{'operators':{'A':wire(block(S,E,CT)),'Z':wire(block(Z,Z,Z)),'K':wire(block(scale(Z,2),zero,zero))},'program':[{'name':'AZ','op':'multiply','inputs':['A','Z']},{'name':'ZA','op':'multiply','inputs':['Z','A']},{'name':'minus_ZA','op':'scale','inputs':['ZA'],'factor':'-1'},{'name':'comm','op':'add','inputs':['AZ','minus_ZA']},{'name':'residual','op':'add','inputs':['comm','K']}],'output':'residual'}},'expected_matrix':wire([[F(0)]*48 for _ in range(48)])}
    task2={'operation':'GEN3_SOURCE_OPERATOR_WORD','payload':{'name':'chapter3_full_scaling_epsilon_only_residual','context':contexts(['Hs','Hf','Hint','Hct'],'Original Hamiltonian formal coefficient response; not a finite replacement continuum'),'source_binding':sb,'data':{'operators':{'PARTIAL':wire(diagm(partial)),'NEG_FULL':wire(diagm([-x for x in full]))},'program':[{'name':'residual','op':'add','inputs':['PARTIAL','NEG_FULL']}],'output':'residual'}},'expected_matrix':wire(diagm(residual))}
    tasks={'schema':'SAM_CH3_CLOCK_DUCK_NATIVE_TASKS_V1','tasks':[task1,task2]}
    task_path=HERE/'DUCK_R1_TASKS.json'
    rendered=json.dumps(tasks,indent=2)+'\n'
    if task_path.exists():ok('frozen R1 task bytes preserved',task_path.read_text()==rendered)
    else:task_path.write_text(rendered)
    r2=HERE/'DUCK_R2_TASKS.json'
    if r2.exists():
        r2=json.loads(r2.read_text())['tasks'][0]
        ok('R2 source binding',r2['payload']['source_binding']['actual_clock_input_sha256']==sha(HERE/'chapter1_certificate.json'))
        ok('R2 current response derivation binding',r2['payload']['source_binding']['response_derivation_sha256']==sha(HERE/'DERIVATION.md'))
        for k,lane in enumerate(lanes):
            lo,hi=F(lane['actual_rate_enclosure']['lower']),F(lane['actual_rate_enclosure']['upper'])
            expected=r2['expected_matrix']
            ok('R2 exact ratio '+str(k),F(expected[k][k])==lo/hi)
            ok('R2 phase threshold '+str(k),F(r2['derived_sufficient_lift_thresholds'][k])==1-(lo/hi)**2)
    result={'schema':'SAM_CH3_ACTUAL_CLOCK_RESPONSE_V1','status':'PASS','checks_passed':len(checks),'checks':checks,'lanes':lanes,'four_current_dark_source_energies':[show(x) for x in diag],'raw_background_sensitivity_factor':show(fac),'full_source_dimensions':16,'native_commutator_output_dimensions':48,'epsilon_only_minus_full_scale_coefficients':[str(x) for x in residual],'native_executions':0}
    (HERE/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','checks':len(checks),'lanes':len(lanes),'native_tasks':2,'source_dimensions':16}))

if __name__=='__main__':run()
