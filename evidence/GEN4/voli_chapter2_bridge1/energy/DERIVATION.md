# Retained displacement, complete payment, and the receiving floor

Sean Brady is originator and conceptual director. OpenAI ChatGPT and Codex
are research collaborators. These are new analytical deductions from the
retained wave action and common spin energy families. The source laws and
completed native spin results remain inherited. Independent exact checks
are in `RESULTS.json`; any new native check has a separate root receipt.

## 1. A boundary can return while the complete account retains the pulse

Use the regular-interior/outgoing-exterior spherical wave action and source
normalization of `GEN4/voli_radiative_memory1/PROOF.md`, R1–R10. Choose one
normalized real monopole in one channel. Its mean boundary coordinate is
`phi(R,t)=a(t)/R`; its coupling energy is `-a(t)J(t)/R`. Let `R,kappa,c>0`
and `H=2R/c`. The exact monopole response is

    g0(u)=(c/R) 1_(0<u<H),
    a(t)=(1/kappa) integral_0^H g0(u) J(t-u) du.             (E1)

Take a prescribed clamped pulse `J(t)=q 1_(0<=t<tau)`, `tau>0`, starting
from the same stationary centered Gaussian field reference. Define

    ell(t)=max(0,min(t,tau)-max(0,t-H)).
    a(t)=q c ell(t)/(kappa R).                              (E2)

Equivalently the overlap length is zero before zero; rises as `t` until
`min(tau,H)`; stays at `min(tau,H)` until `max(tau,H)`; falls as
`tau+H-t` until `tau+H`; and is zero thereafter. This covers short and
long pulses, including their continuous corner values and either sign of q.

The source ON work is zero for the bare linear coupling because `a(0)=0`.
At release the coupling work is `q a(tau)/R`. Thus the complete OFF-to-OFF
mean work is

    W=q^2/(kappa R) min(c tau/R,2) >= 0,                    (E3)

strictly positive for nonzero q. If the source carries the retained stored
counterterm `C(J)` with `C(0)=0`, it contributes `+C(q)` at ON and `-C(q)`
at release. Both terms are retained; they cancel over this complete cycle.
This deduction does not select a new physical counterterm.

The mean bulk field energy while the source is held ON is `q a(t)/R`:
the combined field-plus-coupling Hamiltonian remains zero after the initial
bare switch. After release its field energy is the constant W. The complete
time-dependent account, with right-continuous source switches, is therefore

    E_field(t)=q a(t)/R                  for 0<=t<tau,
              W                         for t>=tau;
    E_coupling(t)=-q a(t)/R              for 0<=t<tau,
                  0                     otherwise;
    E_stored(t)=C(q)                    for 0<=t<tau,
                0                       otherwise.       (E4)

Before zero all three mean excess accounts vanish. Their sum equals the
external switch work to date: `C(q)` while ON and W after release. This
is a mean excess above the same thermal reference, not a samplewise claim
that a thermal realization has no fluctuating work.

Since `B0=1/2`, the boundary readout and its complete radial/kinetic
complement satisfy

    E_boundary(t)=kappa a(t)^2/(4R),
    E_radial+kinetic(t)=E_field(t)-E_boundary(t)>=0.         (E5)

For ON times put `x=min(ct/R,2)`. Then their difference is
`q^2/(kappa R)(x-x^2/4)>=0`. For OFF times the maximum magnitude of a is
the release magnitude, and the same inequality applies with
`x=min(c tau/R,2)`. Thus every time keeps the full positive remainder.
It includes propagating gradient energy and kinetic energy. Before complete
departure it should not be called only a far-field radiation flux.

There is also an independent spatial calculation. Write the outgoing
monopole field as `u(r,t)=r phi(r,t)`. For `r>=R`,

    u(r,t)=q c/(kappa R) length([0,tau] intersect
                    [t-(r+R)/c, t-(r-R)/c]).               (E6)

After `t>tau+H` its whole mean pulse lies outside R. It is a translating
trapezoid. Integration by parts gives
`integral (u_r-u/r)^2 dr=integral u_r^2 dr`; all endpoint terms vanish.
Outgoing motion gives `u_t=-c u_r` and `rho_kin=kappa/c^2`. Consequently

    E_bulk=(kappa/2) integral_0^infty u_r^2 dr
          =q^2 c/(kappa R^2) min(tau,H)=W.                  (E7)

The independent test integrates the exact trapezoid slopes in r rather than
using E3. No radial truncation or boundary-only energy substitution is used.

