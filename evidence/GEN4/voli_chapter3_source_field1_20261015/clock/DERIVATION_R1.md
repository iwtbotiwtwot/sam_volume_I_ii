# Actual interacting clock and a declared spatial lift

Sean Brady: originator and conceptual director. OpenAI ChatGPT and Codex:
research collaborators and co-authors. New receiving constructions: Codex.
This is a source-bound response calculation and specification, not a physical
redshift measurement or a derived microscopic gravitational coupling.

## K1. The complete original Hamiltonian

Retain the Chapter I source Q, S=Swap, D=Q_L-Q_R, C=iSD and
E_even=Q_L+Q_R+Q_L Q_R. The full Hamiltonian is

    H0 = Hs + Hf + Hint + Hct,
    Hs = epsilon (S+E_even),
    Hint = -epsilon(D phi_+ + C phi_cross),
    Hct = epsilon^2 mu(D^2+C^2), mu=1/(4R).

The original two fields, counterterms, all frequencies and form domain remain
present. Source matrices are sixteen dimensional; there are six two-state
lanes and four unforced diagonal states. On lane l, d_l<0,

    Z_l=(D+iC)/d_l, z_l=<Z_l>,
    zdot_l=-i Delta z_l+2g_l w_l,
    nu_l=Delta-2g_l Im(w_l/z_l), Delta=2epsilon, g_l=epsilon d_l.

The current receiver exists while z_l is nonzero. The retained Chapter I
amplitude and instantaneous-rate certificates provide this condition for the
original preparation and original H0 over its stated finite window.

## K2. Exact common-energy invisibility

Use the real non-Hermitian unnormalized current Zraw=D+iC=(I-S)D. On the
complete original sixteen-state source, exact matrix multiplication gives

    [S,Zraw]=-2 Zraw,
    [E_even,Zraw]=0,
    [D^2+C^2,Zraw]=0.

The field operators commute with E_even, and E_even commutes with the original
source operators S,D,C. Consequently E_even commutes with H0. For any bounded
real function F of E_even,

    exp(i(H0+F)t) Zraw exp(-i(H0+F)t)
      =exp(iH0 t) Zraw exp(-iH0 t).

Thus this receiver's entire time record is unchanged by that added common
source energy for every initial state, although total energy changes. A scalar
F=f I is the simplest instance and also changes the state's common phase.
This does not identify the original common Write phase chi with E_even.

An exact finite-source example is provided by the four states |q_a q_a>:
D=C=0 for every one, but their source energies are epsilon(1+q_a)^2 and
are distinct. They are a useful energy-versus-current control, not clocks with
nonzero current amplitude. These identities prevent inferring all gravitating
energy from a clock rate or from one current expectation.

## K3. Response to a supplied perturbation V

Let the external lift parameter be a, and specify a differentiable family
H(a)=H0+a V+O(a^2), with a fixed initial state unless stated otherwise. For a
bounded V, Duhamel gives

    delta z(t)= i integral_0^t <[V_I(s),Z_I(t)]>_0 ds.

For a field form V this equation requires its matrix elements and differentiated
evolution to exist in the common energy-form rigging; bounded-operator norm
estimates must not be assigned to an unbounded field. A sufficient route is a
common closed semibounded form family, continuous form Duhamel forcing and a
dominating energy-norm bound. The Chapter I weighted estimates are the starting
point, but their constants must be recalculated for the supplied V.

Whenever z0(t) stays away from zero, differentiation of -Im(zdot/z) yields

    delta nu(t)=-Im[delta zdot(t)/z0(t)
                      - zdot0(t) delta z(t)/z0(t)^2].       (K1)

An a-dependent preparation contributes <delta Psi|Z_I(t)|Psi>
+<Psi|Z_I(t)|delta Psi>; calibration and preparation response cannot be hidden
inside V. The stationary hard-branch specialization, when differentiable
isolated eigenbranches are used, is Hellmann-Feynman:

    Omega_l'(0)=<Phi_1,l|V|Phi_1,l>-<Phi_0,l|V|Phi_0,l>.

This is not automatically the actual full-field rate: soft evolution and its
uniform remainder still require propagation. A universal first-order clock
target for the source-only local lapse is

    nu_l'(t;0)/nu_l(t;0)=-1/2

for all six separately prepared lanes, subject to a shared preparation,
time/energy assignment and explicit timing/amplitude errors. Lane-specific fits
to epsilon or to each measured gap would not test that target.

## K4. A complete scaling control and the epsilon-only countercontrol

If one DECLARES H(a)=n(a)H0+f(a)I for static a, then

    z_l(t;a)=z_l(n(a)t;0),
    nu_l(t;a)=n(a)nu_l(n(a)t;0).                (K2)

