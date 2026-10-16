"""Independent retained-cycle/custody checks; never start a worker."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,sys
BASE=Path(__file__).resolve().parent;ROOT=BASE.parents[1]
RUN=ROOT/'GEN4/duck_gen6_local/runs/chapter2-signature-memory-20261015-01'
sys.path.insert(0,str(BASE/'memory'))
from exact_memory import I
def read(p):return json.loads(Path(p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
checks=0
def require(x,label):
    global checks
    if not x:raise AssertionError(label)
    checks+=1

def main():
    final=read(RUN/'COMPLETE.json');runtime=read(RUN/'RUNTIME_RESULT.json');cfg=read(RUN/'CONFIG.json')
    original_root=Path(cfg['prepared_run']).parents[3]
    require(final['status']=='COMPLETE','actual complete cycle')
    require(final['native_returns']==14 and final['research_returns']==5 and final['failed_returns']==0,'actual outcomes')
    require(cfg['round_seconds']==180,'user three-minute windows')
    require(len(runtime['round_starts'])==2,'exactly two windows')
    starts={str(x['round']):x for x in runtime['round_starts']}
    for x in starts.values():
        require(x['seconds']==180,'recorded window seconds')
        require(x['deadline_monotonic_ns']-x['start_monotonic_ns']==180000000000,'exact monotonic duration')
    admitted=[json.loads(s) for s in (RUN/'ADMISSIONS.jsonl').read_text().splitlines()]
    require(len(admitted)==19,'all actual admissions retained')
    for x in admitted:
        require(x['admitted_monotonic_ns']<=x['deadline_monotonic_ns'],'no late admission')
    review=read(RUN/'REVIEW_SELECTION.json')
    r1=read(RUN/'REVIEW_R1.json')
    require(review['review_packet_sha256']==sha(RUN/'REVIEW_R1.json'),'complete R1 packet binding')
    require({x['id']for x in review['accounting']}=={x['id']for x in r1['outcomes']},'all R1 outcomes reviewed')
    require(len(review['accounting'])==7 and review['parent_retained'],'parent and seven outcomes')
    require({x['id']for x in final['selected_targets']}=={x['id']for x in read(BASE/'ORGANIZATION.json')['coverage']},'all selected targets retained')
    custody=read(RUN/'helper_custody/RAM_CUSTODY.json')
    helper=read(RUN/'HELPER_READBACK.json')
    cm={x['path']:x for x in custody['files']};hm={x['path']:x for x in helper['files']}
    require(custody['status']=='PASS' and helper['status']=='PASS','actual helper custody')
    require(sha(RUN/'helper_custody/RAM_CUSTODY.json')==hm['RAM_CUSTODY.json']['sha256'],'custody receipt readback')
    records=[];web=0;native=0
    for p in sorted((RUN/'native_returns').glob('*.json')):
        x=read(p);require(x['status']=='COMPLETED','completed '+x['key'])
        pointer=x.get('record_file',x.get('receipt'));expected=x.get('record_file_sha256',x.get('receipt_sha256'))
        require(pointer is not None and expected is not None,'original result receipt pointer')
        if x['task_kind']=='research_web':
            web+=1
            rel=Path(pointer).relative_to(Path(custody['original_scratch'])).as_posix()
            require('..'not in Path(rel).parts,'safe custody path')
            require(rel in cm and cm[rel]['sha256']==expected,'manifest-listed original RAM record')
            kept='retained_ram/'+rel
            require(kept in hm and hm[kept]['sha256']==expected,'helper complete readback binding')
            record=RUN/'helper_custody'/kept
            require(record.stat().st_size==cm[rel]['bytes'],'retained record original length')
            require(x['returned']['index_sha256']==sha(BASE/'inputs/RESEARCH_WEB.sqlite'),'immutable local source index')
        else:
            native+=1
            rel=Path(pointer).relative_to(original_root)
            require('..'not in rel.parts,'safe native project-relative record')
            record=ROOT/rel
        require(sha(record)==expected,'byte-identical actual result '+x['key'])
        d=read(record);require(d['key']==x['key'] and d['status']=='COMPLETED','original result identity')
        records.append(dict(key=x['key'],path=str(record.relative_to(ROOT)),sha256=expected))
    require((native,web)==(14,5),'native/retrieval distinction')
    # The only primitive outside the three specialist readback scripts:
    # original R015_BASE single-profile R1 solve, preserved after metadata clarification.
    r1m=read(RUN/'native_returns/r1_memory_Usolve.json')
    if 'returned'not in r1m:
        rr=Path(r1m['record_file']).relative_to(original_root);r1m=read(ROOT/rr)
    p=read(BASE/'memory/SOURCE_OPERANDS.json')['profiles'][0]
    require(p['profile_id']=='R015_BASE','literal R1 profile identification')
    data=r1m['native_payload']['data'];u=[[I.make(v)for v in row]for row in p['U']];w=[I.make(p['W'][i][0])for i in range(2)]
    require(data['matrix']['entries']==p['U'],'literal original single-profile U')
    require(data['rhs']['entries']==[[p['W'][i][0]]for i in range(2)],'literal original source W')
    det=u[0][0]*u[1][1]-u[0][1]*u[1][0]
    expected=[(u[1][1]*w[0]-u[0][1]*w[1])/det,(u[0][0]*w[1]-u[1][0]*w[0])/det]
    got=r1m['returned']['result']['output']['matrix']['entries']
    for i in range(2):
        v=I.make(got[i][0]);require(max(v.lo,expected[i].lo)<=min(v.hi,expected[i].hi),'single-profile independent solve enclosure')
    release=read(RUN/'RESOURCE_RELEASE.json')
    require(release['status']=='PASS' and release['own_local_cpu_leases_free'],'CPU release')
    require(release['helper_RAM_released'] and release['local_service']==dict(ActiveState='inactive',MainPID='0'),'owned runtime shutdown')
    report=dict(status='PASS',checks=checks,native_returns=native,research_returns=web,
        round_seconds=[180,180],selected_targets=len(final['selected_targets']),native_executions=0,
        record_sources=records,helper_relocation='Only manifest-listed original scratch suffix with original SHA, byte count and complete helper-readback binding',
        r1_memory_metadata='Original payload is R015_BASE; preserved null descriptive label clarified separately')
    (BASE/'CYCLE_VERIFICATION.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in report.items()if k not in ['record_sources','helper_relocation','r1_memory_metadata']}))
if __name__=='__main__':main()
