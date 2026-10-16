# One new source moment for the difference response

This is the authorized continuation of H002601. Original preparations,
couplings, retained moment intervals and the uniform N-site attempt clock
are inherited. The scalar reduction and finite-N background enclosure below
are Codex mathematical contributions. All new files are on the T500.

## Exact requested operand

A=N(I-P), f is the original centered 15-component port Walsh row,
u=Af-fB and w=Au-f V^-1 R-u R^-1 U. Use the inherited exact symmetry
sector S=[e1-e2,e13-e14], and denote V2=S^T V S, D2=S^T Ds S,
R2=S^T R S, U2=S^T U S, W2=S^T W S. Put d=f1-f2 and
e=f13-f14=d*s2*s3. All these observables are odd under global inversion,
so centering introduces no constant. In the sector, set

    B2=V2^-1 D2, C2=R2^-1 U2,
    p=(B2+C2)[:,1], q=(B2 C2-V2^-1 R2)[:,1].

Then exactly

    g1=w1-w2=A^2 d-(A d,A e)p+(d,e)q,
    J=<g1,A g1>=(1/2) sum_l E[r_l (g1(x)-g1(x^l))^2].

The port and residual coefficient indices are mapped explicitly; their
functions are distinct. No coefficient is fitted to a response target.

## Exact finite core and all after-flip fields

Use the original physical field y=beta*M/N and a=beta/N. The inherited
rates include self-exclusion -a*s_l. A flip changes y to y-2*a*s_l.
Let A_c sum the four port and sixteen hidden updates. Only ports change
d or e, hence A d=A_c d and A e=A_c e exactly. Define

    K=A_c A d-(A d,A e)p+(d,e)q.

The finite contraction enumerates all 16 port rows and all 65,536 hidden
assignments. It evaluates A_c A d by the inherited single-support
coefficient identity in H002597. Five global-field cache shifts
(-4,-2,0,2,4)*a supply K and both actual post-flip values. No after-flip
field is replaced by its pre-flip value. Hidden rates have three shifts.

The contracted features are (A_c A d,A d,A e,d,e). Separate 5-by-5
port and hidden Dirichlet Grams retain their complete signed cross terms.
Their contraction with (1,-p1,-p2,q1,q2) gives the core energy of K.
The source preparation and its density still include the full background.

## Exact background representation and explicit enclosure

There are Nb=N-20 background sites: F-6 free sites, P+3 pairs and T
triangles. Their exact counts satisfy (F-6)+2(P+3)+3T=Nb. The identity
from H002597 gives the entire background component in A^2 d:

    b=a^2 E C0+a O C1, g1=K+b,
    C0=sum_background r_l, C1=sum_background s_l*r_l.

E and O are the first-pair signed combinations of the exact even/odd
port-rate changes in H002597. At real y, for a<1e-10,

    |E|<=16, |O|<=8, |E'|<=64, |O'|<=32.

The native source integral uses the original auxiliary Gaussian field
Y|state ~ Normal(beta*M/N,beta/N). Conditional on Y=y, all background
blocks are independent, with the original size-1/2/3 block Gibbs weights.
The comparison with the physical field is paid separately below.

For the unshifted block rates at a=0, detailed balance gives E[C1]=0.
Actual self-exclusion and either core flip shift move any rate argument
by at most 3a. Since a real heatbath rate has derivative at most 1/2,
|E[C1(y+t)]|<=3*Nb*a/2 for t=0,+/-2a. Consequently, for a core flip,

    |E[Delta b | y,core]|<=56*Nb*a^2,
    Var(Delta b | y,core)<=972*Nb*a^2,
    E[(Delta b)^2 | y,core]<=972*Nb*a^2+3136*(Nb*a^2)^2.

For the variance bound, a size-m block's contribution to Delta b has
absolute value <=18*m*a; sum m^2<=3*Nb. Independence is used only
conditional on the original auxiliary field, where it holds exactly.

Define nonnegative coefficient bounds

    L=160+4|p1|+12|p2|+2|q1|+2|q2|,
    Lr=160+2|p1|+6|p2|,
    Lc=320+4|p1|+12|p2|.

