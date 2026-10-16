# Proposed continuation: complete the existing five-coordinate upper response

This is a Codex mathematical recommendation, not an executed calculation.
It reuses H002602's completed fifth direction and H002609's source gap
certificate. The proposed new source package consists of two scalar
contractions per original preparation. Their values and the resulting upper
response have not been calculated in this campaign.

## Inherited source and basis

Use the original self-adjoint operator `A=N(I-P)`, original Gibbs inner
product, all 54 preparations and all 37 positive history parameters xi.
Mean history remains `N/xi` original site attempts. The existing basis is

    b4=(d,e,u_d,u_e),   w=(w_d,w_e),   b5=(b4,w_d),
    G=<b4,b4>, D=<b4,A b4>, W=<w,w>, H=G^-1 D,
    E=[[0,0],[0,0],[1,0],[0,1]], e1=(1,0)^T.

Here d=f1-f2, e=f13-f14=d*s2*s3, and the retained residual columns are
u_d=u1-u2, u_e=u13-u14 and w_d=w1-w2, w_e=w13-w14.
The same symbols label different stages of the retained residual chain;
u_d and w_d are different source functions. H002602's g1 is exactly w_d.

The inherited orthogonality and operator identities are

    <b4,w>=0,
    A b4=b4 H+w E^T,
    T4=<A b4,A b4>=H^T G H+E W E^T
                          =D G^-1 D+E W E^T.

Functions are written as row vectors, so the displayed matrix orientations
are fixed. Self-adjointness gives

    <b4,A w>=<A b4,w>=E W.

Write J_ab=<w_a,A w_b>, with indices (d,e). H002602 has already supplied
J11=<w_d,A w_d> and the complete source intervals for

    k=E W e1=(0,0,W11,W21)^T,
    G5=[[G,0],[0,W11]],
    D5=[[D,k],[k^T,J11]].

Its completed five-coordinate lower response is retained. Recomputing J11
or merely adding w_d again would repeat that completed extension.

## Exactly two new contractions complete T5

For the cross column of T5=<A b5,A b5>, the operator identity gives

    t=<A b4,A w_d>
     =H^T<b4,A w_d>+E<w,A w_d>
     =H^T k+E (J11,J21)^T.

Consequently

    T5=[[T4,t],[t^T,F11]],
    J21=<w_e,A w_d>,
    F11=<A w_d,A w_d>.

Every other entry is inherited or obtained by these exact contractions.
The two missing scalar source operands are therefore the mixed
fifth-moment payment J21 and the sixth-moment payment F11. Symmetry supplies
J12=J21; J22 and the other sixth-moment entries are unnecessary for this
five-coordinate calculation. No numerical cancellation is assumed.

In terms of the original single-site heatbath flip rates r_l and
Delta_l f=f(x)-f(x^l), their source meanings are

    J21=(1/2) sum_l E[r_l Delta_l w_e Delta_l w_d],
    F11=E[(sum_l r_l Delta_l w_d)^2]
       =sum_(l,m) E[r_l r_m Delta_l w_d Delta_m w_d].

The first is a signed mixed Dirichlet contraction. The second includes
every l,m cross term and is not the Dirichlet payment J11. All background
sites, source correlations, actual after-flip fields, physical-field
payments, integration errors and arithmetic errors remain part of the
source enclosure, using the inherited full-source meaning. These displayed
identities do not supply those two enclosures by themselves.

## Sign and residual checks

The retained residual definition in H002602 is

    w_d=A^2 d-(A d,A e)p+(d,e)q.

Thus its source feature contraction has coefficients
`(1,-p1,-p2,q1,q2)`. Applying A to this identity preserves those minus
signs; the coefficients are constants for each preparation. The mixed
contraction J21 must retain its returned sign, and every signed feature
cross term must remain in F11.

In the four-coordinate operator identity, the term `w E^T` has a plus
sign. The upper receiver residual nevertheless has a minus sign because

    q=d-(A+xi)b4 c
     =b4[e_d-(H+xi I)c]-w E^T c.

This is the same retained-minus-complement orientation used in this
campaign's generalized directions. It does not change the plus signs in
`t=H^T k+E(J11,J21)^T`. In particular, no sign of J21 is prescribed.

