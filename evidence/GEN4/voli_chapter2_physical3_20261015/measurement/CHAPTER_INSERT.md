# Eight times require repeated preparations

Let `|a>=|q_a q_a>`. Prepare
`|psi>=(|0>+|1>+|2>)/sqrt(3)` with the field vacuum. The protected diagonal
span is annihilated by D, C and their counterterms under the full retained
Hamiltonian. Its adjacent-coherence receiver is

    O=|0><1|+|1><0|+|1><2|+|2><1|,
    y(t)=(2/3)[cos(omega10 t)+cos(omega21 t)].

The three receiver eigenvectors are `(1,sqrt(2),1)/2`,
`(1,-sqrt(2),1)/2`, and `(1,0,-1)/sqrt(2)`, with outcomes
`+sqrt(2),-sqrt(2),0`. Complementary outcomes report zero. A source-basis
rotation followed by this projective readout is a specified mathematical
instrument; its physical construction remains to be supplied. Every sample
time uses fresh preparations. A destructive measurement of one copy cannot
supply the next undisturbed expectation.

The error allowance must cover four apparatus terms before sampling error.
With trace distance `D(rho,sigma)=||rho-sigma||_1/2`, preparation bias is at
most `2sqrt(2)d_prep`. Leakage l and conditional preparation error d_cond
obey `d_prep<=sqrt(l)+d_cond`; leakage alone says nothing about the state
inside the protected space or about its field preparation. Let the actual
effective readout observable be M: `||M-O||<=b_read` bounds its mean bias,
including pulse disturbance and outcome misassignment.

Unwanted evolution contributes at most `2sqrt(2)kappa`, where the Duhamel
path integral `kappa=integral ||delta H(s)psi_ideal(s)|| ds/hbar` is bounded
through the latest allowed trigger. A source-only matrix norm does not bound
an unbounded field interaction. The derivative bound from the retained
calibration, `Xi=1382784+/-1` and `alpha/alpha_nominal=1+/-10^-6`, is

    |y'(t)|<=L_upper<114081.396605 alpha_nominal.

Thus bounded trigger error delta_t contributes `L_upper delta_t`. Calibration
uncertainty is already included in the ideal source family and is not charged
again as trigger jitter.

# A source-selected cadence makes the protocol less expensive

Keep the same independently calibrated source and choose, before acquiring
the target record,

    h_new=5pi/(2 alpha_nominal D_nominal),
    D_nominal=6348467821812271/80000000000,
    t_k=kh_new, k=0,...,7; I={0,2,3}.

This cadence is 7.5 times the earlier one. It was selected from a declared
finite list using only the retained source, not fitted to measured target
data. Rational interval arithmetic gives the order3 difference-Hankel minor

    det A in [5.318723982743267,5.941782789331066],
    |A_ij|<2,

with full rational endpoints in the certificate. Both sampled frequencies
remain distinct and nonaliased. A per-expectation allowance eta=0.01 is now
sufficient, since

    72eta(2+4eta)^2=2.996352<5.318723982743267.

Allocate 0.001 each to preparation, unwanted evolution, readout and timing,
and 0.006 to statistical mean error. Sufficient apparatus requirements are
`d_prep,kappa<=0.001/(2sqrt(2))`, `||M-O||<=0.001`, and
`delta_t<=8.76567e-9/alpha_nominal`. Conditional preparation must still be
controlled; if it is exact, coherent leakage `l<=1.25e-7` suffices.

For N independent outcomes in `[-sqrt(2),sqrt(2)]`, Hoeffding's bound and a
union bound over eight means give

    Pr(any |yhat_k-E[yhat_k]|>s)<=16 exp(-Ns^2/4),
    N>=ceil[4 log(16/beta)/s^2].

At s=0.006 and beta=0.01 this requires **819,751 fresh measurement shots per
time**, or **6,558,008 total**, excluding preparation failures, calibration,
reset and cooling. The earlier eta=1e-4 allocation would require
8,197,509,899 shots per time. The longer cadence reduces this conservative
sufficient count by nearly10,000, while imposing a longer stability demand.
These are requirements, not achieved apparatus precision. If calibration
bounds themselves have failure probability beta_cal, total failure is bounded
by `0.01+beta_cal`.

For a direct decision compute `dhat_k=yhat_(k+1)-yhat_k`,
`Ahat_ij=dhat_(I_i+I_j)`, and `Bhat=max|Ahat_ij|`. Reject the closed autonomous
two-state, fixed-linear-receiver class when

    |det Ahat|>36eta(Bhat+2eta)^2.

Indeed every ideal TLS difference-Hankel has rank at most2. Per-mean error
eta changes each entry by at most2eta; telescoping the three factors in
each of six determinant terms gives this threshold. For the calibrated
source the empirical determinant exceeds it by more than2.35160 on the
simultaneous 99% sampling event, conditional on the apparatus bounds.
Driven/open two-state sources and arbitrary multilevel sources are outside
this null. Physical epsilon, independent calibration, coherent mode access,
receiver pulses and reset remain explicit instrument work.
