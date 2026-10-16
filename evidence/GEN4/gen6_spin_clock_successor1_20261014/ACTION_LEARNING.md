# Learning an action from source histories

Date: 2026-10-14. Author: Codex, following Sean Brady's direction to extend
the spin integration transfer and use its results for source-first action
research. This is an analytical development accompanying the successor.
Original runs and the mathematical core are unchanged.

All five H02–H06 successor trajectories now complete and independently
reproduce: 4,781 prepared native steps and 80,940 independent checks. The
actual source-clock order effect, reverse-path duration and a cross-case
reuse identity below guide the source-action work.

## What the integration transfer lets us ask

The useful source object is already richer than a scalar action: a signed
Write, its continuous phase path, the contact witness along that path, its
positive duration, and the retained order of completed events. Certified
integration makes the continuous part available to the existing receiver.

The next action construction can therefore begin with three objects that are
separately determined: a phase-action one-form, a source-path metric, and a
clock map. Their coefficients and their different behavior under reversal
can be followed into a common history calculation. This gives a concrete
alternative to beginning with the frozen quadratic action family.

The equations below distinguish source statements from Codex deductions.
They introduce no fit to the withheld cases.

## 1. The source already fixes a metric and an action one-form

**Source:** [H001083 local action derivation](../../SAM_REVIEW/campaigns/RH_LOCAL_ACTION_ACTIVATION1/DERIVATION.md),
sections 1–3, and [AN0005](../../CURRENT_REVISION/engines/SLC/gen2/dependencies/write_sources/AN0005_CEFF_SUBSTRATE_RATE_AND_SECONDS_PER_WRITE.md),
sections 1, 3 and 5. Write the lifted phases as
\(\theta=(\phi_a,\phi_b,\phi_p)\), with the native address equal to the
quarter-turn phase modulo four. At fixed activation \(B\),

\[
C_a=-2B e^{i(\phi_a-\phi_p)},\quad
C_b=2B e^{i(\phi_b-\phi_p)},\quad
E_B=6+\Re(C_a+C_b),\quad
u=\log(E_B/6),\quad g=\nabla_\theta E_B.
\]

Here \(E_B\) is the native contact account. Its physical-energy map is a
separate source-reception question; the numeral 6 is the fixed contact
reference, not a physical mass or an accumulation floor.

The role-\(j\) source chart and one-form are

\[
X_j=R_H(\operatorname{sech}u\cos\phi_j,
          \operatorname{sech}u\sin\phi_j,-\tanh u),
\qquad \omega_j=\hbar\,d\phi_j.
\]

**Codex deduction — full pullback, rather than just a sampled density:**

\[
ds_j^2=d\theta^T G^{(j)}(\theta)d\theta,\qquad
G^{(j)}=R_H^2\operatorname{sech}^2u
\left[\frac{gg^T}{E_B^2}+e_je_j^T\right]. \tag{1}
\]

Every entry follows from the declared chart and signed contact witness.
The metric has rank at most two because this is one role's sphere chart;
it need not be promoted to a nonsingular kinetic metric on all phases.
The retained role and phase lift specify which chart is being used.

For a pure active stroke \(d\theta=\sigma e_j\,d\ell\), with
\(d\ell\ge0\) and \(\sigma=\pm1\),

\[
\mathcal D_j^{-2}=\operatorname{sech}^2u
\left[1+(g_j/E_B)^2\right],\quad
ds_j=\frac{R_H}{\mathcal D_j}d\ell,\quad
dS_j=\sigma\hbar\,d\ell. \tag{2}
\]

The source effective-speed map \(ds_{\rm native}/dt=c(1-A_{\rm path})\)
therefore gives

\[
dt=\frac{R_H\,d\ell}
 {c(1-A_{\rm path})\mathcal D_j(\theta)},\qquad
\frac{d\theta}{dt}=\sigma e_j
 \frac{c(1-A_{\rm path})\mathcal D_j(\theta)}{R_H}. \tag{3}
\]

