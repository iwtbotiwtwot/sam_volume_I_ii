#!/usr/bin/env python3
"""Independent readback of the physical-protocol Duck native returns.

No native execution. Exact Fraction algebra checks receiving observables,
counter rank and work coefficients. Independent dyadic interval elimination
checks actual full-N source minors, inverse consistency and Gibbs witnesses.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse
import hashlib
import importlib.util
import json
import sys

BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[1]
DEFAULT_RUN=ROOT/'GEN4/duck_gen6_local/runs/chapter2-physical-protocols-20261015-01'
checks=[]
receipts=[]
entries=0
source_certificates=[]


def require(name,condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def read(path):
    return json.loads(Path(path).read_text())


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def matrix(a):
    return [[F(x) for x in row] for row in a]


def eye(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]


def mul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def add(a,b):
    return [[x+y for x,y in zip(row,col)] for row,col in zip(a,b)]


def rank(a):
    a=[row[:] for row in a]
    i=0
    for j in range(len(a[0]) if a else 0):
        pivot=next((k for k in range(i,len(a)) if a[k][j]),None)
        if pivot is None:
            continue
        a[i],a[pivot]=a[pivot],a[i]
        f=a[i][j];a[i]=[x/f for x in a[i]]
        for k in range(i+1,len(a)):
            f=a[k][j]
            a[k]=[x-f*y for x,y in zip(a[k],a[i])]
        i+=1
        if i==len(a):
            break
    return i


def inverse(a):
    n=len(a)
    aug=[row[:]+eye(n)[i] for i,row in enumerate(a)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if aug[i][j])
        aug[j],aug[pivot]=aug[pivot],aug[j]
        f=aug[j][j];aug[j]=[x/f for x in aug[j]]
        for i in range(n):
            if i!=j:
                f=aug[i][j]
                aug[i]=[x-f*y for x,y in zip(aug[i],aug[j])]
    return [row[n:] for row in aug]


def same_matrix(name,a,b):
    global entries
    require(name+'_rows',len(a)==len(b))
    for i,(row,expected) in enumerate(zip(a,b)):
        require(name+'_columns_'+str(i),len(row)==len(expected))
        for j,(actual,value) in enumerate(zip(row,expected)):
            require(name+f'_{i}_{j}',actual==value)
            entries+=1


def import_point_verifier():
    path=BASE/'closure/verify_point_certificate.py'
    name='sam_ch2_physical_point_independent'
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module


def map_original_path(path,oldroot):
    p=Path(path)
    if p.is_absolute():
        relative=p.relative_to(oldroot)
    else:
        relative=p
    require('safe_relative_source_path_'+p.name,'..' not in relative.parts)
    return ROOT/relative


def native(run,key,operation):
    wrapper_path=run/'native_returns'/(key+'.json')
    request_path=run/'native_requests'/(key+'.json')
    wrapper=read(wrapper_path)
    request=read(request_path)['task']
    config=read(run/'CONFIG.json')
    oldroot=Path(config['prepared_run']).parents[3]
    pointer=wrapper.get('record_file',wrapper.get('receipt'))
    digest=wrapper.get('record_file_sha256',wrapper.get('receipt_sha256'))
    require(key+'_receipt_pointer_present',bool(pointer and digest))
    receipt_path=map_original_path(pointer,oldroot)
    receipt=read(receipt_path)
    require(key+'_receipt_hash',sha(receipt_path)==digest)
    require(key+'_identity',receipt['key']==key and wrapper['key']==key)
    require(key+'_operation',receipt['operation']==operation and request['operation']==operation)
    require(key+'_completed',receipt['status']==wrapper['status']=='COMPLETED')
    require(key+'_native_arithmetic',receipt['host_domain_arithmetic'] is False)
    require(key+'_payload_unchanged',receipt['native_payload']==request['payload'])
    if 'returned' in wrapper:
        require(key+'_wrapper_return',receipt['returned']==wrapper['returned'])
    else:
        require(key+'_large_record_reference',wrapper['record_file_sha256']==digest and
                wrapper['bytes']==receipt_path.stat().st_size)
    for item in receipt.get('checks',[]):
        require(key+'_native_contract_'+str(item.get('predicate',item.get('name','check'))),item['passed'])
    binding=receipt['native_payload']['source_binding']
    for path,digest in binding.get('source_files',{}).items():
        mapped=map_original_path(path,oldroot)
        require(key+'_source_hash_'+mapped.name,sha(mapped)==digest)
    receipts.append({'key':key,'operation':operation,
                     'request_path':str(request_path.relative_to(ROOT)),'request_sha256':sha(request_path),
                     'wrapper_path':str(wrapper_path.relative_to(ROOT)),'wrapper_sha256':sha(wrapper_path),
                     'receipt_path':str(receipt_path.relative_to(ROOT)),'receipt_sha256':sha(receipt_path)})
    return receipt['native_payload'],receipt['returned']


def exact_word(run,key,expected_operators,expected_program,expected_output,expected_rank):
    payload,returned=native(run,key,'GEN3_SOURCE_OPERATOR_WORD')
    data=payload['data']
    require(key+'_operator_names',set(data['operators'])==set(expected_operators))
    for name,expected in expected_operators.items():
        same_matrix(key+'_operand_'+name,matrix(data['operators'][name]),matrix(expected))
    require(key+'_program',data['program']==expected_program)
    require(key+'_output_binding',data['output']==expected_output)
    env={k:matrix(v) for k,v in expected_operators.items()}
    for step in expected_program:
        a,b=(env[k] for k in step['inputs'])
        require(key+'_supported_exact_program_operation',step['op'] in ('multiply','add'))
        env[step['name']]=mul(a,b) if step['op']=='multiply' else add(a,b)
    expected=env[expected_output]
    same_matrix(key+'_returned_matrix',matrix(returned['matrix']),expected)
    require(key+'_exact_rank',rank(expected)==returned['rank']==expected_rank)
    require(key+'_native_backend',returned['execution']['backend']=='NATIVE_CPP_GMP_CPU')
    return expected


def exact_solve(run,key,a):
    global entries
    payload,returned=native(run,key,'GEN3_COMPLEX_SOLVE')
    same_matrix(key+'_matrix_payload',matrix(payload['data']['matrix']['entries']),a)
    same_matrix(key+'_rhs_payload',matrix(payload['data']['rhs']['entries']),eye(len(a)))
    require(key+'_precision',payload['precision_bits']==1024)
    output=returned['result']['output']
    require(key+'_solve_certified',output['status']=='CERTIFIED_SOLVE')
    exact=inverse(a);actual=output['matrix']['entries']
    require(key+'_inverse_shape',len(actual)==len(a) and all(len(row)==len(a) for row in actual))
    for i,row in enumerate(actual):
        for j,value in enumerate(row):
            require(key+f'_inverse_real_{i}_{j}',F(value['re']['lower'])<=exact[i][j]<=F(value['re']['upper']))
            require(key+f'_inverse_imag_{i}_{j}',F(value['im']['lower'])<=0<=F(value['im']['upper']))
            entries+=1
    same_matrix(key+'_independent_exact_identity',mul(a,exact),eye(len(a)))


def interval_source_solve(run,key,source_path,point):
    global entries
    source=read(source_path)
    if 'profiles' in source:
        source=source['profiles'][0]
    certificate=point.verify(source)
    selected=source['certificate']['row_indices'];n=len(selected)
    expected=[[source['evaluation_rows'][i][j] for j in range(n)] for i in selected]
    payload,returned=native(run,key,'GEN3_COMPLEX_SOLVE')
    actual=payload['data']['matrix']['entries']
    require(key+'_source_matrix_shape',len(actual)==n and all(len(row)==n for row in actual))
    for i,row in enumerate(actual):
        for j,cell in enumerate(row):
            require(key+f'_literal_source_input_{i}_{j}',cell['re']==expected[i][j] and cell['im']==0)
            entries+=1
    same_matrix(key+'_identity_rhs',matrix(payload['data']['rhs']['entries']),eye(n))
    require(key+'_high_precision_inverse',payload['precision_bits']==1024)
    output=returned['result']['output']
    require(key+'_native_certified_solve',output['status']=='CERTIFIED_SOLVE')
    source_matrix=[[point.I.make(x) for x in row] for row in expected]
    determinant,independent=point.inverse(source_matrix)
    inverse_output=output['matrix']['entries']
    require(key+'_returned_inverse_shape',len(inverse_output)==n and all(len(row)==n for row in inverse_output))
    actual_inverse=[]
    for i,row in enumerate(inverse_output):
        outrow=[]
        for j,cell in enumerate(row):
            interval=point.I.make(cell['re'])
            expected_interval=independent[i][j]
            require(key+f'_independent_inverse_overlap_{i}_{j}',
                    max(interval.lo,expected_interval.lo)<=min(interval.hi,expected_interval.hi))
            require(key+f'_imaginary_zero_{i}_{j}',F(cell['im']['lower'])<=0<=F(cell['im']['upper']))
            outrow.append(interval);entries+=1
        actual_inverse.append(outrow)
    # Independent interval product verifies compatibility with the literal
    # uncertain matrix, without treating interval midpoints as exact source.
    for i in range(n):
        for j in range(n):
            product=sum((source_matrix[i][k]*actual_inverse[k][j] for k in range(n)),point.I.make(0))
            require(key+f'_inverse_product_identity_{i}_{j}',product.lo<=F(i==j)<=product.hi)
    require(key+'_strict_point_rank',not determinant.contains0() and certificate['rank_lower_bound']==n)
    source_certificates.append({'key':key,'source_path':str(source_path.relative_to(ROOT)),
                                'source_sha256':sha(source_path),'profile_id':source['profile_id'],
                                'N_exact':source['N_exact'],'rank_lower_bound':n,
                                'determinant':determinant.wire(),
                                'inverse_comparison':'Every real enclosure overlaps independent dyadic elimination; imaginary enclosures contain0; full interval product contains identity.',
                                'closure_status':'Reached source rank certified; stabilization not asserted.'})


def interval_overlap(a,b):
    return max(F(a['lower']),F(b['lower']))<=min(F(a['upper']),F(b['upper']))


def stroke(run,key,event,state,orientation,reference):
    payload,returned=native(run,key,'GEN5_SOURCE_STROKE_INTEGRAL')
    expected={'law':'AN0005_J4_B1_SIGNED_WRITE_V1','state':state,'event':event,
              'orientation':orientation,'clock_path':'LOCAL_DENSITY_INTEGRAL'}
    require(key+'_original_stroke_payload',payload['data']==expected)
    require(key+'_qualified_precision',payload['precision_bits']==384)
    output=returned['result']['output']
    require(key+'_certified_stroke',output['status']=='CERTIFIED_SOURCE_STROKE_INTEGRAL')
    require(key+'_native_coordinate_crosscheck',output['coordinate_crosscheck'] is True)
    require(key+'_returned_original_identity',all(output[k]==v for k,v in expected.items()))
    require(key+'_returned_precision',output['precision_bits']==384)
    integral=output['integral']
    require(key+'_strict_positive_integral',F(integral['lower'])>0)
    require(key+'_original_integral_overlap',interval_overlap(integral,reference['row']['integral']))
    require(key+'_strict_positive_angular_integral',F(output['angle_integral']['lower'])>0)
    require(key+'_two_coordinates_overlap',interval_overlap(integral,output['angle_integral']))
    require(key+'_original_angular_integral_overlap',interval_overlap(output['angle_integral'],reference['row']['angle_integral']))
    require(key+'_entire_half_angle_receiver',output['receiver_operand']=='Half-angle enclosure; no midpoint replacement or coordinate intersection')
    return integral


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--run',type=Path,default=DEFAULT_RUN)
    args=parser.parse_args();run=args.run.resolve()
    measurement=read(BASE/'inputs/MEASUREMENT_R2.json')
    protocol=read(BASE/'inputs/PROTOCOL_R2.json')
    require('frozen_measurement_operands_equal_current',measurement==read(BASE/'measurement/NATIVE_OPERANDS.json'))
    require('frozen_protocol_operands_equal_current',protocol==read(BASE/'protocol/NATIVE_PAYLOAD.json'))
    original=read(BASE/'protocol/ORIGINAL_CERTIFICATES.json')
    fwd=stroke(run,'r1_forward_duration','W1+',[0,0,0],1,original['forward'])
    rev=stroke(run,'r1_reverse_duration','W1-',[1,0,0],-1,original['reverse'])
    require('native_forward_reverse_positive_duration_overlap',interval_overlap(fwd,rev))
    point=import_point_verifier()
    interval_source_solve(run,'r1_actual_source_rank10',BASE/'closure/native_v001-p4/SOURCE_RAW.json',point)
    O=measurement['O']
    exact_word(run,'r1_observable_cube',{'O':O},
               [{'name':'O2','op':'multiply','inputs':['O','O']},
                {'name':'O3','op':'multiply','inputs':['O2','O']}],'O3',2)
    H=measurement['improved_nominal_H3_rounded']
    exact_word(run,'r2_improved_H3_word',{'H':H,'I':eye(3)},
               [{'name':'HI','op':'multiply','inputs':['H','I']}],'HI',3)
    exact_solve(run,'r2_improved_H3_inverse',matrix(H))
    exact_word(run,'r2_paid_work_coefficients',protocol['data']['operators'],
               protocol['data']['program'],protocol['data']['output'],0)
    interval_source_solve(run,'r2_deep_source_inverse',BASE/'inputs/DEEP_SOURCE_R2.json',point)
    interval_source_solve(run,'r2_largest_N_inverse',BASE/'inputs/LARGEST_SOURCE_R2.json',point)
    exact_word(run,'r2_zero_readout_projector',{'O':O,'P0twice':measurement['P0_twice']},
               [{'name':'zero','op':'multiply','inputs':['O','P0twice']}],'zero',0)
    exact_word(run,'r2_min_counter_rank',{'C':[[1,2],[3,8]],'I':eye(2)},
               [{'name':'CI','op':'multiply','inputs':['C','I']}],'CI',2)
    require('all_eleven_native_outputs_read_back',len(receipts)==11)
    report={'schema':'SAM_CH2_PHYSICAL_NATIVE_READBACK_V1','status':'PASS',
            'role':'Independent native output readback; this verifier launches no native operation.',
            'native_outputs_verified':len(receipts),'matrix_entries_checked':entries,
            'independent_checks':len(checks),'checks':checks,'native_receipts':receipts,
            'actual_source_minors':source_certificates,
            'original_stroke_integral_overlap':{'forward':fwd,'reverse':rev,
                                               'calibration':'positive original duration=integral/10'},
            'inverse_scope':'Exact rational receiving inverse is enclosed; uncertain source inverses are independently compatible as explicitly reported.',
            'verifier_sha256':sha(Path(__file__)),'native_executions_from_this_script':0}
    (BASE/'NATIVE_VERIFICATION.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['status','native_outputs_verified','matrix_entries_checked','independent_checks']},indent=2))


if __name__=='__main__':
    main()
