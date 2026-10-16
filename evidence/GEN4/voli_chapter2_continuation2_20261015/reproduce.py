"""Offline standard-library replay of new derivations and retained native science."""
from pathlib import Path
import json,subprocess,sys
BASE=Path(__file__).resolve().parent
SCRIPTS=['signature/check_signature.py','memory/exact_memory.py','instrument/verify.py','records/verify.py',
    'signature/verify_native.py','memory/verify_native.py','instrument/verify_native.py','verify_cycle.py']
def main():
    rows=[]
    for script in SCRIPTS:
        p=subprocess.run([sys.executable,'-B',str(BASE/script)],cwd=BASE,capture_output=True,text=True)
        rows.append(dict(script=script,returncode=p.returncode,stdout=p.stdout,stderr=p.stderr))
        if p.returncode:
            print(p.stdout);print(p.stderr,file=sys.stderr)
            (BASE/'REPRODUCTION.json').write_text(json.dumps(dict(status='FAIL',native_executions=0,scripts=rows),indent=2)+'\n')
            raise SystemExit(p.returncode)
    result=dict(status='PASS',native_executions=0,scripts=rows)
    (BASE/'REPRODUCTION.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',scripts=len(rows),native_executions=0)))
if __name__=='__main__':main()
