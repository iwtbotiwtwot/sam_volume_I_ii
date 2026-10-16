# An eight-time measurement protocol with an apparatus budget

ORIGINATOR / CONCEPTUAL DIRECTOR: Sean Brady. AI RESEARCH COLLABORATORS:
OpenAI ChatGPT and Codex. This is a new receiving-instrument candidate and
self-contained finite-shot certificate, bound to the retained Chapter II source.
It assigns a mathematical measurement law and sufficient tolerances; it does not
report an implemented preparation, detector, physical epsilon calibration, or
experimental precision. The result suggests possible physical contact.

## M1. Retained source and eight expectations

Use `GEN4/voli_chapter2_continuation2_20261015/signature/{DERIVATION.md,RESULTS.json}`
and the primary `GEN4/duck_chapter1_lane1_20261015/sources/EXACT_INPUTS.json`.
`RESULTS.json` in this directory binds each SHA-256. Keep
`Q=T+g_H K_response`, the complete pair source, the common field/counterterms,
and positive `alpha=epsilon_phys/hbar`; do not identify `K_response` with
`K_even`. In the protected span, let `|a>=|q_a q_a>` and

    |psi>=(|0>+|1>+|2>)/sqrt(3),
    O=|0><1|+|1><0|+|1><2|+|2><1|,                (M1)
    y(t)=<O>(t)=(2/3)[cos(omega10 t)+cos(omega21 t)].

Extend O by zero on every other source state. The ideal protected preparation
is tensored with the retained field vacuum. D and C annihilate the entire
protected diagonal source span, as do their counterterms; thus this signal
uses the full Hamiltonian, not a field cutoff. Source energies are
`epsilon_phys(1+q_a)^2`. Keep the inherited independent calibration:

    Xi=1382784 +/-1,
    alpha/alpha_nominal in [1-10^-6,1+10^-6],
    h=pi/(3 alpha_nominal D_nominal),
    D_nominal=6348467821812271/80000000000,
    t_k=kh, k=0,...,7.                            (M2)

The retained source intervals include both calibration uncertainties. Numerical
seconds, the preparation pulses, source-mode selection, and receiver couplings
remain physical assignments. Xi is independently measured signed-lane/source
coupling information; it is not extracted by fitting these eight samples.

For each k, prepare N fresh copies with the same procedure and independently
evolve each to t_k. Destructively read one copy once, then reset or replace it.
Do not measure one copy eight times: its first readout changes its subsequent
state. Randomizing the run order of k helps diagnose drift, but does not replace
the error bounds or independence conditions below. The ideal t0 is read after
preparation with zero free-evolution duration; its actual delay belongs to the
timing budget. Preparation and detector calibration shots are additional.

## M2. A specified readout and its disturbance

On the three-mode span the orthonormal detector vectors are

    v+=(|0>+sqrt(2)|1>+|2>)/2,
    v-=(|0>-sqrt(2)|1>+|2>)/2,
    v0=(|0>-|2>)/sqrt(2).                         (M3)

Apply the corresponding source-basis rotation, then a projective outcome
measurement, reporting X=+sqrt(2),-sqrt(2),0 respectively. All complementary
outcomes report zero. Thus `E[X]=y(t)` and `|X|<=sqrt(2)`; in particular,
the target expectation's smaller range `[-4/3,4/3]` is **not** the detector
outcome range. The normalized alternative `O/sqrt(2)` has outcomes [-1,1],
but the error allowance and witness must then be scaled consistently.

The ideal postmeasurement map is `rho -> sum_j P_j rho P_j`. It generally
destroys the phases being measured. No nondisturbance of that discarded copy
is needed. Pre-detection pulse disturbance is instead included in the actual
POVM: if `F_x` is its effective pre-readout effect and
`M=sum_x x F_x`, require `||M-O||<=b_read`. This bounds mean readout bias for
every input state. The actual reported outcomes must stay in
`[-sqrt(2),sqrt(2)]`, by bounded reporting if necessary. Outcome misassignment,
coherent rotation error, and disturbance before the ideal measurement are
all included in this one operator bound; they cannot be assumed negligible
because the final measurement is projective. It is a physical requirement,
not a readout performance inferred from the source algebra.

