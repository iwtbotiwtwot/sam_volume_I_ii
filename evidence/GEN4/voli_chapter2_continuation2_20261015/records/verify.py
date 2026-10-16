"""Independent exact original-source record and feasible-cost checks."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import json,hashlib,math
BASE=Path(__file__).resolve().parent;ROOT=BASE.parents[2]
OLD=ROOT/'GEN4/voli_chapter2_bridge1'
checks=[]
def ok(name,test):
    assert test,name
    checks.append(name)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rank(a):
    a=[[F(x) for x in r] for r in a]
    if not a:return 0
    i=0
    for j in range(len(a[0])):
        p=next((k for k in range(i,len(a)) if a[k][j]),None)
        if p is None:continue
        a[i],a[p]=a[p],a[i];c=a[i][j];a[i]=[x/c for x in a[i]]
        for k in range(i+1,len(a)):
            c=a[k][j]
            if c:a[k]=[x-c*y for x,y in zip(a[k],a[i])]
        i+=1
        if i==len(a):break
    return i

def solve(a,b):
    n=len(a);m=len(b[0]);q=[[F(x) for x in r]+[F(x) for x in s] for r,s in zip(a,b)]
    for j in range(n):
        p=next(k for k in range(j,n) if q[k][j]);q[j],q[p]=q[p],q[j]
        c=q[j][j];q[j]=[x/c for x in q[j]]
        for i in range(n):
            if i==j:continue
            c=q[i][j]
            q[i]=[x-c*y for x,y in zip(q[i],q[j])]
    return [r[n:n+m] for r in q]
def mul(a,b):return [[sum((x*y for x,y in zip(r,c)),F(0)) for c in zip(*b)] for r in a]
def trans(a):return list(map(list,zip(*a)))
source_path=ROOT/'GEN4/native_history_reduction1/REDUCTION.json';S=json.loads(source_path.read_text())
points=S['points'];P={tuple(p):i for i,p in enumerate(points)};T=S['quotient_transitions'];O=[P[tuple(o[0])] for o in S['quotient_outputs']]
def record(blocks,d=3):
    word=[e for b in blocks for e in ([0]*4 if b=='A' else [1]*4)]
    q=0;mom=[[0]*len(points) for k in range(d+1)];seen=[]
    for n,e in enumerate(word,1):
        q=T[q][e];j=O[q];seen.append(j)
        for k in range(d+1):mom[k][j]+=n**k
    return q,mom,seen,word
qa,ma,sa,wa=record('A');qb,mb,sb,wb=record('B')
ok('A is native closed word',qa==0);ok('B is native closed word',qb==0)
expected=[['0','24/25','-7/25'],['-15/17','0','-8/17'],['0','-24/25','-7/25'],['1','0','0']]
ok('actual A point sequence',[points[i] for i in sa]==expected)
ok('actual B point sequence',all(points[i]==['1','0','0'] for i in sb))
a=record('ABBA');b=record('BAAB')
ok('quadratic witness same native endpoint',a[0]==b[0]==0)
ok('quadratic witness same Write counts',a[3].count(0)==b[3].count(0)==8 and a[3].count(1)==b[3].count(1)==8)
ok('quadratic witness same point counts',a[1][0]==b[1][0]);ok('quadratic witness same first phase moments',a[1][1]==b[1][1])
diff=[x-y for x,y in zip(a[1][2],b[1][2])]
expected_diff=[0]*8
for i in sa[:3]:expected_diff[i]=64
expected_diff[sa[3]]=-192
ok('quadratic witness exact second phase difference',diff==expected_diff)
ok('quadratic witness total second moment cancels',sum(diff)==0)
# Exact symbolic positive source-time variant. Coordinates are T_A,T_B,
# followed by four independent within-A and four within-B event offsets.
def timed_polynomial(blocks,power):
    start=[0]*10;out=[{} for _ in points]
    for b in blocks:
        for event,j in enumerate(sa if b=='A' else sb):
            t=start[:];t[2+(0 if b=='A' else 4)+event]+=1
            if power==1:
                for i,c in enumerate(t):
                    if c:out[j][(i,)]=out[j].get((i,),0)+c
            else:
                for i,c in enumerate(t):
                    for k in range(i,len(t)):
                        value=c*t[k]*(1 if i==k else 2)
                        if value:out[j][(i,k)]=out[j].get((i,k),0)+value
        start[0 if b=='A' else 1]+=1
    return out
source_time=[]
for degree in [1,2]:
    x=timed_polynomial('ABBA',degree);y=timed_polynomial('BAAB',degree)
    diffs=[]
    for j in range(len(points)):
        delta={key:x[j].get(key,0)-y[j].get(key,0) for key in set(x[j])|set(y[j])}
        delta={key:v for key,v in delta.items() if v}
        expected={}
        if degree==2:
            if j in sa[:3]:expected={(0,1):2,(1,1):2}
            elif j==sa[3]:expected={(0,0):-8,(0,1):-6,(1,1):2}
        ok('original source-time symbolic degree'+str(degree)+' point'+str(j),delta==expected)
        diffs.append({','.join(map(str,k)):v for k,v in delta.items()})
    source_time.append({'degree':degree,'difference_by_native_point':diffs})
# Source-bound family of all permutations of two A/two B blocks.
family=[]
for positions in combinations(range(4),2):
    blocks=''.join('A' if i in positions else 'B' for i in range(4));q,m,seen,w=record(blocks)
    family.append({'blocks':blocks,'endpoint':q,'moments':m})
ranks=[]
for d in range(3):
    f=[sum(x['moments'][:d+1],[]) for x in family];ref=f[0]
    got=rank([[x-y for x,y in zip(row,ref)] for row in f[1:]])
    ranks.append(got)
    ok('actual closed-word contrast rank degree'+str(d),got==d)
# General Prouhet same-source witnesses through degree four.
hierarchy=[]
for d in range(5):
    count=2**(d+1)
    even=[b for b in range(count) if b.bit_count()%2==0];odd=[b for b in range(count) if b.bit_count()%2]
    for k in range(d+1):ok('Prouhet equal powers d'+str(d)+' k'+str(k),sum(b**k for b in even)==sum(b**k for b in odd))
    nextdiff=sum(b**(d+1) for b in even)-sum(b**(d+1) for b in odd)
    theory=(-1)**(d+1)*math.factorial(d+1)*2**(d*(d+1)//2)
    ok('Prouhet exact next coefficient d'+str(d),nextdiff==theory)
    word0=''.join('A' if i in even else 'B' for i in range(count));word1=''.join('A' if i in odd else 'B' for i in range(count))
    x=record(word0,d+1);y=record(word1,d+1)
    ok('actual hierarchy endpoint d'+str(d),x[0]==y[0]==0)
    for k in range(d+1):ok('actual hierarchy lower moments d'+str(d)+' k'+str(k),x[1][k]==y[1][k])
    delta=[a-b for a,b in zip(x[1][d+1],y[1][d+1])]
    expected=[0]*8
    for i in sa[:3]:expected[i]=4**(d+1)*theory
    expected[sa[3]]=-3*4**(d+1)*theory
    ok('actual hierarchy next source moment d'+str(d),delta==expected)
    hierarchy.append({'equal_degrees_through':d,'writes_per_word':4*count,'block_difference_at_next_power':nextdiff,'source_moment_difference_scaled_by_h_power':delta})
# Actual literal source energy, with entire retained B18 (no diagonal substitute).
energy_path=OLD/'energy/NATIVE_INPUTS.json';E=json.loads(energy_path.read_text())
B=[[F(x) for x in r] for r in E['exact_operands']['B18_literal']]
L=[[F(x) for x in r] for r in E['exact_operands']['L_diagnostic']]
r=[F(-1),F(0)]
X=solve(B,L);M=mul(trans(L),X);u=solve(M,[[x] for x in r]);v=mul(X,u)
ambient=sum((r[i]*u[i][0] for i in range(2)),F(0))
ok('ambient receiver exact',mul(trans(L),v)==[[x] for x in r])
# Make every native endpoint displacement and exact cost explicit.
costs=[];D=[]
for z in range(1,16):
    dy=[F(0)]*18;dy[2]=-1;dy[2+z]=1
    record_value=[sum((L[i][j]*dy[i] for i in range(18)),F(0)) for j in range(2)]
    c=sum((dy[i]*B[i][j]*dy[j] for i in range(18) for j in range(18)),F(0))
    h=[dy[i]-v[i][0] for i in range(18)]
    residual=sum((h[i]*B[i][j]*h[j] for i in range(18) for j in range(18)),F(0))
    if record_value==r:ok('exact feasibility residual z'+str(z),c==ambient+residual and residual>0)
    costs.append({'z':z,'record_change':list(map(str,record_value)),'displacement_cost':str(c),'single_literal_flip_from_zero':z in (1,2,4,8)})
    D.append(dy)
compatible=[x for x in costs if x['record_change']==list(map(str,r))]
minimum=min(F(x['displacement_cost']) for x in compatible);minimizers=[x['z'] for x in compatible if F(x['displacement_cost'])==minimum]
ok('source-fiber minimum',minimum==F(1085537,573049));ok('source-fiber minimizers are actual single flips',minimizers==[2,8])
ok('strict positive realizability correction',minimum>ambient)
# Every outside change adds squares because the source metric is block diagonal.
ok('H and REST energy baselines exactly separate',all(B[i][j]==F(i==j) for i in range(2) for j in range(18)))
ok('source-fiber costs retain every original offdiagonal energy',F(costs[0]['displacement_cost'])==F(2006049,573049))
# Native operand for one full source-bound 15x15 contact product.
Dt=trans(D)
operands={'schema':'SAM_CH2_RECORD_AND_FEASIBLE_ENERGY_NATIVE_OPERANDS_V1','B18_literal':[[str(x) for x in row] for row in B],
'D_endpoint_displacements_18x15':[[str(x) for x in row] for row in Dt],
'expected_all_endpoint_contact_15x15':[[str(x) for x in row] for row in mul(trans(Dt),mul(B,Dt))],
'actual_closed_word_moment_contrast_matrix':[[x-y for x,y in zip(sum(row['moments'][:3],[]),sum(family[0]['moments'][:3],[]))] for row in family[1:]],
'expected_contrast_rank':2,'original_sources':{'transition_table':{'path':str(source_path.relative_to(ROOT)),'sha256':sha(source_path)},'literal_energy':{'path':str(energy_path.relative_to(ROOT)),'sha256':sha(energy_path)}},
'scope':'Native product/rank targets; independent checker emits operands but launches no native execution.'}
(BASE/'NATIVE_OPERANDS.json').write_text(json.dumps(operands,indent=2)+'\n')
result={'schema':'SAM_CH2_TIMED_RECORD_AND_SOURCE_FEASIBLE_ENERGY_V1','status':'PASS','independent_checks_passed':len(checks),'checks':checks,
'quadratic_witness':{'left':'ABBA','right':'BAAB','A':'W1+^4','B':'W7+^4','native_point_order':points,'scaled_second_moment_difference':diff,'phase_step':'h=3*pi/32 under declared 16-event actual-clock schedule'},
'original_source_time_symbolic_witness':source_time,'actual_six_word_family':family,'linear_additive_contrast_ranks_degree_0_to_2':ranks,'source_polynomial_hierarchy':hierarchy,
'feasible_energy':{'diagnostic_record_change':list(map(str,r)),'ambient_minimum':str(ambient),'source_fiber_minimum':str(minimum),'positive_feasibility_correction':str(minimum-ambient),'minimizing_port_labels':minimizers,'all_endpoints':costs,
'ambient_minimizer':[str(x[0]) for x in v],'source_preparation_scope':'Pure original source configurations on fixed-outside fiber; actual selection/preparation and physical kappa_E not newly assigned'},
'source_bindings':operands['original_sources'],'native_launches':0,'generator_sha256':sha(Path(__file__))}
(BASE/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'source_family_ranks':ranks,'actual_hierarchy_degrees':len(hierarchy),'source_fiber_minimum':str(minimum),'ambient_minimum_decimal':float(ambient),'feasibility_correction_decimal':float(minimum-ambient)}))
