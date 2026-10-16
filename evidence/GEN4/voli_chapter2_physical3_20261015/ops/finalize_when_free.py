"""Retry only final retention while unrelated workers hold the required leases.

No research preparation, launch, arithmetic, window reset, or global resource
change occurs here. Existing cycle completion remains the installed CLI's job.
"""
from pathlib import Path
import json,subprocess,sys,time
BASE=Path(__file__).resolve().parents[1];ROOT=BASE.parents[1]
sys.path.insert(0,str(ROOT))
from SAM_PROJECT.gen6_duck_t500.resources import own_cpus
from SAM_PROJECT.gen6_duck_t500 import WORKER_CPUS,COORDINATOR_CPU
RUN=ROOT/'GEN4/duck_gen6_local/runs/chapter2-physical-protocols-20261015-01'
PLUGIN=Path('/home/lilhelper/.codex/plugins/cache/duck-integration-test/gen6-duck/0.1.0/scripts/duck_host.py')
def main():
 log=[];deadline=time.monotonic()+1800
 while time.monotonic()<deadline:
  if (RUN/'COMPLETE.json').exists():print('Already complete');return
  try:
   with own_cpus(tuple(WORKER_CPUS)+(COORDINATOR_CPU,)):pass
  except BlockingIOError:
   log.append(dict(utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),status='WAIT_UNRELATED_CPU_LEASE'))
   (BASE/'ops/FINALIZATION_WAIT.json').write_text(json.dumps(log,indent=2)+'\n');time.sleep(20);continue
  cmd=[sys.executable,str(PLUGIN),'invoke','duck-gen6-local','finalize','--run',str(RUN),'--file',str(BASE/'ORGANIZATION.json')]
  p=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
  log.append(dict(utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),status='FINALIZE',returncode=p.returncode,stdout=p.stdout,stderr=p.stderr))
  (BASE/'ops/FINALIZATION_WAIT.json').write_text(json.dumps(log,indent=2)+'\n')
  if p.returncode==0:print(p.stdout);return
  print(p.stderr,file=sys.stderr);raise SystemExit(p.returncode)
 raise SystemExit('Final retention is still waiting for unrelated CPU leases; completed science is preserved.')
if __name__=='__main__':main()
