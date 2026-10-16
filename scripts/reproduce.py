#!/usr/bin/env python3
"""Replay compact source-bound Chapter II reference consequences offline.

The complete original evidence replay is the separate verify_native.py route.
These finite reference examples do not rerun a native engine or an experiment.
"""
from dataclasses import asdict, is_dataclass
from fractions import Fraction as F
from pathlib import Path
import csv
import hashlib
import json
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from sam_chapter2 import (Interval, radial_shell_solution, radial_green,
    residual_certificate, shot_count, SamplingPlan, correlated_phase_bounds,
    independent_band_threshold, difference_minor)

def encode(value):
    if isinstance(value,F):return str(value)
    if is_dataclass(value):return encode(asdict(value))
    if isinstance(value,dict):return {k:encode(v) for k,v in value.items()}
    if isinstance(value,(tuple,list)):return [encode(v) for v in value]
    return value

def main():
    checks=[]
    def require(label,condition):
        if not condition:raise ValueError(label)
        checks.append(label)
    bindings=json.loads((ROOT/'data/SOURCE_BINDINGS.json').read_text())
    for row in bindings['files']:
        compact=ROOT/row['path'];evidence=ROOT/row['evidence_path']
        for label,path in [('compact',compact),('frozen evidence',evidence)]:
            require(label+' '+row['path'],path.is_file() and path.stat().st_size==row['bytes']
                    and hashlib.sha256(path.read_bytes()).hexdigest()==row['sha256'])
    fixture=json.loads((ROOT/'data/radial_fixture.json').read_text())
    radial=radial_shell_solution(fixture['mass'],fixture['kappa'])
    require('same eight-shell source',len(radial.lift)==8)
    for i,a in enumerate(radial.lift):require('source lift '+str(i),a==F(fixture['expected_a'][i]))
    h=radial_green(fixture['L'])
    for i,row in enumerate(h):
        for j,x in enumerate(row):require('source Green '+str((i,j)),x==F(fixture['Green_H'][i][j]))
    for i,flux in enumerate(radial.flux,1):require('source flux '+str(i),flux==F(fixture['kappa'])*sum(map(F,fixture['mass'][:i])))
    require('finite-boundary binding',radial.reduced_binding==F(-9427,252000))
    require('isolated binding',radial.reduced_binding-F(1,18)==F(-2603,28000))
    protected=shot_count(8,'3/500','1/100',outcome_radius_squared=2)
    reference=SamplingPlan(882,26624,'1/32','1/100',1)
    require('protected per-mean count',protected.shots_per_mean==819751)
    require('eight independent means',protected.total_fresh_preparations==6558008)
    require('retained conservative reference budget',reference.sufficient and reference.total_fresh_preparations==23482368)
    minimum=shot_count(882,'1/32','1/100')
    require('exact ceiling for sufficient reference inequality',minimum.shots_per_mean==24741)
    cert=json.loads((ROOT/'data/clock_certificate.json').read_text())
    lift=F(199300220900,143149231093306629611)
    phases=[]
    for lane in cert['lanes']:
        rates=lane['certificate']['actual_uniform_rate'];time=lane['clock']['time_CYCLE']
        ell,u=F(rates['lower']),F(rates['upper'])
        lower=correlated_phase_bounds(ell,u,lift,F(time['upper'])).lower
        upper=correlated_phase_bounds(ell,u,lift,F(time['lower'])).upper
        require('signed original-lane phase '+str(lane['pair']),lower<=upper<0)
        phases.append(dict(lane=''.join(map(str,lane['pair'])),lower=lower,upper=upper,
            independent_band_lift_threshold=independent_band_threshold(ell,u)))
    # Explicit finite receiving illustration, not a spin-source replacement.
    memory=residual_certificate([[4,0],[0,9]],[[8,6],[6,27]],[[24,42],[42,126]])
    require('illustrative source-Gram rank',memory.rank==1)
    require('illustrative normalized memory',memory.memory_norm_upper==5)
    cosines=[F(1),F(3,5)]
    for _ in range(6):cosines.append(F(6,5)*cosines[-1]-cosines[-2])
    require('autonomous two-state control minor',difference_minor([F(2,7)+x/3 for x in cosines])==0)
    result=dict(schema='SAM_CHAPTER_II_REFERENCE_REPRODUCTION_V1',status='PASS',checks_passed=len(checks),checks=checks,
        radial=radial,protected_sampling=protected,reference_sampling=reference,
        reference_hoeffding_minimum=minimum,correlated_phase=phases,
        illustrative_gram_memory=memory,native_executions=0,network_requests=0,
        scope='Retained source consequences and explicitly identified finite controls; complete evidence replay is verify_native.py')
    out=ROOT/'build';out.mkdir(exist_ok=True)
    (out/'reproduction.json').write_text(json.dumps(encode(result),indent=2)+'\n')
    with (out/'phase_bounds.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(phases[0]));writer.writeheader();writer.writerows(encode(phases))
    print(json.dumps(dict(status='PASS',checks_passed=len(checks),source_lanes=len(phases),native_executions=0)))

if __name__=='__main__':
    try:main()
    except (OSError,ValueError,KeyError) as error:
        print(json.dumps(dict(status='FAIL',error=str(error))));raise SystemExit(1)