The compact polynomial certificate is `O^3=2O`, with eigenvalues
`+sqrt(2),0,-sqrt(2)` and projectors
`P0=I-O^2/2`, `P+/-=O^2/4 +/- O/(2sqrt(2))`.
`NATIVE_OPERANDS.json` gives the exact rational matrices O, O squared and
twice P0 for a Duck source-word cross-check; the irrational projectors are
specified by the polynomial identities, not rounded detector matrices.

## M3. Four systematic errors kept separate

For density operators define `D(rho,sigma)=||rho-sigma||_1/2`. Since
`||O||=sqrt(2)`, Holder's inequality gives

    |Tr O(rho-sigma)| <=2sqrt(2) D(rho,sigma).     (M4)

1. **Preparation.** Require total source-plus-field preparation distance
   `D(rho_prep,|psi,vac><psi,vac|)<=d_prep`. The bias is at most
   `2sqrt(2)d_prep`. Leakage alone does not control preparation inside the
   protected span or the field state. If a certified projection onto the
   intended protected source-plus-vacuum space has leakage probability l,
   and its normalized conditional state is within distance d_cond of the
   intended pure state, then

       d_prep <=sqrt(l)+d_cond.                   (M5)

   To see this, projecting a purification succeeds with probability 1-l;
   its normalized overlap is sqrt(1-l), so the pure-state distance is
   sqrt(l). Partial trace cannot increase distance; use the triangle
   inequality for the conditional preparation error. The same statement
   applies to a separate source-only projector if field/conditional error
   is still included in d_cond. If d_cond=0, the conservative leakage-only
   requirement for the allocation below is `l<=1.25e-11`. If both terms
   are allowed, one sufficient equal split is
   `l<=3.125e-12` and `d_cond<=1.76776695e-6`.

2. **Evolution and unwanted coupling.** Let U be the implemented propagator,
   U0 the ideal full propagator at the actual calibrated parameters. On the
   ideal state path require the Duhamel-domain conditions and

       kappa_k=integral_0^(t_k+delta_t)
           ||(H_actual(s)-H_ideal)U0(s)|psi,vac>||/hbar ds
           <=kappa_max.                          (M6)

   The upper limit covers the latest allowed trigger. Duhamel's integral
   formula and unitarity give vector distance, hence
   trace distance, at most kappa_k. The bias is at most
   `2sqrt(2)kappa_max`. In finite bounded accessible spaces it suffices to
   bound `integral ||delta H|| ds/hbar`. The full field has unbounded
   operators: a finite matrix norm on the source block is **not** such a
   certificate. Off-block leakage and field errors must satisfy (M6), or a
   separately established energy-constrained bound. Calibration uncertainty
   already retained in (M2) is not charged again here.

3. **Readout.** The effective-observable requirement in M2 contributes
   `b_read`. The same detector law and error bound are used at every time.

4. **Timing.** Permit bounded error `|delta t_k|<=delta_t` relative to t_k
   after preparation, including trigger and finite readout-window error.
   The derivative obeys

       |y'(t)| <=L=(2/3)(omega10+omega21),
       L<=114081.396605 alpha_nominal.            (M7)

   The second inequality is an outward source/calibration bound checked
   using the inherited rational root intervals and Weyl error. Therefore
   timing bias is at most L delta_t. A run-average bound can replace a
   per-shot bound only if its weighted mean absolute timing error is
   certified. A zero mean jitter claim without a size bound is insufficient.

One declared diagnostic allocation in the original O normalization is

| contribution | maximum absolute expectation error | sufficient condition |
| --- | ---: | --- |
| preparation | 1e-5 | d_prep <=1e-5/(2sqrt(2)) =3.5355339e-6 |
| unwanted evolution | 1e-5 | kappa_max <=1e-5/(2sqrt(2)) |
| readout | 1e-5 | ||M-O||<=1e-5 |
| timing | 1e-5 | delta_t <=8.76567e-11/alpha_nominal |
| statistical mean error | 6e-5 | M4's repeated-shot bound |
| total | 1e-4 | sum of all five contributions |