The clock uses the positive path length. A reverse traversal reverses the
signed action and preserves its duration when the same path, activation,
radius and accumulation context are used. The completed quarter has signed
action \(\sigma\pi\hbar/2\) even while its local metric and action density
vary. These are deductions from the source equations, not new acceptance
criteria for the successor.

For a general role-projected path \(\theta(s)\), the same calculation is

\[
T_j[\theta]=\frac{R_H}{c}\int
\frac{\operatorname{sech}u}
 {1-A_{\rm path}}\sqrt{(u')^2+(\phi_j')^2}\,ds,\qquad
S_j[\theta]=\hbar\int\phi_j'\,ds. \tag{4}
\]

Both are invariant under an orientation-preserving reparameterization.
One is a positive path-length clock; the other retains signed phase and
winding. Their joint information is available before any separate
reservoir inertia is selected.

## 2. An exact contact Hessian provides a coefficient-origin calculation

Let \(a=(1,0,-1)^T\) and \(b=(0,1,-1)^T\). Directly differentiating the
source contact account gives

\[
H_E=\nabla_\theta^2E_B
=2B\cos(\phi_a-\phi_p)aa^T
 -2B\cos(\phi_b-\phi_p)bb^T. \tag{5}
\]

**Codex deduction:** the two coefficient magnitudes, signs, cross terms and
common-phase null direction \(H_E(1,1,1)^T=0\) follow together from the
source couplings. They should be received together. Keeping only diagonal
curvatures would discard source information that is already known.

The phase-action form and chart can still see common-phase motion: the
contact account's null direction does not erase a completed role phase or
its retained winding. Thus contact curvature alone is not the whole action
or the whole metric.

For a source-to-receiver coordinate map \(\theta=F(x)\), the complete
pullback Hessian of the contact account is

\[
\nabla_x^2(E_B\circ F)
=J_F^T H_EJ_F+\sum_k g_k\,\nabla_x^2F_k. \tag{6}
\]

The second term vanishes for an affine map or at a stationary contact
point. Away from those cases it is part of the received coefficient, not
a counterterm to be chosen after seeing a result. If a source supplies a
physical energy map \(U(x)=\mathscr E(E_B(F(x)))\), its curvature is

\[
\nabla_x^2U=\mathscr E'\nabla_x^2(E_B\circ F)
 +\mathscr E''\nabla_x(E_B\circ F)\nabla_x(E_B\circ F)^T. \tag{7}
\]

For a supplied linear energy conversion, only its multiplicative factor
remains. A nonlinear conversion contributes the displayed additional
term. This gives a concrete route to the full received potential block,
including mixed and field-boundary terms, before comparing with the frozen
\(gJ^TB_{68}J\) block. The incidence \(F\), physical-energy map and field
boundary map still need their source assignments.

## 3. H02/H03 isolate a source-clock circulation

The supplied H02 and H03 source histories start at the same state, perform
\(W1+\) and \(W4-\) in opposite orders, and reach the same native endpoint.
Use positive phase-progress coordinates
\(x=\phi_a\), \(y=-\phi_b\), with \(\phi_p=0\), on the square
\([0,\pi/2]^2\). At \(B=1\), the contact account throughout that square is

\[
E_B(x,y)=6-2\cos x+2\cos y.
\]

Define the source clock factors
\(f_a=1/[(1-A_{\rm path})\mathcal D_a]\) and
\(f_b=1/[(1-A_{\rm path})\mathcal D_b]\). The histories use the two
axis-ordered paths around this square. For their unchanged common radius,
speed and accumulation context, their active durations satisfy the exact
**Codex deduction**

\[
T_{H02}-T_{H03}=\frac{R_H}{c}
\int_0^{\pi/2}\!\int_0^{\pi/2}
 \left(\partial_x f_b-\partial_y f_a\right)\,dx\,dy. \tag{8}
\]

