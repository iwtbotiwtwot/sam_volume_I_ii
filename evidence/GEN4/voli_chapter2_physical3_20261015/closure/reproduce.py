#!/usr/bin/env python3
"""Offline actual-source closure verification; standard library only.

Never imports the native generator evaluator or starts a scientific worker.
"""
from pathlib import Path
import json,subprocess,sys
HERE=Path(__file__).resolve().parent
for name,args in [('verify_source_law.py',[]),('exact_lumped_upper_bound.py',[]),('verify_cache_semantics.py',[]),('finalize_closure.py',['--require54'])]:
 subprocess.run([sys.executable,str(HERE/name),*args],check=True)
cache=json.loads((HERE/'CACHE_SEMANTICS_VERIFICATION.json').read_text());law=json.loads((HERE/'SOURCE_LAW_VERIFICATION.json').read_text());rank=json.loads((HERE/'FINAL_CLOSURE.json').read_text())
out=dict(status='PASS',source_preparations=54,independent_exact_source_law_checks=law['independent_exact_rational_checks'],
 independent_point_certificate_checks=rank['independent_point_certificate_checks'],
 exact_integer_lumped_inventory_checks=54,independent_cache_policy_overlap_checks=cache['independent_exact_interval_overlap_checks'],native_calls=0,source_integrals=0,
 meaning='Replays physical Gibbs energy-difference identities, retained point-minor rank certificates and exact invariant upper-bound combinatorics')
(HERE/'REPRODUCTION.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
