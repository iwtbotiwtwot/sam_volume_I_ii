# The actual uniform excitation-density coupling and a retained transfer signal

## Outcome and source binding

The proposed uniform coupling to the positive excitation account has an exact
response: it leaves the retained incoming/outgoing population history
unchanged. Full scaling of the coherent generator gives a different response.
This selects the next physical coupling question for this source; it is not
a general verdict on gravity.

The source operands are the actual retained Si29 `Q`, incoming occupations and
outgoing Grams in `EXACT_INPUTS.json` and `retained/SI29_Q01_RESULT.json`.
`GEN4/volii_duck_expansion1/REPORT.md`, sections1,2,5, gives the incoming and
outgoing propagation, outgoing-event acceptance and inherited positive energy.
`GEN4/volii_duck_expansion2/REPORT.md`, sections1,2, gives the same local
effects and source/load transfer probabilities. Exact input SHA-256 identities
are retained in `UNIFORM_COUPLING_RESPONSE.json`.

No smaller source or replacement two-level model is introduced. The following
eight-dimensional representation is the full invariant bright sector of the
retained four incoming configurations and their four coupled outgoing modes.
The other outgoing modes are dark under the declared coherent interaction.

## 1. The sector observable comes from the retained receiver

Let `h=sqrt(Q)>0`. In the orthonormal bright basis,

    Hgen = [[0,h],[h,0]],       H0=|Hgen|=diag(h,h).

The original evolution explicitly retains its orthogonal incoming and outgoing
sectors. Define their projectors and contrast

    P_in=diag(I4,0),   P_out=diag(0,I4),   B=P_in-P_out.

These projectors also follow by aggregating the retained sector-resolved slot
effects. Split the existing effect into its original two blocks:

    O_tx^in  = diag(N_tx,0)/8,
    O_tx^out = diag(0,h^-1 G_tx h^-1)/(8d),    d=240.

The retained identities `sum_(t,x)N_tx=8I` and
`sum_(t,x)G_tx=8d Q` give

    sum_(t,x) O_tx^in=P_in,     sum_(t,x) O_tx^out=P_out.

Thus B is a sector-resolved aggregate of the source/receiver record already
present, rather than an invented microscopic degree of freedom. Reading only
the all-species spatial sum discards that sector tag and cannot recover B.

For an initially incoming normalized state `(psi,0)`, the actual retained
propagation gives

    P_out(theta)=psi^* sin(h theta)^2 psi,
    <B(theta)>=psi^* cos(2h theta) psi.

It is a nonconstant population-transfer clock signal: its initial curvature
is `-4 psi^*Q psi<0`. In particular incoming `e0` gives curvature `-512`.
It is not a claim that every preparation is a single-frequency oscillator or
that B is the Chapter I certified phase clock. A mode preparation gives one
of its actual transfer frequencies; a general preparation is a weighted
mixture of the four source frequencies. Sector measurement uses fresh
preparations when estimating the history and has its stated readout cost.

## 2. Evaluate the proposed uniform density coupling

The candidate finite-ball coupling from the source account is

    delta H_phys[a]=-(eu/2) sum_x abar_x E_x,
    E_x=H0/8.

For a uniform received lift, `abar_x=a`, this becomes exactly

    H_phys(a)=eu[Hgen-(a/2)H0],     theta=eu t/Iu.

Because `H0` commutes with both `Hgen` and B,

    U_a(theta)=exp(-i Hgen theta) exp(+i a H0 theta/2),
    B_a(theta)=U_a^* B U_a=B_0(theta).

The equality holds as an operator, for every initial state and every static a
in this declared coupling. Every incoming/outgoing probability is unchanged,
so this candidate gives zero population-clock response even at nonzero lift.
More generally, adding any real function of H0 has the same invariance for B.

For comparison, the separately declared full-generator scaling

    H_phys,n=eu n(a)Hgen

gives `B_n(theta)=B_0(n(a)theta)`. With `n(a)=sqrt(1-a)`, its nonzero
time-dilation response is visible already in the initial curvature:

    <B>''_candidate(0)=-4< Q >,
    <B>''_full_scaling(0)=-4(1-a)< Q >.

The finite algebraic control `a=1/50`, incoming `e0`, therefore gives `-512`
for the excitation-only coupling and `-12544/25=-501.76` for full scaling.
This is a controlled comparison of two stated couplings, not a fitted
gravitational prediction or an apparatus precision claim.

## 3. Why equal excitation energy matters for this signal

For an h eigenmode `h_j`, use the actual generator eigenstates `|+,j>` and
`|-,j>`. Under the excitation-only perturbation their dimensionless generator
eigenvalues are

    e_(+,j)=(1-a/2)h_j,
    e_(-,j)=-(1+a/2)h_j.

B connects the two signs of the same j. Both carry the same positive account
`H0=h_j`, so their gap stays exactly `2h_j`. Positive-branch differences scale
by `1-a/2`; negative-branch differences scale by `1+a/2` relative to their
signed baseline. The same-mode transfer gap is unchanged. Hence coupling to
the positive account is not full scaling of the signed coherent generator.

This invariance is specific to observables commuting with H0. Species/site
effects generally do not. The retained input supplies an explicit witness:
`[Q,N_(species0,site5)]` is nonzero, so `[h,N_(0,5)]` cannot vanish.
The candidate can therefore change other source records. No assertion that
all observables, all clocks or the whole spatial receiver are invariant is
made.

## 4. Compact rational certificate without evaluating sqrt(Q)

The retained closure also supplies companion coordinates `(a,c)`, with outgoing
amplitude `b=M c`, norm metric `W=diag(I,Q)` and generator

    K=[[0,Q],[I,0]],       T=diag(I,h),
    T K T^-1=Hgen,         T^*T=W.

B is unchanged by T. Exact rational products verify

    W K-K^T W=0,
    K^2=diag(Q,Q),
    [K^2,B]=0,
    [K,B]=[[0,-2Q],[2I,0]] != 0.

The retained Q is positive definite. Spectral calculus in this physical
W-inner product therefore identifies
`sqrt(K^2)=diag(h,h)=H0`, which commutes with K and B. These algebraic facts
give the full invariance above, without substituting a numerical square root.

`verify_uniform_coupling.py` independently checks the source aggregation and
all rational identities. It launches no native session or propagation.
`DUCK_UNIFORM_RESPONSE_TASK.json` supplies the parent-owned native operator
word: three8-by8 blocks are `[K^2,B]`, `[K,B]`, and `WK-K^TW`, in that order.
Only the middle block is nonzero. Its expected matrix is kept outside the
native payload, along with the source and analytic-frame bindings.

## 5. Physical continuation selected by the calculation

The concrete density coupling has now been evaluated on an actual retained
source signal. A physical source-to-field completion must specify how a
uniform lift affects the coherent transfer interaction and its time chart,
alongside the positive excitation account and the spatially averaged source
coupling. The two displayed choices have distinct exact responses; a common
physical coupling can now be derived or tested against these source controls.
