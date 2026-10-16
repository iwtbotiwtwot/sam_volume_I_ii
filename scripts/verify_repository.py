#!/usr/bin/env python3
"""Authenticate the portable manuscript, code, tests and documentation inventory."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]

def verify_assets(root=ROOT,manifest_path=None):
    root=Path(root).resolve();manifest_path=Path(manifest_path) if manifest_path else root/'MANIFEST.json'
    data=json.loads(manifest_path.read_text());seen=set();total=0
    if data.get('schema')!='SAM_CHAPTER_II_PORTABLE_ASSETS_V1' or not data.get('files'):
        raise ValueError('Unknown or empty asset manifest')
    for entry in data['files']:
        name=entry['path'];relative=PurePosixPath(name)
        if (not name or relative.is_absolute() or '..' in relative.parts or '\\' in name
            or str(relative)!=name or name in seen):raise ValueError('Unsafe or duplicate asset path: '+name)
        seen.add(name);path=root/relative
        if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(root):
            raise ValueError('Missing or escaped asset: '+name)
        content=path.read_bytes()
        if len(content)!=entry['bytes'] or hashlib.sha256(content).hexdigest()!=entry['sha256']:
            raise ValueError('Asset content mismatch: '+name)
        total+=len(content)
    return dict(status='PASS',files=len(seen),bytes=total)

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--manifest',type=Path)
    args=parser.parse_args()
    try:print(json.dumps(verify_assets(manifest_path=args.manifest),indent=2));return 0
    except (OSError,ValueError,KeyError,TypeError) as error:
        print(json.dumps(dict(status='FAIL',error=str(error))));return 1

if __name__=='__main__':raise SystemExit(main())
