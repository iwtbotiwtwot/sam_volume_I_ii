# Correlated phase comparison on the actual common trajectory

The existing independent-band threshold is not a mathematical limit on the
sign of the clock change. For the declared complete-H scaling, the two phases
are points on the same strictly increasing original trajectory. Keeping that
correlation gives a signed interval for every positive lift.

## Theorem and short proof

Use one of the six original Chapter I preparations and the complete autonomous
source-field Hamiltonian H0. Its current z0 never vanishes over the retained
window `[0,T0]`, and its unique phase lift starts at theta0(0)=0 with
`0<ell<=nu0(s)<=u`. Suppose a static external coupling is declared to be

    H(a)=n(a)H0+f(a)I,       0<n(a)<1.

The common scalar changes the common phase but not the current. Spectral
calculus gives `z_a(t)=z0(n(a)t)`. The nonvanishing amplitude and common
initial branch therefore imply the exact lifted identity

    theta_a(t)=theta0(n(a)t).

For `0<T<=T0`, the original path includes both nT and T. The fundamental
theorem of calculus on that one path gives

    Delta theta(T)=theta_a(T)-theta0(T)
                 =-integral_(nT)^T nu0(s) ds,
    -u(1-n)T <= Delta theta(T) <= -ell(1-n)T <0.       (CP1)

Only the already retained C1 phase regularity is used. No derivative of nu,
new hard-reference approximation, independently fitted gap, or subtraction
of unrelated rate enclosures enters this argument.

For the source-only square root `n=sqrt(1-a)`, `0<a<1`, put delta=1-n. Then

    delta=a/(1+sqrt(1-a)),
    a/2<delta<=a/(2-a).

Equivalently, the positive rational square-root endpoints are
`2(1-a)/(2-a)` and `1-a/2`. Their exact square margins are

    (1-a)-[2(1-a)/(2-a)]^2 = a^2(1-a)/(2-a)^2 >0,
    (1-a/2)^2-(1-a) = a^2/4 >0.

This yields a rational enclosure without evaluating a square root:

    -u*a*T/(2-a) <= Delta theta(T) <= -ell*a*T/2 <0.  (CP2)

The raw-total-account normalized lapse uses the same construction with its
own declared rescaled lift; it cannot silently retain a different mechanical
normalization. No lapse or external material coupling is derived by CP1/CP2.

## Exact retained Earth example

The CR004 premise file supplies, as exact finite decimals/integers,

    mu=398600441800000 m^3/s^2,
    b=6371000 m, c=299792458 m/s,
    a=2mu/(c^2 b)=199300220900/143149231093306629611.

These are the frozen illustrative inputs, not a new observation or fit.
Use the actual native-derived ell/u in each original lane. Outward display
enclosures below are in radians per **model time**, multiplied by10^15:

| Lane | Lower | Upper |
|---|---:|---:|
|01|-2.429556488|-2.429556482|
|02|-2.429556474|-2.429556457|
|03|-2.429553675|-2.429551372|
|12|-2.429556488|-2.429556481|
|13|-2.429553889|-2.429551761|
|23|-2.429554109|-2.429552161|

Multiplying CP2 by the original certified bare-cycle duration
`T0=573049*pi` gives the following outward nanoradian enclosures:

| Lane | Lower | Upper |
|---|---:|---:|
|01|-4.373897816|-4.373897806|
|02|-4.373897791|-4.373897760|
|03|-4.373892751|-4.373888606|
|12|-4.373897815|-4.373897804|
|13|-4.373893136|-4.373889307|
|23|-4.373893533|-4.373890027|

CORRELATED_PHASE_RESULTS.json retains every exact rational endpoint and the
original native duration interval. The displayed result is a conditional model
phase change. No physical value of the model time unit is assigned.

## Independent bands and apparatus are distinct questions

If the phases are treated as independent interval predictions, one instead
compares `[ell*T,u*T]` and `[n*ell*T,n*u*T]`. Their nonoverlap is sufficient
when `a>1-(ell/u)^2`; the lane01 threshold is about2.844e-9. Earth lies below
it. CP1 keeps the common unknown original path, so all six correlated shifts
are nevertheless strictly negative. That shared mathematical path is not an
assumption that experimental noise or calibration errors cancel.

Physical comparison requires the same original preparation, supplied full-H
coupling, time/energy calibration and a phase readout precise enough to resolve
the change. The current receiver divides D/C by the signed lane d. Fresh
preparations and the phase-turn record retain their separate measurement and
systematic budgets; one endpoint modulo2pi is not automatically the lifted
phase. Existing all-cycle amplitude and window bounds remain in force.

This result supplies neither an apparatus sensitivity guarantee nor a physical
external perturbation V. It removes the independent-band threshold as a
mathematical sign boundary for the already declared full-scaling control.

## Execution and source custody

`python3 clock/verify_correlated_phase.py` performs47 standard-library exact
checks: original clock input hashes, frozen Earth premise binding, positive
root square margins, all six actual rate bindings, strict signed bounds,
original-cycle enclosures and the independent-band comparison. It writes only
CORRELATED_PHASE_RESULTS.json and verifies that protected clock/RESULTS.json,
which is bound by the completed native R2 solve, remains byte-identical.
It launches no native operation, scientific cycle or network request.
