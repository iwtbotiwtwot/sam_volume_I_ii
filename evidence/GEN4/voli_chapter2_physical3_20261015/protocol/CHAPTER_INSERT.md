## A source-paced Write, inverse Write and wait

Keep the complete Chapter I lane01 preparation and joint Hamiltonian. Its conserved energy E is not a two-level toy energy. Positivity of the completed field form and the retained preparation bound give

    epsilon*e01-epsilon <= E <= epsilon*e01+epsilon+Kprep,
    E in[0.917629340281369063,0.917632830384309734].       (P1)

Physical energies are hbar/t_u times displayed values; t_u still needs physical calibration. Choose the declared source ratio R_H/(c*t_u)=1/10, A_path=0. Execute000→100 by W1+, then100→000 by W1-, then wait4 model-time units. Their positive active durations are the same retained certified integral,

    T=(1/10) integral_0^(pi/2)
       12sqrt(68-32cos ell)/(100-32cos ell+4cos²ell)dell
      in[.158555895876030285,.158555895876030286].        (P2)

Thus gamma=delta rises0→pi/2 and returns0, chi=0, and signed Write actions are +pi*hbar/2,-pi*hbar/2,0. Original phase progress and actual current-clock phase remain distinct.

Give the balanced reference h_R=2(w-E)P during ledger-matching intervals, where w=+v,-v,0 for forward, reverse and wait. In particular **a source wait has h_R=-2E P**. Before matching, hold the source at000 and ramp h_R from0 to2(10-E)P over a=.01; after the wait ramp from-2E P to0 over b=.01. These are external entry/release intervals with their own action account. Internal endpoint changes are the specified sudden-control idealization, with their work retained.

| Boundary | Model time | gamma=delta | Reference phase beta |
|---|---:|---:|---|
| Matching begins |a|0|.1-Ea|
| Forward ends |a+T|pi/2|.1+pi-E(a+2T)|
| Reverse ends |a+2T|0|.1-E(a+4T)|
| Wait ends |a+2T+4|0|.1-E(a+4T+8)|
| Release ends |a+2T+4+b|0|.1-E(a+b+4T+8)|

The actual clock remains the original full-field trajectory. At every boundary theta lies in[ell01*tau_lower,u01*tau_upper]. Its final phase is[.000015136966570142,.000015136966591669]; the final reference phase is[-7.841399681709530363,-7.841369477578352354]. The wait alone winds the reference by more than a full turn. On matching intervals,

    E d tau+(1/2)d beta = w d tau = d gamma.             (P3)

The entry and release canonical integrals are (E+10)a/2 and Eb/2, outside that original signed ledger. The reference energy and variance during matching are w-E and(w-E)^2. The source-clock energy, including even energy, correlations and both counterterms, is retained in E.

For a numerical control available from this certificate alone, use its exact rational midpoint Ehat in the reference waveform. This has |E-Ehat|<1.746e-6; the actual connection becomes[w+(E-Ehat)]d tau. Total matching-ledger bias is then<7.54e-6*hbar. The source energy stays E and its calibrated residual is retained. All phase-turn and sampling bounds below hold for both prescriptions.

The original source rate has v0=10, vL=125/(3sqrt17), and an interior minimum vmin≈9.810320323234103 at cos ell*=(11-sqrt73)/4. All reference work pieces, in units hbar/t_u, are

| Piece | Mean drive work |
|---|---:|
| External entry |10-E|
| Forward:10→vmin→vL |vmin-10; vL-vmin|
| Forward→reverse | -2vL |
| Reverse:-vL→-vmin→-10 |vL-vmin; vmin-10|
| Reverse→wait |10|
| Wait with nonzero h_R |0 drive work|
| External release |E|

Their signed sum is0, but positive and withdrawn amounts are each2vL+2(10-vmin)≈20.590661439892877. Recoverable work exchange is distinct from dissipation. Source actuation, preparation, control, readout, memory/reset and recovery losses require their own apparatus accounts. Enforcing a nonnegative reference Hamiltonian adds a baseline integral C=pi+2ET+8E+Eb; that extra canonical payment must also be retained.

To read and unwrap beta, estimate X=cos beta and Y=-sin beta on separate fresh copies at each prefix. Include all boundaries and a grid with gaps<=.01; at most441 prefixes suffice. Since E<1 and v<=50/3, |beta_dot|<=106/3. Coordinate errors<=1/16 imply angular errors<1/8; the true increment plus two endpoint errors is at most53/150+1/4<pi. Nearest-branch continuation from beta0=0 therefore fixes every turn. An external counter stores those turns; an endpoint qubit alone stores phase modulo2pi.

Use atan2(-Yhat,Xhat), then nearest-branch continuation. Allocate total coordinate tolerance1/16 as systematic1/32 plus statistical1/32. Four systematic budgets of1/128 each cover reference preparation, evolution/waveform, readout and timing. Sufficient bounds are reference trace distance and Duhamel integral<=1/256, Pauli-readout norm error<=1/128, and trigger error<=3/13568 model time. Full continuum source energy and clock preparation retain their separate energy-form requirement.

For independent binary Pauli measurements,4M exp(-Nd²/2) bounds failure over both coordinates of M prefixes. M<=441,statistical d=1/32,N=26624 gives joint failure<1/100 conditional on those apparatus bounds, at most23,482,368 fresh preparations. Each prefix readout disturbs that copy; fresh prefix preparations carry the phase record. Energy and timing errors enter reconstructed ledger action through U*dE+(|E|+dE)*dt+eta. A material autonomous controller must supply its further energy and entanglement account.

Actual theta needs a separate lane-current receiver: z=<D>/d01+i<C>/d01 with signed d01<0, and theta=-atan2(<C>/d01,<D>/d01). Its retained nonzero amplitude exceeds0.999999998. Fresh source copies can estimate the two bounded Pauli coordinates; their coordinate tolerance delta gives phase error<=arcsin(sqrt(2)delta/0.99). Those receiver, systematic and sampling requirements are additional. Reported theta intervals here are predictions from the actual rate certificate, not achieved current tomography or reference-qubit readout.
