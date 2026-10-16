# Compact Chapter II proofs and certificates

Sean Brady is originator and conceptual director. OpenAI ChatGPT and Codex are
research collaborators. These are source-bound mathematical arguments and
independent checks; no new hardware measurement is reported here.

## C1. Elimination gives memory, and exact closure is invariance

In the original Gibbs Hilbert space restrict to the invariant exchange-odd
sector and take its orthogonal decomposition V plus V-perp. With the original
self-adjoint generator write

    A=[[B,C*],[C,D]], p'=-Bp-C*q, q'=-Cp-Dq.

Variation of constants gives
`q(t)=exp(-Dt)q0-integral_0^t exp[-D(t-s)]Cp(s)ds`. Substitution gives

    p'=-Bp-C*exp(-Dt)q0+integral_0^t K(t-s)p(s)ds,
    K(t)=C*exp(-Dt)C.                              (C1)

For arbitrary q0, autonomous retained evolution implies C*=0 by its derivative
at zero. Even with q0=0, exact equality of retained and compressed propagators
implies `Pi A^2 Pi=B^2`; block multiplication instead gives `B^2+C*C`.
Thus C=0. Conversely C=0 decouples both equations. This establishes the
equivalence of exact retained autonomous evolution, K(0)=0, and `AV subset V`.
A vanishing hidden initial state removes initial forcing but not later returns.

## C2. Source-metric rank and finite-time error

For a nonorthonormal basis b, its Gram G is positive. Put
`D_b=<b,A b>` and `T=<A b,A b>`. Orthogonal projection gives the residual form

    L=T-D_b G^-1 D_b,
    K0_orth=G^-1/2 L G^-1/2.                        (C2)

The same residual map has Gram C*C, so `rank L=rank K0_orth=rank C`.
Congruence preserves rank and positivity; ordinary eigenvalues of L do not
give the physical norm. That norm is the largest generalized eigenvalue of
`Lv=lambda Gv`. For the original five-coordinate spin basis, only the
`(u_e,w_d)` columns carry memory, with residual form

    L2=[[delta,s],[s,R5]],
    norm(K0)<=delta U11/det(U)+R5/W11.              (C3)

The inverse source-metric coefficient is `U11/det(U)`, including the mixed
u_d/u_e Gram. Its replacement by `1/U22` would discard a source correlation.
All54 retained preparations have delta>0 and delta*R5-s²>0, so rank2. The
independent replay checks the exact intervals and the common bound
`norm(K0)<7.524585`; the new closure work computes further Krylov ranks.

Let `gamma I<=A<=N I` on this original odd sector and
`F(t)=Pi exp(-At)|V`. Substituting (C1) once into variation of constants gives

    F(t)-exp(-Bt)=integral_0^t integral_0^s
      exp[-B(t-s)] C*exp[-D(s-r)] C F(r) dr ds.

The three semigroup bounds multiply to exp(-gamma*t), since their durations
sum to t. The integration triangle has area t²/2. Hence

    norm(F(t)-exp(-Bt)) <=(t²/2) exp(-gamma*t) norm(K0).

Replacing the three semigroup factors by their identities changes the
integrand by at most `N*t*norm(K0)` (telescope the three factors, using
`norm(exp(-Xs)-I)<=N*s`). Thus

    norm(F(t)-exp(-Bt)-(t²/2)K0)<=(N*t³/2)norm(K0).   (C4)

These are operator-norm statements, not a semigroup ordering or a physical
seconds assignment. Original A-time has mean N*t attempted site updates.

## C3. The minimum number of linear additive counters

For the admitted histories let F(h) contain every required receiver moment.
Given initial data and fixed total duration/count, subtract one baseline
F(h0), and set `W=span{F(h)-F(h0)}`, dim W=r. If c additive linear counters
with a linear decoder recover all those moments, their map restricted to W
must be injective. Rank-nullity gives c>=r. A basis of W supplies r coordinates
and an inverse linear decoder, attaining the bound. This concerns exact linear
additive summaries, not arbitrary real encodings or the number of storage bits.
The predictive state and phase index needed for online continuation are separate.