The exact timing allowance is `1e-5/L_upper` stored in RESULTS.json; the
displayed shortened value is rounded down. It is approximately
`6.64256e-6` of cadence h. A bound on shared alpha and a bound on trigger
timing are distinct. No numerical alpha, time in seconds, or apparatus
feasibility is assigned by this table.

## M4. Eight means, not eight shots

Let `yhat_k=N^-1 sum_j X_kj` and `mu_k=E[yhat_k]`. For independent bounded
outcomes in `[-sqrt(2),sqrt(2)]`, Hoeffding's bound is

    Pr(|yhat_k-mu_k|>s) <=2 exp(-N s^2/4).        (M8)

The range is `2sqrt(2)`, whose square is8. The usual exponential-moment
proof bounds each centered moment generating function by
`exp(lambda^2*8/8)` and optimizes lambda; multiplying independent generating
functions gives (M8). Identical distributions are unnecessary if their mean
biases obey the same budget. Arbitrary correlated shots do not meet this
assumption. A conditional version requires the corresponding conditional
mean bounds and a martingale concentration argument.

The union bound over eight means, with joint failure probability beta, gives

    N >=ceil[(4/s^2) log(16/beta)].               (M9)

At `s=6e-5`, `beta=0.01`, a sufficient count is

    N=8,197,509,899 fresh shots per sample time,
    8N=65,580,079,192 measurement shots total.     (M10)

`verify.py` certifies this integer using rational upper/lower logarithm
bounds, rather than a floating-point ceiling. On the simultaneous 99%
event, systematic plus sampling error is at most eta=1e-4 for every sample.
This confidence statement is conditional on the deterministic calibration
and systematic bounds. If those bounds are only certified with failure
probability beta_cal, the total failure bound is `0.01+beta_cal`; allocate
the desired overall failure probability across both. The sample count does
not pay for establishing those apparatus bounds, discarded preparation
attempts, cooling, calibration, or reset overhead. More efficient receivers,
concentration bounds, and cadence choices can be investigated, but this
particular diagnostic protocol has a severe conservative sampling cost.

## M5. A direct finite-data decision

From the eight means form `dhat_k=yhat_(k+1)-yhat_k` and the order3 Hankel
minor indexed by I={0,1,3}: `Ahat_ij=dhat_(I_i+I_j)`.
Put `Bhat=max_ij |Ahat_ij|` and

    T_hat=36 eta(Bhat+2eta)^2.                   (M11)

Reject the class of closed autonomous two-state sources with a fixed linear
Hermitian receiver, at the stated error allowance, if
`|det Ahat|>T_hat`. For any such ideal TLS, the exact difference-Hankel rank
is at most2. If its eight expectations were within eta of the measurements,
each minor entry would differ by at most2eta. Expanding the six determinant
terms and telescoping their three factors bounds its determinant difference
by `6*3*(2eta)(Bhat+2eta)^2`, which is (M11). This is a data-evaluable
certificate without fitting frequencies or selecting a cadence from the data.

For the retained calibrated source, the ideal determinant is enclosed by

    [-0.106706899733662,-0.085302278620110].       (M12)

Since its samples are in [-4/3,4/3], their Hankel entries are bounded by
B=8/3. On the simultaneous error event,

    |det Ahat-det A| <=36eta(B+2eta)^2,
    |det Ahat| >=0.059698438364110,
    T_hat <=36eta(B+4eta)^2 <0.025608,
    |det Ahat|-T_hat >0.034090.                  (M13)

Exact rational checks use the full inherited interval rather than these
displayed decimals. Thus the source meets the rejection criterion on the
99% sampling event if all stated systematic requirements hold. The null
class is a closed autonomous TLS with a fixed receiver. This is neither a
test against arbitrary open/driven two-state dynamics nor a claim that a
generic multilevel source cannot reproduce the record.

