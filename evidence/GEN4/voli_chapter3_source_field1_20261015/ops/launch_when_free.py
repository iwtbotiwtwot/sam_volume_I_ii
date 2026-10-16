"""Launch the already prepared authorized run once unrelated CPU leases release."""
from pathlib import Path
import json,subprocess,time,sys
BASE=Path(__file__).resolve().parents[1];ROOT=BASE.parents[1]
sys.path.insert(0,str(ROOT))
from SAM_PROJECT.gen6_duck_t500.resources import own_cpus
from SAM_PROJECT.gen6_duck_t500 import WORKER_CPUS,COORDINATOR_CPU
RUN=ROOT/'GEN4/duck_gen6_local/runs/chapter3-source-field-20261015-02'
PLUGIN='/home/lilhelper/.codex/plugins/cache/duck-integration-test/gen6-duck/0.1.0/scripts/duck_host.py'
rows=[]
for attempt in range(120):
 if (RUN/'LAUNCH.json').exists(): print('Launch receipt already exists; no restart');break
 try:
  with own_cpus(tuple(WORKER_CPUS)+(COORDINATOR_CPU,)):pass
 except BlockingIOError:
  rows.append(dict(utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),status='WAIT_UNRELATED_CPU_LEASE'))
  (BASE/'ops/LAUNCH_WAIT.json').write_text(json.dumps(rows,indent=2)+'\n');time.sleep(20);continue
 p=subprocess.run([sys.executable,PLUGIN,'invoke','duck-gen6-local','deploy','--run',str(RUN)],capture_output=True,text=True,cwd=ROOT)
 rows.append(dict(utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),status='DEPLOY_ATTEMPT',returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));(BASE/'ops/LAUNCH_WAIT.json').write_text(json.dumps(rows,indent=2)+'\n')
 print(p.stdout,p.stderr);raise SystemExit(p.returncode)
else:raise SystemExit('Research services still hold CPU leases; prepared run unlaunched')
