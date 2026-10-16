"""Offline independent readback of three actual GEN6 Duck native returns.

No native imports or executions. Exact Fraction contractions use the original
literal B18 and source endpoint increments; the separate qubit control retains
its declared finite-apparatus status.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
BASE=Path(__file__).resolve().parent;ROOT=BASE.parents[2]
parser=argparse.ArgumentParser()
parser.add_argument('--run',type=Path,default=ROOT/'GEN4/duck_gen6_local/runs/chapter2-signature-memory-20261015-01')
args=parser.parse_args();RUN=args.run.resolve()
checks=[];receipts=[];native_entries=0;native_outputs=0

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def read(path):return json.loads(path.read_text())
def ok(name,value):
    assert value,name
    checks.append(name)
def matrix(rows):return [[F(x) for x in row] for row in rows]
def transpose(a):return list(map(list,zip(*a)))
def mul(a,b):return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*b)] for row in a]
def tensor(a,b):return [[x*y for x in rowa for y in rowb] for rowa in a for rowb in b]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]

def native(key,worker,operation):
    global native_outputs
    wrapper_path=RUN/'native_returns'/(key+'.json');req_path=RUN/'native_requests'/(key+'.json')
    wrapper=read(wrapper_path);request=read(req_path)['task']
    path=RUN/'workers'/worker/'tasks'/key/'RESULT.json';receipt=read(path)
    ok(key+' receipt file hash',sha(path)==wrapper['receipt_sha256'])
    ok(key+' expected key and worker',receipt['key']==key and receipt['id']==worker)
    ok(key+' native completed',receipt['status']=='COMPLETED' and receipt['operation']==operation)
    ok(key+' host arithmetic absent',receipt['host_domain_arithmetic'] is False)
    ok(key+' request to receipt payload',receipt['native_payload']==request['payload'])
    if 'returned' in wrapper:ok(key+' inline return same worker record',wrapper['returned']==receipt['returned'])
    native_outputs+=1
    receipts.append({'key':key,'request_path':str(req_path.relative_to(ROOT)),'request_sha256':sha(req_path),
      'wrapper_path':str(wrapper_path.relative_to(ROOT)),'wrapper_sha256':sha(wrapper_path),
      'worker_receipt_path':str(path.relative_to(ROOT)),'worker_receipt_sha256':sha(path),
      'operation':operation,'status':receipt['status']})
    return receipt

def exact_entries(label,actual,expected):
    global native_entries
    ok(label+' shape',len(actual)==len(expected) and all(len(a)==len(b) for a,b in zip(actual,expected)))
    for i,(row,values) in enumerate(zip(actual,expected)):
        for j,(x,v) in enumerate(zip(row,values)):
            ok(label+f' entry {i},{j}',F(x)==v)
            native_entries+=1

def enclosure_entries(label,actual,expected):
    global native_entries
    ok(label+' shape',len(actual)==len(expected) and all(len(a)==len(b) for a,b in zip(actual,expected)))
    for i,(row,values) in enumerate(zip(actual,expected)):
        for j,(x,v) in enumerate(zip(row,values)):
            ok(label+f' real enclosure {i},{j}',F(x['re']['lower'])<=v<=F(x['re']['upper']))
            ok(label+f' imaginary zero {i},{j}',F(x['im']['lower'])<=0<=F(x['im']['upper']))
            native_entries+=1

# The finite reference fixture has its own explicitly declared source density.
fixture_path=BASE/'NATIVE_OPERANDS.json';fixture=read(fixture_path)
ref=native('r2_reference_paid_inverse','G6_11','GEN3_SOURCE_OPERATOR_WORD')
ok('qubit fixture operand hash',ref['source_binding']['operand_sha256']==sha(fixture_path))
ok('qubit fixture not continuum assignment',ref['source_binding']['declared_fixture'] is True and ref['source_binding']['original_continuum_energy_assigned'] is False)
ops=ref['native_payload']['data']['operators']
expected_ops={'Hs':fixture['fixture_H_source'],'Hr':fixture['fixture_H_reference_inverse_write'],
'rs':fixture['fixture_density_source'],'rr':fixture['fixture_density_reference_balanced'],'I2':fixture['I2']}
ok('qubit fixture original declared operands',all(matrix(ops[k])==matrix(v) for k,v in expected_ops.items()))
Hs,Hr,rs,rr,I=(matrix(expected_ops[k]) for k in ['Hs','Hr','rs','rr','I2'])
rho=tensor(rs,rr);H=add(tensor(Hs,I),tensor(I,Hr));rhoH=mul(rho,H)
exact_entries('reference rhoH',ref['returned']['matrix'],rhoH)
w=F(fixture['fixture_w']);E=F(fixture['fixture_E_source'])
actual_trace=sum((F(ref['returned']['matrix'][i][i]) for i in range(4)),F(0))
ok('reference exact signed total expectation',actual_trace==w==F(-1))
ok('source fixture E independently contracted',sum(mul(rs,Hs)[i][i] for i in range(2))==E==F(19,5))
ok('reference fixture energy receives deficit',sum(mul(rr,Hr)[i][i] for i in range(2))==w-E==F(-24,5))
ok('reference native exact backend',ref['returned']['execution']['backend']=='NATIVE_CPP_GMP_CPU')

# Actual inherited original source energy and actual allowed endpoint changes.
records_path=BASE.parent/'records/NATIVE_OPERANDS.json';records=read(records_path)
original_path=ROOT/'GEN4/voli_chapter2_bridge1/energy/NATIVE_INPUTS.json'
original=read(original_path)
ok('literal original source hash',records['original_sources']['literal_energy']['sha256']==sha(original_path))
B=matrix(original['exact_operands']['B18_literal']);D=[[F(0) for _ in range(15)] for _ in range(18)]
for z in range(1,16):D[2][z-1]=-1;D[z+2][z-1]=1
ok('all endpoint increments independently reconstructed',D==matrix(records['D_endpoint_displacements_18x15']))
ok('record B18 same full original source',B==matrix(records['B18_literal']))
BD=mul(B,D);Gram=mul(transpose(D),BD)
ok('independent Gram matches source operands',Gram==matrix(records['expected_all_endpoint_contact_15x15']))
bd=native('r2_record_BD','G6_12','GEN3_COMPLEX_PRODUCT')
ok('record B18 native operand hash',bd['source_binding']['operand_sha256']==sha(records_path))
ok('native B18 exact input matches original',matrix(bd['native_payload']['data']['matrix']['entries'])==B)
ok('native endpoint input matches independent source increments',matrix(bd['native_payload']['data']['right']['entries'])==D)
bd_matrix=bd['returned']['result']['output']['matrix']['entries']
enclosure_entries('source B18D',bd_matrix,BD)
gram=native('r2_record_contact_Gram','G6_12','GEN3_COMPLEX_PRODUCT')
ok('native Gram left operand actual source transpose',matrix(gram['native_payload']['data']['matrix']['entries'])==transpose(D))
ok('native Gram reuses actual native BD',gram['native_payload']['data']['right']['entries']==bd_matrix)
gram_matrix=gram['returned']['result']['output']['matrix']['entries']
enclosure_entries('source contact Gram',gram_matrix,Gram)
ok('full Gram symmetry retained',Gram==transpose(Gram))
negative_bd=sum(v<0 for row in BD for v in row)
negative_gram=sum(v<0 for row in Gram for v in row)
ok('source signed cross operands not discarded',negative_bd>0)
# Every offdiagonal Gram entry is checked even if it is positive in this fiber.
diagonal=[Gram[i][i] for i in range(15)]
compatible=[z for z in range(2,16)]
minimum=min(diagonal[z-1] for z in compatible)
minimizers=[z for z in compatible if diagonal[z-1]==minimum]
ok('native checked feasible minimum',minimum==F(1085537,573049) and minimizers==[2,8])
result={'schema':'SAM_CH2_INSTRUMENT_AND_RECORD_NATIVE_READBACK_V1','status':'PASS',
'independent_checks_passed':len(checks),'checks':checks,'native_outputs_verified':native_outputs,
'native_matrix_entries_verified':native_entries,'entry_breakdown':{'declared_qubit_rhoH':16,'actual_original_B18D':270,'actual_original_contact_Gram':225},
'declared_qubit_fixture':{'source_energy':str(E),'reference_energy':str(w-E),'total_signed_write_rate':str(actual_trace),
'original_continuum_energy_assigned':False,'scope':'Finite controlled reference algebra; actual continuum preparation remains inherited, not replaced'},
'actual_source_energy':{'minimum_displacement_cost':str(minimum),'minimizing_port_labels':minimizers,'BD_negative_entries_retained':negative_bd,'Gram_negative_entries_retained':negative_gram,
'all_signed_cross_entries_checked':True,'physical_kappa_E_assigned':False},
'operand_sources':[{'path':str(p.relative_to(ROOT)),'sha256':sha(p)} for p in [fixture_path,records_path,original_path]],
'native_receipts':receipts,'generator_sha256':sha(Path(__file__)),'native_launches_from_this_verifier':0}
(BASE/'NATIVE_VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'native_outputs':native_outputs,'native_entries':native_entries,'reference_trace':str(actual_trace),'source_minimum':str(minimum)}))
