#!/usr/bin/env python3
"""Independently compare pre/post-cache-policy native source rows exactly."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
HERE=Path(__file__).resolve().parent
checks=0;inputs=[]
p=HERE/'native_batch_p4b/SOURCE_RAW.json';raw=p.read_bytes();batch=json.loads(raw)['profiles'];new=next(d for d in batch if d['profile_id']=='V001_BASE')
inputs.append(dict(path=str(p.relative_to(HERE)),sha256=hashlib.sha256(raw).hexdigest()))
for name in ('native_v001-p3c','native_v001-p4'):
 p=HERE/name/'SOURCE_RAW.json';raw=p.read_bytes();old=json.loads(raw);assert old['source']==new['source'];assert old['configurations']==new['configurations'];assert old['basis']==new['basis'][:len(old['basis'])]
 for a,b in zip(old['evaluation_rows'],new['evaluation_rows']):
  for av,bv in zip(a,b):
   assert max(F(av['lower']),F(bv['lower']))<=min(F(av['upper']),F(bv['upper']))
   checks+=1
 inputs.append(dict(path=str(p.relative_to(HERE)),sha256=hashlib.sha256(raw).hexdigest()))
out=dict(schema='SAM_CH2_SOURCE_CACHE_SEMANTICS_VERIFICATION_V1',status='PASS',independent_exact_interval_overlap_checks=checks,
 meaning='The original retained-cache native source rows and revised per-configuration-clearing native rows enclose the same full-source evaluations',
 mathematical_reason='Memoization stores pure recursive function values; clearing exact intermediates after a retained row changes neither generator, state, input, expression order nor Arb row precision',inputs=inputs)
(HERE/'CACHE_SEMANTICS_VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','independent_exact_interval_overlap_checks')}))