## M6. A source-selected cadence reduces the sufficient shot count

The short-cadence baseline above is retained exactly. It is not necessary to
use that particular cadence. The protected full-field signal remains valid
for all times, so one can choose a better fixed cadence from the source and
independent calibration **before collecting any of the eight target means**.
No extension of the physical field protection is required.

`verify.py` checks a small declared source-only list of cadence factors
`{1/3,2/3,4/3,5/2,3}` multiplying `pi/(alpha_nominal D_nominal)`. A useful
choice, not a claimed optimum, is

    h_new=5pi/(2 alpha_nominal D_nominal),
    I_new={0,2,3}, eta_new=0.01.                  (M14)

This is 7.5 times the baseline cadence. It must be specified before target
data acquisition; it is not fitted to the eight measured means. With the
same Xi and alpha calibration intervals, the certified minor satisfies

    det A_new in[5.318723982743267,5.941782789331066],
    max_ij |(A_new)_ij|<2.                       (M15)

The exact lower endpoint is retained in RESULTS.json. Compact decimals in
this document are explanatory rather than substitute rational endpoints.
Interval arithmetic uses the rational Machin pi bracket, Taylor remainder
after certified range reduction, and the cosine Chebyshev recurrence. In
particular the two calibrated cosine intervals are distinct and strictly
inside (-1,1), so all four sampled exponentials are distinct and nonconstant.
This cadence preserves the four-exponential receiving rank.

For eta=0.01 and B=2 the two-error-ball determinant allowance becomes

    72eta(B+4eta)^2=2.996352<5.318723982743267.    (M16)

Use the same four systematic allocations, now 0.001 each, plus statistical
mean allowance s=0.006. The trace-distance and evolution-path limits become
`0.001/(2sqrt(2))=0.00035355339`; the readout operator error limit is0.001.
If the conditional preparation is exact, the conservative coherent leakage
allowance is `1.25e-7`; otherwise (M5) still applies. Timing must satisfy

    delta_t <=0.001/L_upper,
    0.001/L_upper >8.76567e-9/alpha_nominal,
    delta_t/h_new approximately8.85675e-5        (M17)

when its largest permitted value is used. For a simple conservative apparatus
limit, require `delta_t<=8.76567e-9/alpha_nominal`; RESULTS.json stores the
exact maximal allowance. The shortened displayed lower bound on that
allowance is not permission for a larger trigger error.

Equation (M9), unchanged except for s, then gives

    N_new=819,751 shots at each of eight times,
    total=6,558,008 fresh measurement shots.      (M18)

This lowers the sufficient count by nearly a factor10,000 while retaining
99% simultaneous sampling confidence, the same independently calibrated
source family, and four separate apparatus-error allocations. The measured
decision remains (M11) with eta_new and the selected I_new. Its worst-case
source success margin obeys

    |det Ahat|-T_hat >2.351603982743266.          (M19)

This is an illustrative improvement, not an optimized experiment or an
achieved detector budget. Longer free evolution raises the burden on control,
stability and (M6), and total calibration/reset/cooling/preparation costs are
still outside the measurement-shot count. The experiment could investigate
better concentration bounds or receivers; none is needed for this certificate.

## M7. Physical status and next breadcrumb

The source law, field protection, detector spectrum, interval timing/error
transfer, and finite-shot count are mathematically specified and independently
replayed. A physical instrument still has to prepare its named coherent modes,
certify the source-plus-field error and independent shared calibration, perform
the specified receiver rotation, bound unwanted couplings, and establish reset
and independence. Endpoint placements 1 and 3 remain source-cyclic for all
g_H>=0; placement 0 has the retained blind-mode exception at g_H=1/164.
Source cyclicity supplies an access breadcrumb, not a pulse-control or detector
fidelity construction. The large conservative shot count is now visible and
can guide a later receiver/cadence optimization rather than being hidden in
the phrase 'eight samples.'
