# Chapter III source-to-field development and Chapter II update

Sean Brady: originator and conceptual director. OpenAI ChatGPT and Codex:
research collaborators and co-authors. The new derivations, candidate couplings,
finite fixtures and research selections in this pass are Codex contributions.

This successor preserves the supplied eight-page Chapter III and completed
20-page Chapter II PDFs in `inputs/`. The new readers have14pages/28sections
and24pages/48sections respectively. Chapter II preserves its previous40sections
verbatim and adds the source-to-space interface, clock response and precision
work. Editable sources, exact operands and independent checks accompany both.

## Results now available

### 1. An actual energy-effect map, with physical localization stated

The recovered Si29 Q/N/G matrices give exact all-eight-site identities
`sum_t N_tx=I` and `sum_t G_tx=240Q`. In the original orthonormal bright chart,
`Hgen=[[0,h],[h,0]]`, `h=sqrt(Q)`, while the declared positive excitation account
is `H0=|Hgen|=diag(h,h)`. These have different roles; replacing a signed
spectrum by its magnitude is not a common scalar energy shift.

The positive effects `E_tx=H0^(1/2) O_tx H0^(1/2)` sum at every site to
`E_x=H0/8`, and their complete sum is H0. The normalized scalar spatial share
is therefore exactly1/8 for every preparation. Total energy can still vary
between preparations. The full species/coherence record remains in its
retained36-coordinate closure.

One explicitly chosen localization puts normalized uniform balls of radius
`delta<ell` at the orthogonal cube centers `X_x=ell*(+/-1,+/-1,+/-1)`. The cube
angles, physical ell, delta, energy unit eu, mass conversion and receiving law
are stated assignments. An abstract equal-edge graph alone does not fix those
angles. This gives a finite source

    rho_exc(x) = (eu/c²) sum_x <E_x> zeta_x(x-X_x),
    M = eu <H0>/c².

Its compatible weak source coupling averages a over each ball before coupling
to E_x. Sampling only at each center instead would define point sources or a
long-wavelength approximation, rather than the stated finite-ball density.
The excitation account is not silently identified with all rest, interaction,
field, counterterm or apparatus energy.

Outside the eight balls, the conditional Poisson potential is their exact
point-center sum. Cube symmetry removes odd multipoles and the quadrupole.
The first shape term is

    Kcube(r n) = 1/r + [7 ell^4/(4r^5)] (3-5 sum_j n_j^4) + R6,
    |R6| <= q^6/[r(1-q²)], q=sqrt(3)ell/r<1.

It is negative on a cube axis and positive on a body diagonal. Smearing fixes
finite interiors and self-energy while leaving that exterior center sum exact.
The common energy account is

    Uself = -3GM²/(40delta),
    Umutual = -GM²/(64ell) [6+3sqrt(2)+2/sqrt(3)].

The dimensionless physical strength remains `2G eu/(c^4 ell)`. The source
matrices do not assign this number or the separate action/time conversion.

Sources and complete proofs: `source/REPORT.md`, `EXACT_INPUTS.json`, retained
JSONs and bindings. The old NPZ/coordinate files missing from this T500 copy
were not guessed: the exact retained JSON reconstructs the required operators,
and the physical embedding is declared separately.

### 2. Evaluate the proposed coupling on an actual source clock

The sector-resolved sum of the actual effects gives `P_in` and `P_out`, so
`B=P_in-P_out=diag(I,-I)` is a retained incoming/outgoing population signal.
For an incoming preparation its history is `<cos(2h theta)>`. This is distinct
from Chapter I's certified phase receiver.

For the declared static candidate `Hgen(a)=Hgen-aH0/2`, the entire B history is
unchanged: H0 commutes with both B and Hgen. Full-generator scaling instead
replaces its history by B(n theta). At a=1/50, the incoming e0 initial curvature
remains -512 under the positive-energy candidate; source-only full scaling
changes it to -12544/25=-501.76. Other species/site receivers can respond.

The exact companion chart retains its physical metric W=diag(I,Q). Its native
certificate checks `[K²,B]=0`, nonzero rank-eight `[K,B]`, and `WK=K^T W`.
Functional calculus then supplies the positive-square-root commutation. This
is a calculated response of the specified candidate, with no universal gravity
classification inferred from it. It makes the next physical coupling choice
concrete: identify how the complete localized energy/stress deforms the actual
evolution generator.

Proof and23 exact independent checks: `source/UNIFORM_COUPLING_RESPONSE.md` and
`verify_uniform_coupling.py`.

### 3. A complete finite field, flux, force and energy account

The retained radial conductance is `c_i=i(i+1)`. With source shells at `r_i=ih`,
no central sink and outer condition `a_L=0`, its stiffness K=B^T C B is positive.
The exact Green inverse and source flux are

    H_ij=1/max(i,j)-1/L,
    a_i=kappa sum_j H_ij m_j,
    c_i(a_i-a_(i+1))=kappa sum_(j<=i)m_j,
    kappa=2G M_unit/(c²h).

