#!/usr/bin/env python3
"""Build the unchanged reviewed Chapter II from bundled editable sources."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[1]

def build(output):
    with tempfile.TemporaryDirectory(prefix='sam-chapter2-pdf-') as temporary:
        stage=Path(temporary)/'campaign/chapter2'
        shutil.copytree(ROOT/'manuscript/source',stage,ignore=shutil.ignore_patterns('__pycache__'))
        shutil.copytree(ROOT/'assets/fonts',stage/'fonts')
        result=subprocess.run([sys.executable,'-B',str(stage/'build_pdf.py')],capture_output=True,text=True)
        if result.returncode:raise RuntimeError(result.stdout+result.stderr)
        generated=stage.parent/'output/pdf/SAM_Volume_I_Chapter_II_Source_to_Field_Update_20261015.pdf'
        reviewed=ROOT/'manuscript/Chapter_II.pdf'
        if generated.read_bytes()!=reviewed.read_bytes():
            raise ValueError('Rebuild differs from reviewed manuscript; use the pinned PDF environment')
        output.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(generated,output)
        metrics=json.loads((stage/'LAYOUT.json').read_text())
    return dict(status='PASS',pages=24,sections=48,output=str(output),
        sha256=hashlib.sha256(output.read_bytes()).hexdigest(),
        byte_identical_to_reviewed=True,layout_frames=len(metrics),
        minimum_unused_height=min(x['unused_height'] for x in metrics))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT/'build/Chapter_II.pdf')
    args=parser.parse_args()
    try:print(json.dumps(build(args.output.resolve()),indent=2))
    except (OSError,ValueError,RuntimeError) as error:
        print(json.dumps(dict(status='FAIL',error=str(error))));return 1
    return 0

if __name__=='__main__':raise SystemExit(main())
