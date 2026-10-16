#!/usr/bin/env python3
"""Refresh the public asset inventory after intentional, reviewed source changes."""
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
SKIP={'.git','.venv','build','dist','__pycache__','.pytest_cache','.replay','evidence'}
files=[]
for path in sorted(ROOT.rglob('*')):
    relative=path.relative_to(ROOT)
    if any(part in SKIP or part.endswith('.egg-info') for part in relative.parts):continue
    if not path.is_file() or relative.as_posix()=='MANIFEST.json':continue
    if path.is_symlink():raise ValueError('Do not inventory symlinks')
    content=path.read_bytes();files.append(dict(path=relative.as_posix(),sha256=hashlib.sha256(content).hexdigest(),bytes=len(content)))
(ROOT/'MANIFEST.json').write_text(json.dumps(dict(schema='SAM_CHAPTER_II_PORTABLE_ASSETS_V1',
    scope='Portable manuscript, source, docs, assets and configuration; frozen evidence has its own manifest',files=files),indent=2)+'\n')
print(json.dumps(dict(files=len(files))))