Here |K|<=L and |dK/dy|<=Lr on the real line. The constants follow
from |Ad|<=4, |Ae|<=12 and 20 original core updates. The signed
core/background cross term and nonnegative square obey

    |cross|<=2240*L*Nb*a^2,
    square<=9720*Nb*a^2+31360*(Nb*a^2)^2.

For an actual background flip, its own block changes at most three spins'
local rates; all other rates see the field shift -2a*s_l. Thus
|Delta C0|<=3+Nb*a and |Delta C1|<=6+Nb*a. Together with the E,O
derivative bounds these give

    |Delta b|<=a*(50+74*beta),
    0<=background_update_energy<=Nb*a^2*(2*Lr+50+74*beta)^2/2.

These are finite-N inequalities for the complete background, including
all cross-block terms. Their exact endpoints are retained as payments.
Background contributions are enclosed, not individually numerically
resolved in this campaign. No background contribution is declared zero.

## Physical field, integration and arithmetic payments

On |Im y|<=pi/4, every source rate has magnitude <=1 and derivative
magnitude <=1. The same exact hyperbolic identities yield
|E|<=20, |O|<=10, |E'|<=128, |O'|<=64. Hence

    |g1|<=L+11*beta,
    |Delta_background g1|<=a*(2*Lc+100+300*beta).

The complete physical Dirichlet integrand is bounded on this strip by

    BH=40*(L+11*beta)^2
       +Nb*a^2*(2*Lc+100+300*beta)^2/2.

The inherited Gaussian heat identity and Cauchy derivative estimate pay
the entire physical-to-auxiliary discrepancy by BH*a/(pi/4)^2. This
bound is applied to the complete Dirichlet integrand, including the
background, before interpreting the integrated core and background bounds.
Thus no conditional auxiliary independence is assumed in the physical law.

Let Jc be the integrated core Gram contraction. The final full-source
enclosure is

    J in Jc + [-cross_bound-heat, cross_bound+heat]
            + [0, square_bound+background_update_bound].

All inherited coefficient intervals propagate through Jc and the payments.

Arb supplies 27,555 positive signed-scale dyadic cache entries per node,
each relative error below 2^-60. Compiled contractions require at least
64-bit long-double precision, round-to-nearest, no fast math and no FMA.
All sums use 32-state blocks with binary merges. Expanded features have
amplitudes <=160,12,12,2,2; expanded Gram entries are below 2e6.
Fewer than 4096 rounded operations lie on any expanded path. Every
expanded term has at most nine cache factors; 1e8*2^-60 covers their
perturbations and decimal output rounding. The absolute node payment is

    mass(y)*(2e6*gamma_4096+1e8*2^-60).

The source chart, normalizer and full-tail enclosure are inherited from
H002594. Newly integrated original-density Chebyshev moments use Arb1024,
four panels, abs_tol=1e-65 and rel_tol=1e-55. The ellipse has imaginary
height <1/2 and the inherited finite mass bound Wb. The analytic numerator
bound 1e7*Wb pays interpolation; degree increases until its normalized
bound is below 1e-14. All five features are odd under global inversion,
so every Gram is even and the positive half-grid suffices. A uniform
1,100,000 bound pays each Gram entry on the entire omitted tail.

## Five-coordinate original response

The exact four-coordinate basis is (d,e,u1-u2,u13-u14). Since g1 is
orthogonal to all f and u, and Af lies in their span,

    G5=diag(G4,W2_11),
    D5=[[D4,k],[k^T,J]], k=(0,0,W2_11,W2_21)^T,
    r5=(V2_11,V2_21,0,0,0)^T.

For every inherited positive xi,

    L5=r5^T(xi*G5+D5)^-1 r5 <= <d,(xi+A)^-1 d>.

Native interval solves retain J's complete enclosure. The original
H002599/H002600 upper response remains available. New output reports
the lower gain and fraction of the previous upper-minus-lower interval
removed, without interpreting that fraction as a measured physical mode.
Mean geometric history length stays N/xi original spin attempts.

## Independent reconstruction

The independent route uses literal NumPy spin updates, a different
two-sided interpolation grid, mpmath120 original-density integration,
and mpmath400 sector algebra. It does not use native rate caches or
native core coefficients. Inherited V,Ds,R,U,W are inputs. Numerical
core reproduction and algebra reproduction are reported separately;
background and physical-field payments remain analytical enclosures.
