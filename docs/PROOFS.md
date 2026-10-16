# Compact proofs and certificate guide

These arguments explain the main certificates in the reader. Their operands,
original derivations and receipts travel in the selected evidence export.
The public code independently reconstructs finite consequences; analytical
continuum statements retain the domains and preparation hypotheses stated in
their source. See [native evidence](NATIVE_EVIDENCE.md) for replay boundaries.

| Topic | Retained technical source |
|---|---|
| Actual spin closure and full source | [Closure derivation](../evidence/GEN4/voli_chapter2_physical3_20261015/closure/DERIVATION.md) |
| Paid reference and phase readout | [Worked protocol](../evidence/GEN4/voli_chapter2_physical3_20261015/protocol/DERIVATION.md) |
| Leakage, timing, detector and sampling | [Measurement derivation](../evidence/GEN4/voli_chapter2_physical3_20261015/measurement/DERIVATION.md) |
| Memory, counters, offsets and endpoints | [Short proofs](../evidence/GEN4/voli_chapter2_physical3_20261015/certificates/SHORT_PROOFS.md), [exact compact certificates](../evidence/GEN4/voli_chapter2_physical3_20261015/certificates/COMPACT_CERTIFICATES.json) |
| Recovered spatial source effects | [Source report](../evidence/GEN4/voli_chapter3_source_field1_20261015/source/REPORT.md) |
| Finite radial inverse, flux and energy | [Radial report](../evidence/GEN4/voli_chapter3_source_field1_20261015/radial/REPORT.md) |
| Current response and same-history phase | [Clock derivation](../evidence/GEN4/voli_chapter3_source_field1_20261015/clock/DERIVATION.md), [correlated phase proof](../evidence/GEN4/voli_chapter3_source_field1_20261015/clock/CORRELATED_PHASE.md) |
| Positive free-field source and reference | [Field-energy account](../evidence/GEN4/voli_chapter3_source_field1_20261015/energy/FIELD_SOURCE.md) |

## Predictive equivalence and a sufficient history

For a source, permitted event alphabet and receiver, define
`h ~ h'` when every permitted continuation `u` gives the same receiver output
from `h` and `h'`. Appending the same event preserves the relation because
each later test is already one of those continuations. The resulting quotient
is a sufficient predictive state.

To preserve phase traces, refinement must preserve each event's supplied
positive phase increment and successor class as well as present output.
Equal final accumulated phase is insufficient. For a fixed phase-polynomial
receiver family, counters

```text
M_(j,k) = integral theta^k 1_j d theta
```

update on a label segment `[a,b]` by `(b^(k+1)-a^(k+1))/(k+1)`.
This uses actual phase endpoints and needs no constant within-segment rate.

## Exact elimination gives memory

In the original Gibbs Hilbert space decompose the self-adjoint generator:

```text
A = [[B,C*],[C,D]],
p' = -B p - C* q,     q' = -C p - D q.
```

Variation of constants in the second equation and substitution into the first
give

```text
p'(t) = -B p(t) - C* exp(-Dt) q(0)
        + integral_0^t C* exp[-D(t-s)] C p(s) ds.
```

The memory kernel is `M(t)=C* exp(-Dt) C`. For initially retained data,
block multiplication gives `Pi A^2 Pi=B^2+C*C`. Thus equality of the exact
retained propagator with `exp(-Bt)` for every retained initial state requires
`C*C=0`, hence `C=0`. Conversely `C=0` decouples the equations. Exact closure,
zero initial memory Gram and invariance `AV subset V` are equivalent.

Setting `q(0)=0` removes initial forcing; it does not remove later memory.
Exact Krylov rank must stabilize, or a minimal-polynomial identity must close
the span, before a smallest invariant closure is claimed.

## Normalize the residual by the actual Gram matrix

For a nonorthonormal source basis `b`, put

```text
G = <b,b>,     D_b = <b,A b>,     T = <A b,A b>,
L = T-D_b G^-1 D_b,
M_orth(0) = G^-1/2 L G^-1/2.
```

The form `L` is the residual Gram. Congruence preserves its positivity and
rank, so its rank equals the outgoing map's rank. Its ordinary eigenvalues
do not give the physical residual norm: use the largest generalized
eigenvalue of `L v=lambda G v`, or the orthonormal form above. The full mixed
source metric is retained.

