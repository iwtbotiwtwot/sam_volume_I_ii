# Actual finite-source closure after seven coordinates

This extension keeps the original finite-N Gibbs law and the original uniform
all-site heatbath operator `A=N(I-P_transition)`. It does not promote the
20-site conditional contraction into a replacement source. The explicit finite
configuration calculations retain all original sites, integer multiplicities,
self-exclusion, signed short couplings, and original attempt-clock units.

## 1. Which source span is the seven-dimensional construction?

The completed source residual constructions are triangular with leading
coefficient one. Therefore their spans agree exactly with these Krylov spans:

    V5=span(d,e,Ad,Ae,A²d),
    V7=V5+A V5=span(d,e,Ad,Ae,A²d,A²e,A³d).

Here `d=s1-s0`, `e=d*s2*s3`. This is the same V7 previously written as
`span(b5,w_e,r_next)`. Orthogonalizing or rescaling a basis changes no span.
The previous rank-two certificate established only `dim V7=7`.

For any finite list of source functions `f1,...,fm`, a nonzero determinant of
`[f_j(x_i)]` at m literal source configurations establishes linear independence:
a function relation would hold at all selected configurations and would make
that matrix singular. The full finite Gibbs law has positive mass at every
configuration. Hence pointwise independence is also independence in its actual
Gibbs Hilbert space. No auxiliary measure, limit, fitted norm, or quadrature is
needed for this implication.

## 2. Literal finite-N generator, including all background sites

Write `F_b=F-6`, `P_b=P+3`, `T_b=T`; then
`F_b+2P_b+3T_b+20=N`. The four ports and sixteen labelled hidden spins remain
individually represented. For a core configuration s and background block
occupancies, let M be the magnetization of all N spins. Put

    kappa=15 log(3)/128, g=2 beta kappa,
    t_p=beta kappa+epsilon product(p).

The physical self-excluded fields are

    F_j=beta(M-s_j)/N +sum_p t_p p_j tau_p
        +zeta sum_(opposite pair) s_k -1_(j<2)g s_(1-j),
    F_tau_p=beta(M-tau_p)/N+t_p(p dot s).

For a background block of size b=1,2,3 having k negative spins, a site with sign
sigma has physical field

    F_bk_sigma=beta(M-sigma)/N-g(b-2k-sigma),

where the last term is absent for b=1. Its actual accepted flip rate is
`r=(1-sigma*tanh(F))/2`. A block type with n_k blocks supplies exactly
`n_k*(b-k)` positive-site flips and `n_k*k` negative-site flips. Each accepted
flip moves one block from occupancy k to k+1 or k-1. This is an exact lumping of
exchangeable original sites, not a deletion of background sites. It is valid for
each labelled original preparation separately.

The evaluator recursively applies

    (Af)(x)=sum_actual_site_classes multiplicity*r(x)*(f(x)-f(x^i)).

Core rates use the literal labels and all post-flip M values. Only exact zero
terms in A(d,e) from sites outside the four ports are omitted. No frozen field,
auxiliary Gaussian update, replacement clock, or background error allowance is
inserted: this finite-depth point evaluation is the full original operator.

## 3. Seven-dimensional residual and continued exact ranks

Let `Pi7` be the original Gibbs-orthogonal projection onto V7. Since
`A V7` adds only `A³e` and `A⁴d`, its nonzero complementary rank is

    rank((I-Pi7)A|V7)=dim span(V7,A³e,A⁴d)-7.             (C3.1)

In the original residual coordinates take the actual seven basis as
`(b4,w_d,w_e,A w_d)`. The first five image columns lie in V7. Write the completed
leading-one source residual as `w_d=A²d-p_d1 Ad-p_d2 Ae+q_d1 d+q_d2 e`.
The two possible complementary image columns are exactly

    r_e=Q7 A w_e=Q7 A³e,
    r_d=Q7 A² w_d=Q7 A⁴d-p_d2 Q7 A³e.                 (C3.1a)

Thus a point certificate for `(Q7 A³e,Q7 A⁴d)` computes the residual rank for
the actual residual coordinates by an invertible triangular change of columns.
The known full-source bounds also give
`||r_e||²<=N² W22` and `||r_d||²<=N² F11`; neither assigns their unknown global
norms zero. The strict positive lower certificates below are complementary to
these inherited, conservative upper bounds.

An eight-column certificate through `(A³d,A³e)` makes the residual on `w_e`
strictly nonzero:

    (I-Pi7)A w_e=(I-Pi7)A³e !=0.                        (C3.2)

The equality follows from the leading-one residual definition: all other terms
of A w_e already belong to V7. A ten-column certificate through `(A⁴d,A⁴e)`
establishes the independence of the nine-column subset in (C3.1). It therefore
makes the residual rank exactly two and establishes

    V9=V7+A V7, dim V9=9, (I-Pi9)A V9 !=0,              (C3.3)

because A⁴e is independent of V9. In general, a full rank certificate for both
seeds through power m establishes `dim span(A^j d,A^j e;0<=j<=m)=2m+2`.
These are exact source ranks, not singular-value thresholds. Since
`K7(t)=C7* exp(-D7 t) C7` and the finite-source exponential is positive definite
at every finite t, `rank K7(t)=rank C7`. A certified rank-two seven-span residual
therefore retains a rank-two memory kernel at every finite original source
time, although its norm may decay. This does not assign that rank to a
propagator difference or discard any hidden initial-preparation term.

The result files specify the highest computed power and which original
preparations were evaluated. A reported rank lower bound is not stabilization.
The exact smallest invariant space remains the union of these Krylov spans;
only equality `V+A V=V`, or a source minimal-polynomial identity, closes it.

