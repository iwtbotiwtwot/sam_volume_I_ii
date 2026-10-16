"""Chapter II §§47–48: correlated phase under declared complete-H scaling."""
from ._exact import Interval, rational


def correlated_phase_bounds(lower_rate, upper_rate, lift, elapsed):
    """Enclose theta_0(sqrt(1-a)*T)-theta_0(T) with exact rationals.

    Requires one common preparation, continuously unwrapped branch, full-H
    scaling, and certified ell<=nu<=u on the entire relevant source window.
    This function does not establish the coupling or apparatus sensitivity.
    """
    ell, u, a, t = map(rational, (lower_rate, upper_rate, lift, elapsed))
    if not 0 < ell <= u or not 0 <= a < 1 or t < 0:
        raise ValueError("require 0<ell<=u, 0<=lift<1, elapsed>=0")
    return Interval(-u*a*t/(2-a), -ell*a*t/2)


def independent_band_threshold(lower_rate, upper_rate):
    """Strict nonoverlap requires lift > this value; not a correlated-sign limit."""
    ell, u = rational(lower_rate), rational(upper_rate)
    if not 0 < ell <= u:
        raise ValueError("require 0<ell<=u")
    return 1-(ell/u)**2


def actual_clock_phase(lower_rate, upper_rate, elapsed):
    """Rate enclosure times nonnegative elapsed interval, starting theta=0."""
    from ._exact import as_interval
    ell, u = rational(lower_rate), rational(upper_rate)
    t = as_interval(elapsed)
    if not 0 < ell <= u or t.lower < 0:
        raise ValueError("positive ordered rates and nonnegative elapsed required")
    return Interval(ell, u)*t