If `gamma I <= A <= N I` in the original odd sector, one further substitution
of the memory equation gives a double Duhamel integral. Its three semigroup
times sum to `t`, and the integration triangle has area `t^2/2`. Therefore

```text
||Pi exp(-At)|V - exp(-Bt)||
    <= (t^2/2) exp(-gamma t) ||M_orth(0)||.
```

Telescoping each factor against the identity, using
`||exp(-Xs)-I|| <= N s`, also gives the remainder bound
`(N t^3/2)||M_orth(0)||` after subtracting `t^2 M_orth(0)/2`.
These use original source time, with mean `N t` attempted site updates.

## Literal point minors certify the actual spin ranks

A relation among source functions holds at every literal configuration.
Consequently an invertible point-evaluation matrix certifies their linear
independence. Every configuration has positive original Gibbs weight, so
pointwise independence is also independence in its actual Gibbs Hilbert space.

For the original seven-span, the only two new Krylov columns can be taken as
`A^3 e` and `A^4 d`. An invertible nine-column point subset certifies rank two
for its complementary action; a tenth independent column shows the resulting
nine-span is still noninvariant. All 54 preparations have this certificate.
The selected deeper preparation reaches fourteen independent functions, while
its thirteen-span remains noninvariant.

Inverse rows supply a quantitative nonzero residual witness. If `lambda`
annihilates the retained columns and reads the next column as one, then

```text
1 <= [sum_i |lambda_i|^2 / pi(x_i)] ||residual||_Gibbs^2.
```

A strictly positive lower bound on the original point weights gives a positive
full-Gibbs residual norm. It does not evaluate an uncomputed global higher
moment. The separate exact exchangeable count-space construction gives a
finite invariant upper dimension, not the reachable minimum.

## Minimum additive counters and ABBA/BAAB

Subtract one baseline record and let `W` be the linear span of admissible
receiver-record contrasts. A linear decoder from `c` additive counters must
be injective on `W`, so `c >= dim W`. A basis of `W` attains that count.
This concerns linear additive monitoring, not arbitrary encodings in a real
number or a storage-bit claim.

For the six two-A/two-B words, the source certificate recovers all required
second moments from `S1=b1+b2` and `S2=b1^2+b2^2`, where `b1,b2` are the
zero-based A-block indices. Two record contrasts have determinant two, so
two counters are both necessary and sufficient for that family.

Keep actual repeated block durations `T_A,T_B` and each internal event offset.
ABBA and BAAB have equal sums of A starts; their squared-start sums differ by
`2 T_B(T_A+T_B)`. Expanding `(start+r)^2` cancels each event offset. Thus

```text
Delta M2_A = 2 T_B(T_A+T_B),
Delta M2_common = 2(T_A+T_B)(T_B-4T_A).
```

Equal phase-event durations `T_A=T_B=4h` give `64h^2` and `-192h^2`.
A nonlinear clock change transports the receiver weights; equality of physical
time moments is not automatically equality of unweighted phase moments.

## The feasible endpoint minimum

For attainable `r=L^T y`, positivity of `B` and orthogonality of the constrained
minimizer give

```text
y_* = B^-1 L (L^T B^-1 L)^+ r,
y^T B y = r^T (L^T B^-1 L)^+ r + ||y-y_*||_B^2.
```

The compatibility condition is essential. Restricting `y` to original
microscopic endpoints retains the final nonnegative feasibility term.
For the selected record `(-1,0)`, the original B18 gives:

| Endpoint | Cost numerator, denominator 573049 |
|---:|---:|
| 2 | 1085537 |
| 3 | 1146097 |
| 4 | 2006049 |
| 5 | 4965618 |
| 6 | 2155185 |
| 7 | 2163505 |
| 8 | 1085537 |
| 9 | 2155185 |
| 10 | 1142898 |
| 11 | 1146097 |
| 12 | 1146097 |
| 13 | 2163505 |
| 14 | 1146097 |
| 15 | 1146098 |

Endpoints 2 and 8 attain the minimum and each is an available single flip.
Every signed off-diagonal term is retained. The physical scale, actuator
payment, signed reference energy and source incidence remain separate.

## A finite-data discriminator and its shots

