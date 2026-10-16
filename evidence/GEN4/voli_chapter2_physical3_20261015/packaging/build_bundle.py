#!/usr/bin/env python3
"""Package exact predecessor bytes, this scoped campaign and declared evidence.

Validates the released predecessor ZIP before extracting its files. Only the
new campaign is copied recursively; native object stores/runtime/checkpoints
are excluded. External evidence is selected by source bindings and authenticated
Duck receipt/custody manifests. This launches no native operation.
"""
from __future__ import annotations
import argparse,hashlib,json,os,shutil,stat,zipfile
from pathlib import Path,PurePosixPath
HERE=Path(__file__).resolve().parent;BASE=HERE.parent;ROOT=BASE.parents[1]
ORIGINAL_ROOT=Path('/home/lilhelper/SAM_Research_Overflow/SAM_Research_Project')
PRIOR_NAME='SAM_Volume_I_Chapter_II_Continuation_and_Verification_20261015.zip'
PRIOR_SHA='39d339b049e5580b11c4f2c7ec85ad687452c40e6e8e674411e9f8ac7e5e8d93'
PDF_NAME='SAM_Volume_I_Chapter_II_Physical_Development_Draft_20261015.pdf'
ZIP_NAME='SAM_Volume_I_Chapter_II_Physical_Development_and_Verification_20261015.zip'
RUN_REL=Path('GEN4/duck_gen6_local/runs/chapter2-physical-protocols-20261015-01')
STAGE_MAGIC='SAM_CHAPTER2_PHYSICAL_PORTABLE_STAGE_V1\n'
SKIP_DIRS={'tmp','__pycache__','.pytest_cache','.git','R3_STATE','checkpoints','runtime','CURRENT_REVISION','ram_scratch'}
SKIP_FILES={'BUNDLE.json','STAGING_RECEIPT.json'}
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def read(p):return json.loads(Path(p).read_text())
def relative(path):
 p=Path(path)
 if p.is_absolute():
  if p.is_relative_to(ROOT):p=p.relative_to(ROOT)
  elif p.is_relative_to(ORIGINAL_ROOT):p=p.relative_to(ORIGINAL_ROOT)
  else:raise ValueError('Dependency outside declared project: '+str(path))
 if p.is_absolute() or '..' in p.parts:raise ValueError('Unsafe dependency: '+str(path))
 return p

def safe_members(archive):
 names={};prefix='sam_chapter2/'
 for item in archive.infolist():
  if item.is_dir():continue
  if item.filename in names:raise ValueError('Duplicate predecessor member: '+item.filename)
  p=PurePosixPath(item.filename)
  if p.is_absolute() or '..' in p.parts or not item.filename.startswith(prefix):raise ValueError('Unsafe predecessor member: '+item.filename)
  if stat.S_ISLNK(item.external_attr>>16):raise ValueError('Predecessor symlink member: '+item.filename)
  names[item.filename]=item
 return names