An explicit source certificate uses the six words made of two A and two B
blocks, `A=(W1+)^4`, `B=(W7+)^4`. If A occurs at zero-based block indices
b1,b2, put S1=b1+b2 and S2=b1²+b2². For each of the first three A-only output
points its internal event offset is r=1,2,3, so the atomic moments are

    count=2,
    M1=4S1+2r,
    M2=16S2+8rS1+2r².                            (C5)

The common point receives each remaining event; its moments are the fixed
total sums minus these three points' moments. Other points receive none.
Therefore all moments through degree2 decode from S1,S2. Relative to AABB,
the ABAB and ABBA contrasts in (S1,S2) are (1,3),(2,8), with determinant2.
Thus contrast ranks are0 for counts,1 through first moments,2 through second.
Two counters attain, and rank requires, that last dimension on this family.

## C4. ABBA/BAAB offsets without an equal-duration assumption

Keep repeated source context fixed. Let the actual positive block durations
be TA,TB and keep each block's internal event offsets. The A-block start sets
are `{0,TA+2TB}` and `{TB,TB+TA}`. Their sums agree and their squared sums
differ by `2TB(TA+TB)`. For any fixed A-event offset r, expansion of
`sum(start+r)^2` cancels its constant and linear terms. Every A-only point
therefore has the same first moment and second-moment difference

    Delta M2_A=2TB(TA+TB)>0.                      (C6)

The B-block start sets `{TA,TA+TB}` and `{0,TB+2TA}` also have equal sums;
their squared-sum difference is `-2TA(TA+TB)`. The common point gets one A
event and four B events per pair of blocks, giving

    Delta M2_common=2(TA+TB)(TB-4TA).             (C7)

Under equally spaced phase events, TA=TB=4h and these become64h² on each
of three A-only points and -192h² on the common point. In physical source time
TA and TB need not agree: the sign in (C7) is retained. A nonlinear clock
change transports its receiver weights and does not preserve unweighted first
phase moments automatically. These offsets are conditional on the stated
repeated source context; history-updated accumulation must update durations.

## C5. All feasible source endpoints and the exact minimum

Use the original literal B18 and the stated diagnostic receiver reading the
first two port indicators. Start at z=0; fix the outside configuration. A pure
port endpoint z has `dy=(0,0,e_z-e_0)`. For requested record(-1,0), z=0 has
record(0,0), z=1 has record(-1,1); precisely z=2,...,15 are compatible. The
table gives exact `573049*dy^T B18 dy`, before physical scale kappa_E.

| endpoint z | cost numerator | one literal flip from0 | minimum |
| ---: | ---: | :---: | :---: |
| 2 | 1085537 | yes | yes |
| 3 | 1146097 | no | |
| 4 | 2006049 | yes | |
| 5 | 4965618 | no | |
| 6 | 2155185 | no | |
| 7 | 2163505 | no | |
| 8 | 1085537 | yes | yes |
| 9 | 2155185 | no | |
| 10 | 1142898 | no | |
| 11 | 1146097 | no | |
| 12 | 1146097 | no | |
| 13 | 2163505 | no | |
| 14 | 1146097 | no | |
| 15 | 1146098 | no | |

Every row is recomputed from the complete original B18, including its signed
off-diagonal entries. The minimum `1085537/573049` is attained at2 and8;
both are available one-port-flip endpoints. Outside changes add nonnegative
squares in B18's first two coordinates, so they cannot lower this endpoint
minimum. The ambient continuous minimum is smaller, approximately0.987626.
Writing the compatible displacement as `dy=dy_*+h` gives `L^T h=0` and
`dy_*^T B h=0`; hence its extra feasibility payment is exactly `h^T B h`.
Source actuation, endpoint selection, physical kappa_E and SI calibration are
separate instrument accounts. Signed total energy change still retains
`2y0^T B dy`; it is not replaced by positive displacement cost.

`verify_protocols.py` authenticates the source matrices and transition table,
replays both new protocols into separate output directories, checks the compact
counter decoder and rank, all fourteen feasible costs, the event offsets, and
the noncommuting block-square identity. No native research session is launched.