A closed autonomous two-level source with fixed preparation and linear
receiver gives equally spaced samples
`y_n=c+a cos(n vartheta)+b sin(n vartheta)`. First differences remove `c` and
are a sum of at most two exponentials. Their difference-Hankel matrix has
rank at most two.

The protected three-state source generally has four distinct sampled phase
factors. Eight expectations suffice to form the selected three-by-three
minor. If each expectation has error at most `eta`, each difference entry has
error at most `2 eta`. Telescoping the six determinant products gives a
data-evaluable rejection condition

```text
|det A_hat| > 36 eta (B_hat+2 eta)^2,
B_hat = max_ij |(A_hat)_ij|.
```

The source-selected cadence is fixed before target data acquisition. With the
retained independent calibration, its ideal determinant lies in the displayed
outer interval `[5.31872398, 5.94178279]`, and `eta=0.01` retains a strict
separation margin. The certificate preserves sharper exact rational bounds.

Allocate `0.001` each to preparation, unwanted evolution, readout and timing,
and `s=0.006` to sampling. For independent detector outcomes in
`[-sqrt(2),sqrt(2)]`, Hoeffding and a union bound over eight means give

```text
Pr(any sampling error > s) <= 16 exp(-N s^2/4),
N >= ceil[(4/s^2) log(16/beta_sampling)].
```

At `beta_sampling=0.01`, `N=819751` per time suffices: 6,558,008 measurements.
Exact rational logarithm bounds certify the integer. The count is conditional
on the systematic requirements and independent-shot assumptions. Calibration,
failed preparation, cooling and reset have additional costs. If calibration
itself can fail with probability `beta_cal`, the total bound is
`0.01+beta_cal`.

## Paid reference, work and winding

With balanced reference state
`(|0>+exp(-i beta)|1>)/sqrt(2)`, conventional Pauli Y gives
`<X>=cos beta`, `<Y>=-sin beta`. The estimator is `atan2(-Y_hat,X_hat)`.
The canonical connection is `d beta/2`. Choosing `beta_dot=2(w-E)` yields
the original signed Write connection while leaving the actual clock unchanged.

During matching, mean reference energy is `w-E` and drive power is `w_dot`.
Continuous monotonic pieces and every switch are retained. A source wait has
`w=0`, hence energy `-E` and phase rate `-2E`. External entry/release are
outside the matching ledger. Telescoping signed payments does not erase their
positive/withdrawn parts or establish zero apparatus cost.

At most 441 freshly repeated prefixes, with the stated phase/timing bounds,
allow nearest-branch continuation from `beta(0)=0`. A retained external counter
stores the turn. The sufficient 26,624 binary measurements per X or Y mean
give at most 23,482,368 fresh preparations. Each prefix measurement consumes
that copy's coherence; it is not a nondisturbing monitor.

## Radial receiving limit and common-history phase

For conductances `c_i=i(i+1)`, inner shells `1,...,L-1`, no central sink and
outer value `a_L=0`, the exact inverse is
`H_ij=1/max(i,j)-1/L`. Taking differences yields
`c_i(a_i-a_(i+1))=kappa sum_(j<=i)m_j`. This verifies the source flux and
the inverse against the positive Dirichlet operator.

The isolated lift adds `2GM/(c^2 Lh)` to the finite-wall reference. Its
energy correction is `-GM^2/(2Lh)`. For uniform-ball shell refinement,
the reduced lift error is at most `3/n-2H_n/n^2 < 3/n`; the finite wall has
its own error. A radial result alone does not establish a three-dimensional
isotropic microscopic operator or causal propagation law.

For the declared full scaling `H_a=n H_0+f I`, fixed preparation gives
`theta_a(T)=theta_0(nT)` on the same lifted branch. If `ell<=nu_0<=u`,

```text
Delta theta = -integral_(nT)^T nu_0(s) ds,
-u(1-n)T <= Delta theta <= -ell(1-n)T < 0.
```

For `n=sqrt(1-a)`, `a/2 < 1-n <= a/(2-a)` gives a rational enclosure.
This retains the correlation lost by comparing two independent phase bands.
It is conditional on the declared coupling and does not cancel preparation,
timing or measurement error. Epsilon-only scaling gives a different
field/counterterm remainder and is a separately identified diagnostic.
