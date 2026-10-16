"""Independent stdlib check of the complete paid-reference protocol.

No native imports or executions. Retained native duration/rate/preparation
certificates are read unchanged and authenticated by SHA-256. Algebraic E
is the actual full continuum energy, bounded here from those certificates.
"""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
import hashlib, json, math

BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[2]
PREV=ROOT/'GEN4/gen6_spin_clock_successor1_20261014'
INPUT=ROOT/'GEN4/duck_chapter1_lane1_20261015/sources/EXACT_INPUTS.json'
RATE=ROOT/'GEN4/duck_chapter1_lane1_20261015/RESULTS.json'
checks=[]
def ok(name,test):
    assert test,name
    checks.append(name)
def read(path): return json.loads(path.read_text())
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def pair(value):
    if 're' in value:value=value['re']
    return F(value['lower']),F(value['upper'])
def cell(group,key):return pair(inputs[group][key]['entries'][0][0])
def outward(bounds,places=18):
    with localcontext() as ctx:
        ctx.prec=200
        scale=Decimal(10)**(-places)
        return {'lower':str((Decimal(bounds[0].numerator)/Decimal(bounds[0].denominator)).quantize(scale,rounding=ROUND_FLOOR)),
            'upper':str((Decimal(bounds[1].numerator)/Decimal(bounds[1].denominator)).quantize(scale,rounding=ROUND_CEILING))}
def wire(bounds):return {'lower':str(bounds[0]),'upper':str(bounds[1])}
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def scale(a,c):return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)

paths=[INPUT,RATE,PREV/'ACTION_LEARNING.md',PREV/'native.py',
       PREV/'runs/H02_1/CLOCK_REFINEMENT.json',PREV/'runs/H05_1/CLOCK_REFINEMENT.json',
       ROOT/'GEN4/duck_chapter1_lane1_20261015/derivation/DOMAIN_SUPPLEMENT.md',
       ROOT/'GEN4/duck_chapter1_lane1_20261015/derivation/REFERENCE_SUPPLEMENT.md',
       ROOT/'GEN4/voli_chapter2_continuation2_20261015/instrument/DERIVATION.md']
