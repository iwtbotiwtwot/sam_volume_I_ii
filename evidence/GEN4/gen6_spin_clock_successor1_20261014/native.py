"""Source-local certified original signed-stroke integrals and native clock map."""
from fractions import Fraction as F
from flint import acb, arb, ctx
from CURRENT_REVISION.engines.SLC.gen3 import retained

OPERATION = 'GEN6_ORIGINAL_STROKE_INTEGRAL_V1'


def wire(x):
    return {'lower': str(x.lower().fmpq()), 'upper': str(x.upper().fmpq())}


def bounds(x):
    if isinstance(x, dict) and 're' in x:
        x = x['re']
    if isinstance(x, dict):
        return F(x['lower']), F(x['upper'])
    return F(x), F(x)


def integrate(payload):
    ctx.prec = 384
    ctx.threads = 1
    state = payload['state']
    event = payload['event']
    orientation = payload['orientation']
    assert len(state) == 3 and all(type(x) is int and x in range(4) for x in state)
    assert event in ['W'+str(j)+s for j in [1, 4, 7] for s in ['+', '-']]
    assert orientation in [-1, 1]
    assert orientation == (1 if event.endswith('+') else -1)
    role = int(event[1:-1])
    ka = 1 if role == 1 else -1 if role == 7 else 0
    kb = 1 if role == 4 else -1 if role == 7 else 0
    ia, ib = (state[0]-state[2]) % 4, (state[1]-state[2]) % 4
    cos0, sin0 = [1, 0, -1, 0], [0, 1, 0, -1]
    counts = {'angle': 0, 'half_angle': 0}

    def density(ca, sa, cb, sb, analytic):
        E = 6-2*ca+2*cb
        g = 2*sa if role == 1 else -2*sb if role == 4 else -2*sa+2*sb
        return 12*(E*E+g*g).sqrt(analytic=analytic)/(E*E+36)

    def angle(z, analytic):
        counts['angle'] += 1
        a = ia*arb.pi()/2+ka*orientation*z
        b = ib*arb.pi()/2+kb*orientation*z
        return density(a.cos(), a.sin(), b.cos(), b.sin(), analytic)

    def half_angle(t, analytic):
        counts['half_angle'] += 1
        den = 1+t*t
        c, s = (1-t*t)/den, 2*t/den
        def relative(i, k):
            if k == 0:
                return acb(cos0[i]), acb(sin0[i])
            signed = k*orientation
            return cos0[i]*c-sin0[i]*signed*s, sin0[i]*c+cos0[i]*signed*s
        ca, sa = relative(ia, ka)
        cb, sb = relative(ib, kb)
        return density(ca, sa, cb, sb, analytic)*2/den

    options = dict(abs_tol=arb('1e-70'), rel_tol=arb('1e-70'), eval_limit=20000, depth_limit=40)
    first = acb.integral(half_angle, 0, 1, **options)
    second = acb.integral(angle, 0, arb.pi()/2, **options)
    assert first.is_finite() and second.is_finite()
    assert first.imag.contains(0) and second.imag.contains(0)
    assert first.real > 0 and second.real > 0
    assert first.real.overlaps(second.real)
    assert first.real.rad() < arb('1e-60') and second.real.rad() < arb('1e-60')
    constant = payload['clock_path'] == 'CONSTANT_D1_PARTNER_QUARTER'
    if constant:
        assert first.real.overlaps(arb.pi()/2)
    return dict(status='CERTIFIED_SOURCE_STROKE_INTEGRAL', integral=wire(first.real),
        angle_integral=wire(second.real), coordinate_crosscheck=True, state=state,
        event=event, orientation=orientation, clock_path=payload['clock_path'],
        constant_quarter_check=constant, precision_bits=384, evaluation_counts=counts,
        scope='Same original completed signed Write and AN0005 density; analytic sqrt flag forwarded')