The eight-equation example uses L=9, kappa=1/50 and the declared shell fractions
`(0,1/5,0,3/10,1/10,0,2/5,0)`. It is a separate source fixture, not an
identification of microscopic cube sites with concentric shells. Exact harmonic
interpolation returns the continuum thin-shell field between sample radii.
The chapter includes every field value and enclosed source fraction.

In units `G M_unit²/h`, its finite-boundary energy is -9427/252000 and its
isolated energy is -2603/28000. In physical units,

    a_infinity=a_L+2GM/(c²R_outer),
    U_infinity=U_L-GM²/(2R_outer).

Every acceleration and enclosed flux agrees; potential and escape to infinity
need the reference correction. The radial shell work derivative includes its
half-self term, `-G M_j[M_<j+M_j/2]/r_j²`. This is work under a radius change,
not a net translation force on a concentric shell.

Removing the outer exit leaves a constant zero mode. Positive total injection
is incompatible with that closed conservative graph. The separately declared
cube Laplacian likewise has rank7 and a constant null mode; its actual flat
source share lies in that mode. A physical exterior flux account must remain
visible when a spatial field is added.

### 4. A controlled radial limit and compact continuum proofs

For a uniform ball, move each radial cell's mass to its outer endpoint and let
eta=GM/(c²b). The exact global reduced-lift bound is

    0 <= (a_ball-a_shells)/eta <= 3/n-2H_n/n² <3/n.

The finite wall adds the independent reduced offset2b/R_outer. Refining at a
fixed R_outer/b=2 leaves lift bias1 and binding-energy bias1/4. Thus both mesh
refinement and the outer-boundary limit are specified. This derives a controlled
radial Poisson receiving limit; a microscopic three-dimensional isotropic
operator and its physical stiffness normalization remain to be selected.

The chapter now contains the finite-energy domain, weak uniqueness and exact
minimum identity

    J[a_*+v]-J[a_*]=c^4/(32piG) integral |grad v|²,

and the symmetric two-source interaction

    U[rho1+rho2]=U1+U2-G double_integral rho1(x)rho2(y)/|x-y|.

Differentiation under disjoint compact supports returns the same mechanical
force and opposite source forces. The -GM1M2/d specialization uses spherical
bodies with disjoint enclosing balls, not nested hollow shells. Finite-boundary
terms, whole-space gradient energy and the point-source self singularity are
retained. The source-record pseudoinverse formula now states its feasibility
condition explicitly.

### 5. Carry a Chapter I field sector into the source equation

The original static quadrupole profiles give positive free energy
`Uf=sum_alpha x_alpha²/R`, with2/5 inside R and3/5 outside. Under the explicitly
chosen angular-average density `rho_f=energy_density/c²`, let Mf=Uf/c². Then

    M_f(<r)=Mf[1-(3/5)(R/r)^5],
    a_f(r)=2GMf/(c²r)[1-(1/10)(R/r)^5], r>=R.

The interior matches continuously, and the conditional self-binding is
`-421 GMf²/(990R)`. The positive free-field tail makes r>R sourced; it is not a
vacuum exterior of this density. Truncating an unchanged field integral and
imposing a finite Dirichlet boundary are different constructions, with energies
`Uf[1-(3/5)(R/L)^5]` and `Uf/[1-(R/L)^5]` respectively.

The full account is especially informative. In the commuting classical static
chart, the original stationary boundary amplitudes give free energy +Uf,
interaction -2Uf and counterterm +Uf: the three integrated contributions cancel.
The noncommuting quantum D/C source is retained. The positive field sector is
therefore a worked density example; the complete gravitating density requires
a joint localization of field, interaction and counterterms under one reference.

### 6. A precise interacting-clock receiving test

The complete16-state source gives its original current commutator and zero
even-energy/counterterm commutators. The source-even energy and counterterm
commute with the complete Hamiltonian and current; their energy can remain
unread throughout the current history. A current record therefore does not fix
all source energy or its physical mass reference.

For an externally derived `H(a)=H(0)+aV+...`, the Duhamel/Kubo derivative and
phase-rate quotient give a six-lane response test. A field V requires the stated
energy-form estimates. Preparation response and a nonzero current amplitude
remain explicit.

The declared full scaling `H(a)=n(a)H(0)+f(a)I` gives
`z(t;a)=z(n(a)t;0)` and `nu(t;a)=n(a)nu(n(a)t;0)`. A universal n rate ratio holds
at matched internal age or on a stationary reference. At equal coordinate time
there is also the transient term `n'(0)t nudot`, wherever the latter derivative
exists. The accumulated-phase identity needs no extra second derivative.