def prepare_prior(path,dest):
 if sha(path)!=PRIOR_SHA:raise ValueError('Released predecessor ZIP hash mismatch')
 with zipfile.ZipFile(path) as z:
  members=safe_members(z);manifest=z.read('sam_chapter2/MANIFEST.sha256');expected={}
  for line in manifest.decode().splitlines():
   digest,name=line.split('  ',1);p=PurePosixPath(name)
   if p.is_absolute() or '..' in p.parts or name in expected:raise ValueError('Unsafe/duplicate predecessor manifest path: '+name)
   expected[name]=digest
  if set(members)!={'sam_chapter2/'+x for x in expected}|{'sam_chapter2/MANIFEST.sha256'}:raise ValueError('Predecessor ZIP and manifest file sets differ')
  for name,digest in expected.items():
   payload=z.read('sam_chapter2/'+name)
   if hashlib.sha256(payload).hexdigest()!=digest:raise ValueError('Predecessor manifest mismatch: '+name)
  for name,item in members.items():
   rel=PurePosixPath(name).relative_to('sam_chapter2');target=dest/Path(*rel.parts);target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(z.read(item))
 metadata=dest/'predecessor_metadata';metadata.mkdir(exist_ok=True)
 for name in ('MANIFEST.sha256','SOURCE_DEPENDENCIES.json','RECEIPT_CUSTODY_RELOCATIONS.json','README.txt'):
  p=dest/name
  if p.is_file():shutil.copy2(p,metadata/name)
 receipt=dict(schema='SAM_CH2_PREDECESSOR_BYTES_V1',zip_name=path.name,zip_sha256=PRIOR_SHA,
  zip_bytes=path.stat().st_size,verified_manifest_sha256=hashlib.sha256(manifest).hexdigest(),verified_files=len(members),
  scientific_payload_modified=False,root_metadata_preserved_under='predecessor_metadata/')
 (metadata/'BUNDLE_PROVENANCE.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
 return receipt

def campaign_files():
 for current,dirs,files in os.walk(BASE):
  kept=[]
  for name in dirs:
   p=Path(current)/name
   if name in SKIP_DIRS:continue
   if p.is_symlink():raise ValueError('Campaign directory symlink: '+str(p))
   kept.append(name)
  dirs[:]=kept
  for name in files:
   if name in SKIP_FILES or name.endswith(('.pyc','.pyo','.zip','.partial')):continue
   p=Path(current)/name
   if p.is_symlink() or not p.resolve().is_relative_to(BASE.resolve()):raise ValueError('Campaign file escapes scope: '+str(p))
   if p.is_file():yield p

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--stage-only',action='store_true')
 ap.add_argument('--stage-root',type=Path,default=Path('/tmp/sam-chapter2-physical-portable-stage'))
 ap.add_argument('--destination',type=Path,default=Path('/home/lilhelper/Downloads')/ZIP_NAME)
 ap.add_argument('--prior-zip',type=Path,default=Path('/home/lilhelper/Downloads')/PRIOR_NAME)
 ap.add_argument('--history-entry',action='append',default=[])
 ap.add_argument('--pdf-name',default=PDF_NAME);args=ap.parse_args()
 if Path(args.pdf_name).name!=args.pdf_name:raise ValueError('PDF name must be a basename')
 stage=args.stage_root.expanduser().resolve();dest=stage/'sam_chapter2';marker=stage/'.SAM_CH2_STAGE'
 if dest.exists():
  if not marker.is_file() or marker.read_text()!=STAGE_MAGIC:raise ValueError('Refusing to replace an unrecognized stage')
  shutil.rmtree(dest)
 stage.mkdir(parents=True,exist_ok=True);marker.write_text(STAGE_MAGIC);dest.mkdir()
 prior=prepare_prior(args.prior_zip.expanduser().resolve(),dest)
 deps={Path(x['path']):x for x in read(dest/'SOURCE_DEPENDENCIES.json')}
 for row in deps.values():row.setdefault('roles',[])
 def add(path,digest=None,size=None,role='Explicit physical-development replay dependency'):
  rel=relative(path);source=ROOT/rel
  if not source.is_file():raise FileNotFoundError('Required source/evidence: '+str(rel))
  if not source.resolve().is_relative_to(ROOT.resolve()):raise ValueError('Source resolves outside checkout: '+str(rel))
  actual=sha(source);n=source.stat().st_size
  if digest is not None and actual!=digest:raise ValueError('Bound source hash mismatch: '+str(rel))
  if size is not None and n!=size:raise ValueError('Bound source byte count mismatch: '+str(rel))
  target=dest/rel
  if target.exists():
   if sha(target)!=actual:raise ValueError('Predecessor or staged scientific bytes differ: '+str(rel))
  else:
   target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
   if sha(target)!=actual:raise ValueError('Source changed while copying: '+str(rel))
  previous=deps.get(rel)
  if previous and previous['sha256']!=actual:raise ValueError('Conflicting source bindings: '+str(rel))
  row=deps.setdefault(rel,dict(path=str(rel),original_path=str(ORIGINAL_ROOT/rel),sha256=actual,bytes=n,roles=[]))
  if role not in row['roles']:row['roles'].append(role)
  return read(source) if source.suffix=='.json' else None
 # Overlay only this scoped campaign. Existing predecessor science is retained.
 new_files=list(campaign_files());new_target=dest/BASE.relative_to(ROOT)
 if new_target.exists():raise ValueError('New campaign unexpectedly occurs in predecessor')
 for source in new_files:
  before=sha(source);target=dest/source.relative_to(ROOT);target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
  if sha(target)!=before or sha(source)!=before:raise ValueError('Campaign file changed during snapshot: '+str(source))
 # Explicit physical protocol bindings include both actual clock certificates.
 for row in read(BASE/'protocol/SOURCE_BINDINGS.json')['sources']:
  add(row['path'],row['sha256'],row.get('bytes'),'Original physical protocol/clock source')
 # Authenticate all exact full-source preparation and executed-code bindings.
 # Iterate scoped JSON files only; native object stores are never traversed.
 checked_bindings=0
 for p in new_files:
  if p.suffix!='.json':continue
  try:data=read(p)
  except (ValueError,UnicodeDecodeError):continue
  stack=[data]
  while stack:
   item=stack.pop()
   if isinstance(item,list):stack.extend(x for x in item if isinstance(x,(dict,list)));continue
   if not isinstance(item,dict):continue
   source_files=item.get('source_files')
   if isinstance(source_files,dict):
    for name,digest in source_files.items():
     if isinstance(digest,str) and len(digest)==64:
      add(name,digest,role='Frozen source binding in '+str(p.relative_to(BASE)));checked_bindings+=1
   # Historical retrieval-index path metadata is not an instruction to copy
   # an entire old source corpus. Frozen source_files maps and the explicit
   # protocol manifest above supply the actual scientific dependency contract.
   stack.extend(v for v in item.values() if isinstance(v,(dict,list)))
 history=list(args.history_entry)
 install=BASE/'HISTORY_INSTALLATION.json'
 if install.is_file():
  d=read(install)
  for name in d.get('history_entries',[]):
   if name not in history:history.append(name)
 for name in history:add(name,role='Immutable physical-development result installation')
 run=ROOT/RUN_REL
 if not run.is_dir():raise FileNotFoundError('Exact Duck cycle is missing')
 for source in sorted(run.iterdir()):
  if source.is_file() and source.suffix in {'.json','.jsonl','.log','.md'}:add(source,role='Actual two-by-180-second Duck cycle record')
 for name in ('native_requests','native_returns','ready'):
  folder=run/name
  if folder.exists():
   for source in sorted(folder.rglob('*')):
    if source.is_file() and '__pycache__' not in source.parts:add(source,role='Actual Duck request, return or readiness record')
 for name in ('RESULT.json','REQUEST.json'):
  for source in sorted((run/'workers').glob('*/tasks/*/'+name)):add(source,role='Exact native worker task envelope')
 custody_path=run/'helper_custody/RAM_CUSTODY.json';readback_path=run/'HELPER_READBACK.json'
 custody=read(custody_path);readback=read(readback_path)
 if custody.get('status')!='PASS' or readback.get('status')!='PASS':raise ValueError('Helper custody/readback not complete')
 cm={r['path']:r for r in custody['files']};hm={r['path']:r for r in readback['files']}
 for source in sorted(custody_path.parent.glob('*.json')):
  row=hm.get(source.name);add(source,row['sha256'] if row else None,role='Original helper custody/resource metadata')
 add(readback_path,role='Verified original helper custody readback manifest')
 relocations=[]
 def receipt(ptr,digest):
  original=Path(ptr);prefix=Path(custody['original_scratch'])
  if original.is_absolute() and original.is_relative_to(prefix):
   suffix=original.relative_to(prefix)
   if '..' in suffix.parts:raise ValueError('Unsafe helper custody suffix')
   c=cm.get(str(suffix));h=hm.get('retained_ram/'+str(suffix))
   if c is None or h is None or c['sha256']!=digest or h['sha256']!=digest:raise ValueError('Helper receipt absent from exact custody/hash manifests')
   kept=custody_path.parent/'retained_ram'/suffix;add(kept,digest,c.get('bytes'),'Exact manifest-authenticated helper receipt')
   relocations.append(dict(original_receipt_path=ptr,retained_path=str(kept.relative_to(ROOT)),sha256=digest,
    custody_manifest=str(custody_path.relative_to(ROOT)),custody_manifest_sha256=sha(custody_path),
    readback_manifest=str(readback_path.relative_to(ROOT)),readback_manifest_sha256=sha(readback_path)))
   return
  rel=relative(ptr)
  if not rel.is_relative_to(RUN_REL):raise ValueError('Unexpected native receipt scope: '+str(rel))
  add(rel,digest,role='Exact hash-authenticated Duck native receipt')
 returns=0
 for source in sorted((run/'native_returns').glob('*.json')):
  wrapper=read(source);returns+=1
  for pk,hk in (('receipt','receipt_sha256'),('record_file','record_file_sha256'),('path','sha256')):
   ptr=wrapper.get(pk);digest=wrapper.get(hk)
   if isinstance(ptr,str) and isinstance(digest,str) and len(digest)==64:receipt(ptr,digest)
  for item in (wrapper,wrapper.get('native_payload',{})):
   for name,digest in item.get('source_binding',{}).get('source_files',{}).items():add(name,digest,role='Actual native request/receipt scientific operand')
 # Native request operands may bind files not repeated in a wrapper.
 for source in sorted((run/'native_requests').glob('*.json')):
  data=read(source);task=data.get('task',data);payload=task.get('payload',{})
  for name,digest in payload.get('source_binding',{}).get('source_files',{}).items():add(name,digest,role='Actual native request scientific operand')
 index_manifest=BASE/'inputs/RESEARCH_WEB.sqlite.manifest.json'
 if index_manifest.is_file() and sha(BASE/'inputs/RESEARCH_WEB.sqlite')!=read(index_manifest)['index_sha256']:raise ValueError('Research index source differs from manifest')
 if not args.stage_only:
  for name in ('reproduce.py','README.md','REPORT.md','RESOURCE_RELEASE.json','NATIVE_VERIFICATION.json','CYCLE_VERIFICATION.json'):
   if not (BASE/name).is_file():raise FileNotFoundError('Finish delivery record before packaging: '+name)
  if not history:raise ValueError('Pass the exact installed history entry with --history-entry')
  if read(run/'COMPLETE.json')['status']!='COMPLETE':raise ValueError('Duck cycle is not complete')
  if read(BASE/'NATIVE_VERIFICATION.json')['status']!='PASS' or read(BASE/'CYCLE_VERIFICATION.json')['status']!='PASS':raise ValueError('Final native/cycle readback must pass')
 pdf=BASE/'output/pdf'/args.pdf_name
 if not pdf.is_file():raise FileNotFoundError('Physical development PDF missing: '+str(pdf))
 rows=[row for _,row in sorted(deps.items())]
 (dest/'SOURCE_DEPENDENCIES.json').write_text(json.dumps(rows,indent=2,sort_keys=True)+'\n')
 previous_relocations=read(dest/'predecessor_metadata/RECEIPT_CUSTODY_RELOCATIONS.json')
 (dest/'RECEIPT_CUSTODY_RELOCATIONS.json').write_text(json.dumps(previous_relocations+relocations,indent=2,sort_keys=True)+'\n')
 (dest/'README.txt').write_text('SAM Volume I Chapter II physical development and verification\n\n'
  'Read: '+str(BASE.relative_to(ROOT))+'/README.md\n'
  'Offline replay: python3 '+str(BASE.relative_to(ROOT))+'/reproduce.py\n'
  'Editable manuscript and pinned PDF build: '+str(BASE.relative_to(ROOT))+'/chapter/\n'
  'Verify MANIFEST.sha256 before replay; replay regenerates derived reports.\n'
  'All native science is retained evidence; offline replay launches zero native operations.\n'
  'Exact predecessor science and PDFs are retained. predecessor_metadata/ preserves its original root metadata.\n'
  'SOURCE_DEPENDENCIES.json binds original paths to exact retained bytes.\n'
  'No research repository commit, sync, runtime installation or native reexecution is performed by this builder.\n')
 # Exclude only the new root manifest; original nested manifests are scientific inputs.
 files=sorted(p for p in dest.rglob('*') if p.is_file() and p!=dest/'MANIFEST.sha256')
 (dest/'MANIFEST.sha256').write_text(''.join(sha(p)+'  '+str(p.relative_to(dest))+'\n' for p in files))
 for line in (dest/'MANIFEST.sha256').read_text().splitlines():
  digest,name=line.split('  ',1)
  if sha(dest/name)!=digest:raise ValueError('Staged manifest mismatch: '+name)
 result=dict(schema='SAM_CH2_PHYSICAL_BUNDLE_V1',status='STAGED' if args.stage_only else 'PACKAGED',stage=str(dest),
  predecessor=prior,files=len(files)+1,source_dependencies=len(rows),checked_source_binding_occurrences=checked_bindings,
  actual_Duck_returns=returns,authenticated_new_helper_receipt_relocations=len(relocations),
  manifest_sha256=sha(dest/'MANIFEST.sha256'),builder_sha256=sha(Path(__file__)),scientific_records_modified=False,native_reexecutions=0)
 if args.stage_only:(HERE/'STAGING_RECEIPT.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 else:
  output=args.destination.expanduser().resolve();output.parent.mkdir(parents=True,exist_ok=True);temporary=output.with_name(output.name+'.partial')
  with zipfile.ZipFile(temporary,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
   for source in sorted(dest.rglob('*')):
    if not source.is_file():continue
    info=zipfile.ZipInfo(str(source.relative_to(stage)),date_time=(2026,10,15,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=(stat.S_IFREG|0o644)<<16
    z.writestr(info,source.read_bytes(),compresslevel=6)
  temporary.replace(output);download_pdf=output.parent/args.pdf_name;shutil.copy2(pdf,download_pdf)
  if sha(download_pdf)!=sha(pdf):raise ValueError('Downloaded PDF differs')
  result.update(zip_path=str(output),zip_sha256=sha(output),zip_bytes=output.stat().st_size,pdf_path=str(download_pdf),pdf_sha256=sha(pdf))
  (HERE/'BUNDLE.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print(json.dumps(result,sort_keys=True))
if __name__=='__main__':main()
