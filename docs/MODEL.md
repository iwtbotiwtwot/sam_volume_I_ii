# Model, notation and scientific scope

Chapter II asks what a later receiver needs a source to retain. Its examples
use specified source states, histories, dynamics, observables and reference
energies. A current address, a predictive state, a history statistic and an
outgoing field can therefore be different records of the same process.

The 24-page reader contains 48 sections. Sections 1–40 preserve the completed
physical-development reader; sections 41–48 add its source-to-field interface.
The [proof guide](PROOFS.md) gives compact arguments and
[provenance](PROVENANCE.md) identifies their source lineage.

## Units and four different phases

Model time `t` becomes physical time only after choosing `t_phys = t_u t`.
A displayed Hamiltonian has physical energy scale `hbar/t_u`. A physical
source energy `epsilon_phys` gives `alpha = epsilon_phys/hbar`; its numerical
value is not supplied by choosing a convenient model chart.

| Symbol | Meaning |
|---|---|
| `gamma = phi_a + phi_b - 2 phi_p` | Original signed Write phase |
| `chi = phi_p` | Original common phase |
| `theta = -arg z`, continuously lifted | Actual interacting current-clock phase |
| `beta` | Relative phase of the added reference qubit |

A reverse Write has negative signed action and positive elapsed time. A wait
has zero Write rate while the actual clock and its reference can continue.
An endpoint qubit phase is modulo `2 pi`; a retained turn index is an
additional record. None of these phases is interchangeable by notation alone.

The original Write connection is

```text
omega_W = hbar (d gamma + 3 d chi).
```

For the occupied receiving lift, with `N = (I+S)/2`,
`Psi_W = exp(-3i chi) exp(-i gamma N) psi`, its canonical connection is
`hbar (<N> d gamma + 3 d chi)`. It matches the original coefficient of
`d gamma` on the occupied class. That class has zero active clock amplitude;
the actual coherent clock preparation is a different state.

## The complete source and its active lanes

The original four-dimensional one-source operator is
`Q = T + g_H K_r`, with signed-response operator `K_r`. Its four ordered
eigenvalues give a sixteen-dimensional pair source. The pair Hamiltonian
contains swap and the original even source contribution. Its six unequal-
occupation lanes carry the driven current; its four equal-occupation states
have zero `D` and `C` but retain distinct source energies.

Keep three uses of the letter K distinct:

| Object | Role |
|---|---|
| `K_r` | Ledger-derived signed response in `Q` |
| `K_e` | Commuting even pair-energy operator |
| Completed-square interacting form | Positive field/interaction/counterterm account in Chapter I |

The full source-field Hamiltonian retains

```text
H = H_s + H_f + H_int + H_ct,
H_int = -epsilon (D phi_+ + C phi_cross).
```

Both polarizations and both counterterms belong to the same preparation and
energy reference. The actual Chapter I clock is the joint-state correlator
of the normalized lane current, with a continuously lifted phase on its
certified nonzero-amplitude time window. A bare gap, a hard-branch gap and
this actual phase rate have different meanings.

An individual lane with the same source, field, couplings, counterterms and
preparation has exactly the corresponding two-level dynamics. A physical
epsilon supplies its scale. Additional predictions come from requiring one
complete source to supply several lanes and protected intersector receivers
with shared calibration.

## Shared calibration and a complementary receiver

For nonnegative `g_H`, the retained source yields the strictly increasing
dimensionless relation

```text
Xi(g_H) = 384 + 5120 g_H + 1377280 g_H^2.
```

It can identify `g_H` within the source law. One absolute calibration then
sets the physical frequency scale. Independent fitting of every lane would
discard this shared-source prediction.

The protected diagonal states `|q_a q_a>` have `D=C=0`; the interaction and
counterterms vanish on their whole span. Their exact adjacent coherence
frequencies are

```text
omega_ba = alpha (q_b-q_a)(q_b+q_a+2).
```

Removing only the pair-product energy gives the additive control with
frequency `2 alpha(q_b-q_a)`. Its current-lane histories remain identical,
while the protected intersector coherences distinguish the two accounts.
For the same nonnegative `g_H`, the pair/additive frequency-ratio comparison
is strictly larger than `1 + 1/132`.

The finite-data null class is a **closed autonomous two-state source with a
fixed linear receiver**. Generic multilevel sources, open dynamics, driven
two-state systems and time-dependent receivers are outside that class. The
instrument must supply the named coherent preparation and readout.

## Spin: retain the actual source metric and complement

The spin source uses its original finite number of sites, Gibbs preparation,
signed couplings and all-site heatbath generator `A = N(I-P_transition)`.
The positive-gap estimates act in its invariant exchange-odd sector. Source
time `t` corresponds to mean `N t` attempted site updates; no physical seconds
are assigned by that normalization.

