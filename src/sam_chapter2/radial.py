"""Chapter II §43: declared spherical shell receiver, not a locality proof."""
from dataclasses import dataclass
from fractions import Fraction
from ._exact import rational


def _outer_index(value):
    if isinstance(value, bool) or not isinstance(value, int) or value < 2:
        raise ValueError("outer_index L must be an integer at least 2")
    return value


def radial_green(outer_index):
    """H_ij=1/max(i,j)-1/L on retained shells i,j=1,...,L-1."""
    L = _outer_index(outer_index)
    return tuple(tuple(Fraction(1, max(i, j))-Fraction(1, L)
                       for j in range(1, L)) for i in range(1, L))


def radial_dirichlet_operator(outer_index):
    """K=B^T C B with c_i=i(i+1), zero outer lift and zero central flux."""
    L = _outer_index(outer_index)
    return tuple(tuple(Fraction((i-1)*i+i*(i+1)) if i == j
                       else Fraction(-min(i, j)*(min(i, j)+1)) if abs(i-j) == 1
                       else Fraction(0) for j in range(1, L)) for i in range(1, L))


@dataclass(frozen=True)
class RadialSolution:
    masses: tuple
    kappa: Fraction
    lift: tuple
    flux: tuple
    infinity_shift: Fraction
    reduced_binding: Fraction

    @property
    def isolated_lift(self):
        return tuple(a+self.infinity_shift for a in self.lift)


def radial_shell_solution(masses, kappa):
    """Solve a=H*kappa*m and retain all edge fluxes, including the boundary.

    m is in one declared mass unit. kappa=2G*M_unit/(c²*h). The returned
    reduced_binding is U_L/(G*M_unit²/h), namely -m^T H m/2; it is not the
    complete source energy. Positive shell masses and kappa are required.
    """
    masses = tuple(rational(x) for x in masses)
    scale = rational(kappa)
    if not masses or any(m < 0 for m in masses) or scale <= 0:
        raise ValueError("nonempty nonnegative masses and positive kappa required")
    L = len(masses)+1
    h = radial_green(L)
    reduced = tuple(sum((row[j]*masses[j] for j in range(L-1)), Fraction(0))
                    for row in h)
    a = tuple(scale*x for x in reduced)
    with_boundary = a+(Fraction(0),)
    flux = tuple(Fraction(i*(i+1))*(with_boundary[i-1]-with_boundary[i])
                 for i in range(1, L))
    return RadialSolution(masses, scale, a, flux,
                          scale*sum(masses)/L,
                          -sum((m*u for m, u in zip(masses, reduced)), Fraction(0))/2)