For `t>=tau+H`, the boundary mean is exactly zero. Deterministic forcing of
this linear Gaussian field shifts its mean and keeps its stationary covariance.
The complete reduced boundary Gaussian marginal therefore agrees with the
untouched reference, while the complete mean bulk field retains positive W.
This supplies an exact recipient for Chapter II's distinction between an
observed endpoint and the history of the complete physical account.

There are two different physical forms of retention here. The pulse leaves
an outgoing record. A persistent written source `f_H` instead remains in
the existing source law
`J_i=lambda_C c_i f_rho(v_w)+lambda_R s_i f_H` and continues to sustain its
displaced field. The finite impulse horizon does not remove that source.
The clamped pulse calculation is not an autonomous 22-spin calculation and
does not identify that source with Chapter I's 16-state pair preparation.

## 2. A specified readout has an exact minimum displacement payment

Let B be one fixed positive source energy form selected before preparation,
and let `kappa_E>0` be its own physical energy prefactor. Existing examples
are the declared common current completion and literal source form in
`GEN4/spin_interaction_metric1/DERIVATION.md`. They have different physical
incidences; this result holds for either specified positive choice.

Choose a source reference y0 and displacement `dy=y-y0`. A fixed affine
receiver `z=c+L^T y` has record change

    r=z-z0=L^T dy,     z0=c+L^T y0.                        (E8)

The receiver and its affine reference must be the same on both sides. If its
constant is already embedded in the indicator coordinates, it is not added a
second time. The positive displacement payment is
`E_disp=kappa_E dy^T B dy`. This differs from the signed source energy change:

    E(y)-E(y0)=kappa_E[2 y0^T B dy+dy^T B dy].              (E9)

In particular a transition to a lower source energy can have negative E9
while its positive displacement payment remains nonzero. The fixture uses
the inherited literal energy to check that distinction explicitly.

Put `M=L^T B^-1 L`. For a compatible r, choose the least-energy source vector

    dy*=B^-1 L M^+ r.

Then `L^T dy*=r`. Every other vector with this same record is `dy*+h` with
`L^T h=0`. The mixed payment vanishes because
`(dy*)^T B h=r^T M^+ L^T h=0`. Therefore

    dy^T B dy = r^T M^+ r + h^T B h,
    E_disp >= kappa_E r^T M^+ r.                           (E10)

Here `+` denotes the Moore–Penrose inverse. A compatible record means
`r in range(L^T)`. The exact code handles dependent receiver columns by
selecting independent constraints and verifying the entire record; it does
not turn an inconsistent record into a nearby one.

E10 is the exact minimum in the ambient linear source-coordinate space.
It is a lower bound on the microscopic spin state set, whose indicators and
allowed histories impose further constraints. Attainment by that source
requires that dy* be a physically realizable displacement. A nonzero record
has a strictly positive ambient payment for a fixed positive B; continuously
smaller records have quadratically smaller payments. No discrete universal
energy gap follows without an independently supplied allowed-record rule.

The independent literal fixture uses the actual inherited matrix `Q=T+K`,
port index `z=a+4b`, and

    B18=diag(1,1,H2_port/573049),
    H2=Swap+Q tensor I+I tensor Q+Q tensor Q.                (E11)

The two diagnostic readouts are specifically the original port-indicator
coordinates `z=0` and `z=1`. They are not substituted for the complete
original 34-column affine receiver. The normalization is the retained
unit-strength reference; no microscopic coupling, physical seconds, or SI
energy has been newly selected. `NATIVE_INPUTS.json` supplies all E11 entries,
both receiver columns, and exact independent expectations for a native check.

## 3. Means, covariance, complement, and signed mixed energy remain

For a random source with mean m and covariance Sigma,

    E[y^T B y]=m^T B m+Tr(B Sigma).                         (E12)

Applying E10 pointwise and averaging gives

    E[dy^T B dy]>=r_mean^T M^+ r_mean
                    +Tr(M^+ L^T Sigma_dy L).              (E13)

The residual expectation remains on the left as a nonnegative payment.
For correlated reference and final states,
`Sigma_dy=Sigma_1+Sigma_0-Cov(y1,y0)-Cov(y0,y1)`; independent redraws cannot
replace their joint history. Existing whole-source spin energies already
retain means and fluctuations. These deductions consume their common form
without re-integrating the 54 preparations.

For any chosen linear source projection P, write `p=P y`, `q=(I-P)y`.
Then the complete source payment is

    y^T B y=p^T B p+q^T B q+2p^T B q.                      (E14)

