# Compact static energy, uniqueness, interaction and domain derivations

These are conditional consequences of Chapter III's declared receiving law,
not a microscopic assignment of gravitating mass. They complement the finite
radial source construction in `../radial/REPORT.md`.

## 1. A sufficient domain and the unique minimum

Let `rho` be bounded with compact support in three dimensions. In particular
`rho` belongs to `L^(6/5)`. Use the homogeneous Sobolev space
`D^(1,2)(R^3)`, the completion of smooth compactly supported functions in
the gradient norm. Its Sobolev embedding into `L^6` makes the source pairing
`integral rho*a` bounded. The positive gradient form is coercive on this
space. The weak source problem therefore has a unique finite-energy
solution. Its Green representation is Chapter III Eq. (3.6).

For

    J[a;rho] = c^4/(32 pi G) integral |grad a|^2
                                  - c^2/2 integral rho a,

and the weak solution `a_*`, integration against an admissible `v` gives

    c^4/(16 pi G) integral grad a_* dot grad v
                                           = c^2/2 integral rho v.

Expanding `J[a_*+v]` therefore cancels the linear cross term exactly:

    J[a_*+v;rho]-J[a_*;rho]
                         = c^4/(32 pi G) integral |grad v|^2 >= 0.

Equality forces `v=0` in this domain. A nonzero constant is not an element
of `D^(1,2)` represented in `L^6`; it cannot supply a hidden potential
reference. This supplies the energy version of isolated-source uniqueness.
In a bounded domain with Dirichlet data, use `H_0^1` for the variations and
retain the chosen boundary data explicitly.

An ideal thin shell is a surface measure rather than a bounded volume
density. The radial example handles it through its explicit continuous
potential, finite gradient energy and distributional derivative jump, or
equivalently as the finite-thickness-shell limit. It does not identify the
surface measure with the bounded-density assumption of the preceding
sufficient-domain argument. A point mass has a different singularity and
infinite unregularized self energy.

## 2. Boundary terms and the signed energy

On a regular bounded domain,

    integral |grad a|^2
       = integral_boundary a*partial_n(a)
                                    + 8 pi G/c^2 integral rho a.

Thus a nonzero boundary contribution must accompany a finite-domain energy
claim. In whole space with isolated `a=O(1/r)` the surface term vanishes
at infinity. On the resulting solution,

    U = J[a_*;rho] = -c^2/4 integral rho a_*
                  = (1/2) integral rho Phi
                  = -c^4/(32 pi G) integral |grad a_*|^2.

The positive gradient term inside the off-solution functional and the
negative on-solution binding energy have different jobs. For radial outer
radius `R`, the exact correction is `U_infinity=U_R-GM^2/(2R)`; the radial
report keeps both the exterior field integral and the source-reference
shift, avoiding an omitted-tail or double-counted-tail account.

## 3. Two sources and one pair interaction

For two sufficiently regular localized densities let

    a_i(x) = (2G/c^2) integral rho_i(y)/|x-y| dy.

Linearity and the symmetric kernel give

    U[rho_1+rho_2] = U[rho_1]+U[rho_2]+U_12,
    U_12 = -G double_integral rho_1(x)rho_2(y)/|x-y| dx dy.

The two cross terms of the quadratic source energy combine into one pair
interaction. Each self interaction retains its factor `1/2`. A common
energy reference is needed before any mass conversion is attached to
these quantities; positive microscopic record cost is not this negative
binding energy.

Translate the first density by `q`, `rho_1^q(x)=rho_1(x-q)`. Differentiation
under the integral, for disjoint compact supports or other hypotheses that
make it legitimate, gives

    F_1 = -grad_q U_12
        = -G double_integral rho_1(x-q)rho_2(y)
                                      (x-y)/|x-y|^3 dx dy
        = integral rho_1(x-q) g_2(x) dx.

Exchange the sources to obtain `F_2=-F_1`. This is the same force obtained
from the mechanical receiver; it is not a new independent coupling.

For concentric thin shells the exact interaction is
`U_12=-GM_1 M_2/max(r_1,r_2)`. Varying the inner shell's radius leaves the
interaction fixed, while varying the outer radius gives the inward radial
work derivative. This directly distinguishes a shell's nonzero interior
potential from its zero interior force.

## 4. Domain boundaries that matter physically

A bounded source has finite central potential and finite field energy.
For a central cusp `rho(r)~r^(-q)`, nonzero positive prefactors give:

* finite mass near zero when `q<3`;
* finite central potential when `q<2`;
* finite local field energy when `q<5/2`.

The last statement follows from `M(r)~r^(3-q)`,
`|grad a|~r^(1-q)`, and radial energy integrand
`r^2 |grad a|^2~r^(4-2q)`. The threshold cases have logarithmic divergence.
Finite mass alone therefore does not justify the central or energy
integrals. An ideal point source requires a finite-radius model or an
explicit regularization for its self account.

## 5. What this supplies to the chapter

These short derivations put uniqueness, the negative binding sign, pair
counting, virtual work and finite-boundary correction in one account. They
leave the chapter's source-to-density and physical calibration questions
visible. The finite-shell rational checker supplies an independent
executable instance of every algebraic energy identity; the parent-owned
Duck cycle supplies the native matrix counterparts.