An orthogonal retained projection `Pi` gives an exact memory equation. A
nonzero hidden complement changes the evolution even when its initial value
is zero. The physical residual norm uses the full source Gram matrix,
including mixed terms; an unnormalized coordinate Gram does not give it.

The current results are:

| Scope | Exact established statement |
|---|---|
| All 54 original preparations | Seven-span residual rank two; at least ten invariant coordinates |
| Selected `V001_BASE` continuation | At least fourteen invariant coordinates; the thirteen-span remains noninvariant |
| All 54 preparations | Explicit finite invariant symmetry-lumped upper space |
| Smallest reachable invariant closure | Open: no computed rank stabilizes |

The upper space represents exchangeable original sites exactly. It is not a
twenty-site replacement, and it does not assert that the two seed functions
reach every coordinate. Point-minor independence and positive Gibbs weights
give exact rank lower bounds. New global higher residual-moment integrals
remain separate work.

## Record payment and physical feasibility

For a positive source metric `B` and linear receiver `r=L^T y`, the attainable
ambient minimum is

```text
min y^T B y = r^T (L^T B^-1 L)^+ r.
```

Restricting to allowed microscopic source displacements can increase this
minimum. The chapter enumerates every compatible pure endpoint for one
declared diagnostic receiver and finds the source minimum
`1085537/573049`, before its physical energy factor.

Positive displacement payment is distinct from signed total energy change:
the latter also contains `2 y_0^T B delta_y`. An ensemble additionally retains
its covariance energy. A diagnostic minimum is therefore not the complete
source-field-controller energy or an automatic gravitational mass.

## Structural ledger and its receiving map

The structural construction receives binary distinction arity `h=2` and
spatial support `d=3`. Its bounded product kernel retains
`{1,2,3,4,6,8,9,12}` through radix `R=h^2 d=12`; the smallest admitted overflow
is `Theta=18`. The square account is `R^2=144`, with carrier share 18 and
retained complement 126. The structural floor is `A_0=1/(12 pi)`.

These are the chapter's typed structural operands. A carrier fraction is not
automatically a measured energy fraction, and equal cardinalities of address
sets do not supply an incidence map. Physical energy, spatial source and clock
receivers must state how they consume this account. A common floor cancels
from gradients and shared differences; a raw lapse ratio retains a different
background normalization from a declared source-only lapse.

## A paid reference and measured expectations

With conserved actual joint energy `E` and original signed Write rate
`w=gamma_dot+3 chi_dot`, the balanced reference uses

```text
h_R = 2(w-E) P_R,
beta_dot = 2(w-E),
E dt + (1/2) d beta = d gamma + 3 d chi.
```

Its product construction leaves the actual source-field marginal unchanged.
It is a driven receiving instrument. During a source wait, `h_R=-2E P_R`.
Ledger-matching intervals and external entry/release intervals have separate
payments. Signed net switch work can cancel while positive/withdrawn work,
control, source actuation, storage, preparation and reset remain nonzero.

Both phase and coherence protocols use freshly repeated preparations. The
eight-time receiver has outcomes `-sqrt(2), 0, sqrt(2)`. Its allowed error
includes the conditional prepared state, leakage, full ideal-path evolution
error, readout bias/disturbance, timing and calibration. The sufficient shot
count is conditional on meeting those requirements; it is not an observed
apparatus performance.

## Spatial receiving constructions in sections 41–48

The recovered Si29 effects satisfy `sum_t E_(t,x)=H_pos/8` at every site.
Their whole-space positive excitation account is `H_pos=|H_tr|`, distinct
from the signed transfer generator. Physical positions, smearing radii,
energy units and the coupling law are additional assignments.

One example places equal uniform balls at the vertices of an orthogonal
cube. Another, separately declared radial example uses concentric shells,
conductances `i(i+1)` and an outer Dirichlet boundary. They are different
geometries. Exact inverse/flux/energy formulas follow for the radial example;
mesh error and the outer-boundary error are controlled separately.

A complete density must localize source, field, interaction, counterterms,
support and reference terms consistently. In the commuting classical static
chart the free, interaction and counterterm contributions are `+U_f,-2U_f,+U_f`.
Selecting only the positive free-field term changes the source question.
The noncommuting quantum model remains retained.

The positive excitation coupling `H_tr-a H_pos/2` leaves the actual Si29
incoming-minus-outgoing population history unchanged. Full-generator scaling
changes its internal age instead. These calculated controls identify which
receiving law must be supplied; they do not determine it from a desired clock
output.

For the separately declared full scaling `H(a)=n(a)H(0)+f(a)I`, the actual
current obeys `z_a(t)=z_0(n t)`. The chapter's same-history phase comparison
gives a strict conditional shift for positive lift within the original
window. Epsilon-only scaling leaves a different field/counterterm remainder.
Complete physical localization, external perturbation, continuum response
bounds and apparatus sensitivity remain the next interfaces.