sources=[{'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size} for p in paths]
inputs=read(INPUT);rates=read(RATE);h02=read(paths[4]);h05=read(paths[5])
fwd=h02['rows'][0];rev=h05['rows'][1]
ok('forward original event',fwd['event']=='W1+' and fwd['state']==[0,0,0])
ok('retained reverse event',rev['event']=='W1-' and rev['state']==[2,1,1])
ok('reverse common-phase shift gives100',[(x-1)%4 for x in rev['state']]==[1,0,0])
ok('source diagnostic scale',h02['calibration']['radius']=='1' and h02['calibration']['c']=='10' and h02['calibration']['A_los']=='0')
ok('reverse same source scale',all(h02['calibration'][k]==h05['calibration'][k] for k in ['radius','c','A_los','clock_to_elapsed_scale']))
T=pair(fwd['stroke_time']);Tr=pair(rev['stroke_time'])
ok('certified reverse overlap',max(T[0],Tr[0])<=min(T[1],Tr[1]))
T=(max(T[0],Tr[0]),min(T[1],Tr[1]))
ok('duration positive',T[0]>0)
ok('integral divides by ten',pair(fwd['integral'])[0]/10<=T[1] and T[0]<=pair(fwd['integral'])[1]/10)
even=cell('source_outputs','even_energy');eps=cell('clock_outputs','epsilon');Kprep=cell('clock_outputs','Kprep')
energy=(even[0]-eps[1],even[1]+eps[1]+Kprep[1])
ok('actual continuum energy positive',energy[0]>0)
ok('actual continuum energy less than one',energy[1]<1)
Ehat=(energy[0]+energy[1])/2
dE=(energy[1]-energy[0])/2
ok('finite calibration halfwidth',0<dE<F(1746,10**9))
ok('actual epsilon bound contains exact',eps[0]<=F(1,573049)<=eps[1])
a=b=F(1,100);wait=F(4)
matching=plus(scale(T,2),(wait,wait));total=plus(matching,(a+b,a+b))
matching_bias=matching[1]*dE
ok('midpoint calibration signed-ledger bias',matching_bias<F(754,10**8))
ok('complete duration in actual certificate',total[1]<573049*F(333,106))
rate=pair(rates['lanes'][0]['actual_uniform_rate'])
amplitude=cell('clock_outputs','CYCLE_amplitude_lower')
lane_d=cell('source_outputs','signed_d_vector')
ok('actual clock amplitude exceeds certified coarse margin',amplitude[0]>F(99,100))
ok('actual clock amplitude exceeds reported strong margin',amplitude[0]>F(499999999,500000000))
ok('actual lane current scale retains negative sign',lane_d[1]<0)
ok('lane01 rate positive',rate[0]>0)
ok('lane01 phase below bare gap',rate[1]<F(2,573049))

# Each beta row is pi*pi_coefficient + constant - E*positive_energy_time.
records=[('external_entry_start',(F(0),F(0)),F(0),F(0),F(0),(F(0),F(0)),False),
 ('matching_start',(a,a),F(0),F(0),F(1,10),(a,a),False),
 ('forward_complete',plus(T,(a,a)),F(1,2),F(1),F(1,10),plus(scale(T,2),(a,a)),True),
 ('reverse_complete',plus(scale(T,2),(a,a)),F(0),F(0),F(1,10),plus(scale(T,4),(a,a)),True),
 ('wait_complete',plus(scale(T,2),(a+wait,a+wait)),F(0),F(0),F(1,10),plus(scale(T,4),(a+2*wait,a+2*wait)),True),
 ('external_release_complete',total,F(0),F(0),F(1,10),plus(scale(T,4),(a+b+2*wait,a+b+2*wait)),False)]
timeline=[]
pi=cell('clock_outputs','pi')
ok('retained pi inside rational bracket',F(333,106)<pi[0]<pi[1]<F(355,113))
for name,t,gamma,beta_pi,beta_const,etime,ledger in records:
    phase=(rate[0]*t[0],rate[1]*t[1])
    beta=(beta_pi*pi[0]+beta_const-energy[1]*etime[1],beta_pi*pi[1]+beta_const-energy[0]*etime[0])
    timeline.append({'event':name,'model_time':wire(t),'time_outward_18dp':outward(t),
        'gamma_over_pi':str(gamma),'delta_over_pi':str(gamma),'chi_over_pi':'0',
        'actual_clock_theta':wire(phase),'theta_outward_18dp':outward(phase),
        'reference_beta':{'pi_coefficient':str(beta_pi),'constant':str(beta_const),'minus_E_times':wire(etime)},
        'beta_outer_using_rational_pi':wire(beta),'beta_outer_display':outward(beta),
        'completed_ledger_action_over_hbar_pi':str(gamma),'matching_interval_endpoint':ledger})
ok('wait causes more than one full reference turn',2*wait*energy[0]>2*pi[1])
ok('full beta below minus two pi',F(timeline[-1]['beta_outer_using_rational_pi']['upper'])<-2*pi[1])
ok('full beta above minus three pi',F(timeline[-1]['beta_outer_using_rational_pi']['lower'])>-3*pi[0])
ok('actual clock advances during source wait',rate[0]*wait>0)

# Rate extrema: differentiating f(c) gives a positive denominator times
# 96*(2c^2-11c+6), with c=cos(ell). Only one root lies in[0,1].
ok('stationary polynomial has sign change',(2-11+6)<0 and 6>0)
ok('small stationary root lies in unit interval',8<math.sqrt(73)<9)
cstar=(11-math.sqrt(73))/4
v0=10.;vL=125/(3*math.sqrt(17))
f=lambda c:12*math.sqrt(68-32*c)/(100-32*c+4*c*c)
vmin=10/f(cstar)
ok('native density endpoint0',f(1)==1)
ok('source density endpoint1 agrees',abs(10/f(0)-vL)<1e-13)
ok('rate has genuine minimum',0<vmin<v0<vL)
for j in range(1001):
    v=10/f(j/1000)
    ok('sampled extremum diagnostic '+str(j),v>=vmin-1e-13 and v<=vL+1e-13)

# Exact coefficient vectors [E,vL,vmin,1] retain every continuous-drive
# monotonic piece, sharp change, and external entry/release.
work=[('external entry',[-1,0,0,10]),('forward first monotone piece',[0,0,1,-10]),
 ('forward second monotone piece',[0,1,-1,0]),('forward to reverse quench',[0,-2,0,0]),
 ('reverse first monotone piece',[0,1,-1,0]),('reverse second monotone piece',[0,0,1,-10]),
 ('reverse to wait quench',[0,0,0,10]),('external release',[1,0,0,0])]
ok('every work coefficient cancels',all(sum(row[j] for _,row in work)==0 for j in range(4)))
for E in [F(0),F(1,2),F(1),F(10),F(20)]:
    W=[row[0]*float(E)+row[1]*vL+row[2]*vmin+row[3] for _,row in work]
    wp=sum(max(0,z) for z in W);wm=-sum(min(0,z) for z in W)
    gross=2*vL+2*(v0-vmin)+max(float(E)-v0,0)
    ok('gross positive work '+str(E),abs(wp-gross)<1e-12)
    ok('gross negative work '+str(E),abs(wm-gross)<1e-12)
ok('actual E is low-energy gross-work branch',energy[1]<10)

# Safe prefix tomography cadence. The exact source density obeys f>=3/5,
# hence v<=50/3. E<1 bounds |beta_dot|<=106/3, including both ramps.
step=F(1,100);speed_bound=F(106,3);angular_error=F(1,8);coordinate_error=F(1,16)
ok('successive phase separation safe',speed_bound*step+2*angular_error<pi[0])
# sqrt(2)/16 < 3/32 < sin(1/8), using sqrt2<3/2 and Taylor lower bound.
ok('coordinate to angular error',F(3,32)<F(1,8)-F(1,8)**3/6)
maxprefix=math.ceil(total[1]/step)+4
ok('prefix count at most441',maxprefix<=441)
statistical_error=F(1,32);systematic_error=F(1,32)
ok('coordinate budget includes apparatus and sampling',statistical_error+systematic_error==coordinate_error)
ok('four apparatus budgets sum to systematic allowance',4*F(1,128)==systematic_error)
N=26624;M=441;failure=F(1,100)
ok('Hoeffding exponent exact',N*statistical_error**2/2==13)
# e^13 > lower partial Taylor sum; then 4M/e^13 <1/100.
exp13lower=sum((F(13)**j/math.factorial(j) for j in range(40)),F(0))
ok('joint sampling failure below one percent',F(4*M,1)/exp13lower<failure)
ok('fresh copies shot accounting',2*M*N==23482368)

bindings={'schema':'SAM_CH2_PAID_PROTOCOL_SOURCE_BINDINGS_V1','sources':sources,
 'retained_native_execution_unchanged':True,'new_native_calls_in_this_script':0}
cert={'schema':'SAM_CH2_PAID_PROTOCOL_ORIGINAL_CERTIFICATES_V1',
 'forward':{'source_path':str(paths[4].relative_to(ROOT)),'source_sha256':sha(paths[4]),'row':fwd},
 'reverse':{'source_path':str(paths[5].relative_to(ROOT)),'source_sha256':sha(paths[5]),'row':rev},
 'reuse':'Common-phase shift211→111 maps to100→000, the exact reverse of000→100; same activation/path accumulation/radius/speed.',
 'duration_intersection':wire(T),'actual_lane01_rate':wire(rate),
 'actual_current_clock_receiver':{'D_over_d':'sigma_z','C_over_d':'sigma_y',
 'd01_signed_enclosure':wire(lane_d),'z':'<D>/d01+i<C>/d01',
 'phase_estimator':'-atan2(<C>/d01,<D>/d01) with continuous branch from theta0=0',
 'amplitude_lower_exact':str(amplitude[0]),'coarse_amplitude_lower':'99/100',
 'status':'Predicted actual phase enclosure; no achieved D/C apparatus or current-tomography sample reported',
 'coordinate_tolerance_to_phase':'angle error <=arcsin(sqrt(2)*delta/m), requiring sqrt(2)*delta<m',
 'separate_fresh_copy_receiver_required':True},
 'actual_continuum_energy':{'derivation':'epsilon*e01-epsilon <= E <= epsilon*e01+epsilon+Kprep',
 'exact_enclosure':wire(energy),'outward_18dp':outward(energy),
 'even_energy':wire(even),'epsilon':wire(eps),'Kprep_upper':str(Kprep[1]),
 'retained_preparation':'(Phi0+Phi1)/sqrt(2) tensor full soft vacuum; complete original joint Hamiltonian',
 'exact_identity':'E=epsilon*e01+(E0+E1)/2+c_soft; soft interaction initial expectation0',
 'operable_midpoint_calibration':{'Ehat':str(Ehat),'maximum_absolute_error':str(dE),
 'matching_interval_signed_ledger_bias_bound':str(matching_bias),
 'bias_outward_18dp':outward((F(0),matching_bias)),
 'control_rule':'Replace E by Ehat in every reference waveform; total matching connection becomes w+(E-Ehat).'}}}
result={'schema':'SAM_CH2_COMPLETE_PAID_REFERENCE_PROTOCOL_V1','status':'PASS','checks_passed':len(checks),
 'checks':checks,'source_calibration':{'R_H_over_c_tu':'1/10','A_path':'0','time_unit_seconds_assigned':False},
 'durations':{'forward':wire(T),'reverse':wire(T),'wait':'4','external_entry':'1/100','external_release':'1/100','total':wire(total)},
 'timeline':timeline,'work_coefficient_basis':['E_actual_full_continuum','v_L','v_min','1'],
 'switch_and_continuous_work':[{'piece':n,'coefficients':row} for n,row in work],
 'gross_exchange':{'W_positive_equals_W_negative':'2*v_L+2*(10-v_min) for actual E<1',
 'diagnostic_display':2*vL+2*(10-vmin),'physical_unit':'hbar/t_u',
 'not_a_dissipation_lower_bound':True},
 'rate_extrema':{'v0':'10','vL':'125/(3*sqrt(17))','cos_ell_star':'(11-sqrt(73))/4',
 'vmin':'10/f((11-sqrt(73))/4)','display_only':{'vL':vL,'vmin':vmin}},
 'readout':{'prefix_spacing_model_time':'<=1/100','phase_error_per_prefix_rad':'1/8',
 'phase_estimator':'atan2(-Yhat,Xhat), followed by nearest-branch continuation',
 'mean_coordinate_error':'1/16','systematic_coordinate_budget':'1/32','statistical_coordinate_budget':'1/32',
 'four_systematic_budgets_each':'1/128: reference preparation, evolution/waveform, readout, trigger timing',
 'reference_preparation_trace_distance_bound':'1/256','reference_evolution_Duhamel_integral_bound':'1/256',
 'readout_observable_operator_norm_bound':'1/128','model_trigger_time_error_bound':'3/13568',
 'max_prefixes':M,'shots_per_X_or_Y_mean':N,
 'maximum_fresh_preparations':2*M*N,'joint_failure_bound':'<1/100',
 'single_trajectory_nondisturbing_measurement_claimed':False,'external_winding_counter_required':True},
 'remaining_apparatus_accounts':['original source actuator','control waveform generation','preparation','X/Y rotations and measurement','external phase counter and reset','energy recovery losses'],
 'generator_sha256':sha(Path(__file__)),'new_native_executions':0}
diag=lambda vals:[[str(vals[i]) if i==j else '0' for j in range(4)] for i in range(4)]
operators={f'W{i}':diag(row) for i,(_,row) in enumerate(work)}
program=[{'name':'sum1','op':'add','inputs':['W0','W1']}]
for i in range(2,len(work)):program.append({'name':'sum'+str(i),'op':'add','inputs':['sum'+str(i-1),'W'+str(i)]})
native={'name':'paid_protocol_all_work_coefficients','context':{'basis':['E','vL','vmin','1'],
 'field':{'radicand':0},'units':{'work':'coefficient space; physical unit hbar/t_u'},
 'history':{'semantic_class':'Source-derived formal coefficient identity; not a substitute continuum Hamiltonian'},
 'spectral_coordinate':'ordered coefficient space'},
 'data':{'operators':operators,'program':program,'output':'sum7'},
 'expected_matrix':diag([0,0,0,0]),
 'source_binding':{'source_derived_protocol':True,'actual_continuum_energy_replaced':False,'operand_sha256_pending':True}}
for name,obj in [('SOURCE_BINDINGS.json',bindings),('ORIGINAL_CERTIFICATES.json',cert),('RESULTS.json',result),('NATIVE_PAYLOAD.json',native)]:
    (BASE/name).write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'actual_energy_outer':outward(energy),
 'model_total_time_outer':outward(total),'phase_prefixes_bound':M,'max_shots':2*M*N}))
