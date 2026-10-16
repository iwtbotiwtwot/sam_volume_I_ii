"""Editable expanded Chapter II reader manuscript, source-bound 15 October 2026.

Original sections1-14 retained verbatim. Remaining chapters integrate prior
continuation results with compact derivations and physical instrument budgets.
"""
from pathlib import Path
import json
from continuation_content import PAGES as CONT
TITLE='Retention, accumulation, and the finite ledger'
ABSTRACT=('A retained account can outlast its present address. Original Write, interacting-clock, spin and outgoing-field results distinguish predictive state, timed history and energetic complement. This development adds source-linked spectral predictions, compact memory and monitor derivations, exact finite-source nonclosure certificates, a worked paid-reference protocol, and an eight-time ensemble measurement with explicit apparatus and sampling budgets. Signed phases, full source energy and physical calibration remain in the same account.')

# Replaced by the final source batch summary before release; no stabilization
# or all54 extension is inferred from the current point pilot.
CLOSURE_TEXT=('The literal finite-source point certificate for V001_BASE reaches rank at least ten through both seeds and power four. It establishes a rank-two outgoing residual after the seven-dimensional enlargement, a nine-dimensional next span, and a further nonzero residual. Exact stabilization has not been reached. The final source-batch certificate determines the preparation coverage reported here.')
final=Path(__file__).resolve().parent/'FINAL_CLOSURE.json'
if final.exists():
    data=json.loads(final.read_text())
    CLOSURE_TEXT=data.get('chapter_summary',CLOSURE_TEXT)