def install(session, binding):
    base = session.consumer
    machine = base.ce.runtime_for('MATTER_SEARCH').machine
    class Adapter:
        def __getattr__(self, name):
            return getattr(base, name)
        def execute(self, operation, payload):
            if operation != OPERATION:
                return base.execute(operation, payload)
            if payload['source_binding'] != binding:
                raise ValueError('Source-bound integral payload identity differs')
            out = integrate(payload)
            ref = retained.put(machine, 'mathematical_result', out, payload,
                {'origin': operation, 'source_binding': binding}, sorted(retained.nested_refs(out)))
            return dict(result_ref=ref, output=out)
    session.consumer = Adapter()


def refine(session, specification, binding, save_call):
    ep = specification['event_parameters']
    events = session.execute('GEN3_EXECUTE', dict(initial=ep['initial'], program=ep['program'], source_binding=binding),
        purpose='Recover actual original signed Write states and clock-path types for all source strokes')
    save_call('native_events', events)
    assert events['program'] == ep['program'] and events['motion']['complete']
    assert events['schema'] == 'SLC_GEN2_FORWARD_V1'
    local_events = events['motion']['write_foundation']['local_sources'][0]['events']
    cal = specification['calibration']
    scalar = lambda values: dict(entries=values, row_basis=['scalar'], column_basis=['scalar'], structure='GENERAL')
    count = 0

    def call(name, operation, data, status):
        nonlocal count
        count += 1
        answer = session.execute(operation, dict(source_binding=binding, precision_bits=192, data=data),
            purpose='Apply unchanged original source clock mapping: '+name)
        save_call(name, answer)
        assert answer['result']['output']['status'] == status
        return answer['result']['output']['matrix']['entries'][0][0]

    def multiply(name, a, b):
        return call(name, 'GEN3_COMPLEX_PRODUCT', dict(matrix=scalar([[a]]), right=scalar([[b]])), 'CERTIFIED_ENCLOSURE')

    def add(name, a, b, sign='1'):
        left = dict(entries=[['1', sign]], row_basis=['scalar'], column_basis=['first','second'], structure='GENERAL')
        right = dict(entries=[[a],[b]], row_basis=['first','second'], column_basis=['scalar'], structure='GENERAL')
        return call(name, 'GEN3_COMPLEX_PRODUCT', dict(matrix=left, right=right), 'CERTIFIED_ENCLOSURE')

    def divide(name, a, b):
        return call(name, 'GEN3_COMPLEX_SOLVE', dict(matrix=scalar([[b]]), rhs=scalar([[a]])), 'CERTIFIED_SOLVE')

    available = add('available_fraction', '1', cal['A_los'], '-1')
    assert bounds(available)[0] > 0
    radius_over_c = divide('radius_over_c', cal['radius'], cal['c'])
    scale = divide('stroke_scale', radius_over_c, available)
    rows = []
    for i, event in enumerate(ep['program']):
        source = dict(state=events['states'][i], event=event,
            orientation=local_events[i]['orientation'], clock_path=local_events[i]['clock_path'], source_binding=binding)
        answer = session.execute(OPERATION, source,
            purpose='Refine the entire original signed continuous density stroke '+str(i)+' '+event)
        save_call('integral_'+str(i), answer)
        value = answer['output']['integral']
        stroke = multiply('stroke_time_'+str(i), scale, value)
        total = add('with_wait_'+str(i), stroke, specification['waiting_gaps'][i])
        elapsed = multiply('elapsed_'+str(i), cal['clock_to_elapsed_scale'], total)
        assert bounds(elapsed)[0] > 0
        rows.append(dict(occurrence=i, event=event, state=source['state'], orientation=source['orientation'],
            clock_path=source['clock_path'], integral=value, angle_integral=answer['output']['angle_integral'],
            integral_result_ref=answer['result_ref'], stroke_time=stroke, waiting_gap=specification['waiting_gaps'][i],
            elapsed=elapsed, native_source_record=local_events[i]))
    return dict(schema='GEN6_SIGNED_SOURCE_CLOCK_REFINEMENT_V1', rows=rows, calibration=cal,
        source_initial=ep['initial'], source_program=ep['program'], source_native_states=events['states'],
        receiver_precision_bits=192, integration_precision_bits=384, scalar_native_calls=count,
        source_evaluation='All original signed strokes; no fitting or coefficient changes')
