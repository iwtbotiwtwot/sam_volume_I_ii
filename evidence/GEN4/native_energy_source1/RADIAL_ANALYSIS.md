# Returned radial geometry and boundary-response analysis

All four source-bound radial operations returned successfully. The exact
entries are extracted in [RADIAL_READOUT_SUMMARY.json](RADIAL_READOUT_SUMMARY.json);
[RADIAL_METHOD.md](RADIAL_METHOD.md) distinguishes analytic inputs from native
operations and specifies the boundary and normalization conventions.

The strongest result is a geometric origin for the quarter shift compatible
with the previously executed inverse-radius receiver geometry. The result
does not by itself select a physical energy unit, action scale or elapsed-time
generator.

## 1. The quarter is supplied by the three-dimensional radial Jacobian

[NES1_RADIAL_CONJUGATION](returned/NES1_RADIAL_CONJUGATION.json) evaluates the
log-radius change of variables in the separated scalar Laplace equation:

```
r² f''+(d-1)r f'-kappa f=0,
t=log(r/R), f=e^(-(d-2)t/2)u,
u_tt=[kappa+(d-2)²/4]u.
```

The native transformed generators return shifts **0,1/4,1** in d2,3,4.
For d3 and kappa0,2,6,12, the lower-left coefficients are exactly
**1/4,9/4,25/4,49/4**. Their positive radial exponents are1/2,3/2,5/2,7/2.
The quarter has therefore been obtained from a stated geometric operator,
rather than inserted to fit a desired spacing. The existing receiver source
already proposed this three-dimensional scalar transport geometry in its
monopole sector; extending it to angular harmonics remains explicit.

For this geometric derivation within the declared scalar extension:
**The test result suggests strong contact with the concept.** Here t is log
radius and the radial generator grows/decays; it is not an oscillation in
physical time.

## 2. Balanced boundary energy is concrete, but spacing alone cannot select it

[NES1_BOUNDARY_BALANCE](returned/NES1_BOUNDARY_BALANCE.json) returns
`B=diag(1/2,3/2,5/2,7/2,9/2)`. Its square-minus-Casimir-minus-quarter residual
is exactly zero. Regular interior and decaying exterior DtN operators are
`l/R` and `(l+1)/R`, with outward normals defined separately for each domain.
Their difference is exactly I/R. Their adjacent-gap difference is zero.

With equal interior/exterior stiffness and a shared boundary field,
the minimized quadratic Dirichlet form is
`(D/2) integral |grad(phi)|² =D*R sum B_l |a_lm|²` for harmonics normalized
on the unit sphere. Thus the balanced operator arises naturally from the
two-sided form. The receiver network currently supplies only the sourced
exterior monopole; it does not select the interior completion or equal
stiffness by itself.

Interior l, exterior l+1 and balanced l+1/2 all have the same gaps and differ
by scalar offsets. Their closed unitary density propagation and antipodal
recurrence therefore cannot distinguish the offset. An additional source
transformation law, boundary energy/flux measurement or external phase
reference is needed. This makes the parallel conformal source/receiver
selection tests substantive rather than redundant.

“Dirichlet energy” here denotes a positive mathematical quadratic form.
The actual receiver conductances are service/transport rates: identifying
their form with physical stored energy requires a field and unit map.

## 3. A finite receiver boundary predicts specific unequal gaps

[NES1_FINITE_BOUNDARY_INVERSE](returned/NES1_FINITE_BOUNDARY_INVERSE.json)
returns a unique solution for57 unknowns: exterior harmonic coefficients,
normal responses, balanced responses and gaps. The inverse was given the
boundary conditions `f(R)=1`, `f(L)=0`, not a desired response spectrum.

| L/R | Native gap0→1 | Native gap1→2 | Native gap2→3 |
|---|---:|---:|---:|
| 2 | 5/7 | 188/217 | 3728/3937 |
| 4 | 6/7 | 2336/2387 | 1858048/1862201 |
| 8 | 68/73 | 340736/341713 | 200327168/200342119 |