Scaling epsilon alone leaves `s(Hct-Hf)`, s=n'(0), relative to full scaling.
For s=-1/2 its four coefficients are `(0,1/2,0,-1/2)`. The counterterm remains
current-dark; the free-field part can change the correlated current history.
The retained hard-branch second-order epsilon responses have six disjoint exact
enclosures below1, with the proof split held fixed. These are identified
second-order diagnostics, not finite-a full-field perturbation remainder bounds.

Keeping the common clock trajectory sharpens the phase comparison. Under the
declared full scaling, for `0<T<=T0` and `0<n<1`,

    Delta theta = -integral_(nT)^T nu_0(s) ds,
    -u_rate(1-n)T <= Delta theta <= -ell_rate(1-n)T <0.

For `n=sqrt(1-a)`, rational endpoints give
`-u_rate*a*T/(2-a) <= Delta theta <= -ell_rate*a*T/2` for every `0<a<1`.
All six lanes therefore have a signed conditional change at the frozen Earth
lift. Lane01's one-original-bare-cycle shift lies between -4.373897816 and
-4.373897806 nanoradians. No physical model-time unit is assigned.

The separate-enclosure threshold `a>1-(ell_rate/u_rate)^2`, about2.8441e-9 for
lane01, remains a sufficient independent-band comparison. It is not a sign
boundary for the correlated history. `clock/CORRELATED_PHASE.md` gives the
short proof and47 exact independent checks. This analytic supplement was added
after the completed Duck cycle; its native-bound `clock/RESULTS.json` is unchanged.
Preparation, timing, phase unwrapping and readout retain the separate Chapter II
apparatus account; shared theoretical history does not cancel apparatus errors.

The raw floor-inclusive lapse retains sensitivity factor1/(1-A0) after
background normalization. It is not the same source-only prescription with
a=2GM/(c²r) and the same G left unchanged. Static Poisson and an endpoint lapse
do not assign spatial gamma or a causal propagation law.

## Execution and verification

The installed GEN6 Duck plugin delegates to the existing local runtime. This
pass uses qualified deployment1.2.3, unchanged mathematical core0.10.2,
SLC-GEN5-R1/G2-SPIN-CLOCK, native exact source words and certified complex solves.
It uses six controllers and three helpers, profileA, two180-second rounds,
Connections mode, an all-outcome shared review, and all four selected targets.
The completed cycle returned11 native outputs and4 local-corpus retrieval
receipts, with zero failed returns. Independent readback passed29,585 checks
covering28,528 matrix entries. Completion, custody and readback are recorded in
`CYCLE_VERIFICATION.json`, `NATIVE_VERIFICATION.json` and `RESOURCE_RELEASE.json`;
these receipts are the execution authority.

Earlier preparations -01/-02 were never launched. The first hit the old default
memory preflight; the second waited for unrelated work and was superseded by the
owner's concurrency instruction before launch. Their source packets and attempt
metadata remain preserved. No clocks were reset, completed campaigns relaunched,
scientific core replaced, commit made or repository published. The chapter
calculations use retained T500 inputs; this pass performed no I9 transfer.

The seven portable mathematical checkers total3341 independent assertions. The
PDF artifact checks include byte-identical relocated rebuilds and all modified
pages visually inspected. Native readback separately checks full source matrices,
ranks, exact solutions inside native enclosures, interval equations, source hashes,
request identity and receipt/custody hashes. Counts and hashes are in their own
receipts; historical scientific calls are not relabeled as new execution.

## Breadcrumbs and next physical work

`BREADCRUMBS.md` retains every selected useful connection and the bounded corpus
retrieval provenance. The next physical work is to derive the complete localized
energy/stress coupling V from one source action, including its interaction,
boundary and reference terms; then use it in the actual six-lane response test.
The two positive-energy receiving colors recovered by the local research web are
a concrete additional source for that localization calculation.

The restored T500 electron-orbital archive supplies another concrete local
source: retained angular/radial orbitals, massive kinetic integrals, direct and
exchange terms, and collective recoil accounting. All nine restored files
match their restoration hashes. Its original helium/carbon/oxygen prepared
families are distinct from the Si29 source above. The archive is a newly
available follow-up ingredient, not an operand of the completed chapter cycle.
`inputs/ORBITAL_ARCHIVE_REVIEW.json` records this bounded local review.

The radial continuum error is controlled for the declared spherical receiver.
A three-dimensional source graph family, angular isotropy, shared physical
length/energy/action calibration and stiffness/G remain explicit assignments.
Causal evolution, spatial response and nonlinear metric completion are further
receiving laws. These open items have specific operands and tests in FOLLOW_UP.md.
The completed original spin closure boundary and paid measurement protocols stay
unchanged under their retained source authority.

The final bounded frustrated-spin review identifies a useful transfer: retain
the full mixed Gram, its physical normalization, the complementary memory and
boundary payments when reducing the source/field system. The current V7
rank-two residual and open minimum closure remain unchanged. This closes the
research review; subsequent delivery steps only package and authenticate the
completed work.

The test result suggests strong contact with the concept.
