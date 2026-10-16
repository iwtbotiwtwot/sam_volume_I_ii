#!/usr/bin/env python3
"""Install completed Chapter II/III results after all delivery gates exist.

Prepared for a final parent-owned invocation. This file starts no science,
changes no runtime/core/package, and does not archive, commit, publish or sync.
It creates numbered history first and checks every authority preimage before
writing. An interrupted transaction is retained for inspection, not repeated.
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess

BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parents[1]
REL=BASE.relative_to(ROOT).as_posix()
RUNREL='GEN4/duck_gen6_local/runs/chapter3-source-field-20261015-03'
RUN=ROOT/RUNREL
SCOPE='latest_chapter3_source_field_cycle'
DATE='2026-10-15'
LIVE=['SAM_LIVE/00_CURRENT.md','SAM_LIVE/15_VOLI_EXPANSION_CURRENT.md',
      'SAM_LIVE/13_GEN4_RESEARCH_WEB_CURRENT.md']
MISC=['GEN4/DUCK_CURRENT.json','SAM_PROJECT/CONTINUITY.json','SAM_HISTORY/HISTORY_INDEX.md']
SPIN='SAM_LIVE/03_STARBREAKER_GW_CURRENT.md'
COUNTERS=[('source/CHECKS.json','independent_exact_checks'),
          ('radial/VERIFICATION.json','checks'),('clock/RESULTS.json','checks_passed'),
          ('energy/FIELD_SOURCE_RESULTS.json','checks'),('core/RESULTS.json','checks_passed'),
          ('source/UNIFORM_COUPLING_RESPONSE.json','independent_exact_checks'),
          ('clock/CORRELATED_PHASE_RESULTS.json','checks_passed')]


def require(value,message):
    if not value:raise ValueError(message)


def read(path):return json.loads(Path(path).read_text())
def digest(data):return hashlib.sha256(data).hexdigest()
def sha(path):return digest(Path(path).read_bytes())
def encoded(value):return (json.dumps(value,indent=2,sort_keys=True)+'\n').encode()
def front(text,entry):return re.sub(r'^history_entry: H\d{6}$','history_entry: '+entry,text,count=1,flags=re.M)


def preflight():
    """Read completed authorities; do not infer completion from a running phase."""
    bound={}
    def data(path,status='PASS'):
        path=Path(path);raw=path.read_bytes();value=json.loads(raw)
        if status is not None:require(value.get('status')==status,str(path)+' must have status '+status)
        bound[str(path.relative_to(ROOT))]=digest(raw)
        return value
    complete=data(RUN/'COMPLETE.json','COMPLETE')
    result=data(RUN/'RUNTIME_RESULT.json','SCIENCE_COMPLETE_AWAITING_OPERATOR_ORGANIZATION')
    config=data(RUN/'CONFIG.json',None)
    release=data(RUN/'RESOURCE_RELEASE.json')
    data(RUN/'HELPER_READBACK.json')
    require(complete.get('failed_returns')==0,'Resolve every failed native return before installation')
    require(complete.get('resource_release')=='PASS' and complete.get('complete_helper_readback')=='PASS',
            'Actual complete helper/resource custody required')
    require(release.get('global_host_lock_acquired') is False,'Own-core release authority required')
    require(complete.get('actual_native_controllers')==6 and complete.get('actual_native_helpers')==3,
            'This successor must use the qualified6+3 topology')
    require(complete.get('actual_directed_controller_greeting_ACKs')==30 and result.get('actual_ready')==9,
            'Nine actual identities and30 directed ACKs required')
    require(config.get('round_seconds')==180 and len(result.get('round_starts',[]))==2,
            'Two actual180-second windows required')
    require(all(r.get('seconds')==180 and r['deadline_monotonic_ns']-r['start_monotonic_ns']==180_000_000_000
                for r in result['round_starts']),'Original admission clocks must be retained')
    native=data(BASE/'NATIVE_VERIFICATION.json')
    require(native.get('run')==RUNREL,'Native verification belongs to another run')
    require(native.get('native_outputs_verified')==complete['native_returns'] and
            native.get('research_receipts_authenticated')==complete['research_returns'],
            'Independent native/source count must match actual COMPLETE')
    reproduction=data(BASE/'REPRODUCTION.json')
    require(reproduction.get('native_executions',0)==0 and reproduction.get('network_requests',0)==0,
            'Offline replay must not launch scientific work')
    organization=data(RUN/'ORGANIZATION.json',None)
    selected={x['id'] for x in complete['selected_targets']}
    require(organization.get('parent_retained') is True and
            {x['id'] for x in organization['coverage']}==selected,
            'Retain the parent and every selected scientific target')
    pdfs={}
    for folder,pages,sections in [('chapter3',14,28),('chapter2',24,48)]:
        receipt=data(BASE/folder/'PDF_VERIFICATION.json')
        pdf=BASE/receipt['pdf']['path']
        require(pdf.resolve().is_relative_to((BASE/'output/pdf').resolve()),'PDF path escapes current output')
        require(sha(pdf)==receipt['pdf']['sha256'],'Current PDF differs from verified receipt')
        require(receipt.get('pages',receipt['pdf'].get('pages'))==pages and receipt.get('sections')==sections,
                folder+' reader page/section accounting differs')
        qa=data(BASE/folder/'VISUAL_QA.json',None)
        require(qa.get('status') in ['PASS','COMPLETE'],'Completed visual review required for '+folder)
        qa_sha=qa.get('pdf_sha256',qa.get('pdf',{}).get('sha256',qa.get('full_review_pdf_sha256')))
        require(qa_sha==sha(pdf),'Visual review must bind the current '+folder+' PDF')
        if folder=='chapter2':
            require(receipt.get('predecessor_sections_preserved')==40,'Original40 Chapter II sections must survive')
        bound[str(pdf.relative_to(ROOT))]=sha(pdf)
        pdfs[folder]={'path':str(pdf.relative_to(ROOT)),'sha256':sha(pdf),'pages':pages,
                      'sections':sections,'checks':receipt['checks_passed']}
    math={}
    for path,key in COUNTERS:
        value=data(BASE/path)
        require(type(value.get(key)) is int and value[key]>0,'Positive independent count required: '+path)
        math[path]=value[key]
    closing=data(BASE/'CLOSING_SPIN_REVIEW.json')
    require(closing.get('no_new_science_after_this_review') is True,
            'Parent-owned final bounded spin review must close scientific work')
    for source in closing.get('sources',[]):
        require(sha(ROOT/source['path'])==source['sha256'],'Closing review source changed: '+source['path'])
    require(bool(closing.get('disclosure')),'Closing spin transfer must be disclosed')
    for filename in ['REPORT.md','README.md','FOLLOW_UP.md']:
        path=BASE/filename;raw=path.read_bytes()
        require(bool(raw.strip()),filename+' must exist before current authority installation')
        bound[str(path.relative_to(ROOT))]=digest(raw)
    return complete,native,pdfs,math,closing,bound


def main():
    require(not (BASE/'HISTORY_INSTALLATION.json').exists(),'Already installed; inspect HISTORY_INSTALLATION.json')
    require(not (BASE/'ops/AUTHORITY_PLAN.json').exists(),
            'A retained authority transaction already exists; inspect it before a retry')
    complete,native,pdfs,math,closing,bound=preflight()
    before={name:(ROOT/name).read_bytes() for name in LIVE+MISC}
    spin_before=sha(ROOT/SPIN)
    entries=ROOT/'SAM_HISTORY/entries'
    numbers=[int(p.name[1:7]) for p in entries.glob('H*.md') if re.match(r'H\d{6}_',p.name)]
    entry='H'+str(max(numbers)+1).zfill(6)
    filename=entry+'_'+DATE+'_CHAPTER_III_SOURCE_FIELD_AND_CHAPTER_II_BRIDGE.md'
    history=entries/filename
    oldcursor=json.loads(before['GEN4/DUCK_CURRENT.json'])
    oldroutes=json.loads(before['SAM_PROJECT/CONTINUITY.json'])
    require(SCOPE not in oldcursor,'Preserve the existing Chapter III result; prepare a scoped successor')
    changed={}
    for name in LIVE:
        text=front(before[name].decode(),entry)
        if name.endswith('00_CURRENT.md'):
            text,count=re.subn(r'(\[I\]\(15_VOLI_EXPANSION_CURRENT\.md\))\(H\d{6}\)',r'\1('+entry+')',text,count=1)
            require(count==1,'Current Volume I hub pointer changed; inspect its preimage')
        elif name.endswith('15_VOLI_EXPANSION_CURRENT.md'):
            old=[line for line in text.splitlines() if line.startswith('[ChII]')]
            require(len(old)==1,'Exactly one existing Chapter II pointer required')
            text=text.replace(old[0],'[ChII/III](../'+REL+'/REPORT.md)('+entry+'):24/14pp.',1)
        else:
            block=('## Chapter II/III source-to-field — '+entry+'\n\n'
                '[Source/field](../'+REL+'/REPORT.md)('+entry+'):III14pp/28sections;companionII24pp/48,old40preserved.\n'
                'ActualSi29energy-effects flatH0/8;uniformpositive-energycoupling leaves sectorBhistory unchanged;fullgeneratorscaling differs.\n'
                'Finitecubeballs/multipoles/binding,radialshellGreen/flux/error,completequadrupolefield-energytail and staticpayments explicit.\n'
                'Actualsix-laneclock response/common-energy distinctions and conditionalprecision retained;physicalV/stress/3Disotropy/gamma unassigned.\n'
                f'6+3 Connections2x180 COMPLETE;{complete["native_returns"]}native/{complete["research_returns"]}web/0fail;allselected+parent;helper/releasePASS.\n'
                f'Offline{sum(math.values())}checks;native{native["independent_checks"]}checks/{native["matrix_entries_checked"]}entries;'
                f'PDF{pdfs["chapter3"]["checks"]}+{pdfs["chapter2"]["checks"]}checks;[next](../{REL}/FOLLOW_UP.md). H002636minimalspinclosure/H002640runtime preserved.\n\n')
            marker='# Combined GEN4 research web\n\n'
            require(marker in text,'Web current heading changed')
            text=text.replace(marker,marker+block,1)
        cap=16384 if name.endswith('00_CURRENT.md') else 32768
        require(len(text.encode())<=cap,f'{name} exceeds its live cap: {len(text.encode())}>{cap}')
        changed[name]=text.encode()
    cursor=dict(oldcursor)
    cursor['history_entry']=entry
    cursor[SCOPE]=dict(campaign=REL,history=entry,status='COMPLETE',run=RUNREL,
        completion=RUNREL+'/COMPLETE.json',target=REL+'/TARGET.md',policy=REL+'/RUN_POLICY.json',
        guide=REL+'/README.md',report=REL+'/REPORT.md',follow_up=REL+'/FOLLOW_UP.md',
        round_seconds=[180,180],round_two_selector='CODEX_CURRENT_SESSION',research_mode='connections',
        native_returns=complete['native_returns'],research_returns=complete['research_returns'],failed_returns=0,
        actual_controllers=complete['actual_native_controllers'],actual_helpers=complete['actual_native_helpers'],
        resource_release='PASS',helper_readback='PASS',parent_retained=True,
        selected_targets=[x['id'] for x in complete['selected_targets']],
        automatic_repeat=False,automatic_third_round=False,storage='T500_ONLY',archive_status='NOT_REQUESTED_NO_COMMIT',
        next='Read completed source-field derivations and explicit physical interfaces; new work needs a separate authorized successor.')
    require(all(cursor[k]==v for k,v in oldcursor.items() if k!='history_entry'),
            'An unrelated Duck scope or qualified runtime default would change')
    changed['GEN4/DUCK_CURRENT.json']=encoded(cursor)
    routes=dict(oldroutes);routes['history_entry']=entry
    routes['chapter_iii_source_field']=dict(history_entry=entry,status='COMPLETE_SOURCE_FIELD_DEVELOPMENT_PASS',
        report=REL+'/REPORT.md',pdf=pdfs['chapter3']['path'],reproduce=REL+'/reproduce.py',next=REL+'/FOLLOW_UP.md',run=RUNREL,
        remaining_interfaces=['physical density and complete stress','external coupling V','physical units',
                              'source-derived three-dimensional isotropy','causal dynamics and metric gamma'])
    routes['chapter_ii_source_field_update']=dict(history_entry=entry,status='COMPLETE_COMPANION_UPDATE',
        report=REL+'/REPORT.md',pdf=pdfs['chapter2']['path'],reproduce=REL+'/reproduce.py',
        prior='H002636',prior_sections_preserved=40,smallest_actual_spin_closure='OPEN_UNCHANGED')
    require(all(routes[k]==v for k,v in oldroutes.items() if k!='history_entry'),
            'Existing scientific default, runtime defaults or Chapter II physical result would change')
    changed['SAM_PROJECT/CONTINUITY.json']=encoded(routes)
    index=before['SAM_HISTORY/HISTORY_INDEX.md'].decode()
    require(entry not in index,'History number already indexed')
    index+=('\n| [`'+entry+'`](entries/'+filename+') | '+DATE+' | `RESULT` | ChapterIII14pp/source-field and II24pp/48sections;'
            f'{complete["native_returns"]}native/{complete["research_returns"]}web/{sum(math.values())}offlinechecks | '
            'Physicalsource/V/stress/isotropy/gamma open;H002636closure/H002639scope/H002640runtime preserved;custody/releasePASS |\n')
    changed['SAM_HISTORY/HISTORY_INDEX.md']=index.encode()
    snapshots=BASE/'ops/authority_preimages'
    require(not snapshots.exists(),'Prior authority preimage snapshot already exists')
    # Validate all preimages and bound science before creating immutable history.
    for name,raw in before.items():require((ROOT/name).read_bytes()==raw,'Concurrent authority change: '+name)
    for name,value in bound.items():require(sha(ROOT/name)==value,'Bound final result changed: '+name)
    require(sha(ROOT/SPIN)==spin_before,'Spin authority changed during preparation')
    plan={'history':entry,'history_path':str(history.relative_to(ROOT)),'status':'PREPARED_FOR_SINGLE_INSTALL',
          'bound_results':bound,'authority_preimages':{k:digest(v) for k,v in before.items()},
          'changed_files':list(changed),'spin_live_preserved_sha256':spin_before}
    with (BASE/'ops/AUTHORITY_PLAN.json').open('x') as out:json.dump(plan,out,indent=2);out.write('\n')
    for name,raw in before.items():
        dest=snapshots/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
    selected=', '.join(x['id'] for x in complete['selected_targets'])
    classification=next((x for x in ['The test falsifies the concept.','The test result suggests the concept is possible.',
                         'The test result suggests strong contact with the concept.'] if x in (BASE/'REPORT.md').read_text()),'')
    note=f'''---
entry_id: {entry}
entry_date: {DATE}
entry_type: RESULT
status: IMMUTABLE_HISTORY
supersedes: NONE
affects_live:
  - SAM_LIVE/00_CURRENT.md
  - SAM_LIVE/15_VOLI_EXPANSION_CURRENT.md
  - SAM_LIVE/13_GEN4_RESEARCH_WEB_CURRENT.md
---

# Chapter III source-to-field receiving and Chapter II companion update

The user authorized the source-field derivations and a companion Chapter II
update. Sean Brady is originator/conceptual director; OpenAI ChatGPT and Codex
are research collaborators. New constructions and checks are Codex work.

Source authority: {REL}/REPORT.md, README.md and FOLLOW_UP.md. Completed Duck:
{RUNREL}. Integration1.2.3/core0.10.2 and own-core6+3 topology from H002640
are retained; actual readiness9/ACK30, two180-second windows,
{complete['native_returns']}native/{complete['research_returns']}source-retrieval returns,0failures.
All selected targets ({selected}) and parent are retained. Native readback:
{native['independent_checks']}checks/{native['matrix_entries_checked']}entries. Mathematical offline
checks:{sum(math.values())}; artifact checks:{pdfs['chapter3']['checks']}III/{pdfs['chapter2']['checks']}II.

The actual retained Si29 channel-summed local energy effects are H0/8 per
site. A declared cube-ball spatial incidence gives explicit conditional
density, exterior multipoles and finite self/pair binding. The closed cube
graph obstruction and a separate radial-shell receiver distinguish spatial
incidence from the chosen Poisson receiving law. The radial Green inverse,
exact flux, infinity-reference correction and continuum error are supplied.

The original quadrupole free-field energy retains its exterior tail; it is
not compactly supported at the source boundary. Its conditional scalar field
and binding account are calculated. Source, signed interaction and both
counterterm payments remain distinct; a positive free-field sector alone
is not the complete gravitational source. The commuting classical static
sector cancels field+interaction+counterterm without replacing quantum D/C.

The actual Chapter I sixteen-state source retains energy unread by its
current phase clock. Complete-H scaling and epsilon-only scaling differ;
the counterterm commutes with the full H/current while the free-field
part can change the interacting clock. Six-lane response diagnostics and
conditional phase precision retain their own source and calibration. The
postcycle47-check analytic supplement keeps the shared original trajectory
and gives a strictly negative phase change for every positive lift under
declared full-H scaling. Independent-band nonoverlap remains a separate
comparison; all frozen native operands and apparatus budgets are preserved.
Separately, the actual Si29 incoming/outgoing contrast B is unchanged by
the proposed uniform positive-energy coupling, while full signed-generator
scaling dilates its nonconstant history. This is the retained population
signal, not a substituted two-state source or the Chapter I phase theorem.

ChapterIII is14pages/28sections. CompanionII is24pages/48sections and
preserves its original40sections. Full physical local density/stress,
external perturbation V, SI assignments, source-derived3D isotropy, causal
dynamics and spatial metric gamma remain unassigned. No physical apparatus
or empirical redshift is reported. H002636 actual spin closure remains
open and unchanged; no spin-live statement is edited. Closing transfer:
{closing['disclosure']}

H002639 remains the default scientific Duck scope; H002640 runtime defaults,
concurrent qualification and all unrelated routes remain intact. Only the new
scoped Chapter III result and companion pointers are installed. No new Duck,
runtime installation, I9 access, archive, commit, sync or publication occurs.

{classification}

## Bound results and preserved authority

```json
{json.dumps({'results':bound,'preimages':plan['authority_preimages']},indent=2)}
```

Prior authority bytes are retained under {REL}/ops/authority_preimages/.
'''
    with history.open('x') as out:out.write(note)
    installed=[]
    for name,raw in changed.items():
        require((ROOT/name).read_bytes()==before[name],'Concurrent authority change: '+name)
        (ROOT/name).write_bytes(raw);installed.append(name)
    require(sha(ROOT/SPIN)==spin_before,'Scientific spin live must remain unchanged')
    validation=subprocess.run([str(ROOT/'SAM_HISTORY/validate_live_history.sh')],cwd=ROOT,capture_output=True,text=True)
    log=BASE/'ops/HISTORY_VALIDATION.log';log.write_text(validation.stdout+validation.stderr)
    receipt={'status':'INSTALLED' if validation.returncode==0 else 'INSTALLED_VALIDATION_FAILED',
        'history':entry,'history_entries':[str(history.relative_to(ROOT))],'history_sha256':sha(history),
        'bound_results':bound,'live_files':[{'path':k,'bytes':len(v),'before_sha256':digest(before[k]),'after_sha256':sha(ROOT/k)} for k,v in changed.items()],
        'preserved_default_scientific_scope':oldroutes.get('duck_default_scope'),
        'runtime_defaults_preserved':cursor.get('runtime_defaults')==oldcursor.get('runtime_defaults'),
        'spin_live_unchanged':sha(ROOT/SPIN)==spin_before,'unrelated_scopes_preserved':True,
        'history_validation_returncode':validation.returncode,'history_validation_log':str(log.relative_to(ROOT)),
        'native_or_scientific_execution':False,'runtime_or_package_changed':False}
    with (BASE/'HISTORY_INSTALLATION.json').open('x') as out:json.dump(receipt,out,indent=2);out.write('\n')
    require(validation.returncode==0,'History validation failed; installation receipt and original preimages retained')
    print(json.dumps({'status':'INSTALLED','history':entry,'path':str(history.relative_to(ROOT))}))


if __name__=='__main__':main()