The last term has its actual sign. An ordinary coordinate or statistical
projection need not be orthogonal in B. The independent actual literal
fixture has a strictly negative mixed term; deleting it changes the total.
Only a specifically B-orthogonal projection permits a positive split with
zero mixed term. E10 uses exactly that orthogonality, not an arbitrary
retained/complement truncation.

For the inherited full carrier extension
`B68=I68+F(B18-I18)F^T`, `F^T F=I18`, write `x=F y+z`, `F^T z=0`.
Then its complete energy is `y^T B18 y+||z||^2`. That block-diagonal result
comes from this explicit extension, not from the mere name 'unforced.' All
50 complementary directions and their covariance remain. A receiver that
also reads z needs its full 68-coordinate contract. A reduced six-source
projection may have the nonzero signed mixed payment in E14.

## 4. The spin source-action floor is an exact compatible-record floor

Use the original Gibbs inner product and self-adjoint source
`A=N(I-P)`, with original attempt clocks unchanged. The completed spin
basis is `b4=(d,e,u_d,u_e)` and its two orthogonal residuals are `w_d,w_e`.
Let their Gram matrices be G and W. Put

    v=A w_d,   k=<b4,v>,
    J11=<w_d,v>, J21=<w_e,v>, F11=<v,v>,
    alpha=W21/W11, delta=W22-W21^2/W11>0.

Since both w's are orthogonal to b4, projecting v onto
`b6=(b4,w_d,w_e)` gives

    Ffloor(J21)=k^T G^-1 k+J11^2/W11
                    +(J21-alpha J11)^2/delta,
    F11=Ffloor(J21)+||(I-P_b6)v||^2.                        (E15)

This is E10's compatible-record principle in the completed source Hilbert
geometry. It keeps the returned sign of J21 and every mixed Gram entry.
The current completed source pilots have positive source-action excess
approximately 1.421; source-dependent interval values remain authoritative
in `GEN4/duck_spin_upper1_20261014`. They are not new values computed here.
The exact geometry control in `fixtures.json` separately checks E15 against
a full four-vector projection with signed `J21=-4` and excess 9. Those
fixture numbers are not assigned to the original spin source.

The completed five-coordinate lower instead uses `b5=(b4,w_d)`. Its next
source vector is `r_next=A w_d-P_b5(A w_d)`. The b5 residual and E15's b6
residual have different projections; they are not identified. Existing
G5,D5,T5 supply the next vector's norm and old/new couplings. The next lower
needs one new `<r_next,A r_next>`; the next upper also needs its squared-action
norm. This specifies the next operand without repeating completed J21/F11/T5.

## 5. Receiving the positive account above A0 keeps calibration explicit

Chapter II's `A0=1/(12*pi)` is its declared dimensionless baseline. E10 and
E15 give source-dependent payment floors. Their values change with receiver,
source amplitude, source metric and normalization; they are distinct from A0.
In particular scaling a record by lambda scales its minimum payment by
`lambda^2`, and a zero record has zero displacement payment. Thermal variance
and source-action excess likewise do not assign the universal baseline.

One explicit candidate receiving rule, to be physically selected, is

    A_lift=E_disp/E_*,  E_*>0,
    A_total=A0+A_lift,
    A_total>=A0+(kappa_E/E_*) r^T M^+ r.                   (E16)

E16 is a derived inequality conditional on that receiving rule and a common
energy scale. It assigns no value to E_* or kappa_E and makes no empirical
calibration. A source-to-spatial-field kernel, physical incidence, units and
observational operation must supply them. In this recipient A0 is the minimum
total account when zero lift is admitted; the record-dependent additional
minimum is paid above it. If a different receiving observable is selected,
its map must be derived and E16 changes accordingly.

This gives Chapter II usable physical distinctions now: a returned endpoint
can coexist with a retained outgoing account; a surviving source can maintain
a displaced field; a specified distinction has a source-dependent minimum
payment; and every reduced description must retain its complement and mixed
balance. The finite address ledger and universal baseline keep their stated
roles while these source/action recipients are connected explicitly.

## Reproduce and scope

From this directory run `python3 reproduce.py` (Python standard library only).
The 11 independent tests include complete outgoing radial pulse energy,
short/long signed pulses and endpoint balance, stored-counterterm telescoping,
the inherited full literal energy incidence and positive principal pivots,
KKT conditions and feasible perturbations of the minimum, dependent and
incompatible records, affine-reference and signed-energy distinctions,
negative mixed payment, quadratic scaling, and a full signed Gram projection.
The script writes `RESULTS.json` and `NATIVE_INPUTS.json` only here, preserving
exact source document hashes. It performs no native run and assigns no new
physical calibration. Native receiving evidence belongs to its own receipt.
