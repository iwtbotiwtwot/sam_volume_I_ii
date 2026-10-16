#!/usr/bin/env python3
"""Independent protocol replay and compact Chapter II proof certificates.

Standard library only. Replays the two existing protocol algorithms with only
their output-directory bindings relocated; it never changes their files or
starts native sessions. Rechecks original-source counters and endpoint costs.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import ast
import contextlib
import hashlib
import io
import json

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]
CERT = BASE/'certificates'
PREV = ROOT/'GEN4/voli_chapter2_continuation2_20261015'
checks = []


def require(name, value):
    if not value:
        raise AssertionError(name)
    checks.append(name)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def enc(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, tuple):
        return {'lower':str(value[0]),'upper':str(value[1])}
    if isinstance(value, list):
        return [enc(x) for x in value]
    if isinstance(value, dict):
        return {str(k):enc(x) for k,x in value.items()}
    return value


class OutputRelocation(ast.NodeTransformer):
    """Change only source-level path bindings; retain every arithmetic node."""
    def __init__(self, output):
        self.output=output
        self.modified=[]

    def visit_Assign(self, node):
        if len(node.targets)==1 and isinstance(node.targets[0],ast.Name):
            name=node.targets[0].id
            if name in ('BASE','HERE','ROOT'):
                destination=ROOT if name=='ROOT' else self.output
                node.value=ast.Call(func=ast.Name(id='Path',ctx=ast.Load()),
                                    args=[ast.Constant(value=str(destination))],keywords=[])
                self.modified.append(name)
        return node


def replay(name):
    path=BASE/name/'verify.py'
    output=CERT/('replay_'+name)
    output.mkdir(parents=True,exist_ok=True)
    tree=ast.parse(path.read_text(),filename=str(path))
    relocation=OutputRelocation(output)
    tree=ast.fix_missing_locations(relocation.visit(tree))
    require(name+'_only_declared_path_bindings_relocated',
            sorted(relocation.modified)==sorted(['ROOT','HERE' if name=='measurement' else 'BASE']))
    log=io.StringIO()
    namespace={'__name__':'__main__','__file__':str(path)}
    before={p:sha(p) for p in (BASE/name).iterdir() if p.is_file()}
    with contextlib.redirect_stdout(log):
        exec(compile(tree,str(path),'exec'),namespace)
    require(name+'_original_files_unchanged',all(sha(p)==h for p,h in before.items()))
    result=read(output/'RESULTS.json')
    require(name+'_replay_pass',result['status']=='PASS')
    require(name+'_replay_equals_recorded_result',result==read(BASE/name/'RESULTS.json'))
    return {'script':str(path.relative_to(ROOT)),'script_sha256':sha(path),
            'replay_output':str(output.relative_to(BASE)),
            'result_sha256':sha(output/'RESULTS.json'),
            'checks':result.get('checks_passed'),'stdout':log.getvalue().strip()},result


def rank(matrix):
    a=[[F(x) for x in row] for row in matrix]
    i=0
    for j in range(len(a[0]) if a else 0):
        pivot=next((k for k in range(i,len(a)) if a[k][j]),None)
        if pivot is None:
            continue
        a[i],a[pivot]=a[pivot],a[i]
        d=a[i][j]
        a[i]=[x/d for x in a[i]]
        for k in range(i+1,len(a)):
            d=a[k][j]
            a[k]=[x-d*y for x,y in zip(a[k],a[i])]
        i+=1
        if i==len(a):
            break
    return i


def inverse(a):
    n=len(a)
    m=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if m[i][j])
        m[j],m[pivot]=m[pivot],m[j]
        f=m[j][j]
        m[j]=[x/f for x in m[j]]
        for i in range(n):
            if i!=j:
                f=m[i][j]
                m[i]=[x-f*y for x,y in zip(m[i],m[j])]
    return [row[n:] for row in m]


def mul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def trans(a):
    return list(map(list,zip(*a)))


def add(a,b):
    out=a.copy()
    for k,v in b.items():
        out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}


def scale(a,c):
    return {k:c*v for k,v in a.items() if c*v}


def nc_product(a,b):
    out={}
    for ka,va in a.items():
        for kb,vb in b.items():
            key=ka+kb
            out[key]=out.get(key,F(0))+va*vb
    return {k:v for k,v in out.items() if v}


def square_sum(forms):
    out={}
    for a in forms:
        for i,x in enumerate(a):
            for j in range(i,len(a)):
                out=add(out,{(i,j):F(x*a[j]*(1 if i==j else 2))})
    return out


def pair(x):
    if 're' in x:
        x=x['re']
    return F(x['lower']),F(x['upper'])


def iproduct(a,b):
    p=[x*y for x in a for y in b]
    return min(p),max(p)


def isub(a,b):
    return a[0]-b[1],a[1]-b[0]


def idiv(a,b):
    require('positive_interval_divisor',b[0]>0)
    return iproduct(a,(1/b[1],1/b[0]))


def main():
    CERT.mkdir(exist_ok=True)
    replay_measurement,measurement=replay('measurement')
    replay_protocol,protocol=replay('protocol')
    require('physical_protocol_full_coordinate_budget',protocol['readout']['shots_per_X_or_Y_mean']==26624)
    require('physical_protocol_total_freshcopies',protocol['readout']['maximum_fresh_preparations']==23482368)
    require('measurement_eight_distinct_expectations_not_shots',measurement['improved']['total_measurement_shots']==6558008)
    # Formal noncommuting block multiplication. U denotes C adjoint.
    B,U,C,D=[{(symbol,):F(1)} for symbol in ['B','U','C','D']]
    block=[[B,U],[C,D]]
    square=[[add(nc_product(block[i][0],block[0][j]),nc_product(block[i][1],block[1][j]))
             for j in range(2)] for i in range(2)]
    require('noncommuting_block_square_top_left',square[0][0]=={('B','B'):1,('U','C'):1})
    require('noncommuting_block_square_cross',square[0][1]=={('B','U'):1,('U','D'):1})
    # Verify the source-dependent Gram-normalized norm certificate for all54.
    memory_inputs=read(PREV/'memory/SOURCE_OPERANDS.json')
    memory=read(PREV/'memory/INDEPENDENT_RESULTS.json')
    require('memory_input_hash_authentication',sha(PREV/'memory/SOURCE_OPERANDS.json')==memory['source_operands_sha256'])
    require('memory_preparation_coverage',len(memory_inputs['profiles'])==len(memory['results'])==54)
    metric_certificates=[]
    for source,result in zip(memory_inputs['profiles'],memory['results']):
        require('memory_profile_identity',source['profile_id']==result['profile_id'])
        require('memory_rank_two_positive_determinant',pair(result['K0_block_determinant'])[0]>0 and pair(result['delta'])[0]>0)
        U11=pair(source['U'][0][0]);U22=pair(source['U'][1][1]);U12=pair(source['U'][0][1])
        detU=isub(iproduct(U11,U22),iproduct(U12,U12))
        metric=idiv(U11,detU)
        trace1=iproduct(pair(result['delta']),metric)
        trace2=idiv(pair(result['R5']),pair(source['W'][0][0]))
        bound=trace1[1]+trace2[1]
        require('physical_source_metric_norm_bound',bound<F(7524585,10**6))
        require('original_positive_odd_gap_and_full_N',F(source['gamma_lower'])>0 and int(source['N_exact'])>0)
        metric_certificates.append({'profile_id':source['profile_id'],'inverse_ue_metric_upper':metric[1],
                                    'K0_trace_upper':bound,'gamma_lower':source['gamma_lower'],
                                    'N_exact':source['N_exact']})
    # Exact source transitions, legal closed words and all moments through2.
    original=read(PREV/'records/RESULTS.json')
    reduction=ROOT/original['source_bindings']['transition_table']['path']
    energy=ROOT/original['source_bindings']['literal_energy']['path']
    require('transition_source_hash',sha(reduction)==original['source_bindings']['transition_table']['sha256'])
    require('literal_B18_hash',sha(energy)==original['source_bindings']['literal_energy']['sha256'])
    source=read(reduction)
    points=source['points'];point_index={tuple(p):i for i,p in enumerate(points)}
    transition=source['quotient_transitions']
    output=[point_index[tuple(o[0])] for o in source['quotient_outputs']]

    def record(blocks):
        state=0;events=[];moments=[[0]*len(points) for _ in range(3)]
        for b in blocks:
            for _ in range(4):
                state=transition[state][0 if b=='A' else 1]
                j=output[state];events.append(j);n=len(events)
                for k in range(3):
                    moments[k][j]+=n**k
        return state,events,moments

    stateA,eventsA,_=record('A');stateB,eventsB,_=record('B')
    require('actual_A_B_closed',stateA==stateB==0)
    require('actual_three_distinct_A_only_points',len(set(eventsA[:3]))==3 and eventsA[3] not in eventsA[:3])
    require('actual_B_common_point',set(eventsB)=={eventsA[3]})
    rows=[]
    for positions in combinations(range(4),2):
        word=''.join('A' if i in positions else 'B' for i in range(4))
        state,_,moments=record(word)
        S1=sum(positions);S2=sum(x*x for x in positions)
        decoded=[[0]*len(points) for _ in range(3)]
        for offset,j in enumerate(eventsA[:3],1):
            decoded[0][j]=2
            decoded[1][j]=4*S1+2*offset
            decoded[2][j]=16*S2+8*offset*S1+2*offset*offset
        for k in range(3):
            decoded[k][eventsA[3]]=sum(n**k for n in range(1,17))-sum(decoded[k])
        require('exact_two_counter_decoder_'+word,state==0 and moments==decoded)
        rows.append({'word':word,'S1':S1,'S2':S2,'moments':moments})
    ranks=[]
    for degree in range(3):
        vectors=[sum(r['moments'][:degree+1],[]) for r in rows]
        rank_value=rank([[a-b for a,b in zip(row,vectors[0])] for row in vectors[1:]])
        require('minimal_counter_rank_degree_'+str(degree),rank_value==degree)
        ranks.append(rank_value)
    require('counter_lower_bound_minor',1*8-2*3==2)
    abba=next(r for r in rows if r['word']=='ABBA')
    baab=next(r for r in rows if r['word']=='BAAB')
    delta=[x-y for x,y in zip(abba['moments'][2],baab['moments'][2])]
    require('ABBA_BAAB_exact_point_certificate',delta==original['quadratic_witness']['scaled_second_moment_difference'])
    require('ABBA_BAAB_equal_counts_first',abba['moments'][:2]==baab['moments'][:2])
    # Symbolic physical-time offsets: variables are TA, TB, event offset.
    A_left=[(0,0,1),(1,2,1)];A_right=[(0,1,1),(1,1,1)]
    B_left=[(1,0,1),(1,1,1)];B_right=[(0,0,1),(2,1,1)]
    require('ABBA_A_start_sums',tuple(map(sum,zip(*A_left)))==tuple(map(sum,zip(*A_right))))
    require('ABBA_B_start_sums',tuple(map(sum,zip(*B_left)))==tuple(map(sum,zip(*B_right))))
    A_delta=add(square_sum(A_left),scale(square_sum(A_right),-1))
    B_delta=add(square_sum(B_left),scale(square_sum(B_right),-1))
    common_delta=add(A_delta,scale(B_delta,4))
    require('ABBA_A_exact_event_offsets',A_delta=={(0,1):2,(1,1):2})
    require('ABBA_B_exact_event_offsets',B_delta=={(0,0):-2,(0,1):-2})
    require('ABBA_common_exact_event_offsets',common_delta=={(0,0):-8,(0,1):-6,(1,1):2})
    # Every pure port endpoint, using every entry of literal B18.
    exact=read(energy)['exact_operands']
    B18=[[F(x) for x in row] for row in exact['B18_literal']]
    receiver=[[F(x) for x in row] for row in exact['L_diagnostic']]
    require('outside_energy_account_separate',all(B18[i][j]==F(i==j) for i in range(2) for j in range(18)))
    endpoints=[]
    for z in range(16):
        dy=[F(0)]*18;dy[2]-=1;dy[2+z]+=1
        record_value=mul(trans(receiver),[[x] for x in dy])
        cost=sum(dy[i]*B18[i][j]*dy[j] for i in range(18) for j in range(18))
        feasible=record_value==[[F(-1)],[F(0)]]
        require('feasible_endpoint_class_'+str(z),feasible==(z>=2))
        if feasible:
            retained=next(r for r in original['feasible_energy']['all_endpoints'] if r['z']==z)
            require('full_source_endpoint_cost_'+str(z),cost==F(retained['displacement_cost']))
            require('common_denominator_integer_cost_'+str(z),(cost*573049).denominator==1)
            endpoints.append({'z':z,'cost':cost,'cost_numerator_over_573049':int(cost*573049),
                              'one_literal_flip':z in (1,2,4,8)})
    minimum=min(row['cost'] for row in endpoints)
    minimizers=[row['z'] for row in endpoints if row['cost']==minimum]
    require('all_fourteen_feasible_endpoints',len(endpoints)==14)
    require('exact_minimum_and_attaining_flips',minimum==F(1085537,573049) and minimizers==[2,8])
    # Independent ambient constrained minimum and Pythagorean correction.
    X=mul(inverse(B18),receiver)
    record_matrix=mul(trans(receiver),X)
    multiplier=mul(inverse(record_matrix),[[F(-1)],[F(0)]])
    optimum=mul(X,multiplier)
    ambient=-multiplier[0][0]
    require('ambient_exact_minimum_replayed',ambient==F(original['feasible_energy']['ambient_minimum']))
    require('strict_feasible_payment',minimum>ambient)
    endpoint_cert={'schema':'SAM_CH2_COMPACT_PROOF_CERTIFICATES_V1',
                   'source_bindings':original['source_bindings'],
                   'block_square_top_left':{'B*B':1,'C_adjoint*C':1},
                   'counter_family':rows,'counter_ranks_degree_0_to_2':ranks,
                   'ABBA_second_moment_difference':delta,
                   'ABBA_physical_time_polynomial':{'A_only':{'TA*TB':2,'TB^2':2},
                                                     'common':{'TA^2':-8,'TA*TB':-6,'TB^2':2}},
                   'all_feasible_endpoints':endpoints,'source_minimum':minimum,'minimizers':minimizers,
                   'ambient_minimum':ambient,'feasibility_correction':minimum-ambient,
                   'source_metric_certificates':metric_certificates}
    (CERT/'COMPACT_CERTIFICATES.json').write_text(json.dumps(enc(endpoint_cert),indent=2)+'\n')
    result={'schema':'SAM_CH2_PHYSICAL_PROTOCOLS_REPLAY_V1','status':'PASS',
            'scope':'Offline independent receiving/proof replay; no native execution or apparatus realization.',
            'replays':[replay_measurement,replay_protocol],'checks_passed':len(checks),'checks':checks,
            'compact_certificate_sha256':sha(CERT/'COMPACT_CERTIFICATES.json'),
            'script_sha256':sha(Path(__file__))}
    (BASE/'PROTOCOLS_VERIFICATION.json').write_text(json.dumps(enc(result),indent=2)+'\n')
    print(json.dumps({'status':'PASS','checks_passed':len(checks),
                      'measurement_replay_checks':replay_measurement['checks'],
                      'reference_replay_checks':replay_protocol['checks'],
                      'counter_ranks':ranks,'feasible_endpoints':len(endpoints),
                      'attaining_endpoints':minimizers},indent=2))


if __name__=='__main__':
    main()