For L/R2, the returned balanced levels are **1,12/7,80/31,448/127**.
They agree with the separately derived expression

```
B_l(L)=(l+1/2)/[1-(R/L)^(2l+1)].
```

The mode-dependent correction tends to zero as the absorbing boundary
recedes. At l0 the integrated normal response, with common4*pi*D removed,
is `R² Lambda_out=1/(1/R-1/L)`: exactly the effective conductance of the
existing receiver network's radial series law. This is a direct source
connection; the angular spectrum is the new extension.

For exact unchanged infinite-sphere spacing at the executed finite absorbing
boundaries: **The test falsifies the concept.** For the stated boundary
response and its source-dependent correction: **The test result suggests
strong contact with the concept.** This does not rule out one universal
overall coupling when the additional geometric ratio L/R is retained.

## 4. The same boundary form admits different temporal laws

[NES1_BOUNDARY_ENERGY_TIME_FORK](returned/NES1_BOUNDARY_ENERGY_TIME_FORK.json)
compares Hamiltonian and gradient dynamics for the same positive form
`E=(q^T B q+pi^T B pi)/2`. The native energy-derivative matrix is zero for
the Hamiltonian completion. For gradient dynamics it is diagonal with
**-1/2,-9/2,-25/2,-49/2**, repeated for the second real component.

An explicit canonical action could give `i I_star dot(z)=E_star Bz`.
That equation requires the symplectic/phase-space term, its normalization
I_star and physical time to be selected. The elliptic DtN calculation
supplies none of them. In particular, a closed phase-count one-form on a
fixed-amplitude orbit does not itself furnish a nondegenerate symplectic
two-form or an inertia. Calling its period an action does not assign the
Planck constant or a temporal kinetic law.

For uniqueness of physical temporal progression from this boundary form
alone: **The test falsifies the concept.** The two explicitly chosen
completions remain mathematically distinct candidates.

## 5. Earned dynamic continuation: actual receiver timing statistics

The retained receiver family supports an isolated lossless M/M/1 candidate,
so a next useful calculation can retain that exact local model instead of
replacing it with a two-state gate. Its temporal law must not be assigned
to a node of the routed network merely from the network's stationary
product-form distribution. The following is an independently checked
analytic derivation for the isolated receiver, separate from the four
native returns above.

Let lambda=rho*mu, 0<rho<1, B(t)=1 when the receiver is empty, and let r(s)
be the stable root

```
mu*r²-(s+lambda+mu)*r+lambda=0,  r(0)=rho.
```

It satisfies `s*r=mu*(1-r)*(rho-r)`. The stationary free-indicator covariance
and arrival-rate susceptibility are

```
Ctilde(s)=(1-rho)*(rho-r)/s
         =(1-rho)*r/[mu*(1-r)],
chi_busy(s)=Ctilde(s)/rho,   chi_free(s)=-chi_busy(s).
```

Thus `Ctilde(0)=rho/mu`, the static busy response to arrival rate is1/mu,
and whole-generator clock time `tau(T)=integral_0^T B(t)dt` has asymptotic
variance rate `Var(tau)/T→2rho/mu`. At rho1/4, its mean rate is3/4 and variance
rate is1/(2mu). The branch points are `-mu*(1±sqrt(rho))²`, which become
-mu/4 and-9mu/4. This retains queue memory beyond a two-state Markov gate.

Scaling all source service and arrival rates by1000 leaves static workload
unchanged while shifting response frequencies and reducing the clock-time
variance rate by1000. Arrival-rate forcing and workload forcing must be
distinguished: the latter response is mu*chi_busy. Native complex resolvent
evaluation can now test these source-selected timing predictions and their
use in a later dynamic boundary closure. The absolute service-rate and
physical clock coupling are still explicit source assignments.