PAGES=CONT[:7]+[
(CONT[7][0],CONT[7][1]),
(CONT[8][0],r'''
## 18. Eight expectation values and a rank test

An autonomous closed two-state source, fixed preparation and fixed linear receiver have equally spaced expectations

$$y_n=c+a\cos(n\vartheta)+b\sin(n\vartheta).$$

Form first differences d_n=y_(n+1)-y_n from eight means and the four-by-four difference-Hankel H_ij=d_(i+j). The constant disappears and the two exponentials give rank at most two. A nonzero three-by-three minor distinguishes the protected source record from this class. Eight means are not eight individual shots. [11,12]

The earlier cadence supplied a determinant separated from zero at a per-mean allowance of 0.0001. Source-guided cadence selection now allows 0.01 under the same independently declared calibration family. It trades a longer coherent evolution for fewer repeated preparations; the physical stability cost stays explicit.

The next sections state the exact retained-memory recipient before specifying the preparation, readout, errors and shot counts for this test. Driven or open two-state sources and arbitrary multilevel sources remain distinct comparison classes.
'''),
(r'''
## 19. Eliminate the hidden block exactly

Let A be the original finite self-adjoint positive generator, Pi the retained orthogonal projection, and Q=I-Pi. On retained and hidden coordinates p,q, write B=Pi A Pi, C=Q A Pi, D=Q A Q. Then

$$\dot p=-Bp-C^*q,\qquad\dot q=-Cp-Dq.$$

Variation of constants gives

$$q(t)=e^{-Dt}q_0-\int_0^t e^{-D(t-s)}Cp(s)\,ds.$$

Substitution retains both the initially hidden state and its feedback:

$$\dot p=-Bp-C^*e^{-Dt}q_0$$
$$+\int_0^t M(t-s)p(s)\,ds,\quad M(t)=C^*e^{-Dt}C.$$

For initially retained data, differentiating twice gives Pi A squared Pi=B squared+C†C. Thus equality of compressed evolution and exp(-Bt) for every retained preparation forces C†C=0, hence C=0. Conversely C=0 decouples the equations. Exact autonomous closure is therefore equivalent to invariance AV contained in V. [12]

For v in V, its initial memory strength is exactly ||QAv|| squared. Memory comes from the actual omitted source directions, not from a fitted delay term.
''',r'''
## 20. Normalize the residual in its source Gram

Let b be a nonorthonormal retained basis with Gram G>0. Put D_b and T_b equal to the source inner-product matrices shown below. Projection gives

$$D_b=\langle b,Ab\rangle,\quad T_b=\langle Ab,Ab\rangle.$$

$$L_b=T_b-D_bG^{-1}D_b,$$
$$K_0=G^{-1/2}L_bG^{-1/2}=C^*C$$

in an orthonormal chart. Rank(L_b)=rank(C); the physical memory norm is the largest generalized eigenvalue of L_b v=lambda Gv. Ordinary eigenvalues of the unnormalized residual matrix do not supply that norm.

Suppose the original invariant exchange-odd sector has gamma I<=A<=N I. Apply variation of constants once more to the retained equation with q0=0. The evolution defect is a double integral with factors exp[-B(t-s)], C†, exp[-D(s-r)], C and Pi exp(-Ar). Their three time intervals sum to t. Consequently

$$\|\Pi e^{-At}|_V-e^{-Bt}\|$$
$$\leq\frac{t^2}{2}e^{-\gamma t}\|K_0\|.$$

Using A<=N I also bounds the difference from its quadratic term by N t cubed ||K0||/2. These are original A-time bounds; the expected attempt count is Nt. A physical time calibration remains separate. [12]
'''),
(r'''
## 21. Continue the actual spin closure

The completed five-function spin span equals

$$V_5=\operatorname{span}(d,e,Ad,Ae,A^2d).$$

Leading-one residual coordinates make the first enlargement exactly

$$V_7=\operatorname{span}(V_5,A^2e,A^3d).$$

The earlier all-54 preparation certificate established dim V7=7. The next two possible outgoing functions are A cubed e and A to the fourth d. A literal full-source point certificate computes their rank rather than assuming the enlargement closes. [7,11,12]

'''+CLOSURE_TEXT+r'''

All original sites, Gibbs weights, self-excluded fields, accepted flip rates and attempt clocks remain present. The evaluator lumps only exactly exchangeable background-site classes and retains their exact multiplicities. This is a full finite-source calculation, distinct from the earlier conditional twenty-site contraction.

The minimum invariant closure is the Krylov union V+AV+A squared V+... . Exact rank stabilization, or a source minimal-polynomial identity, is the stopping condition.

In the deeper selected source, the natural retained dimensions advance 5,7,9,11,13, each with a nonzero outgoing residual. The fourteen-column certificate makes V13 nonclosed because A to the sixth e remains independent. Also M7(t)=C7 adjoint exp(-D7 t)C7 has rank two at every finite time: the hidden exponential is strictly positive in this finite source. This is a kernel-rank statement, not a rank statement for the propagation error.
''',r'''
## 22. Compact certificates and an invariant upper span

Evaluate m source functions at m literal configurations and form M. A nonzero certified determinant establishes their independence pointwise. Every configuration has positive mass in the original finite Gibbs law, so this is independence in that same physical source Hilbert space.

For M=[V7,A cubed e], the last row lambda of M inverse annihilates V7 and reads A cubed e as one. For r=Q7 A cubed e,

$$1\leq\left[\sum_i\frac{|\lambda_i|^2}{\pi(x_i)}\right]\|r\|^2.$$

If the original Gibbs log weights lie within plus or minus L after a common constant is removed, pi(x)>=exp[-N log2-2L]. Hence

$$\|r\|^2\geq\frac{e^{-N\log2-2L}}{\sum_i|\lambda_i|^2}>0.$$

Two inverse witness rows similarly give a positive two-by-two residual-Gram lower bound. This certifies nonclosure in the original Gibbs norm, without assigning a useful approximation size to that very conservative lower bound. [12]

An explicit invariant upper space retains all labelled twenty-site core configurations and counts each exchangeable background block:

$$D_{\rm lump}=2^{20}(F_b+1)$$
$$\times\binom{P_b+2}{2}\binom{T_b+3}{3}.$$

Its dimensions have 96 to 342 decimal digits across the 54 original preparations. This finite upper closure does not assert that the d/e seeds reach it.
'''),
(r'''
## 23. The nonzero-clock reference account

The inherited amplitude bound constrains a simple occupation-compensating reference. Put r=1-n. If actual clock amplitude is at least m>0,

$$\frac{1-\sqrt{1-m^2}}{2}\leq r\leq\frac{1+\sqrt{1-m^2}}{2}.$$

The explicit reference state

$$|r\rangle=\sqrt{n}|0\rangle+\sqrt{1-n}e^{-i\gamma}|1\rangle$$

has connection (1-n)d gamma, even when n changes differentiably: its real amplitude-derivative terms cancel. It restores the occupation coefficient in the receiving lift while keeping the joint-state Berry form. It does not automatically receive that remaining form. [11]

For actual lane01 this reference occupation lies approximately between 0.499975039 and 0.500024961. This is a recipient-specific action bound. The next construction instead receives the entire actual joint-state contribution with a balanced reference and a measurable relative phase.

Finite-energy overlap derivatives suffice for the actual continuum trajectory. No additional assumption that its initial vector belongs to the strong operator domain is inserted.
''',r'''
## 24. A reference retaining the actual energy

Retain the unchanged Chapter I joint H and its preparation Psi0. Its conserved form energy E includes the even source energy, full field, both counterterms and joint correlations. For prescribed legal phase rates, put

$$w=\dot\gamma+3\dot\chi,\quad h_R=2(w-E)P_R.$$

The balanced reference has relative phase beta_dot=2(w-E). The product trajectory retains precisely the original source-field marginal. Its canonical connection is

$$E\,d\tau+\frac{1}{2}d\beta=d\gamma+3d\chi.$$

For the actual lane01 preparation, H=epsilon e01 I+epsilon S+K, with K>=0 and preparation expectation of K at most Kprep. Therefore

$$\epsilon e_{01}-\epsilon\leq E$$
$$\leq\epsilon e_{01}+\epsilon+K_{\rm prep}.$$

The exact rational certificates enclose E within [0.917629340281369063, 0.917632830384309734]. Equivalently E=epsilon e01+(E0+E1)/2+c_soft for the retained hard branches and full soft vacuum. This uses the actual continuum preparation, rather than the earlier finite-qubit diagnostic. Physical energy is hbar E/t_u. [2,12]
'''),
(r'''
## 25. One original forward/reverse/wait protocol

Keep activation B=1, A_path=0 and the declared diagnostic source ratio R_H/(c t_u)=1/10. R_H is the original source radius; its incidence with the field radius stays explicit. Starting at 000, apply W1+ to 100, W1- back to 000, then wait four model-time units.

The lifted phi_b=phi_p=0. Thus gamma=delta=phi_a rises from 0 to pi/2 and returns to 0; chi=0. Original signed actions are +pi hbar/2, -pi hbar/2 and zero. With ell increasing along either traversal,

$$f(\ell)=\frac{12\sqrt{68-32\cos\ell}}{100-32\cos\ell+4\cos^2\ell},$$
$$d\tau=\frac{f(\ell)}{10}d\ell,\qquad v=10/f.$$

Both active durations equal T=0.158555895876030285... . The forward integral is retained from H02; H05 supplies its reverse after a common-phase shift. Native intervals overlap, and exact path reversal identifies their positive durations. [12]

The general source-paced instrument uses w=sigma v_j, including its original positive path clock. A phase-threshold receiving schedule agrees with it only when v_j=(M/3)nu(t). Signed role phase, elapsed source time and actual current phase remain separate operands.
''',r'''
## 26. Entry, matching and release stay distinct

Start the reference balanced with hR=0. Over external entry a=0.01, hold 000 and ramp hR=2(10-E)(s/a)P. During the forward/reverse/wait intervals use 2(w-E)P. Apply the recorded sudden changes at event boundaries. After the wait, release over b=0.01 with hR=-2E(1-s/b)P. These ramps are outside ledger matching.

| Event | tau | beta |
|---|---|---|
| Start |a|.1-Ea|
| Forward |a+T|.1+pi-E(a+2T)|
| Reverse |a+2T|.1-E(a+4T)|
| Wait |a+2T+4|.1-E(a+4T+8)|
| Release |a+2T+4+b|.1-E(a+b+4T+8)|

Source wait has w=0 and hR=-2EP; it is not reference off. The wait winds beta by -8E, more than one full turn. Actual theta advances throughout and is enclosed at every boundary by [ell01 tau_lower,u01 tau_upper].

The final tau is4.337111791752060571... . Final actual theta lies in[0.000015136966570142,0.000015136966591669], while beta lies in[-7.841399681709530363,-7.841369477578352354]. The two phases record different quantities. [12]
'''),
(r'''
## 27. Every switch and continuous-drive payment

On the balanced reference, energy is w-E and variance is(w-E) squared; mean drive work is dw. The original path has v0=10, vL=125/(3 sqrt17), and vmin=9.810320323234103... at cos ell*=(11-sqrt73)/4. Its interior minimum splits each drive into two monotone pieces. [12]

| Reference work piece | Work in hbar/t_u |
|---|---|
| External entry |10-E|
| Forward first piece |vmin-10|
| Forward second piece |vL-vmin|
| Forward to reverse |-2vL|
| Reverse first piece |vL-vmin|
| Reverse second piece |vmin-10|
| Reverse to wait |10|
| Wait |0 drive work|
| External release |E|

The signed sum is zero, but positive and withdrawn work each equal 2vL+2(10-vmin), approximately 20.590661439892877 . Recoverable exchange and irreversible apparatus cost are distinct accounts.

Adding a nonnegative-Hamiltonian baseline adds canonical payment C=pi+2ET+8E+Eb. The total variational form still subtracts energy and vanishes on its own exact driven trajectory. Switching cancellation supplies no zero-cost apparatus claim.
''',r'''
## 28. Read the phase and keep its turn counter

Independent prefix preparations measure X=cos beta and Y=-sin beta. Use atan2(-Yhat,Xhat), then nearest-branch continuation from beta0=0. An endpoint qubit alone records phase modulo2pi; an external counter keeps its turns.

Include all boundaries and a grid with gaps at most 0.01: no more than 441 prefixes. Since E<1 and v<=50/3, |beta_dot|<=106/3. Coordinate errors<=1/16 imply angular errors<1/8 rad. Consecutive true advances plus both angular errors obey

$$53/150+1/4<\pi,$$

so the unwrapped branch is unique. Correct branch choices leave each prefix error below1/8 without summing all prefix errors into drift.

Allocate coordinate tolerance as systematic1/32 plus statistical1/32. Four systematic budgets of1/128 cover reference preparation, evolution/waveform, readout and timing. Sufficient conditions are trace-distance and Duhamel bounds<=1/256, Pauli-readout norm error<=1/128 and trigger error<=3/13568 model time.

With 26,624 independent shots per coordinate and prefix, the simultaneous statistical failure is below1%. Maximum fresh preparations are 23,482,368. Each readout disturbs that copy; fresh prefixes retain the history. Source energy and continuum preparation require their own retained energy-form control. [12]
'''),
(r'''
## 29. Specify the protected-coherence instrument

Write |a> for the protected state |qa qa>. Prepare

$$|\psi\rangle=(|0\rangle+|1\rangle+|2\rangle)/\sqrt{3}$$

with the field vacuum. D,C and their counterterms annihilate this protected span under the full retained Hamiltonian. The adjacent-coherence receiver is

$$O=|0\rangle\langle1|+|1\rangle\langle0|$$
$$+|1\rangle\langle2|+|2\rangle\langle1|.$$

Its outcomes are +sqrt2,-sqrt2,0. Corresponding vectors in the three-state basis are (1,sqrt2,1)/2, (1,-sqrt2,1)/2 and (1,0,-1)/sqrt2; complementary outcomes report zero. A source-basis rotation followed by this projective readout specifies a mathematical instrument. [12]

Its expectation is y(t)=(2/3)[cos(omega10 t)+cos(omega21 t)]. Every sampling time receives fresh preparations. Measuring one copy changes its state and cannot supply its next undisturbed expectation.

The required physical coherent mode access, receiver pulse, field preparation, reset and cooling belong to the apparatus. The complete error budget below assigns their permitted effects before using a sample rank.
''',r'''
## 30. Charge leakage, disturbance and timing

Use trace distance D(rho,sigma)=||rho-sigma||1/2. Preparation distance d_prep gives expectation bias<=2 sqrt2 d_prep. Leakage l and conditional error d_cond satisfy

$$d_{\rm prep}\leq\sqrt{l}+d_{\rm cond}.$$

Leakage alone does not specify the state inside the protected space or its field preparation. An effective measured observable M with ||M-O||<=b_read includes pulse disturbance and outcome assignment in its readout bias.

Unwanted dynamics contributes at most 2 sqrt2 kappa, where

$$\kappa=\int\|\delta H(s)\psi_{\rm ideal}(s)\|\,ds/\hbar.$$

This bound extends through the latest allowed trigger. A source-only finite-matrix norm does not bound an unbounded field interaction.

The retained independent calibration is Xi=1382784 plus or minus one and alpha/alpha_nominal=1 plus or minus one part per million. It gives |y'|<=L with

$$L<114081.396605\,\alpha_{\rm nominal}.$$

Trigger error delta_t contributes L delta_t. Calibration uncertainty is already part of the ideal source family; it is not charged again as timing jitter. [12]
'''),
(r'''
## 31. A cadence selected from the source

Before acquiring the target record, choose

$$h=\frac{5\pi}{2\alpha_{\rm nominal}D_{\rm nominal}},$$
$$D_{\rm nominal}=6348467821812271/80000000000,$$

and t_k=kh for k=0,...,7. This h is 7.5 times the earlier cadence and was selected from a declared finite list using only the retained source. Both sampled frequencies remain distinct and nonaliased. For the three-by-three difference minor A with index set I={0,2,3},

$$5.318723982743267<\det A<5.941782789331066,$$
$$|A_{ij}|<2.$$

For per-expectation allowance eta=0.01, the conservative two-record determinant perturbation bound is

$$72\eta(2+4\eta)^2=2.996352,$$

below the certified lower determinant. This source-selected cadence exchanges a longer stability interval for substantially fewer shots. It is not fitted to measured target data. [12]

Allocate 0.001 each to preparation, unwanted evolution, effective readout and timing, leaving 0.006 for statistical error. The next section turns this allocation into explicit measurement counts and a decision rule.
''',r'''
## 32. Repetitions and an operational decision

Sufficient apparatus conditions are d_prep,kappa<=0.001/(2 sqrt2), ||M-O||<=0.001 and delta_t<=8.76567e-9/alpha_nominal. If conditional preparation is exact, coherent leakage l<=1.25e-7 suffices. These are requirements rather than achieved precision. [12]

For N independent outcomes in[-sqrt2,sqrt2] and eight means, Hoeffding and a union bound give

$$P(\mathrm{any\ mean\ error}>s)\leq16e^{-Ns^2/4}.$$

At s=0.006 and failure allowance 0.01, N=819,751 fresh shots per time suffice: 6,558,008 total. Calibration failures add their probability to that sampling allowance. The earlier 0.0001 allocation would need 8,197,509,899 shots per time under the same split.

Form measured differences, Ahat_ij=dhat_(I_i+I_j), and Bhat=max|Ahat_ij|. Reject the stated closed two-state class when

$$|\det\widehat A|>36\eta(\widehat B+2\eta)^2.$$

Each entry error is<=2eta. Telescoping each product of three entries across six determinant terms gives this threshold because every ideal two-state minor vanishes. The calibrated target exceeds it by more than 2.35160 on the stated simultaneous sampling event, conditional on the apparatus bounds.
'''),
(r'''
## 33. The minimum counter count

For polynomial phase receivers through degree d, retain M_jk=integral theta^k 1_j d theta, and the corresponding event-atomic sums when required. A segment alpha to beta adds(beta^(k+1)-alpha^(k+1))/(k+1), clipped to each specified gate. Actual phase endpoints suffice; no constant-rate approximation is used. [11]

Here is the rank derivation of minimality. Collect required additive receiver values into F(h) and subtract F(h0) when initial endpoints and total duration/count are supplied. Let V be the span of these contrasts with dimension r. A summary with c linear counters and a linear decoder must be injective on V; otherwise a nonzero receiver contrast disappears. Rank-nullity therefore gives c>=r. Coordinates in any basis of V attain r.

Known endpoint identities reduce r. For fixed event addresses theta_n=hn and N events, summing labels at each degree gives h^k sum n^k, already determined by N. Overlapping gates or permitted source histories can supply further constraints.

This is exact minimality for the admitted linear additive receiver class. Online continuation also retains predictive state and current phase; a finite-family contrast basis alone is not a transition-closed realization for every future history.

Counter dimension does not bound precision or stored bit count, and makes no minimum claim for unrestricted nonlinear memory.
''',r'''
## 34. ABBA/BAAB with actual event offsets

Use the original closed blocks A=(W1+)^4 and B=(W7+)^4. Every block returns to 000. In one repeated source context their positive durations are T_A,T_B; retain each internal event offset u. The A-block starts in ABBA are {0,T_A+2T_B}; in BAAB they are {T_B,T_B+T_A}. Their sums agree, while

$$\sum_{ABBA}(s+u)^2-\sum_{BAAB}(s+u)^2$$
$$=2T_B(T_A+T_B).$$

Expansion cancels both 2u sum s and 2u squared. B-block starts similarly have equal sums, with squared-sum difference -2T_A(T_A+T_B). Each of three A-only output points occurs once per A; the common point occurs once per A and four times per B. Its difference is consequently 2(T_A+T_B)(T_B-4T_A). [11]

Counts, endpoints and first physical-time atomic moments agree, while second moments distinguish the histories even with unequal durations. Under the prescribed equal phase-step schedule the A-only differences are 64h squared and the common-point difference is -192h squared.

Prouhet closed-block reorderings extend the phase-event distinction beyond every finite polynomial degree. Nonlinear transport from physical time to actual phase retains original time arguments; it does not automatically preserve unweighted phase moments.
'''),
(r'''
## 35. An attainable source record has a price

For positive B and record r=L†y, let y_star be its ambient energy minimizer and G=L† B inverse L. If F_r is the permitted microscopic displacement set, projection orthogonality gives

$$\min_{y\in F_r}y^*By=r^*G^+r$$
$$+\min_{y\in F_r}\|y-y_\star\|_B^2.$$

Indeed L†(y-y_star)=0, and By_star lies in range(L), so the cross term vanishes. The second term is the realizability correction. A finite nonempty permitted set attains its minimum; an empty compatible set has no allowed endpoint. [11]

For the original eighteen-coordinate literal energy and fixed outside spin configuration, permitted port displacements are(0,0,e_z-e_0). Every signed cross term is retained. The diagnostic record is(-1,0) under the two declared receiver columns, distinct from the complete original receiver family.

| Payment / kappa_E | Value |
|---|---|
| Ambient minimum |0.987626515|
| Pure-source minimum |1.894317938|
| Realizability correction |0.906691423|

The source minimum is 1085537/573049. The complete endpoint enumeration supplies its certificate in the next section.
''',r'''
## 36. Every endpoint and the feasible minimum

The diagnostic reads the e0 and e1 coordinates. A displacement from z0 has record(-1,0) exactly for z=2,...,15. The table gives numerator of cost/kappa_E over denominator573049; z15 has numerator 1146098. [11]

| z | Record | Numerator | One flip? |
|---|---|---|---|
|0|(0,0)|0|reference|
|1|(-1,1)|2006049|yes|
|2|(-1,0)|1085537|yes|
|3|(-1,0)|1146097|no|
|4|(-1,0)|2006049|yes|
|5|(-1,0)|4965618|no|
|6|(-1,0)|2155185|no|
|7|(-1,0)|2163505|no|
|8|(-1,0)|1085537|yes|
|9|(-1,0)|2155185|no|
|10|(-1,0)|1142898|no|
|11|(-1,0)|1146097|no|
|12|(-1,0)|1146097|no|
|13|(-1,0)|2163505|no|
|14|(-1,0)|1146097|no|
|15|(-1,0)|1146098|no|

Thus z2 and z8 attain the smallest cost on the nonzero record fiber(-1,0); both are single accepted port flips. z0 and z1 cannot realize this record. Outside-coordinate changes add nonnegative squares and cannot lower the attained fixed-outside minimum.

Mixtures retaining this exact record obey the same endpoint floor for expected quadratic payment. Energy of mean displacement is a different quantity and retains covariance. Preparation and physical kappa_E remain separate apparatus assignments.
'''),
(r'''
## 37. Calibrate the paid protocol

The ideal paid reference uses actual E. The present source certificates also give a numerical control: take their exact rational energy midpoint Ehat and replace E by Ehat in every reference waveform. Then

$$|E-\widehat E|<1.746\times10^{-6}.$$

The total connection on matching intervals becomes [w+(E-Ehat)]d tau. Across the complete forward/reverse/wait program its signed-ledger bias is below 7.54e-6 hbar. The source energy stays E; its calibration residual remains visible. [12]

The entry and release canonical integrals are (E+10)a/2 and Eb/2 for exact calibration. They are external to the signed Write ledger. A reconstructed matching action with interval U, energy error dE, time error dt and endpoint angular errors eta obeys the conservative allowance

$$U\,dE+(|E|+dE)\,dt+\eta.$$

An actuator using a finite-time turnaround in place of a sudden quench adds its own interval, phase and work. It cannot silently reuse the ideal endpoint account. Actual clock certificates continue to apply only while its original source-field H and preparation are retained.
''',r'''
## 38. Pay for the controller

The specified waveform is an externally driven instrument. A material autonomous controller must produce its schedule, store or recover work and retain the phase-turn record. When coupled to the quantum source or reference it can also become entangled; the enlarged Hamiltonian then determines the clock and energy account.

The protocol has made the required work exchange finite and explicit. It has not assigned a cost to original source actuation, waveform generation, qubit preparation, readout rotations, detector reset, external-counter memory or cooling. Their physical models supply those further payments. Recovering equal positive and negative reference work does not determine their dissipation.

For the protected-coherence experiment, the independent common calibration fixes g_H through Xi and fixes epsilon through one absolute scale. The two-frequency record is then a prediction. Its source-guided cadence and apparatus tolerances specify what a proposed implementation must deliver.

These are concrete construction tasks with quantitative targets. They can receive hardware and channel assignments while preserving the original signed source response, phase lift, full field and energetic complement. [12]

The actual clock has a separate receiver. Divide its D and C expectations by signed d01<0 to obtain the complex current z; theta=-arg z. Its certified amplitude exceeds 0.999999998. Fresh source copies can estimate those two bounded Pauli coordinates, then unwrap -atan2(Im z,Re z). Their sampling and apparatus allowances are additional. The theta intervals in this protocol are predicted from retained actual-rate bounds; reference-qubit measurements read beta.
'''),
(r'''
## 39. The operation determines the retained account

A uniform A0 remains in a total account while gradients and shared endpoint differences remove it. A raw lapse ratio instead rescales lifts through background normalization; a source-normalized local lapse declares a different input. Every readout retains its operation and reference. [1,9]

The source comparison sharpens this lesson. Current clocks leave the commuting pair-product energy unread. Protected coherence receives that energy, linked to the lane family by a common calibration.

Memory gives the dynamical version: a retained span evolves autonomously exactly when it is invariant. The actual seven-dimensional spin enlargement has further outgoing directions; the new point certificates state how far its exact rank reaches. The invariant upper lumping retains the finite source without identifying it as the smallest closure.

History moments identify what a later receiver needs, and feasible endpoint costs identify an attainable payment. The paid reference now has one complete timed Write/inverse/wait program, all reference work pieces, a winding record and a fresh-copy measurement budget. Physical realization can build directly on these specified quantities.
''',r'''
## 40. Sources and reproducibility

The source package retains the original draft, completed Chapter I and prior Chapter II development sources. Editable typesetting, bundled fonts, exact operands, native receipts and independent offline checks accompany this reader. Every calculation retains its source preparation and units. [12]

[1] Owner Chapter II draft and verification ZIP,15 October 2026.

[2] Final Chapter I and actual full-field clocks; H002628/H002630.

[3] Native history reduction; H002165.

[4] Observed-history clock/ruler recipient; H002559.

[5] Original Write/tensor/action map; H002623.

[6] Radiative memory and complete work; H002319.

[7] Completed spin source-action T5; H002627.

[8] Common spin energy and receivers; H002423.

[9] Original Chapter II packet CR001/002/003/005 and local CR113/114/115/218/238.

[10] Chapter II first development; H002634.

[11] Chapter II continuation, two 180-second Duck rounds; H002635.

[12] voli_chapter2_physical3_20261015: current source-bound physical-development packet. New mathematical constructions: Codex. Sean Brady: originator/conceptual director. OpenAI ChatGPT and Codex: research collaborators and co-authors.
''')]
