#!/usr/bin/env python3
"""Offline replay using retained operands/receipts; never launches Duck or a network."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import importlib.metadata
import json
import subprocess
import sys

BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[1]
SOURCE_SCRIPTS=[
    'source/verify.py','source/verify_uniform_coupling.py',
    'radial/verify.py','energy/verify.py','clock/verify.py',
    'core/verify_core.py','clock/verify_correlated_phase.py',
    'source/build_cube_graph.py',
]
PDF_NAMES=[
    'SAM_Volume_I_Chapter_II_Source_to_Field_Update_20261015.pdf',
    'SAM_Volume_I_Chapter_III_Source_to_Field_Development_20261015.pdf',
]
CHECK_REPORTS={
    'source/CHECKS.json':'independent_exact_checks',
    'source/UNIFORM_COUPLING_RESPONSE.json':'independent_exact_checks',
    'radial/VERIFICATION.json':'checks',
    'energy/FIELD_SOURCE_RESULTS.json':'checks',
    'clock/RESULTS.json':'checks_passed',
    'clock/CORRELATED_PHASE_RESULTS.json':'checks_passed',
    'core/RESULTS.json':'checks_passed',
}

def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda:f.read(1024**2),b''):h.update(b)
    return h.hexdigest()

def verify_manifest():
    manifest=ROOT/'MANIFEST.sha256'
    if not manifest.exists():return {'status':'NOT_A_PORTABLE_BUNDLE','files':0}
    seen=set()
    for line in manifest.read_text().splitlines():
        digest,name=line.split('  ',1);p=PurePosixPath(name)
        if p.is_absolute() or '..' in p.parts or name in seen:
            raise ValueError('Unsafe or duplicate manifest path: '+name)
        path=ROOT/Path(*p.parts)
        if path.is_symlink() or not path.resolve().is_relative_to(ROOT.resolve()):
            raise ValueError('Manifest path escapes portable root: '+name)
        if not path.is_file() or sha(path)!=digest:
            raise ValueError('Portable manifest mismatch: '+name)
        seen.add(name)
    actual={str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file()
            and p!=manifest and '__pycache__' not in p.parts and p.suffix!='.pyc'}
    if actual!=seen:raise ValueError('Portable file set differs from initial manifest')
    return {'status':'PASS','files':len(seen),'sha256':sha(manifest)}

def pdf_versions():
    versions={}
    for line in (BASE/'chapter3/requirements-pdf.lock').read_text().splitlines():
        if not line.strip() or line.lstrip().startswith('#'):continue
        name,expected=line.split('==',1)
        actual=importlib.metadata.version(name)
        if actual!=expected:raise ValueError('Pinned PDF dependency differs: '+name+' '+actual+' != '+expected)
        versions[name]=actual
    if (BASE/'chapter2/requirements-pdf.lock').read_bytes()!=(BASE/'chapter3/requirements-pdf.lock').read_bytes():
        raise ValueError('Chapter II/III PDF dependency locks differ')
    return versions

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-only',action='store_true',help='Development preflight: omit completed native receipt readback; not a full replay verdict')
    parser.add_argument('--pdf',action='store_true',help='Use already installed pinned PDF dependencies; verify relocated byte-identical rebuilds')
    parser.add_argument('--skip-manifest',action='store_true',help='Allow an intentional second replay after derived reports changed; verify the fresh extraction first')
    args=parser.parse_args();rows=[]
    result={'schema':'SAM_CH2_CH3_OFFLINE_REPRODUCTION_V1','status':'RUNNING',
            'scope':'SOURCE_ONLY_PREFLIGHT' if args.source_only else 'COMPLETE_RETAINED_EVIDENCE_REPLAY',
            'native_executions':0,'network_requests':0,'runtime_installations':0,'scripts':rows}
    try:
        result['initial_manifest']={'status':'EXPLICITLY_SKIPPED'} if args.skip_manifest else verify_manifest()
        scripts=list(SOURCE_SCRIPTS)
        if not args.source_only:scripts.append('verify_native.py')
        if args.pdf:
            result['pdf_packages']=pdf_versions()
            result['pdf_sha256_before']={name:sha(BASE/'output/pdf'/name) for name in PDF_NAMES}
            scripts.extend(['chapter2/verify_pdf.py','chapter3/verify_pdf.py'])
        graph_before=sha(BASE/'source/CUBE_GRAPH.json')
        for name in scripts:
            p=subprocess.run([sys.executable,'-B',str(BASE/name)],cwd=BASE,capture_output=True,text=True)
            rows.append({'script':name,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
            if p.returncode:raise RuntimeError('Offline replay failed: '+name+'\n'+p.stdout+p.stderr)
        if sha(BASE/'source/CUBE_GRAPH.json')!=graph_before:
            raise ValueError('Exact cube fixture regeneration changed source-bound bytes')
        counts={}
        for name,key in CHECK_REPORTS.items():
            report=json.loads((BASE/name).read_text())
            if report.get('status')!='PASS':raise ValueError('Derived check report is not PASS: '+name)
            counts[name]=report[key]
        result['independent_science_assertions_by_report']=counts
        result['independent_science_assertions']=sum(counts.values())
        if not args.source_only:
            native=json.loads((BASE/'NATIVE_VERIFICATION.json').read_text())
            result['retained_native_readback']={key:native[key] for key in [
                'native_outputs_verified','research_receipts_authenticated','matrix_entries_checked','independent_checks']}
        if args.pdf:
            after={name:sha(BASE/'output/pdf'/name) for name in PDF_NAMES}
            if after!=result['pdf_sha256_before']:raise ValueError('PDF verification changed a delivered PDF')
            result['pdf_sha256_after']=after
            result['pdf_rebuilds']='RELOCATED_FRESH_CACHE_BYTE_IDENTICAL'
        result['status']='SOURCE_ONLY_PASS' if args.source_only else 'PASS'
    except Exception as error:
        result['status']='FAIL';result['error']=repr(error)
        (BASE/'REPRODUCTION.json').write_text(json.dumps(result,indent=2)+'\n')
        print(str(error),file=sys.stderr);raise SystemExit(1)
    (BASE/'REPRODUCTION.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'scripts':len(rows),'native_executions':0,'network_requests':0,
                      'independent_science_assertions':result['independent_science_assertions'],
                      'pdf_rebuilds':result.get('pdf_rebuilds','NOT_REQUESTED')}))

if __name__=='__main__':main()
