# A worked Chapter I positive free-field source

## Source and scope

`CHAPTER_I_MODEL_SOURCE.md` is an exact snapshot of
`/home/lilhelper/sam_volume_I_i/docs/MODEL.md`; its identity and the section
used are retained in `FIELD_SOURCE_BINDINGS.json`. Section 4 gives

    L_f = (kappa/4) sum_alpha integral_0^infinity
              [r^2 dot(phi_alpha)^2-r^2 phi_alpha'^2-6 phi_alpha^2] dr,
    kappa=4/5,
    phi_alpha(r) = x_alpha r^2/R^3       (r<R),
                  x_alpha R^2/r^3       (r>R).

This example uses the static classical **positive free-field energy** of
that model. It angular-averages the radial energy into a spherical volume
density and conditionally supplies `rho=energy_density/c^2`. An angular
average is not the actual anisotropic local stress or a derivation of
three-dimensional isotropy. The full quantum interacting source, boundary
interaction and counterterms have not thereby been localized.

Write `X^2=sum_alpha x_alpha^2`. The two radial integrands are

    dU_f/dr = (5 kappa/2) X^2 r^4/R^6            (r<R),
              (15 kappa/4) X^2 R^4/r^6          (r>R).

Both derivative and angular terms are included. Integration gives

    U_inside = kappa X^2/(2R),
    U_outside = 3 kappa X^2/(4R),
    U_f = 5 kappa X^2/(4R) = X^2/R.

The energy fractions are exactly `2/5` inside and `3/5` outside. In model
units `U_f` has the Chapter I energy unit; an explicit conversion is needed
before `U_f/c^2` is an SI mass. In the following `M_f=U_f/c^2` denotes the
conditional mass after that common energy-unit conversion.

## Full source density, field and force

Dividing the radial energy by `4 pi r^2 c^2` gives the spherical average

    rho(r) = M_f r^2/(2 pi R^5)                  (r<R),
             3 M_f R^5/(4 pi r^8)               (r>R).

The density has a finite jump at `R`, with no assigned delta-function
surface energy in this free-field sector. Its integrated mass is

    M(<r) = (2/5) M_f (r/R)^5                   (r<=R),
            M_f [1-(3/5)(R/r)^5]                (r>=R).

For the chapter's isolated spherical receiving law,

    a(r) = (2G/c^2)[M(<r)/r + integral_r^infinity dM(s)/s].

Performing both the interior and exterior integrals yields

    a(r) = 2 G M_f/(c^2 R) [1-(1/10)(r/R)^4]   (r<=R),
           2 G M_f/(c^2 r) [1-(1/10)(R/r)^5]   (r>=R),

    g_r(r) = -2 G M_f/(5R^2) (r/R)^3           (r<=R),
             -G M_f/r^2 [1-(3/5)(R/r)^5]       (r>=R).

The potential and acceleration agree at the interface. At the center the
lift is finite and nonzero while the acceleration is zero. Direct radial
differentiation gives `Delta a=-8 pi G rho/c^2` on both sides, and
`-c^2 r^2 a'(r)/(2G)=M(<r)` supplies the exact flux check.

A useful physical distinction follows: **the field interface `R` is not a
vacuum boundary if this free-field energy gravitates.** Positive energy
continues outside it, with `rho~r^-8`; the potential has an exact `r^-6`
correction to its far monopole. It approaches `2GM_f/(c^2r)` as the
enclosed mass approaches `M_f`. This is a source-dependent consequence of
the Chapter I profile rather than another assumed compact ball.

## Tail, finite boundaries and finite energy

For `L>=R`, the original unchanged field carries

    U_f(r>L) = (3/5) U_f (R/L)^5,
    M_f(r>L) = (3/5) M_f (R/L)^5.

If only that distant density is discarded, the missing lift at every
`r<=L` is the same constant

    delta a = G M_f/(c^2 R) (R/L)^6.

It contributes no interior acceleration. A radial Poisson computation with
the full enclosed density and `a(L)=0` instead differs from the full
isolated lift by the complete constant `a(L)`, which is larger and contains
the `1/L` monopole term. These are different boundary operations.

There is also an important distinction for the **original quadrupole
field** itself. Merely truncating its unchanged energy integral at `L`
gives `U_f[1-(3/5)(R/L)^5]`. Imposing a new physical condition `phi(L)=0`
with the same trace `phi(R)=x/R` changes the exterior profile to

    q=(R/L)^5,
    phi(r)=(x/R)[(R/r)^3-q(r/R)^2]/(1-q).

Its total interior-plus-exterior free energy is instead

    U_f,Dirichlet = U_f/(1-q).

The first procedure omits positive tail energy; the second increases the
required Dirichlet energy. A finite boundary cannot be represented by
silently dropping an integral while retaining the same solution.

The conditional gravitational binding account is finite too. Three
equivalent integrals give

    U_grav = -G integral_0^infinity [M(r)/r] dM(r)
           = -(1/2) integral_0^infinity [c^2 a(r)/2] dM(r)
           = -c^4/(32 pi G) integral |grad a|^2 d^3x
           = -(421/990) G M_f^2/R.

Here the positive `U_f` is the source energy and negative `U_grav` is the
Newtonian binding account of the conditionally assigned density. Counting
that binding as an additional mass contribution would be a next-order
self-consistent source problem; it is not already included in `M_f`.

For reference, the positive gravitational gradient energy outside `L` is

    G M_f^2/(2R) [(R/L)-(1/5)(R/L)^6+(9/275)(R/L)^11].

These explicit tails make both the source and energy domains controlled.

## Why the full interaction account still matters

For classical simultaneous commuting currents, the retained boundary jump
selects `x_alpha=epsilon J_alpha/2`. At this stationary boundary profile,

    U_f = epsilon^2 sum J_alpha^2/(4R),
    U_interaction = -epsilon^2 sum J_alpha^2/(2R),
    U_counterterm = +epsilon^2 sum J_alpha^2/(4R).

The three integrated contributions sum to zero, as in the retained static
completion. Thus the positive free field alone is a clearly specified
sector, while a full energy-to-density map must also locate the signed
interaction and counterterms. The actual quantum source has noncommuting
`D,C`; simultaneous c-number currents do not replace that joint state.

## Verification and native task

`verify.py` uses exact rational Laurent polynomials to compute derivatives,
all improper integrals, source mass, potential, flux, binding and four finite
boundary examples. `FIELD_SOURCE_RESULTS.json` retains every result. No
transcendental evaluation or new native runtime is used by this independent
check.

`DUCK_R2_TASKS.json` gives a four-variable native inverse for

    alpha_inside=A+B x^4,     alpha_outside=C/x+D/x^6,

with two source-Poisson equations and continuity of value and derivative.
The target coefficients are obtained from the boundary problem, not supplied
as observations. Parent-owned Duck execution and native receipt readback
are retained separately.