This is the circulation of \(f_a dx+f_b dy\): one path goes in \(x\)
then \(y\), while the other goes in \(y\) then \(x\). Both have the
same signed phase-action sum. The clock difference can nevertheless arise
directly from the source geometry, before the frozen canonical flow is
applied. The measured sign and size will come from the returned native
integrals. Equation (8) provides a specific explanation to examine rather
than attributing every order effect to an unspecified extra dynamics.

At the retained constant accumulation, the integrand is also explicit.
For \(q_j=g_j\), define

\[
F(E,q)=\frac{12\sqrt{E^2+q^2}}{E^2+36},\qquad
F_E=\frac{12E(36-E^2-2q^2)}
 {(E^2+36)^2\sqrt{E^2+q^2}}.
\]

With \(q_a=2\sin x\), \(q_b=2\sin y\),

\[
\partial_x f_b-\partial_y f_a
=\frac{q_a F_E(E_B,q_b)+q_b F_E(E_B,q_a)}
 {1-A_{\rm path}}. \tag{9}
\]

This uses the existing source coefficients only. A varying accumulation
would contribute its own derivatives of \((1-A_{\rm path})^{-1}\),
which the full form of (8) already retains.

## 4. A conditional-history functional uses those coefficients directly

The one-form \(\hbar d\phi_j\) is locally exact. Its integral records
signed endpoints and retained winding; by itself it supplies no bulk
Euler–Lagrange evolution equation. The source contributes additional
kinematics through (3) and legal event selection. These can be represented
together without inventing a quadratic kinetic term.

**Codex construction:** on a history segment with supplied role \(j\),
orientation \(\sigma\), gate \(B\) and accumulation context, use a
supplied nonnegative phase-progress parameterization density \(\rho\), a
nonnegative declared wait density \(w\), and multipliers \(\pi,\epsilon\):

