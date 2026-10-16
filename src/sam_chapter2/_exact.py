"""Small exact rational helpers; no floating-point inputs are accepted."""
from dataclasses import dataclass
from fractions import Fraction


def rational(value):
    """Accept integers, Fraction instances and exact rational/decimal strings."""
    if isinstance(value, bool) or not isinstance(value, (int, Fraction, str)):
        raise TypeError("use int, Fraction, or an exact string, not float/bool")
    return Fraction(value)


@dataclass(frozen=True)
class Interval:
    """Closed rational enclosure; arithmetic is exact but may over-enclose."""
    lower: Fraction
    upper: Fraction

    def __post_init__(self):
        object.__setattr__(self, "lower", rational(self.lower))
        object.__setattr__(self, "upper", rational(self.upper))
        if self.lower > self.upper:
            raise ValueError("interval endpoints are reversed")

    @classmethod
    def point(cls, value):
        return cls(rational(value), rational(value))

    def __add__(self, other):
        other = as_interval(other)
        return Interval(self.lower + other.lower, self.upper + other.upper)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.upper, -self.lower)

    def __sub__(self, other):
        return self + -as_interval(other)

    def __rsub__(self, other):
        return as_interval(other) + -self

    def __mul__(self, other):
        other = as_interval(other)
        products = tuple(a*b for a in (self.lower, self.upper)
                         for b in (other.lower, other.upper))
        return Interval(min(products), max(products))

    __rmul__ = __mul__

    def contains(self, value):
        value = rational(value)
        return self.lower <= value <= self.upper


def as_interval(value):
    return value if isinstance(value, Interval) else Interval.point(value)


def matrix(rows):
    result = tuple(tuple(rational(x) for x in row) for row in rows)
    if not result or not result[0] or any(len(r) != len(result[0]) for r in result):
        raise ValueError("matrix must be nonempty and rectangular")
    return result


def square_symmetric(rows):
    a = matrix(rows)
    if len(a) != len(a[0]) or any(a[i][j] != a[j][i]
                                for i in range(len(a)) for j in range(len(a))):
        raise ValueError("matrix must be square and symmetric")
    return a


def multiply(a, b):
    if len(a[0]) != len(b):
        raise ValueError("incompatible matrix dimensions")
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))), Fraction(0))
                       for j in range(len(b[0]))) for i in range(len(a)))


def inverse(a):
    n = len(a)
    work = [list(row) + [Fraction(i == j) for j in range(n)]
            for i, row in enumerate(a)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if work[i][j]), None)
        if pivot is None:
            raise ValueError("singular matrix")
        work[j], work[pivot] = work[pivot], work[j]
        scale = work[j][j]
        work[j] = [x/scale for x in work[j]]
        for i in range(n):
            if i != j:
                scale = work[i][j]
                work[i] = [x-scale*y for x, y in zip(work[i], work[j])]
    return tuple(tuple(row[n:]) for row in work)


def psd_rank(a, *, positive_definite=False):
    """Exact symmetric Schur elimination; rejects indefinite moment data."""
    work = [list(row) for row in a]
    rank = 0
    for k in range(len(a)):
        pivot = work[k][k]
        if pivot < 0 or (not pivot and any(work[k][j] for j in range(k+1, len(a)))):
            raise ValueError("matrix is not positive semidefinite")
        if not pivot:
            if positive_definite:
                raise ValueError("Gram matrix must be positive definite")
            continue
        rank += 1
        for i in range(k+1, len(a)):
            for j in range(i, len(a)):
                work[i][j] -= work[i][k]*work[k][j]/pivot
                work[j][i] = work[i][j]
    return rank
