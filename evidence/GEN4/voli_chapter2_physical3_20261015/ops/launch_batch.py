"""Launch the authorized full-source batch within an existing bounded leaf."""
from pathlib import Path
import argparse,json,subprocess,sys
BASE=Path(__file__).resolve().parents[1];ROOT=BASE.parents[1];sys.path.insert(0,str(ROOT))
from SAM_PROJECT.gen6_duck_t500.resources import environment
p=argparse.ArgumentParser();p.add_argument('--attempt',required=True);p.add_argument('--power',type=int,default=4);p.add_argument('--precision',type=int,default=1024);p.add_argument('--profile');a=p.parse_args()
run=BASE/'closure'/('managed_'+a.attempt);run.mkdir(exist_ok=False);mem=3221225472;env,budget=environment(run,[6],mem)
cmd=['systemd-run','--user','--wait','--pipe','--collect','--quiet','--unit','sam-r3-chapter2-closure-'+a.attempt,'--slice','sam-r3.slice','--working-directory',str(ROOT),
 '--property=Type=exec','--property=KillMode=control-group','--property=AllowedCPUs=6','--property=CPUAffinity=6','--property=CPUQuota=100%',
 '--property=MemoryMax='+str(mem),'--property=MemoryHigh='+str(mem*9//10),'--property=MemorySwapMax=0','--property=TasksMax=32','--property=RuntimeMaxSec=1200']
for k in ['SAM_R3_RUN_ID','SAM_R3_BUDGET','SAM_R3_ALLOWED_CPUS','SAM_R3_CPU_ORDER','SAM_R3_WORKERS','PYTHONDONTWRITEBYTECODE','PYTHONUNBUFFERED']:cmd+=['--setenv='+k+'='+env[k]]
cmd+=['--',str(ROOT/'.venv-r3/bin/python'),'-B',str(BASE/'ops/source_batch.py'),'--attempt',a.attempt,'--power',str(a.power),'--precision',str(a.precision)]
if a.profile:cmd+=['--profile',a.profile]
(run/'COMMAND.json').write_text(json.dumps(dict(command=cmd,budget=budget),indent=2)+'\n')
r=subprocess.run(cmd,capture_output=True,text=True);(run/'stdout.log').write_text(r.stdout);(run/'stderr.log').write_text(r.stderr);(run/'SERVICE_RESULT.json').write_text(json.dumps(dict(returncode=r.returncode))+'\n');print(r.stdout);print(r.stderr,file=sys.stderr);raise SystemExit(r.returncode)
