#!/usr/bin/env python3
"""Package this scoped research and exact dependencies for offline replay.

Only the current campaign tree is copied recursively. External files are
selected from declared source packets or the exact retained Duck run; neither
the repository, Duck installation nor a worker checkpoint is recursively copied.
This is a requested research-deliverable ZIP, not commit-time archival.
"""
from __future__ import annotations
import argparse,hashlib,json,shutil,zipfile
from pathlib import Path

HERE=Path(__file__).resolve().parent
BASE=HERE.parent
ROOT=BASE.parents[1]
ORIGINAL_ROOT=Path('/home/lilhelper/SAM_Research_Overflow/SAM_Research_Project')
RUN_REL=Path('GEN4/duck_gen6_local/runs/chapter2-signature-memory-20261015-01')
PDF_NAME='SAM_Volume_I_Chapter_II_Expanded_Development_Draft_20261015.pdf'
ZIP_NAME='SAM_Volume_I_Chapter_II_Continuation_and_Verification_20261015.zip'
STAGE_MAGIC='SAM_CHAPTER2_CONTINUATION_PORTABLE_STAGE_V1\n'


def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024),b''):h.update(block)
    return h.hexdigest()


def read(path):return json.loads(path.read_text())


def relative(path):
    path=Path(path)
    if path.is_absolute():
        if path.is_relative_to(ROOT):path=path.relative_to(ROOT)
        elif path.is_relative_to(ORIGINAL_ROOT):path=path.relative_to(ORIGINAL_ROOT)
        else:raise ValueError('Dependency outside original project: '+str(path))
    if path.is_absolute() or '..' in path.parts:raise ValueError('Unsafe dependency: '+str(path))
    return path


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--stage-only',action='store_true',help='Prepare/hash a portable tree without publishing a ZIP or PDF')
    parser.add_argument('--stage-root',type=Path,default=Path('/tmp/sam-chapter2-continuation-portable-stage'))
    parser.add_argument('--destination',type=Path,default=Path('/home/lilhelper/Downloads')/ZIP_NAME)
    args=parser.parse_args()
    stage=args.stage_root.resolve();dest=stage/'sam_chapter2';marker=stage/'.SAM_CH2_STAGE'
    if dest.exists():
        if not marker.is_file() or marker.read_text()!=STAGE_MAGIC:
            raise ValueError('Refusing to replace an unrecognized stage: '+str(dest))
        shutil.rmtree(dest)
    stage.mkdir(parents=True,exist_ok=True);marker.write_text(STAGE_MAGIC)
    dest.mkdir()
    dependencies={}

    def add(path,expected=None,expected_bytes=None,role='Explicit replay dependency'):
        rel=relative(path);source=ROOT/rel
        if not source.is_file():raise FileNotFoundError('Required dependency: '+str(rel))
        if not source.resolve().is_relative_to(ROOT.resolve()):
            raise ValueError('Dependency resolves outside this checkout: '+str(rel))
        actual=sha(source);size=source.stat().st_size
        if expected is not None and actual!=expected:raise ValueError('Source hash mismatch: '+str(rel))
        if expected_bytes is not None and size!=expected_bytes:raise ValueError('Source byte count mismatch: '+str(rel))
        if rel in dependencies and dependencies[rel]['sha256']!=actual:raise ValueError('Source changed while selecting: '+str(rel))
        row=dependencies.setdefault(rel,dict(path=str(rel),original_path=str(ORIGINAL_ROOT/rel),sha256=actual,bytes=size,roles=[]))
        if role not in row['roles']:row['roles'].append(role)
        return read(source) if source.suffix=='.json' else None

    # Exact 180 primary source files, including all original preparations/gaps.
    memory=read(BASE/'memory/SOURCE_OPERANDS.json')
    if len(memory['sources'])!=180:raise ValueError('Expected 180 declared memory source files')
    for row in memory['sources']:
        add(row['path'],row['sha256'],row.get('bytes'),row.get('role','Original memory source'))
    for row in read(BASE/'memory/THEORY_SOURCE_BINDINGS.json')['sources']:
        add(row['path'],row['sha256'],role='Source of memory derivation')

    # Direct prior Chapter I/II scientific records used by all four checkers.
    direct=[
      'GEN4/duck_chapter1_lane1_20261015/sources/EXACT_INPUTS.json',
      'GEN4/duck_chapter1_lane1_20261015/RESULTS.json',
      'GEN4/voli_chapter2_bridge1/bridge/ACTUAL_CLOCK_HISTORY.json',
      'GEN4/voli_chapter2_bridge1/bridge/DERIVATION.md',
      'GEN4/voli_chapter2_bridge1/retention/DERIVATION.md',
      'GEN4/voli_chapter2_bridge1/energy/DERIVATION.md',
      'GEN4/voli_chapter2_bridge1/energy/NATIVE_INPUTS.json',
      'GEN4/voli_chapter2_bridge1/comparison/DERIVATION.md',
      'GEN4/native_history_reduction1/REDUCTION.json',
      'GEN4/native_history_reduction1/REPORT.md',
      'GEN4/duck_spin_upper1_20261014/SOURCE_ACTION_SPLIT.json',
      'GEN4/gen6_spin_clock_successor1_20261014/ACTION_LEARNING.md',
      'GEN4/gen6_spin_clock_successor1_20261014/SOURCE_ACTION.md']
    for name in direct:add(name,role='Direct analytic replay or interpretation source')
    # Reader provenance: preserve the owner-supplied Chapter II input packet
    # and its bounded extracted sources, plus the immutable new history entry.
    for source in sorted((ROOT/'GEN4/voli_chapter2_bridge1/inputs').rglob('*')):
        if source.is_file() and '__pycache__' not in source.parts:
            add(source,role='Original Chapter II reader source packet')
    add('SAM_HISTORY/entries/H002635_2026-10-15_CHAPTER_II_SIGNATURE_MEMORY_AND_PAID_CLOCK.md',
        role='Immutable result installation and preserved-scope record')
    for row in read(ROOT/'GEN4/voli_chapter2_bridge1/bridge/ACTUAL_CLOCK_HISTORY.json')['sources']:
        add(row['path'],row['sha256'],role='Actual clock certificate primary source')
    qsource=read(ROOT/'GEN4/duck_chapter1_lane1_20261015/sources/EXACT_INPUTS.json')
    for row in qsource['receipt_bindings']:
        for key in ['envelope','receipt']:
            rec=row[key];add(rec['path'],rec['sha256'],rec.get('bytes'),role='Chapter I original source/native receipt')

    run=ROOT/RUN_REL
    if not run.is_dir():raise FileNotFoundError(run)
    # Exact run records only; exclude raw runtime/checkpoint/code installations.
    # The campaign already includes its authenticated local SQLite search index.
    allowed_suffixes={'.json','.jsonl','.log','.md'}
    for source in sorted(run.iterdir()):
        if source.is_file() and source.suffix in allowed_suffixes:
            add(source,role='Actual Duck cycle policy/events/result record')
    for folder in ['native_requests','native_returns','ready']:
        parent=run/folder
        if parent.exists():
            for source in sorted(parent.rglob('*')):
                if source.is_file() and '__pycache__' not in source.parts:
                    add(source,role='Actual Duck request/return/readiness record')
    # Workers' exact task envelopes are required, not their gen6/runtime trees.
    for source in sorted((run/'workers').glob('*/tasks/*/RESULT.json')):
        add(source,role='Complete native worker receipt')
    for source in sorted((run/'workers').glob('*/tasks/*/REQUEST.json')):
        add(source,role='Complete native worker request')

    # Hash-authenticate every actual return's external receipt pointer. Some
    # read-only web helpers returned from project SAM_RUNTIME scratch; include
    # only the precise returned RESULT.json, never the scratch directory.
    custody_root=run/'helper_custody'
    custody_path=custody_root/'RAM_CUSTODY.json'
    custody=read(custody_path)
    helper_readback_path=run/'HELPER_READBACK.json'
    helper_readback=read(helper_readback_path)
    custody_rows={r['path']:r for r in custody['files']}
    readback_rows={r['path']:r for r in helper_readback['files']}
    for source in sorted(custody_root.glob('*.json')):
        row=readback_rows.get(source.name)
        add(source,row['sha256'] if row else None,role='Original helper custody/resource metadata')
    add(helper_readback_path,role='Verified helper custody readback manifest')
    relocations=[]

    def resolve_receipt(ptr,digest):
        rel=relative(ptr)
        if (ROOT/rel).is_file():return rel
        original=Path(ptr)
        prefix=Path(custody['original_scratch'])
        if not original.is_relative_to(prefix):raise FileNotFoundError('Missing original receipt without custody: '+ptr)
        suffix=original.relative_to(prefix)
        if suffix.is_absolute() or '..' in suffix.parts:raise ValueError('Unsafe custody suffix')
        row=custody_rows.get(str(suffix));readback=readback_rows.get('retained_ram/'+str(suffix))
        if row is None or readback is None or row['sha256']!=digest or readback['sha256']!=digest:
            raise ValueError('Custody manifest/hash mismatch: '+str(suffix))
        retained=custody_root/'retained_ram'/suffix
        add(retained,digest,row.get('bytes'),role='Original helper receipt retained under authenticated RAM custody')
        relocations.append(dict(original_receipt_path=ptr,retained_path=str(retained.relative_to(ROOT)),sha256=digest,
          custody_manifest=str(custody_path.relative_to(ROOT)),custody_manifest_sha256=sha(custody_path),
          readback_manifest=str(helper_readback_path.relative_to(ROOT)),readback_manifest_sha256=sha(helper_readback_path)))
        return retained.relative_to(ROOT)

    return_count=0
    for source in sorted((run/'native_returns').glob('*.json')):
        wrapper=read(source);return_count+=1
        for path_key,hash_key in [('receipt','receipt_sha256'),('record_file','record_file_sha256'),('path','sha256')]:
            ptr=wrapper.get(path_key);digest=wrapper.get(hash_key)
            if isinstance(ptr,str) and isinstance(digest,str) and len(digest)==64:
                rel=relative(ptr)
                if not (rel.is_relative_to(RUN_REL) or rel.is_relative_to(Path('SAM_RUNTIME/GEN6_DUCK')/run.name)):
                    raise ValueError('Unexpected native/helper receipt scope: '+str(rel))
                rel=resolve_receipt(ptr,digest)
                add(rel,digest,role='Hash-authenticated original Duck/helper receipt')
        # Scientific source files bound by retained native requests/receipts.
        for record in [wrapper,wrapper.get('native_payload',{})]:
            binding=record.get('source_binding',{})
            for path,digest in binding.get('source_files',{}).items():
                add(path,digest,role='Frozen native source-binding artifact')
    # Local research index is already in this campaign. Validate the indexed
    # bytes; reconstruction of the wider source export/runtime is unnecessary.
    index_manifest=BASE/'inputs/RESEARCH_WEB.sqlite.manifest.json'
    index=read(index_manifest)
    if sha(BASE/'inputs/RESEARCH_WEB.sqlite')!=index['index_sha256']:
        raise ValueError('Local source research index differs from its manifest')
    if not args.stage_only:
        for name in ['reproduce.py','README.md','REPORT.md','RESOURCE_RELEASE.json']:
            if not (BASE/name).is_file():raise FileNotFoundError('Finish delivery record before packaging: '+name)
        if not (BASE/'output/pdf'/PDF_NAME).is_file():raise FileNotFoundError('Final PDF is required')

    def ignore(folder,names):
        excluded=set()
        for name in names:
            if name in {'tmp','__pycache__','.pytest_cache','.git','BUNDLE.json','STAGING_RECEIPT.json'} or name.endswith(('.pyc','.pyo','.zip','.partial')):
                excluded.add(name)
        return excluded

    scoped_target=dest/BASE.relative_to(ROOT)
    # Reject a symlink escape before the only recursive campaign copy.
    for source in BASE.rglob('*'):
        if source.is_file() and not source.resolve().is_relative_to(BASE.resolve()):
            raise ValueError('Campaign file resolves outside scoped package: '+str(source))
    shutil.copytree(BASE,scoped_target,ignore=ignore)
    rows=[]
    for rel,row in sorted(dependencies.items()):
        source=ROOT/rel;target=dest/rel
        if not target.exists():target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
        if sha(target)!=row['sha256']:raise ValueError('Copied source differs: '+str(rel))
        rows.append(row)
    (dest/'SOURCE_DEPENDENCIES.json').write_text(json.dumps(rows,indent=2,sort_keys=True)+'\n')
    (dest/'RECEIPT_CUSTODY_RELOCATIONS.json').write_text(json.dumps(relocations,indent=2,sort_keys=True)+'\n')
    (dest/'README.txt').write_text(
      'SAM Volume I Chapter II continuation and reproducibility\n\n'
      'Read: GEN4/voli_chapter2_continuation2_20261015/README.md\n'
      'Offline replay: python3 GEN4/voli_chapter2_continuation2_20261015/reproduce.py\n'
      'Editable manuscript/PDF build: GEN4/voli_chapter2_continuation2_20261015/chapter/\n'
      'Verify MANIFEST.sha256 before replay, since replay regenerates derived reports.\n'
      'All native science is retained evidence. Offline replay launches zero native operations.\n'
      'SOURCE_DEPENDENCIES.json maps original source paths to exact retained bytes.\n'
      'This bundle is a requested research deliverable; it does not commit or synchronize the research repository.\n')
    files=sorted(p for p in dest.rglob('*') if p.is_file())
    (dest/'MANIFEST.sha256').write_text(''.join(sha(p)+'  '+str(p.relative_to(dest))+'\n' for p in files))
    # Verify the complete staged manifest once before publication.
    for line in (dest/'MANIFEST.sha256').read_text().splitlines():
        digest,name=line.split('  ',1)
        if sha(dest/name)!=digest:raise ValueError('Staged checksum mismatch: '+name)
    result=dict(schema='SAM_CH2_CONTINUATION_BUNDLE_V1',status='STAGED' if args.stage_only else 'PACKAGED',
      stage=str(dest),files=len(files)+1,source_dependencies=len(rows),memory_primary_sources=180,
      actual_Duck_returns=return_count,authenticated_helper_receipt_relocations=len(relocations),manifest_sha256=sha(dest/'MANIFEST.sha256'),
      scientific_records_modified=False,native_reexecutions=0,builder_sha256=sha(Path(__file__)))
    if args.stage_only:
        (HERE/'STAGING_RECEIPT.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    else:
        output=args.destination.expanduser().resolve();output.parent.mkdir(parents=True,exist_ok=True)
        temporary=output.with_name(output.name+'.partial')
        with zipfile.ZipFile(temporary,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6,strict_timestamps=False) as archive:
            for source in sorted(dest.rglob('*')):
                if source.is_file():archive.write(source,source.relative_to(stage))
        temporary.replace(output)
        # No global download destination is inferred from source chart units.
        pdf=BASE/'output/pdf'/PDF_NAME;download_pdf=output.parent/PDF_NAME
        shutil.copy2(pdf,download_pdf)
        result.update(zip_path=str(output),zip_sha256=sha(output),zip_bytes=output.stat().st_size,
          pdf_path=str(download_pdf),pdf_sha256=sha(pdf))
        if sha(download_pdf)!=result['pdf_sha256']:raise ValueError('Downloaded PDF hash mismatch')
        (HERE/'BUNDLE.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':main()