\[
\begin{split}
\mathcal S_{\rm cond}=\sum_{\rm segments}\int ds\,\Bigg[
 &\hbar e_j^T\theta'
 +\pi^T(\theta'-\sigma e_j\rho)\\
 &+\epsilon\left(t'-
 \frac{R_H\rho}{c(1-A_{\rm path})\mathcal D_j(\theta)}-w\right)
 \Bigg].
\end{split}\tag{10}
\]

Varying the multipliers enforces the existing event path and clock map.
On that path the multiplier terms vanish and the functional returns the
source phase action. A pure wait has \(\rho=0\), unchanged contact phase,
and increasing \(t\). The multipliers are constraint variables, not fitted
material coefficients. Equation (10) is a useful generating representation
of **conditioned, source-selected histories**. It does not choose the event
sequence, activation or waiting law.

This formulation suggests a practical action-building order: compose the
known continuous stroke maps and discrete completions first; then receive
the source law that selects events and couples the accumulation account.
The integration successor supplies the stroke maps now.

## 5. Proper-time recurrence can be joined without identifying unlike clocks

**Source:** [G643c/G642c chain](SOURCES_NEW.md),
[R000040 rate interpretation](../../SAM_RETRIEVAL/packets/R000040_G642C_N_WRITE_RATE_ACCOUNT_INTERPRETATION/INDEX.md)
and the source references in [SOURCE_ACTION.md](SOURCE_ACTION.md).
The source has standing-mode phase accumulation and contact-ledger intensity:

\[
d\psi=\frac{\lambda}{t_{\rm SW}}d\tau_{\rm res},\qquad
d\bar N=\Gamma_{\rm res}\,d\tau_{\rm res},\qquad
d\bar A_{\rm ledger}=A_0\Gamma_{\rm res}\,d\tau_{\rm res}. \tag{11}
\]

Bars here explicitly name the continuous rate account. They do not replace
the realized integer event history. The source supplies
\(A_0=1/(12\pi)\), \(E_{\rm mode}=\hbar\lambda/t_{\rm SW}\) and
\(N_{\rm eff}=1/A_0^2\). The full source functional for
\(\Gamma_{\rm res}=\sum_\mu\langle L_\mu^\dagger L_\mu\rangle D_\mu\)
remains to be received for these histories.

**Codex deduction:** with the specified clock conversion
\(\chi=d\tau_{\rm res}/dt\), the correctly typed composition is

\[
\dot\psi=\frac{\lambda}{t_{\rm SW}}\chi,\qquad
\dot{\bar N}=\Gamma_{\rm res}\chi,\qquad
\dot{\bar A}_{\rm ledger}=A_0\Gamma_{\rm res}\chi. \tag{12}
\]

Consequently a wait in the realized event program may retain a stationary
contact phase while standing-mode phase or contact exposure continues.
There is no need to equate a waiting intensity to the inverse duration of
an active quarter stroke. For constant intensity the recovered probability
law is \(1-e^{-\Gamma_{\rm res}\Delta\tau_{\rm res}}\); this alone does
not select the observed event order or an integer count.

A particularly useful receiving question is whether a given standing-mode
phase \(\psi\) and active role phase \(\phi_j\) are the **same phase
channel**. If a source supplies that identification, equations (3) and (12)
give the compatibility relation

\[
\frac{\lambda_j}{t_{\rm SW}}\chi
=\frac{c(1-A_{\rm path})}{R_H}\mathcal D_j,
\qquad
E_{\rm mode,j}=\frac{\hbar c(1-A_{\rm path})}
 {R_H\chi}\mathcal D_j. \tag{13}
\]

The formula compares positive phase rates; signed event orientation is
retained separately. It neither identifies \(E_B\) as physical energy nor
equates the AN0005 path accumulation with an endpoint-clock accumulation.
For a source-selected constant \(\lambda_j\), it identifies exactly which
combination of metric, radius, accumulation and clock conversion must be
constant. If the phases are distinct channels, (13) is not imposed and the
history retains both phases. This is a focused source-discovery question
with computable operands from the successor, rather than a demand for a
previously written unified action.
When the source identifies the phases as one channel, its two formulas
represent one action contribution. Separate contributions can be composed
when the source assigns distinct channels and their weights; this retains
the existing support-flow account without counting the same phase twice.

## 6. Contact intensity has a source-matrix route of its own

G642c stage 03 supplies the structural intensity
\(\Gamma_{\rm res}=\sum_\mu\langle L_\mu^\dagger L_\mu\rangle D_\mu\).
This already identifies a useful operator contraction. It does not require
borrowing the spin heatbath generator.

**Codex deduction:** for a supplied source state represented as
\(\Psi=\sum_i b_i z_i\), and supplied distinguishability weights \(D_\mu\),
form

\[
G_{ij}=\langle b_i,b_j\rangle,\quad
K_{ij}=\sum_\mu D_\mu\langle L_\mu b_i,L_\mu b_j\rangle,
\qquad \Gamma_{\rm res}=\frac{z^\dagger Kz}{z^\dagger Gz}. \tag{14}
\]

The denominator retains state normalization in a nonorthonormal source
basis. Nonnegative \(D_\mu\) make \(K\) positive semidefinite. If the
source's weights or operators depend on its state, that dependence stays
in \(K\); it is not replaced by a fixed matrix. A density-matrix source
uses the corresponding normalized trace instead of a pure-state ansatz.

Following R000040's direct source pointer gives actual example channels in
the [pinned G107 summary](https://github.com/iwtbotiwtwot/STAM_Model-A.v.1.0/blob/822f8f4241c1b0b7fb272eb30c1022dd860ea18c/tests/Substrate/G107_identify_Lmu_Dmu_decoherence/results/G107_Lmu_Dmu_decoherence_summary.md)
(Git blob `cac7e919790611585c569ce1eaf493f1caac1381`):

| Source channel | Operator | Distinguishability |
|---|---|---|
| Photon scattering | \(L_k=\sqrt{\gamma_k}\exp(ik\hat x)\) | \(1-\operatorname{sinc}(k\Delta x)\) |
| Gas collision | \(L_q=\sqrt{\Gamma_q}\exp(iq\hat x/\hbar)\) | \(1-\cos(q\Delta x/\hbar)\) |
| Detector absorption | \(L_i=\sqrt{\gamma_i}|i\rangle\langle i|\) | approximately one |

These examples use supplied environmental rates and separations. The
remaining reception task is to identify the applicable channel, its rate
and source state, and its relation to the original Write phase history.
Equation (14) then provides the received rate coefficients through source
contractions. The spin work's Gram construction and retained/complement
accounting are directly useful methods for that job.

**Further Codex deduction:** the first two operators have
\(L_\mu^\dagger L_\mu=\gamma_\mu I\) when their phase operator is
unitary. Their scalar intensity keeps the rate and distinguishability but
loses the operator's phase. Retaining \(L_\mu\) alongside its contraction
therefore matters for a phase-action calculation. For the detector channel,
the contraction instead keeps its source projector and the state population.
This gives an explicit source example of why equal aggregate rates need
not supply equal phase histories.

The retained operator phase also gives a direct action coefficient. For
constant transfer label \(k\) or \(q\), pull back its phase along a source
position path and use the original \(dS=\hbar d\phi\):

\[
U_k(x)=e^{ikx}\ \Longrightarrow\ dS_k=\hbar k\,dx,
\qquad
U_q(x)=e^{iqx/\hbar}\ \Longrightarrow\ dS_q=q\,dx. \tag{15}
\]

Thus the channel's spatial action-generator coefficient is \(\hbar k\)
or \(q\), before a native receiver coordinate is chosen. This matches the
\(p\,dx\) source one-form through G405's \(k=p/\hbar\) bridge. For
\(x=F(X)\), the coefficient received by \(dX\) is the exact pullback
\(\hbar k\,\nabla_XF\) or \(q\,\nabla_XF\). Retained phase lift keeps
the action's winding. The supplied rate amplitude determines a different
operand; it is not needed to recover this spatial phase coefficient.

Equation (15) derives the action carried by these source channels. Their
assignment to a specific native Write and the free/support temporal part
remain the subsequent composition tasks. The proposed route can therefore
start with actual channel phases rather than waiting for the scalar rate
account to determine an entire action.

There is also a concrete signed-action question. **If** the source event
map identifies a contact-channel completion with one native signed quarter
Write, its sign-resolved intensities \(\Gamma_{j,\sigma}\) give

\[
\frac{d\mathbb E S_{\rm Write}}{d\tau_{\rm res}}
 =\frac{\pi\hbar}{2}\sum_{j,\sigma}\sigma\Gamma_{j,\sigma},\quad
\frac{d\mathbb E |S|_{\rm event}}{d\tau_{\rm res}}
 =\frac{\pi\hbar}{2}\sum_{j,\sigma}\Gamma_{j,\sigma},\quad
\frac{d\bar A_{\rm ledger}}{d\tau_{\rm res}}
 =A_0\sum_{j,\sigma}\Gamma_{j,\sigma}. \tag{16}
\]

The absolute-event-action coefficient per ledger amount would then be
\(\pi\hbar/(2A_0)=6\pi^2\hbar\), determined by the two source
increments. Signed action additionally needs the signed channel balance.
This is a conditional derivation identifying a useful source-reception
task; it does not identify G107 contact counts with native quarter Writes
without that map. In particular, a scalar total intensity cannot recover
the signed action of a reversing history.

## 7. A field readout can inherit temporal evolution from its sources

The original field kernel in [SOURCE_ACTION.md](SOURCE_ACTION.md) is
\(A_{\rm environment}(x)=\sum_i 2GE_i/(c_{\rm physical}^4|x-x_i|)\).
Its source coordinates and energy assignments are therefore a concrete
receiving route for temporal field information.

**Codex chain-rule deduction:** evaluate this declared kernel along supplied
source histories and a supplied observation path, set
\(r_i=x-x_i\), and retain a common time coordinate. Then

\[
\frac{d A_{\rm environment}}{dt}
=\frac{2G}{c_{\rm physical}^4}\sum_i\left[
\frac{\dot E_i}{|r_i|}
-\frac{E_i\,r_i\!\cdot(\dot x-\dot x_i)}{|r_i|^3}
\right]. \tag{17}
\]

If \(x_i=F_i(\theta)\), their velocities are received as
\(\dot x_i=J_{F_i}\dot\theta\), with the active phase velocity supplied
by (3). This is the temporal change of the source-over-distance readout
along the specified histories. It does not select an independent wave
equation, propagation delay or homogeneous field solution. Those remain
source-channel information if the field under study carries them.

For a source-selected endpoint lapse \(\chi=\sqrt{1-A_{\rm clock}}\),
the same composition gives
\(\dot\chi=-\dot A_{\rm clock}/(2\chi)\). The field supplied to that
clock must retain its declared environmental/support/velocity contributions;
equation (17) supplies the environmental contribution when this kernel
applies. Together with (10)–(12), this organizes a coupled source and
readout evolution before introducing a new clock or reservoir kinetic
coefficient.

The immediate source operands are the physical incidence \(F_i\), the
source energy map and its evolution, and the typed clock/field channel.
This is a specific route to investigate using the retained histories.
The present H02–H06 normalized experiment keeps its original fixed
\(A_{\rm los}=0\); it has not executed the feedback composition (17).

## 8. Reusable computations and the next action calculation

The efficient reusable unit is a signed source stroke with its starting
state, gate, route and accumulation context. A cache key must include those
operands; the Write name alone is insufficient. Reverse traversals of the
same source path can reuse the positive integral while retaining separate
event identities and opposite signed action. Context-changing orderings
must first receive their actual starting-state witness.

For action derivation, the next compact source object is therefore

\[
\{C_a,C_b,E_B,g,H_E,G^{(j)},\omega_j,T_j;
  \hbox{initial state, signed event, gate and retained lift}\}.
\]

The current source equations supply all displayed contact/chart entries.
The fresh certified integrals supply \(T_j\). A receiving map can pull
these into another coordinate system with (6) and (7), keeping the full
cross terms. A source operator can then use the completed spin
retained/hidden elimination method to receive its additional response,
with remaining hidden dynamics kept in the residual. The heatbath
generator itself remains the spin source's generator.

This sequence asks for the missing quantities once: incidence and units,
activation/selection, accumulation feedback, and the conversion between
typed clocks. It avoids repeatedly computing the already-known active
stroke geometry. No further scientific job is required for the analytical
identities in this note; a later native atlas evaluation can receive them
when the concrete coordinate/action comparison is selected.

## Observed successor results

The following are the completed source-clock refinement outputs. Full
trajectory and independent-reproduction status is reported below where
complete. Decimal sums below are a display calculation from the
returned rational intervals, not an additional native operation.

| Case | Retained source path | First active duration | Second active duration | Sum of active durations |
|---|---|---:|---:|---:|
| [H02](runs/H02_1/CLOCK_REFINEMENT.json) | `000 → 100 → 130` | 0.15855589587603028 | 0.15709176360593113 | 0.3156476594819614 |
| [H03](runs/H03_1/CLOCK_REFINEMENT.json) | `000 → 030 → 130` | 0.16101090966785683 | 0.15715218318783655 | 0.3181630928556934 |
| [H04](runs/H04_1/CLOCK_REFINEMENT.json) | `120 → 020 → 120` | 0.12873459382613456 | 0.12873459382613456 | 0.2574691876522691 |
| [H05](runs/H05_1/CLOCK_REFINEMENT.json) | `210 → 211 → 111` | 0.14925727808036948 | 0.15855589587603028 | 0.3078131739563998 |
| [H06](runs/H06_1/CLOCK_REFINEMENT.json) | `301 → 311 → 310` | 0.1450583488942815 | 0.15715878432541006 | 0.30221713321969157 |

All use the inherited normalized \(R_H=1,c=10,A_{\rm los}=0\). H02–H04
have zero waiting gaps. H05 retains a `1/200` wait on its first occurrence;
H06 retains a `1/250` wait on its second occurrence. Their total prescribed
elapsed intervals therefore have midpoint displays 0.3128131739563998 and
0.3062171332196916 respectively. The summed active-interval widths are below
\(9\times10^{-58}\). These are normalized durations, not assigned SI
seconds.

H02/H03 now give a measured source-clock order effect:
\(T_{H02}-T_{H03}\simeq-0.00251543337373197\). They share their final
native state, signed event multiset, total signed phase action and total
absolute event action. Their retained intermediate source states select
different paths through the metric and therefore different durations.
Equation (8) isolates this observed difference at the original source-clock
stage. Additional receiver evolution can now be compared with it instead
of being used to explain a clock difference that is already upstream.

The shared returned endpoint `130` also makes the coefficient-reception
issue concrete. Substituting its phases into the exact source expressions
gives \(H_E=0\) and \(g=(2,2,-4)^T\). These are analytical source values
at the returned state. The metric (1) is still nonzero, and a nonlinear
receiving map can contribute through \(\sum_k g_k\nabla^2F_k\) in (6).
Therefore that map's curvature is an operand with immediate relevance to
these histories, rather than a generic correction for a hypothetical case.
This statement concerns the contact account; it does not assign the
curvature of the complete physical action.

H02 and H03 have now also completed their full native trajectories and
independent reproductions:
[H02 execution](runs/H02_1/EXECUTION.json),
[H03 execution](runs/H03_1/EXECUTION.json),
[H02 independent result](verification/H02_3.json), and
[H03 independent result](verification/H03_1.json).
Each executes all 957 prepared native steps and passes all 16,192
independent checks. The independent trajectory solver makes no native
calls and does not use native output values as trajectory inputs.

Their final full-carrier readouts retain an order-dependent response:

| Observable | H02 | H03 |
|---|---:|---:|
| Cumulative paid work | 0.00021540847986058215 | 0.00021178299799966372 |
| Final elapsed clock time | 1.5928865558203955 | 1.5928814590148197 |
| Final internal time | 0.35 | 0.35 |
| Final clock factor `q` | 0.1097618255865326 | 0.1097633213693786 |
| Final retained `Lambda` | 2.2094424826125185 | 2.209428855172867 |

Values are displays of the native interval midpoints in
[H02 readouts](runs/H02_1/READOUTS.json) and
[H03 readouts](runs/H03_1/READOUTS.json): `carrier_segments[-1]` for
cumulative work and `final_clock_state` for clock entries. Work is in the
inherited action's normalized units.

The active source-duration sum and final elapsed clock time are different
observables. H02 has the smaller active-duration sum and the slightly larger
final elapsed time at the common internal-time endpoint. This makes the
compositional structure useful: (8) describes the measured source-path
contribution, while the complete retained flow accounts for the later clock,
energy and history response. The unchanged receiver action now executes
these compositions successfully. Deriving its physical coefficients still
uses the specific incidence, energy, channel and clock maps above; execution
success does not assign those maps.

H04 retains two reverse traversals of the same source path. The returned
duration intervals overlap and agree at the displayed precision, as
expected from the exact reverse-path identity (2)–(3). Its signed phase
action cancels, while its absolute event action is \(\pi\hbar\) and its
positive duration is retained. Equality of the original native endpoints
therefore does not identify either of these accumulated quantities with
zero.

H04's [full native run](runs/H04_1/EXECUTION.json) also completes all 953
prepared steps, with all 16,172 checks passing in its
[independent reconstruction](verification/H04_1.json). Its two original
paid events have work displays \(+0.00002928260200337268\) and
\(-0.00006109387694315787\), giving net paid work
\(-0.00003181127493978519\). The driver carries the opposite net amount
and the final complete-account residual contains zero. These are returned
values from [H04's full-carrier events/account](runs/H04_1/READOUTS.json).
Thus the actual intervening flow retains a measurable work history even
when the native source endpoint and signed phase action return. The
inherited coupled action computes that history with unchanged coefficients.

H05 yields a concrete reuse beyond the initial reversal comparison. Its
second stroke `211 → 111`, shifted by one common negative quarter turn in
all three roles, is `100 → 000`: the reverse of H02's first stroke. The
source relative phases, positive metric and accumulation context therefore
give the same duration integral. The returned intervals overlap and both
display 0.15855589587603028. A duration cache may quotient this verified
common-phase and reversal symmetry while keeping the raw history identities,
signed orientation and phase lifts separately. This is more useful than
using the Write name alone as a cache key.

H05/H06 also preserve active traversal and waiting as separate operands.
Their nonzero waits remain the prepared values; the refined active integrals
do not replace them or infer a contact intensity. Both full trajectories
now complete and independently reproduce:

| Case | Native steps | Independent checks | Final cumulative paid work | Final elapsed clock time |
|---|---:|---:|---:|---:|
| H05 | 958 | 16,197 | 0.00013150764170655568 | 1.5927984122829542 |
| H06 | 956 | 16,187 | 0.00023139757595925936 | 1.592912294862016 |

The final internal time is 0.35 in both cases, and the complete energy
account balances in each. Sources:
[H05 execution](runs/H05_1/EXECUTION.json),
[H05 independent reproduction](verification/H05_1.json),
[H05 readouts](runs/H05_1/READOUTS.json),
[H06 execution](runs/H06_1/EXECUTION.json),
[H06 independent reproduction](verification/H06_1.json), and
[H06 readouts](runs/H06_1/READOUTS.json).
These histories have different events and starting states; their difference
is not used as an isolated measurement of waiting time. What is observed is
successful composition of each retained active-stroke integral, its own
specified wait, and its full coupled trajectory.

Across the five cases, the source integration transfer now supports all
4,781 prepared native steps and all 80,940 independent checks. Original
precision, logarithm tolerance, action coefficients and histories are
preserved. The campaign also preserves the verification I/O repair and its
earlier attempts; the links above identify the completed corrected
reproductions. The full campaign report carries the numerical qualification
and resource record separately from these source-action deductions.

The actual order, reversal and reuse results select the next action step:
retain the source metric/clock together with the signed one-form, then
receive the source coupling for the additional phase, support and field
variables. The source incidence, physical energy conversion, channel
selection and typed clock conversion are the specific remaining operands.
The completed computations supply the path information to use in those
maps; they do not require choosing the frozen quadratic coefficients as
targets.

The first concrete source-action continuation is to recover the original
position/channel-to-phase incidence and apply it to the known operator
phase coefficients (15), contact Hessian (5)–(7), and path metric (1).
Use H02/H03's shared endpoint and different paths, H04's reversing path,
and H05's common-phase/reversal reuse as the retained operands for that
reception. This combines an explicit source search with already available
mathematical objects, rather than beginning another numerical clock repair.

Closing spin review: the current H002611 result and its directly linked
two-scalar continuation still favor reusing source Grams/contractions and
keeping the complete remaining residual. That method transfers to the
channel-intensity construction (14) once its source operands are received.
The completed integral transfer is already reflected in all five cases;
no additional spin campaign was started for this note.
