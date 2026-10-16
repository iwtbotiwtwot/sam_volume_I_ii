"""Chapter II §§19–22: source-Gram residuals and conditional error bounds.

Matrices are real rational finite-source moments. This module does not compute
the enormous spin closure or substitute a small matrix for its original source.
"""
from dataclasses import dataclass
from fractions import Fraction
import math
from ._exact import rational, square_symmetric, inverse, multiply, psd_rank


@dataclass(frozen=True)
class MemoryCertificate:
    gram: tuple
    residual: tuple
    rank: int
    normalized_trace: Fraction

    @property
    def is_closed(self):
        """Exact closure iff L=0, conditional on supplied original moments."""
        return self.rank == 0

    @property
    def memory_norm_upper(self):
        """tr(G^-1 L) >= ||G^-1/2 L G^-1/2||; equality for rank <=1."""
        return self.normalized_trace

    def generalized_rayleigh(self, coordinates):
        v = tuple(rational(x) for x in coordinates)
        if len(v) != len(self.gram) or not any(v):
            raise ValueError("supply one nonzero vector in the retained basis")
        def form(a):
            return sum((v[i]*a[i][j]*v[j] for i in range(len(v))
                        for j in range(len(v))), Fraction(0))
        return form(self.residual)/form(self.gram)


def residual_certificate(gram, compressed, image_gram):
    """Return L=T-D G^-1 D from G=<b,b>, D=<b,Ab>, T=<Ab,Ab>.

    Source moments must share one inner product and one self-adjoint A.
    Necessary positivity is checked; provenance and an A-time spectral bound
    cannot be established from these three matrices alone.
    """
    g, d, t = map(square_symmetric, (gram, compressed, image_gram))
    if not len(g) == len(d) == len(t):
        raise ValueError("moment matrices must have equal dimensions")
    psd_rank(g, positive_definite=True)
    gi = inverse(g)
    projected = multiply(multiply(d, gi), d)
    residual = tuple(tuple(t[i][j]-projected[i][j] for j in range(len(g)))
                     for i in range(len(g)))
    rank = psd_rank(residual)
    gil = multiply(gi, residual)
    return MemoryCertificate(g, residual, rank,
                             sum((gil[i][i] for i in range(len(g))), Fraction(0)))


def quadratic_error_envelope(time, memory_norm_upper):
    """Exact t² K/2 bound, valid with the chapter's nonnegative A assumption."""
    t, k = rational(time), rational(memory_norm_upper)
    if t < 0 or k < 0:
        raise ValueError("time and memory-norm upper bound must be nonnegative")
    return t*t*k/2


def decaying_error_envelope(time, memory_norm_upper, lower_rate):
    """Floating evaluation of (t²/2) exp(-gamma*t) K; not outward rounding.

    Caller must establish A>=gamma I in the original invariant source sector.
    Physical seconds and expected attempts N*t are separate calibrations.
    """
    t, gamma = rational(time), rational(lower_rate)
    if gamma < 0:
        raise ValueError("lower spectral rate must be nonnegative")
    return float(quadratic_error_envelope(t, memory_norm_upper))*math.exp(-float(gamma*t))


def quadratic_remainder_bound(time, memory_norm_upper, upper_rate):
    """Exact N*t³*K/2, conditional on 0<=A<=N I in original A-time."""
    t, n = rational(time), rational(upper_rate)
    if n < 0:
        raise ValueError("upper spectral rate must be nonnegative")
    return quadratic_error_envelope(t, memory_norm_upper)*n*t
