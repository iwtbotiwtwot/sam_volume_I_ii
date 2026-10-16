"""Authenticate the completed Duck cycle and its separate scientific readback."""
from pathlib import Path
import hashlib,json
BASE=Path(__file__).resolve().parent;ROOT=BASE.parents[1]
RUN=ROOT/'GEN4/duck_gen6_local/runs/chapter2-physical-protocols-20261015-01'
def read(p):return json.loads(Path(p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
checks=[]
def ok(label,v):
 assert v,label
 checks.append(label)
def main():
 final=read(RUN/'COMPLETE.json');runtime=read(RUN/'RUNTIME_RESULT.json');cfg=read(RUN/'CONFIG.json');oldroot=Path(cfg['prepared_run']).parents[3]
 ok('completed actual cycle',final['status']=='COMPLETE' and final['failed_returns']==0)
 ok('user three-minute windows',cfg['round_seconds']==180 and len(runtime['round_starts'])==2)
 for x in runtime['round_starts']:
  ok('exact monotonic round '+str(x['round']),x['seconds']==180 and x['deadline_monotonic_ns']-x['start_monotonic_ns']==180000000000)
 admissions=[json.loads(x) for x in (RUN/'ADMISSIONS.jsonl').read_text().splitlines()]
 for x in admissions:ok('admitted on time '+x['key'],x['admitted_monotonic_ns']<=x['deadline_monotonic_ns'])
 rev=read(RUN/'REVIEW_SELECTION.json');r1=read(RUN/'REVIEW_R1.json')
 ok('complete shared review',rev['review_packet_sha256']==sha(RUN/'REVIEW_R1.json') and {x['id'] for x in rev['accounting']}=={x['id'] for x in r1['outcomes']})
 ok('parent retained',rev['parent_retained'])
 org=read(BASE/'ORGANIZATION.json');ok('all selected targets retained',{x['id'] for x in final['selected_targets']}=={x['id'] for x in org['coverage']})
 custody=read(RUN/'helper_custody/RAM_CUSTODY.json');helper=read(RUN/'HELPER_READBACK.json')
 cm={x['path']:x for x in custody['files']};hm={x['path']:x for x in helper['files']}
 ok('helper custody verified',custody['status']=='PASS' and helper['status']=='PASS' and sha(RUN/'helper_custody/RAM_CUSTODY.json')==hm['RAM_CUSTODY.json']['sha256'])
 records=[];native=web=0
 for p in sorted((RUN/'native_returns').glob('*.json')):
  x=read(p);key=x['key'];ok('completed '+key,x['status']=='COMPLETED')
  ptr=x.get('record_file',x.get('receipt'));expected=x.get('record_file_sha256',x.get('receipt_sha256'));ok('original receipt '+key,bool(ptr and expected))
  if x['task_kind']=='research_web':
   web+=1;rel=Path(ptr).relative_to(Path(custody['original_scratch'])).as_posix();kept='retained_ram/'+rel
   ok('safe manifest custody '+key,'..' not in Path(rel).parts and rel in cm and kept in hm)
   ok('original digest custody '+key,cm[rel]['sha256']==hm[kept]['sha256']==expected)
   record=RUN/'helper_custody'/kept;ok('original length '+key,record.stat().st_size==cm[rel]['bytes'])
   ok('immutable source index '+key,x['returned']['index_sha256']==sha(BASE/'inputs/RESEARCH_WEB.sqlite'))
  else:
   native+=1;rel=Path(ptr).relative_to(oldroot);ok('safe native path '+key,'..' not in rel.parts);record=ROOT/rel
  ok('original receipt bytes '+key,sha(record)==expected)
  d=read(record);ok('receipt identity '+key,d['key']==key and d['status']=='COMPLETED')
  if x['task_kind']!='research_web':
   req=read(RUN/'native_requests'/(key+'.json'))['task'];ok('same payload '+key,d['native_payload']==req['payload'])
   ok('native arithmetic boundary '+key,d['host_domain_arithmetic'] is False)
   for path,digest in d['source_binding'].get('source_files',{}).items():
    source=Path(path);source=ROOT/source.relative_to(oldroot) if source.is_absolute() else ROOT/source
    ok('source bytes '+key+' '+source.name,sha(source)==digest)
  records.append(dict(key=key,path=str(record.relative_to(ROOT)),sha256=expected))
 ok('complete native and research accounting',(native,web)==(final['native_returns'],final['research_returns']) and len(admissions)==native+web)
 release=read(RUN/'RESOURCE_RELEASE.json');ok('owned CPU and RAM release',release['status']=='PASS' and release['own_local_cpu_leases_free'] and release['helper_RAM_released'] and release['local_service']==dict(ActiveState='inactive',MainPID='0'))
 report=dict(status='PASS',checks=len(checks),native_returns=native,research_returns=web,round_seconds=[180,180],selected_targets=len(final['selected_targets']),native_executions=0,record_sources=records)
 (BASE/'CYCLE_VERIFICATION.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='record_sources'}))
if __name__=='__main__':main()
