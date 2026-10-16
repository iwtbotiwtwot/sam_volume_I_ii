#!/usr/bin/env python3
"""Exact correlated-phase consequences of retained six-lane clock bounds.

Writes only CORRELATED_PHASE_RESULTS.json. It never changes RESULTS.json,
submits a native job, or assigns a physical external coupling or time unit.
"""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
import hashlib,json
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def interval(row):return F(row['lower']),F(row['upper'])
def shown(value,rounding,scale=F(1)):
    value*=scale
    with localcontext() as c:
        c.prec=100
        return str((Decimal(value.numerator)/Decimal(value.denominator)).quantize(Decimal('0.000000001'),rounding=rounding))
def encoded_interval(pair):return {'lower':str(pair[0]),'upper':str(pair[1])}


def main():
    protected=HERE/'RESULTS.json';protected_sha=sha(protected)
    retained=json.loads((HERE/'chapter1_certificate.json').read_text())
    previous=json.loads(protected.read_text())
    binding=json.loads((HERE/'SOURCE_BINDINGS.json').read_text())
    checks=[]
    def ok(name,test):
        if not test:raise AssertionError(name)
        checks.append(name)
    for row in binding['frozen_inputs']:
        ok('retained Chapter I input '+row['path'],sha(HERE/row['path'])==row['sha256'])
    premises=BASE/'inputs/CR004_declared_premises.json'
    core=json.loads((BASE/'core/RESULTS.json').read_text())
    ok('frozen physical-anchor input binding',sha(premises)==core['source_sha256'])
    p=json.loads(premises.read_text(),parse_float=str,parse_int=str)
    earth=next(row for row in p['bodies'] if row['name']=='Earth')
    mu=F(earth['mu_m3_s2']);radius=F(earth['radius_m']);c=F(p['constants']['c'])
    a=2*mu/(c*c*radius)
    ok('Earth supplied positive weak lift',0<a<1)
    delta=(a/2,a/(2-a))
    n_lower,n_upper=1-delta[1],1-delta[0]
    ok('positive rational square-root enclosure',0<n_lower<n_upper<1)
    ok('lower square-root endpoint valid',n_lower*n_lower<1-a)
    ok('upper square-root endpoint valid',(1-a)<n_upper*n_upper)
    # Algebraic square margins establish the rational bounds without evaluating sqrt.
    ok('lower root margin exact',1-a-n_lower*n_lower==a*a*(1-a)/(2-a)**2)
    ok('upper root margin exact',n_upper*n_upper-(1-a)==a*a/4)
    ok('delta bounds positive',0<delta[0]<delta[1]<1)
    output=[]
    by_pair={tuple(x['pair']):x for x in previous['lanes']}
    for row in retained['lanes']:
        pair=tuple(row['pair']);label=''.join(map(str,pair))
        ell,u=interval(row['certificate']['actual_uniform_rate'])
        ok(label+' actual native-derived rate binding',(ell,u)==interval(by_pair[pair]['actual_rate_enclosure']))
        ok(label+' positive full-field rate',0<ell<=u)
        per_time=(-u*delta[1],-ell*delta[0])
        ok(label+' strictly negative correlated shift',per_time[0]<per_time[1]<0)
        Tlo,Thi=interval(row['clock']['time_CYCLE'])
        ok(label+' original positive bare-cycle interval',0<Tlo<Thi)
        cycle=(per_time[0]*Thi,per_time[1]*Tlo)
        ok(label+' bare-cycle phase interval negative',cycle[0]<cycle[1]<0)
        independent_threshold=F(by_pair[pair]['full_scaling_sufficient_lift_for_disjoint_phase_bands'])
        ok(label+' Earth below independent-band threshold',a<independent_threshold)
        output.append({'pair':list(pair),'actual_rate':encoded_interval((ell,u)),
            'phase_shift_per_model_time':encoded_interval(per_time),
            'phase_shift_per_model_time_times_1e15':{
                'lower':shown(per_time[0],ROUND_FLOOR,F(10**15)),
                'upper':shown(per_time[1],ROUND_CEILING,F(10**15))},
            'original_bare_cycle_time':encoded_interval((Tlo,Thi)),
            'phase_shift_over_original_bare_cycle':encoded_interval(cycle),
            'bare_cycle_shift_nanoradians':{'lower':shown(cycle[0],ROUND_FLOOR,F(10**9)),
                                            'upper':shown(cycle[1],ROUND_CEILING,F(10**9))},
            'independent_band_threshold':str(independent_threshold),
            'correlated_sign':'STRICTLY_NEGATIVE_UNDER_DECLARED_FULL_H_SCALING'})
    ok('all original six preparations retained',len(output)==6)
    ok('protected native-R2 RESULTS unchanged',sha(protected)==protected_sha)
    result={'schema':'SAM_CORRELATED_ACTUAL_CLOCK_PHASE_BOUND_V1','status':'PASS',
        'checks_passed':len(checks),'checks':checks,
        'earth_input':{'mu_m3_s2':str(mu),'radius_m':str(radius),'c_m_s':str(c),'a_exact':str(a),
                       'a_display':format(float(a),'.17g')},
        'one_minus_sqrt_one_minus_a':encoded_interval(delta),'lanes':output,
        'source_sha256':{'chapter1_certificate.json':sha(HERE/'chapter1_certificate.json'),
                         'RESULTS.json':protected_sha,
                         'inputs/CR004_declared_premises.json':sha(premises),
                         'core/RESULTS.json':sha(BASE/'core/RESULTS.json')},
        'native_executions':0,'network_requests':0,
        'proof':'A shared monotone baseline gives theta_a(T)-theta_0(T)=-integral_(nT)^T nu_0(s)ds; use the retained positive ell,u on that one path. Root endpoint squares give exact rational delta bounds.',
        'conditions':['Static full-H coupling H(a)=n(a)H0+f(a)I is supplied, not derived',
                      'Same original preparation and phase branch for the scaled and baseline evolutions',
                      '0<a<1, 0<T<=the retained baseline window; nT lies in that same window',
                      'Actual amplitude certificate and unwrapped phase are retained; fresh-copy readout has separate errors and cost',
                      'SI time and material external-coupling assignments remain unassigned'],
        'scope':'Exact conditional sign and phase enclosure from correlated original source bounds; independent-band nonoverlap is not a mathematical sign limit; no achieved apparatus sensitivity is asserted.'}
    (HERE/'CORRELATED_PHASE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','checks':len(checks),'lanes':6,'Earth_a':str(a),
                     'lane01_cycle_nanoradians':output[0]['bare_cycle_shift_nanoradians'],
                     'protected_RESULTS_sha256':protected_sha,'native_executions':0}))


if __name__=='__main__':main()
