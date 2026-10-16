"""Chapter II §§28–32: independent-shot budgets and difference-Hankel tests."""
from dataclasses import dataclass
from fractions import Fraction
from ._exact import rational, matrix


def _positive_integer(value, name):
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(name+" must be a positive integer")
    return value


def _log_unit_interval(x, terms):
    """Exact positive atanh-series enclosure for log(x), 1<=x<=2."""
    z = (x-1)/(x+1)
    power, total = z, Fraction(0)
    for k in range(terms):
        total += power/(2*k+1)
        power *= z*z
    lower = 2*total
    remainder = 2*power/((2*terms+1)*(1-z*z))
    return lower, lower+remainder


def log_bounds(value, terms=32):
    """Certified rational lower/upper bounds for log(value>=1)."""
    x = rational(value)
    _positive_integer(terms, "terms")
    if x < 1:
        raise ValueError("log argument must be at least 1")
    shifts = 0
    while x >= 2:
        x /= 2
        shifts += 1
    lo, hi = _log_unit_interval(x, terms)
    lo2, hi2 = _log_unit_interval(Fraction(2), terms)
    return lo+shifts*lo2, hi+shifts*hi2


def _ceil(value):
    return -(-value.numerator//value.denominator)


@dataclass(frozen=True)
class SamplingPlan:
    means: int
    shots_per_mean: int
    statistical_tolerance: Fraction
    failure_allowance: Fraction
    outcome_radius_squared: Fraction

    def __post_init__(self):
        _positive_integer(self.means, "means")
        _positive_integer(self.shots_per_mean, "shots_per_mean")
        for name in ("statistical_tolerance", "failure_allowance", "outcome_radius_squared"):
            object.__setattr__(self, name, rational(getattr(self, name)))
        if (self.statistical_tolerance <= 0 or self.outcome_radius_squared <= 0
                or not 0 < self.failure_allowance < 1):
            raise ValueError("positive tolerance/radius² and 0<failure<1 required")

    @property
    def total_fresh_preparations(self):
        return self.means*self.shots_per_mean

    @property
    def sufficient(self):
        """Check 2m exp[-N*s²/(2R²)] <= delta using exact log bounds."""
        exponent = (self.shots_per_mean*self.statistical_tolerance**2
                    /(2*self.outcome_radius_squared))
        return exponent >= log_bounds(2*self.means/self.failure_allowance, 64)[1]


def shot_count(means, statistical_tolerance, failure_allowance,
               *, outcome_radius_squared=1):
    """Return the least Hoeffding/union-bound sufficient integer per mean.

    Outcomes must lie in [-R,R], shots must be independent, and all systematic
    errors need separate allowances. Pauli coordinates use R²=1; the protected
    Chapter II coherence receiver uses R²=2. No single trajectory is sampled
    repeatedly without disturbance. The logarithm/ceiling uses exact bounds.
    """
    m = _positive_integer(means, "means")
    s, delta, r2 = map(rational, (statistical_tolerance, failure_allowance,
                                outcome_radius_squared))
    if s <= 0 or not 0 < delta < 1 or r2 <= 0:
        raise ValueError("positive tolerance/radius² and 0<failure<1 required")
    factor = 2*r2/s**2
    for terms in (8, 16, 32, 64, 128, 256):
        lo, hi = log_bounds(2*m/delta, terms)
        lower_count, upper_count = _ceil(factor*lo), _ceil(factor*hi)
        if lower_count == upper_count:
            return SamplingPlan(m, upper_count, s, delta, r2)
    raise ArithmeticError("log enclosure has not resolved the integer ceiling")


def difference_hankel(means, size=4):
    """H_ij=y_(i+j+1)-y_(i+j); size4 requires eight expectation values."""
    n = _positive_integer(size, "size")
    values = tuple(rational(x) for x in means)
    if len(values) < 2*n:
        raise ValueError("at least 2*size expectation values required")
    differences = tuple(b-a for a, b in zip(values, values[1:]))
    return tuple(tuple(differences[i+j] for j in range(n)) for i in range(n))


def determinant3(rows):
    a = matrix(rows)
    if len(a) != 3 or len(a[0]) != 3:
        raise ValueError("a three-by-three matrix is required")
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def difference_minor(means, indices=(0, 2, 3)):
    """Selected source-guided difference minor; returns its exact determinant."""
    idx = tuple(indices)
    if (len(idx) != 3 or len(set(idx)) != 3
            or any(isinstance(i, bool) or not isinstance(i, int) or i < 0 for i in idx)):
        raise ValueError("three distinct nonnegative integer indices required")
    values = tuple(rational(x) for x in means)
    if len(values) < 2*max(idx)+2:
        raise ValueError("insufficient means for these indices")
    d = tuple(b-a for a, b in zip(values, values[1:]))
    return determinant3(tuple(tuple(d[i+j] for j in idx) for i in idx))


def determinant_rejection_threshold(per_mean_error, measured_entry_bound):
    """36*eta*(Bhat+2eta)^2; strict exceedance rejects the stated closed class."""
    eta, bound = rational(per_mean_error), rational(measured_entry_bound)
    if eta < 0 or bound < 0:
        raise ValueError("error and measured entry bound must be nonnegative")
    return 36*eta*(bound+2*eta)**2


def two_record_perturbation_bound(per_mean_error, ideal_entry_bound=2):
    """Chapter II source/measurement separation bound 72*eta*(B+4eta)^2."""
    eta, bound = rational(per_mean_error), rational(ideal_entry_bound)
    if eta < 0 or bound < 0:
        raise ValueError("error and ideal entry bound must be nonnegative")
    return 72*eta*(bound+4*eta)**2