## 3a. An explicit finite invariant upper closure

The literal physical Hilbert space has 2^N configurations. The d/e Krylov
functions are fixed by permutations of the F_b free sites, permutations of
identical pair blocks and their internal sites, and permutations of identical
triangle blocks and their internal sites. The original physical generator
commutes with these symmetries. Consequently the count representation in the
evaluator extends to an explicit invariant space of dimension

    D_lump=2^20 (F_b+1) binomial(P_b+2,2) binomial(T_b+3,3). (C3.3a)

The factor 2^20 keeps every labelled core assignment. A free population has
F_b+1 negative counts; pair populations are multisets over three occupancy
classes; triangle populations are multisets over four classes. Every displayed
coordinate corresponds to a nonempty original orbit. The multiplicity-weighted
heatbath transitions close exactly on this space, with the original lumped
Gibbs weights. This is a constructive finite invariant upper closure. It is
not a claim that d/e reach every coordinate.

`EXACT_LUMPED_UPPER_BOUND.json` evaluates this integer formula for all54 original
preparations. Its dimensions have96 to342 decimal digits. The native point
certificates give the lower side. A small minimum cannot be inferred from this
large upper space or from an arbitrary depth cap.

## 4. An explicit positive full-source residual norm bound

Take the eight selected configurations in an invertible point matrix
`M=[V7,A³e]`. Define the exact functional

    lambda^T=e8^T M^-1.

Then `lambda^T V7=0` and `lambda^T A³e=1`. For the actual residual
`r=(I-Pi7)A³e`, Cauchy-Schwarz in the *original* Gibbs weights gives

    1 <= [sum_i |lambda_i|²/pi(x_i)] ||r||_Gibbs².       (C3.4)

A conservative absolute bound on a representative of the original Gibbs log
weight, after removing a common constant, is

    L=beta(N+1)/2+g(P_b+3T_b)+4sum_p |t_p|+g+4|zeta|.

There are 2^N literal states and each log weight is between -L and L, so
`pi(x)>=exp(-N log(2)-2L)`. Thus the actual residual obeys

    ||(I-Pi7)A w_e||² >=
       exp[-N log(2)-2L] / sum_i |lambda_i|² >0.         (C3.5)

The bound is deliberately conservative and can be extremely small. It certifies
nonclosure in the actual Gibbs norm without claiming a useful numerical estimate
of the global eighth moment. It is not a measured apparatus precision target.
The independent verifier provides rational upper bounds on the denominator.

For a nine-column matrix `[V7,A³e,A⁴d]`, the last two inverse rows define Lw
with `Lw V7=0` and `Lw[A³e,A⁴d]=I2`. If R is the full Gibbs Gram of those two
projected residuals, the same argument yields the matrix bound

    R >= exp[-N log(2)-2L] / ||Lw||_F² * I2 >0.         (C3.6)

This gives a compact positive residual-rank certificate without discarding any
signed off-diagonal Gibbs contraction.

## 5. Block-elimination, Gram normalization, and finite-time error

For any retained orthogonal projector Pi in the original exchange-odd sector,
set Q=I-Pi and compress the original self-adjoint positive generator:

    A=[[B,C*],[C,D]], B=Pi A Pi, C=Q A Pi, D=Q A Q.

The two exact equations are `p'=-Bp-C*q`, `q'=-Cp-Dq`. Variation of constants
in the latter and substitution into the former give

    p'=-Bp-C*exp(-Dt)q0+integral_0^t C*exp[-D(t-s)]C p(s) ds.

For initially retained data, differentiate twice at zero:
`Pi A² Pi=B²+C*C`. Therefore retained autonomous evolution for every retained
initial state is equivalent to `C*C=0`, hence C=0, hence `AV subset V`.
Allowing arbitrary q0 gives the same equivalence at the first derivative.

For a nonorthonormal retained source basis b with positive Gram G, write
`D_b=<b,A b>`, `T=<A b,A b>`. Its residual bilinear Gram and physical operator
are

    L_b=T-D_b G^-1 D_b,
    K0_coordinate=G^-1 L_b,
    K0_orthonormal=G^-1/2 L_b G^-1/2.                   (C3.7)

All have the same rank as C. The norm in a physical error bound is the spectral
norm of the last matrix, or equivalently the largest generalized eigenvalue of
`L_b v=lambda G v`. Ordinary eigenvalues of L_b do not supply it.

If the unchanged original odd-sector certificate gives `gamma I<=A<=N I`,
Duhamel substitution gives

    F(t)-exp(-Bt)=integral_0^t integral_0^s
        exp[-B(t-s)] C*exp[-D(s-r)] C F(r) dr ds,
    F(t)=Pi exp(-At)|V.

Each of its three semigroup factors has norm at most its corresponding
`exp(-gamma*time)`; the three times sum to t. Hence

    ||F(t)-exp(-Bt)|| <= (t²/2)exp(-gamma t)||K0||.       (C3.8)

Keeping the full source upper bound N also gives

    ||F(t)-exp(-Bt)-(t²/2)K0|| <= (N t³/2)||K0||.        (C3.9)

These statements use original A-time, whose Poissonized count is N*t attempted
site updates. No physical-seconds or current-clock calibration is silently
introduced.

## Reproduction and scope

`point_source.py` is the literal physical evaluator. The parent native session
wraps its source-bound calculation and preserves exact input/output receipts.
`verify_point_certificate.py` independently checks the point minor, inverse
functional, source inventory, and determinant overlap with outward-rounded
256-bit dyadic rational arithmetic using only Python's standard library.
It does not relabel that offline replay as native execution or as fresh Gibbs
integration. Original old campaign outputs remain unchanged.
