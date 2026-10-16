"""Offline standard-library replay; never launches a scientific native session."""
from pathlib import Path
import json,subprocess,sys
BASE=Path(__file__).resolve().parent
SCRIPTS=[['verify_protocols.py'],['closure/verify_source_law.py'],['closure/exact_lumped_upper_bound.py'],['closure/finalize_closure.py','--require54'],['closure/verify_cache_semantics.py'],['packaging/verify_domain_provenance.py'],['verify_native.py'],['verify_cycle.py']]
def main():
 rows=[]
 for script in SCRIPTS:
  p=subprocess.run([sys.executable,'-B',str(BASE/script[0]),*script[1:]],cwd=BASE,capture_output=True,text=True)
  rows.append(dict(script=script,returncode=p.returncode,stdout=p.stdout,stderr=p.stderr))
  if p.returncode:
   (BASE/'REPRODUCTION.json').write_text(json.dumps(dict(status='FAIL',native_executions=0,scripts=rows),indent=2)+'\n');print(p.stdout);print(p.stderr,file=sys.stderr);raise SystemExit(p.returncode)
 out=dict(status='PASS',native_executions=0,scripts=rows);(BASE/'REPRODUCTION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(dict(status='PASS',scripts=len(rows),native_executions=0)))
if __name__=='__main__':main()