This is an exact control on the full interacting continuum and all six lanes.
It inserts a coupling law; it does not derive n(a) from source incidence. Even
then, comparing instantaneous frequencies at equal coordinate times gives

    partial_a nu_l(t;0)=n'(0)[nu_l(t;0)+t nudot_l(t;0)].

At equal internal ages s=n(a)t, the frequency ratio is n(a). For an accumulated
phase comparison, theta_l(t;a)=theta_l(n(a)t;0)-theta_l(0;0).
The slight actual nonstationarity cannot silently be replaced by a constant
hard-branch gap when comparing equal coordinate durations. Alternatively the
isolated hard-reference frequency is stationary and scales exactly with n.

The four coefficients of Hs,Hf,Hint,Hct must all scale in this control. Merely
replacing epsilon by n epsilon while retaining the same field kernel and Hf
gives instead

    H_epsilon(a)=n Hs+Hf+n Hint+n^2 Hct.

For s=n'(0),

    V_epsilon=s(Hs+Hint+2Hct),
    V_epsilon-sH0=s(Hct-Hf).                    (K3)

This exact residual is not a scalar on the full continuum. The source clock
can respond through changed field dynamics and correlations, even though the
counterterm itself commutes with Z. Within the completed-square convention,
rescaling field frequencies by n while retaining the same smearing u changes
mu=integral |u|^2/omega to mu/n. Then epsilon->n epsilon,
Hf->n Hf, Hint->n Hint and Hct->n Hct form a consistent full-scaling control.
Changing a literal radius, mode coordinate or physical ruler would require its
own transformed kernel and boundary incidence; no such change is inferred.

## K5. Independent second-order six-lane diagnostic

For the retained hard split lambda=64 Delta at the baseline, keep lambda fixed
when defining an epsilon-only perturbation. With J(Delta)=integral_lambda^inf
|u|^2/(omega^2-Delta^2) d omega, the original two-polarization expansion is

    Omega_l^(2)=Delta(1-4g_l^2 J),
    Delta=2epsilon, g_l=epsilon d_l.

At fixed field and d_l, logarithmic differentiation gives

    d log Omega_l^(2)/d log epsilon
      =1-[8g_l^2 J+4g_l^2 Delta J']/(1-4g_l^2 J).  (K4)

J'>=0, so this derivative is strictly below one wherever 0<4g_l^2J<1.
The correction depends on d_l^2; the six original d_l^2 are distinct. This
predicts a lane-dependent epsilon-only response already at second order.
It is a diagnostic of an explicitly declared perturbation, not a certified
remainder bound for finite gravitational a or the full soft-field response.
The fixed-lambda convention avoids differentiating the numerical proof split
as if it were a changed physical Hamiltonian. The source spectrum and bounds
0<J<=b/[1-(Delta/lambda)^2], b=1/(6 kappa pi), imply a small positive correction
for all six retained lanes. Exact rational bounds and rounded displays are
retained in RESULTS.json; they use no numerical eigensolver or fitted gaps.

## K6. The floor is a separate nonlinear input

For A0=1/(12pi), raw lapse normalized to its source-free background is

    n_raw(a)=sqrt(1-A0-a)/sqrt(1-A0)
            =sqrt(1-a/(1-A0)),
    n_raw'(0)=-1/[2(1-A0)].

The source-only convention has n_loc(a)=sqrt(1-a), n_loc'(0)=-1/2.
The first-order ratio of sensitivities is 1/(1-A0), about1.027248616.
A shared background multiplier cancels; its nonlinear lift rescaling remains.
Replacing a by a/(1-A0) must also transform the Poisson coupling and each
mechanical receiver if claiming equivalent parameterizations. It cannot leave
the original a=2GM/(c^2 r) and measured G unchanged in both prescriptions.

## K7. What is executed and what remains

verify.py performs exact original-source commutator checks, coefficient
accounting, all-six-lane source-gap bounds, and safe second-order inequalities.
NATIVE_TASKS.json contains two source-bound formal operator-word receptions:
full-source clock/common-energy algebra and full-H scaling residual. The second
uses a four-coordinate coefficient space, explicitly not a replacement field.

These calculations identify an operational six-lane test and an exact
countercontrol. They do not establish the physical external perturbation V,
gravitating density, shared SI assignment, universal redshift, nonlinear lapse,
spatial gamma, or physical measurement results. The full-source response
derivative and its energy-form errors become executable once V is supplied.

## Source dependencies

- sam_volume_I_i/data/chapter1_certificate.json, original exact compact operand.
- sam_volume_I_i/manuscript/chapter_I.md, sections3.1,4,5,6,7.
- sam_volume_I_i/docs/MODEL.md, sections3-6.
- sam_volume_I_i/docs/SECOND_ORDER.md, original two-polarization expansion.
- voli_chapter2_physical3_20261015/protocol/DERIVATION.md, actual energy,
  reference versus actual phase, and separate actual-current receiver.

Frozen input copies and SHA-256 are recorded in SOURCE_BINDINGS.json.