## Upper response available after T5 is supplied

For each preparation, reuse its H002609 family certificate gamma on the
same original odd sector. Let e_d5=(1,0,0,0,0)^T and V=<d,d>. Set

    r_gamma5=(D5-gamma G5)e_d5,
    K_gamma5=T5+(xi-gamma)D5-xi gamma G5.

The fifth component of r_gamma5 is exactly zero: w_d is orthogonal to
b4, and A d lies in b4. Coupling through K_gamma5 still uses its fifth row
and column. With the retained-form solve on its non-null support,

    c5=K_gamma5^-1 r_gamma5,
    U_gamma5=(V-r_gamma5^T c5)/(xi+gamma).

This is an upper bound on R(xi)=<d,(A+xi)^-1 d>. To see the sign of every
term, for v=b5 c and q=d-(A+xi)v, use the inherited source bound A>=gamma:

    R(xi)=2<d,v>-<v,(A+xi)v>+<q,(A+xi)^-1 q>
         <=2<d,v>-<v,(A+xi)v>+||q||^2/(xi+gamma)
          =[V-2 r_gamma5^T c+c^T K_gamma5 c]/(xi+gamma).

Minimizing gives the displayed solve. Nonsingularity or an exactly
identified compatible support is handled by the same native retained-form
method as the existing receiver; it is not assumed from a midpoint.
Interval source operands and all mixed terms propagate through the solve.

The source spectral bound gamma is independent of the receiver basis, so
the existing certificate applies to b5 without a new gap calculation.
The exact variational minimum over b5 cannot exceed the one over b4,
because b4 is contained in b5. The amount resolved by the source intervals
remains an outcome of the proposed calculation. Retain the minimum with
the inherited upper endpoints and keep H002602's completed L5 lower.
For the inherited normalized response, multiply by the same xi/V factor.
Each preparation's two new source operands serve all 37 histories.

## Why this continuation follows the direction calculation

The generalized direction weights describe where the actual receiver
forces the whole residual. They do not identify an eigenvector with w_d
merely because one generalized weight is near one. The lifted residual
`q_a=b4 Z a-w a` contributes the same new span as w a, since b4 Z a is
already retained. This explains how to translate a residual direction into
a source-basis extension without counting its retained part twice.

For a general mixed a, forming an upper response on (b4,w a) requires the
vector J a and the scalar <A w a,A w a>, not just <w a,A w a>. Moreover,
adding w a to the already completed b5 when a_e is nonzero spans both w_d
and w_e. That is a six-coordinate extension, whose complete upper form
would require J12,J22 and F11,F12,F22, with F_ab=<A w_a,A w_b>.

The recommended first continuation instead completes the already useful
b5 using only J21 and F11. It directly targets its optimized upper payment
while carrying forward the completed lower result. A rotated or full
two-residual extension can be assessed later from that result; none is
executed or required by this recommendation.

## Direct source custody

- [H002602](../../SAM_HISTORY/entries/H002602_2026-10-13_ORIGINAL_SPIN_DIFFERENCE_FIFTH_DIRECTION.md)
  records the completed J11 and five-coordinate lower result.
- [Fifth-direction derivation](../spin_difference_fifth1/DERIVATION.md)
  defines g1, its signed features, full-source payments, G5 and D5.
- [This campaign's input reader](inputs.py) identifies and authenticates
  `GEN4/spin_difference_fifth1/native1/<family>/<profile>_RESULT.json.gz`:
  `output.G5`, `output.D5` and `output.projected_matrices.W`. J11 is the
  final diagonal entry of D5 in its recorded five-coordinate basis.
- [H002609 derivation](../duck_spin_connections1/DERIVATION.md) supplies
  the four-coordinate upper, stationarity and residual identities.
- `GEN4/duck_spin_connections1/field_gamma/<family>.json` supplies the
  unchanged source gamma and coverage of BASE, H_MINUS and H_PLUS.
- [Current direction derivation](DERIVATION.md) supplies the generalized
  projectors and the retained-minus-complement lift.

No new source assumption, source moment value or numerical response is
introduced here. The new contribution is the exact reduction of the
missing five-coordinate upper matrix to two scalar source operands.
