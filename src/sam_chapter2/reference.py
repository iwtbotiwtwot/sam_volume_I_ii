"""Chapter II §§24–28: ideal externally driven balanced-reference account.

All inputs are certified rational enclosures supplied by the retained source
packet. The source's nonrational path integral is not recomputed here. Model
time is in t_u; energies and work are in hbar/t_u; phases are in radians.
"""
from dataclasses import dataclass
from fractions import Fraction
import math
from ._exact import Interval, as_interval, rational


@dataclass(frozen=True)
class ReferenceEvent:
    name: str
    source_time: Interval
    beta: Interval
    matching_interval_endpoint: bool


@dataclass(frozen=True)
class ReferenceInterval:
    name: str
    duration: Interval
    ledger_phase_change: Interval
    beta_change: Interval
    reference_energy: Interval
    ledger_matching: bool


@dataclass(frozen=True)
class WorkPiece:
    name: str
    work: Interval
    # Coefficients in the fixed basis (E, v_end, v_min, 1) preserve correlation.
    coefficients: tuple


@dataclass(frozen=True)
class PaidReferenceProtocol:
    events: tuple
    intervals: tuple
    work_pieces: tuple
    positive_work: Interval
    withdrawn_work: Interval
    net_signed_work: Fraction


def paid_reference_protocol(energy, traversal_duration, pi, endpoint_speed,
                            minimum_speed, *, wait=4, entry="1/100",
                            release="1/100"):
    """Assemble retained W1+, W1-, wait, and external linear entry/release.

    h_R=2(w-E)P on matching intervals. w=0 on the source wait, so the
    reference remains on with h_R=-2EP. Forward/reverse signed ledger phases
    are +/-pi/2. E must bound the full retained source-field form energy.
    The separately supplied pi enclosure must be a genuine enclosure of pi.

    This is the chapter's E<10, v_min<=10<=v_end work branch. Telescoping net
    drive work is not a calculation of apparatus dissipation or source work.
    """
    e, duration, p, vend, vmin = map(as_interval,
        (energy, traversal_duration, pi, endpoint_speed, minimum_speed))
    wait, entry, release = map(rational, (wait, entry, release))
    if not (0 < e.lower <= e.upper < 10 and duration.lower > 0
            and 3 < p.lower <= p.upper < 4
            and 0 < vmin.lower <= vmin.upper <= 10 <= vend.lower
            and wait >= 0 and entry > 0 and release > 0):
        raise ValueError("invalid energy, duration, pi, speed, or ramp enclosure")
    zero = Interval.point(0)
    time, beta = zero, zero
    events = [ReferenceEvent("external_entry_start", time, beta, False)]
    intervals = []

    def append(name, dt, ledger, dbeta, mean_energy, matching, endpoint):
        nonlocal time, beta
        dt = as_interval(dt)
        intervals.append(ReferenceInterval(name, dt, ledger, dbeta, mean_energy, matching))
        time, beta = time+dt, beta+dbeta
        events.append(ReferenceEvent(endpoint, time, beta, matching))

    append("external_entry", entry, zero, (10-e)*entry, Interval(0, 10-e.lower),
           False, "matching_start")
    append("forward_write", duration, p*Fraction(1, 2), p-2*e*duration,
           Interval(vmin.lower-e.upper, vend.upper-e.lower), True, "forward_complete")
    append("reverse_write", duration, -p*Fraction(1, 2), -p-2*e*duration,
           Interval(-vend.upper-e.upper, -vmin.lower-e.lower), True, "reverse_complete")
    # Re-evaluate this shared endpoint after cancelling +pi and -pi, rather
    # than adding independent copies of the same uncertain pi enclosure.
    beta = 10*entry-e*(entry+4*duration)
    events[-1] = ReferenceEvent("reverse_complete", time, beta, True)
    append("source_wait", wait, zero, -2*e*wait, -e,
           True, "wait_complete")
    append("external_release", release, zero, -e*release, Interval(-e.upper, 0),
           False, "external_release_complete")

    specs = (
        ("external entry", (-1, 0, 0, 10)),
        ("forward first monotone piece", (0, 0, 1, -10)),
        ("forward second monotone piece", (0, 1, -1, 0)),
        ("forward to reverse quench", (0, -2, 0, 0)),
        ("reverse first monotone piece", (0, 1, -1, 0)),
        ("reverse second monotone piece", (0, 0, 1, -10)),
        ("reverse to wait quench", (0, 0, 0, 10)),
        ("wait drive", (0, 0, 0, 0)),
        ("external release", (1, 0, 0, 0)),
    )
    basis = e, vend, vmin, Interval.point(1)
    pieces = tuple(WorkPiece(name, sum((c*b for c, b in zip(coeff, basis)), zero), coeff)
                   for name, coeff in specs)
    if any(sum(piece.coefficients[j] for piece in pieces) for j in range(4)):
        raise ArithmeticError("work coefficients did not telescope")
    gross = 2*vend+2*(10-vmin)
    return PaidReferenceProtocol(tuple(events), tuple(intervals), pieces,
                                 gross, gross, Fraction(0))


def unwrap_reference_phase(principal_phases, *, maximum_step):
    """Nearest-branch continuation anchored to the first supplied phase.

    Floating readout utility only, not a certified phase estimator. The caller
    must establish |true step|+2*angular_error < pi, include the initial branch,
    and use fresh prefixes. A principal endpoint alone cannot identify turns.
    """
    if isinstance(maximum_step, bool):
        raise ValueError("maximum_step must lie strictly between 0 and pi")
    step = float(maximum_step)
    if not math.isfinite(step) or not 0 < step < math.pi:
        raise ValueError("maximum_step must lie strictly between 0 and pi")
    values = tuple(float(x) for x in principal_phases)
    if not values or any(not math.isfinite(x) or not -math.pi <= x <= math.pi for x in values):
        raise ValueError("nonempty finite principal phases in [-pi,pi] required")
    result = [values[0]]
    for phase in values[1:]:
        delta = math.remainder(phase-result[-1], 2*math.pi)
        if abs(delta) > step:
            raise ValueError("observed phase increment exceeds the admitted branch budget")
        result.append(result[-1]+delta)
    return tuple(result)
