#!/usr/bin/env python3
"""Build a selected portable evidence tree; no scientific runtime is launched."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import zipfile

HERE=Path(__file__).resolve().parent; BASE=HERE.parent; ROOT=BASE.parents[1]
ORIGINAL_ROOT=Path('/home/lilhelper/SAM_Research_Overflow/SAM_Research_Project')
RUN_REL=Path('GEN4/duck_gen6_local/runs/chapter3-source-field-20261015-03')
OLD_RUNS=['chapter3-source-field-20261015-01','chapter3-source-field-20261015-02']
ZIP_NAME='SAM_Volume_I_Chapters_II_III_Source_to_Field_and_Verification_20261015.zip'
PREFIX='sam_chapters_ii_iii'
MAGIC='SAM_CH2_CH3_SOURCE_FIELD_PORTABLE_STAGE_V1\n'
SKIP_DIRS={'tmp','__pycache__','.pytest_cache','.git','R3_STATE','checkpoints','runtime','ram_scratch','staging'}
SKIP_FILES={'BUNDLE.json','STAGING_RECEIPT.json','PORTABLE_PREFLIGHT.json','FINAL_PORTABLE_VERIFICATION.json'}
DIGEST=re.compile(r'^[0-9a-f]{64}$')

def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1024**2),b''):h.update(b)
    return h.hexdigest()
def read(p):return json.loads(Path(p).read_text())
def relpath(path):
    p=Path(path)
    if p.is_absolute():
        if p.is_relative_to(ROOT):p=p.relative_to(ROOT)
        elif p.is_relative_to(ORIGINAL_ROOT):p=p.relative_to(ORIGINAL_ROOT)
        else:raise ValueError('Dependency outside declared project: '+str(path))
    if not p.parts or p.is_absolute() or '..' in p.parts:raise ValueError('Unsafe dependency path: '+str(path))
    return p
def scoped_files(folder):
    for current,dirs,files in os.walk(folder):
        kept=[]
        for name in dirs:
            p=Path(current)/name
            if name in SKIP_DIRS:continue
            if p.is_symlink():raise ValueError('Scoped directory symlink: '+str(p))
            kept.append(name)
        dirs[:]=kept
        for name in files:
            if name in SKIP_FILES or name.endswith(('.pyc','.pyo','.zip','.partial')):continue
            p=Path(current)/name
            if p.is_symlink():raise ValueError('Scoped file symlink: '+str(p))
            if p.is_file():yield p

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--stage-only',action='store_true')
    ap.add_argument('--source-only',action='store_true',help='Preflight stage only: do not claim or collect completed native custody')
    ap.add_argument('--stage-root',type=Path,default=Path('/tmp/sam-chapters-ii-iii-source-field-stage'))
    ap.add_argument('--destination',type=Path,default=Path('/home/lilhelper/Downloads')/ZIP_NAME)
    ap.add_argument('--history-entry',action='append',default=[])
    ap.add_argument('--extra-file',action='append',default=[])
    args=ap.parse_args()
    if args.source_only and not args.stage_only:raise ValueError('--source-only is a stage-only development preflight')
    stage=args.stage_root.expanduser().resolve(); dest=stage/PREFIX
    if stage==ROOT or stage.is_relative_to(BASE.resolve()) or BASE.resolve().is_relative_to(stage):
        raise ValueError('Stage must be outside the campaign and its ancestor tree')
    marker=stage/'.SAM_CH2_CH3_STAGE'
    if dest.exists():
        if not marker.is_file() or marker.read_text()!=MAGIC:raise ValueError('Refusing to replace an unrecognized stage')
        shutil.rmtree(dest)
    stage.mkdir(parents=True,exist_ok=True);marker.write_text(MAGIC);dest.mkdir()
    dependencies={}; relocations=[]; bound_occurrences=0
    def add(path,digest=None,size=None,role='Selected source or evidence'):
        rel=relpath(path);source=ROOT/rel
        if source.is_symlink() or not source.is_file() or not source.resolve().is_relative_to(ROOT.resolve()):
            raise ValueError('Required regular source outside project scope: '+str(rel))
        before=sha(source);n=source.stat().st_size
        if digest is not None and before!=digest:raise ValueError('Bound source SHA mismatch: '+str(rel))
        if size is not None and n!=size:raise ValueError('Bound source byte mismatch: '+str(rel))
        target=dest/rel
        if target.exists():
            if sha(target)!=before:raise ValueError('Conflicting selected bytes: '+str(rel))
        else:
            target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
        if sha(target)!=before or sha(source)!=before:raise ValueError('Source changed during snapshot: '+str(rel))
        row=dependencies.setdefault(str(rel),{'path':str(rel),'original_path':str(ORIGINAL_ROOT/rel),
              'sha256':before,'bytes':n,'roles':[]})
        if row['sha256']!=before:raise ValueError('Conflicting dependency binding: '+str(rel))
        if role not in row['roles']:row['roles'].append(role)
        return target
    def bindings(value,role):
        nonlocal bound_occurrences
        if isinstance(value,list):
            for v in value:bindings(v,role)
        elif isinstance(value,dict):
            for key in ['source_files','source_files_sha256','files']:
                mapping=value.get(key)
                if isinstance(mapping,dict):
                    for name,digest in mapping.items():
                        if isinstance(digest,str) and DIGEST.fullmatch(digest):
                            add(name,digest,role=role);bound_occurrences+=1
            for v in value.values():
                if isinstance(v,(dict,list)):bindings(v,role)
    # This new campaign is self-contained for its default independent checks.
    # Historical plan snapshots are preserved, but not treated as new bindings.
    campaign=list(scoped_files(BASE))
    for source in campaign:add(source,role='Current Chapter II/III campaign payload')
    # Retain only the bounded PNGs actually cited by visual QA, not the whole
    # temporary equation/render cache. Their original paths and hashes remain.
    for chapter in ['chapter2','chapter3']:
        qa=BASE/chapter/'VISUAL_QA.json'
        if qa.exists():
            q=read(qa)
            for row in q.get('page_reviews',[]):
                if 'render_path' in row and 'render_sha256' in row:
                    add(BASE/row['render_path'],row['render_sha256'],role='Exact PNG cited by original visual review')
            for row in q.get('images',[]):
                add(BASE/chapter/row['path'],row['sha256'],role='Exact PNG cited by original visual review')
    for name in ['PLAN.json','source/SOURCE_BINDINGS.json','source/UNIFORM_COUPLING_RESPONSE.json',
                 'radial/FIXTURE.json','radial/NATIVE_TASKS.json']:
        bindings(read(BASE/name),'Frozen scientific dependency in '+name)
    # Each old attempt is retained as preparation metadata, never as execution.
    for name in OLD_RUNS:
        old=ROOT/RUN_REL.parent/name
        if not old.is_dir():raise FileNotFoundError(old)
        if (old/'LAUNCH.json').exists():raise ValueError('Expected unlaunched predecessor has launch metadata: '+name)
        for source in sorted(old.iterdir()):
            if source.is_file() and source.suffix in {'.json','.jsonl','.md','.log'}:
                add(source,role='Unlaunched predecessor preparation metadata; zero scientific calls')
    topology=ROOT/'GEN4/duck_dual_session_topology1_20261015'
    if topology.is_dir():
        for source in scoped_files(topology):add(source,role='Separate dual-session deployment qualification evidence')
    history=list(args.history_entry)
    install=BASE/'HISTORY_INSTALLATION.json'
    if install.exists():
        d=read(install)
        for name in d.get('history_entries',[]):
            if name not in history:history.append(name)
    for name in history:add(name,role='Immutable source-to-field result installation')
    for name in args.extra_file:add(name,role='Explicitly selected supplementary evidence')
    native_returns=0
    if not args.source_only:
        run=ROOT/RUN_REL
        final=read(run/'COMPLETE.json')
        if final.get('status')!='COMPLETE' or final.get('failed_returns')!=0:
            raise ValueError('Actual scientific Duck cycle must be complete without failed returns')
        for source in sorted(run.iterdir()):
            if source.is_file() and source.suffix in {'.json','.jsonl','.log','.md','.sqlite'}:
                add(source,role='Actual two-by-180-second scientific Duck cycle record')
        for name in ['native_requests','native_returns','ready','control','executed_code']:
            for source in scoped_files(run/name):add(source,role='Actual request, return, readiness or executed-code evidence')
        for source in (run/'workers').glob('*.json'):add(source,role='Actual native worker configuration')
        for name in ['READY.json','CODE_IDENTITY_WORKER.json','RESULT.json','REQUEST.json']:
            for source in (run/'workers').glob('**/'+name):add(source,role='Selected native worker task or identity envelope')
        custody_path=run/'helper_custody/RAM_CUSTODY.json';readback_path=run/'HELPER_READBACK.json'
        custody=read(custody_path);readback=read(readback_path)
        if custody.get('status')!='PASS' or readback.get('status')!='PASS':raise ValueError('Helper custody/readback incomplete')
        cm={r['path']:r for r in custody['files']};hm={r['path']:r for r in readback['files']}
        if len(cm)!=len(custody['files']) or len(hm)!=len(readback['files']):raise ValueError('Duplicate helper manifest path')
        if hm.get('RAM_CUSTODY.json',{}).get('sha256')!=sha(custody_path):raise ValueError('Custody manifest is not authenticated by readback')
        for source in sorted(custody_path.parent.iterdir()):
            if source.is_file():
                r=hm.get(source.name)
                add(source,r['sha256'] if r else None,role='Complete original helper custody/resource manifest')
        add(readback_path,role='Complete original helper readback manifest')
        def receipt(pointer,digest):
            original=Path(pointer);prefix=Path(custody['original_scratch'])
            if original.is_absolute() and original.is_relative_to(prefix):
                suffix=original.relative_to(prefix)
                if '..' in suffix.parts:raise ValueError('Unsafe helper suffix')
                c=cm.get(str(suffix));h=hm.get('retained_ram/'+str(suffix))
                if c is None or h is None or c.get('sha256')!=digest or h.get('sha256')!=digest:
                    raise ValueError('Helper receipt is not in both exact hash manifests')
                if 'bytes' in h and h['bytes']!=c['bytes']:raise ValueError('Helper manifest byte counts differ')
                kept=custody_path.parent/'retained_ram'/suffix
                add(kept,digest,c['bytes'],'Selected helper record authenticated by both manifests')
                row={'original_receipt_path':pointer,'retained_path':str(kept.relative_to(ROOT)),
                     'sha256':digest,'bytes':c['bytes'],'custody_manifest':str(custody_path.relative_to(ROOT)),
                     'custody_manifest_sha256':sha(custody_path),'readback_manifest':str(readback_path.relative_to(ROOT)),
                     'readback_manifest_sha256':sha(readback_path)}
                if row not in relocations:relocations.append(row)
            else:
                rel=relpath(original)
                if not rel.is_relative_to(RUN_REL):raise ValueError('Native receipt outside selected run: '+str(rel))
                add(rel,digest,role='Hash-authenticated selected native receipt')
        for source in sorted((run/'native_returns').glob('*.json')):
            wrapper=read(source);native_returns+=1
            for pk,hk in [('record_file','record_file_sha256'),('receipt','receipt_sha256'),('path','sha256')]:
                ptr=wrapper.get(pk);digest=wrapper.get(hk)
                if isinstance(ptr,str) and isinstance(digest,str) and DIGEST.fullmatch(digest):receipt(ptr,digest)
        # Only actual request source contracts are followed. Embedded native
        # implementation-hash catalogs use package-relative names and are not
        # instructions to copy arbitrary older runtime/object stores.
        for source in sorted((run/'native_requests').glob('*.json')):
            bindings(read(source),'Actual native request scientific dependency')
        packet=read(run/'SOURCE_PACKET.json')
        for row in packet.get('original_sources',[]):add(row['path'],row['sha256'],role='Prepared original scientific input')
        if native_returns!=final['total_returns']:raise ValueError('Native/retrieval wrapper count differs from completed cycle')
    if not args.stage_only:
        for name in ['REPORT.md','REPRODUCIBILITY.md','reproduce.py','NATIVE_VERIFICATION.json','RESOURCE_RELEASE.json',
                     'clock/verify_correlated_phase.py','clock/CORRELATED_PHASE.md','clock/CORRELATED_PHASE_RESULTS.json']:
            if not (BASE/name).is_file():raise FileNotFoundError('Finish delivery record before packaging: '+name)
        if not history:raise ValueError('The final package must identify its installed immutable history entry')
        if read(BASE/'NATIVE_VERIFICATION.json')['status']!='PASS':raise ValueError('Independent native verification must pass')
        if read(BASE/'RESOURCE_RELEASE.json')['status']!='PASS':raise ValueError('Resource release must pass')
        correlated=read(BASE/'clock/CORRELATED_PHASE_RESULTS.json')
        if correlated.get('status')!='PASS' or correlated.get('checks_passed')!=47:
            raise ValueError('Correlated-phase supplement verification must pass')
        if correlated['source_sha256']['RESULTS.json']!=sha(BASE/'clock/RESULTS.json'):
            raise ValueError('Correlated supplement no longer binds the protected native clock result')
        for chapter,name in [('chapter2','SAM_Volume_I_Chapter_II_Source_to_Field_Update_20261015.pdf'),
                             ('chapter3','SAM_Volume_I_Chapter_III_Source_to_Field_Development_20261015.pdf')]:
            pdf=BASE/'output/pdf'/name
            verification=read(BASE/chapter/'PDF_VERIFICATION.json')
            qa=read(BASE/chapter/'VISUAL_QA.json')
            if verification.get('status')!='PASS' or verification['pdf']['sha256']!=sha(pdf):
                raise ValueError('Final PDF structural verification differs: '+chapter)
            if qa.get('status') not in {'PASS','COMPLETE'} or qa.get('pdf_sha256',qa.get('pdf',{}).get('sha256'))!=sha(pdf):
                raise ValueError('Final visual QA differs: '+chapter)
    dep_rows=[dependencies[k] for k in sorted(dependencies)]
    (dest/'SOURCE_DEPENDENCIES.json').write_text(json.dumps(dep_rows,indent=2,sort_keys=True)+'\n')
    (dest/'RECEIPT_CUSTODY_RELOCATIONS.json').write_text(json.dumps(relocations,indent=2,sort_keys=True)+'\n')
    (dest/'README.txt').write_text('SAM Volume I Chapters II and III: source-to-field development and verification\n\n'
        'Read GEN4/voli_chapter3_source_field1_20261015/REPORT.md and REPRODUCIBILITY.md.\n'
        'Fresh-extraction offline replay:\n'
        'python3 -B GEN4/voli_chapter3_source_field1_20261015/reproduce.py\n\n'
        'The complete original helper manifests accompany only selected, authenticated used records.\n'
        'This is a portable selected evidence subset; the full runtime remains in the original project.\n'
        'No native operation, service, installation, network request, commit or sync is launched by replay.\n')
    info={'schema':'SAM_CH2_CH3_SELECTED_EVIDENCE_BUNDLE_V1','builder_sha256':sha(Path(__file__)),
          'campaign':str(BASE.relative_to(ROOT)),'actual_science_run':str(RUN_REL),
          'source_only_preflight':args.source_only,'actual_return_wrappers':native_returns,
          'helper_record_relocations':len(relocations),'source_dependencies':len(dep_rows),
          'evidence_scope':'Portable selected evidence subset; complete original manifests, used records only; full runtime retained at original project.',
          'native_reexecutions':0,'history_entries':history}
    (dest/'BUNDLE_INFO.json').write_text(json.dumps(info,indent=2,sort_keys=True)+'\n')
    files=sorted(p for p in dest.rglob('*') if p.is_file() and p!=dest/'MANIFEST.sha256')
    (dest/'MANIFEST.sha256').write_text(''.join(sha(p)+'  '+str(p.relative_to(dest))+'\n' for p in files))
    for line in (dest/'MANIFEST.sha256').read_text().splitlines():
        digest,name=line.split('  ',1)
        if sha(dest/name)!=digest:raise ValueError('Staged member SHA mismatch: '+name)
    result={**info,'status':'SOURCE_ONLY_STAGED' if args.source_only else 'STAGED' if args.stage_only else 'PACKAGED',
            'stage':str(dest),'files':len(files)+1,'manifest_sha256':sha(dest/'MANIFEST.sha256'),
            'bound_source_occurrences':bound_occurrences,'scientific_records_modified':False}
    if args.stage_only:
        (HERE/'STAGING_RECEIPT.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    else:
        output=args.destination.expanduser().resolve()
        if output.is_relative_to(BASE.resolve()):raise ValueError('ZIP destination must be outside source campaign')
        output.parent.mkdir(parents=True,exist_ok=True);temp=output.with_name(output.name+'.partial')
        with zipfile.ZipFile(temp,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as archive:
            for source in sorted(dest.rglob('*')):
                if source.is_file():
                    item=zipfile.ZipInfo(str(source.relative_to(stage)),date_time=(2026,10,15,0,0,0))
                    item.compress_type=zipfile.ZIP_DEFLATED;item.external_attr=(stat.S_IFREG|0o644)<<16
                    archive.writestr(item,source.read_bytes(),compresslevel=6)
        # Authenticate the actual archive bytes, including its root manifest,
        # rather than relying on the staged-tree check alone.
        archive_files=[p for p in dest.rglob('*') if p.is_file()]
        expected_names={str(p.relative_to(stage)):p for p in archive_files}
        with zipfile.ZipFile(temp) as archive:
            names=[item.filename for item in archive.infolist() if not item.is_dir()]
            if len(names)!=len(set(names)) or set(names)!=set(expected_names):
                raise ValueError('ZIP and staged manifest member sets differ')
            for name,source in expected_names.items():
                if hashlib.sha256(archive.read(name)).hexdigest()!=sha(source):
                    raise ValueError('ZIP byte readback differs: '+name)
        temp.replace(output)
        result.update(zip_path=str(output),zip_sha256=sha(output),zip_bytes=output.stat().st_size,
                      zip_complete_member_readback='PASS')
        (HERE/'BUNDLE.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True))

if __name__=='__main__':main()
