# The original J21 and F11 source integrals

Codex source-bound extension of H002602/H002611/H002626. Preserve the original
finite N Gibbs source and A=N(I-P). Let A=C+B, with C summing the 20 core sites
and B the Nb=N-20 background sites. Put h_d=A d=C d, h_e=A e=C e.
For each preparation the retained coefficients give

    K_d=C h_d-(h_d,h_e)p_d+(d,e)q_d,
    K_e=C h_e-(h_d,h_e)p_e+(d,e)q_e,
    w_d=K_d+B h_d, w_e=K_e+B h_e,
    A w_d=C K_d+epsilon_d,
    epsilon_d=B K_d+C B h_d+B^2 h_d.

The new finite contraction enumerates every 16 port/65536 hidden assignment,
all 20 core updates and actual after-flip fields. It computes the joint Gram
of (d,e,Cd,Ce,C^2d,C^2e,C^3d). The original Arb SPINJ001 caches and original
normalized Chebyshev moments are reused exactly, with their provenance.
No source normalizer, J11, G5,D5 or completed lower campaign is repeated.
Core quantities are

    J21_core=<K_e,C K_d>_aux, F11_core=||C K_d||_aux^2,
    E_e=||K_e||_aux^2, E_d=||K_d||_aux^2.

## Complete background enclosure

Write a=beta/N, R=sqrt(3 Nb). Conditional on the original auxiliary field y,
background blocks of size 1,2,3 are independent. At fixed y their a=0 heatbath
generator is reversible. C1^0=sum s_i r_i^0 has mean zero and variance <=3Nb.
Actual self-exclusion changes each rate by at most a/2. Real rates have bounds
|r|<=1, |r'|<=1/2, |r''|<=1, |r'''|<=2.

For a core function h with uniform real field derivative bounds H1,H2,H3,
Taylor expansion of its field jump yields

    ||B h||_aux <= b(h)=2a H1 R+Nb a^2(H1+2H2).

Under either core flip the field shifts by at most 2a. The conditional mean
of C1^0 at that shifted field changes by at most Nb*a, so a bound usable for
both old and post-core values is b_shift(h)=b(h)+2Nb a^2 H1. Therefore
||C B h||_aux<=40*b_shift(h).

For B^2h split each background jump into a fixed-field block flip and a field
shift. The fixed-field part is a sum of independent block observables. Its
standard deviation is <=12a H1 R. Replacing actual rates by the reversible
a=0 rates bounds its mean by 6Nb a^2 H1. Set D1=H1+2H2 and
D2=2(H1+H2+H3); then |(Bh)'|<=Nb a D1, |(Bh)''|<=Nb a D2.
The signed first field term is 2a*C1*(Bh)' plus a same-block correction.
Their norms are bounded by 2Nb a^2 D1*(R+Nb a/2) and 12Nb a^2 D1.
The second field remainder is <=2Nb^2 a^3 D2. Consequently

    ||B^2h||_aux <= 12a H1 R+6Nb a^2 H1
                     +2Nb a^2 D1*(R+Nb a/2)
                     +12Nb a^2 D1+2Nb^2 a^3 D2.

Use H1,H2,H3=(2,4,8) for h_d and (6,12,24) for h_e. For K_d,

    K1=160+2|p_d1|+6|p_d2|,
    K2=400+4|p_d1|+12|p_d2|,
    ||B K_d||_aux<=2a K1 R+Nb a^2(K1+2K2).

These give a complete epsilon bound Eps by summing the three displayed
background bounds. All background blocks and every cross term remain included.
Cauchy-Schwarz gives signed core/background errors

    |J21_aux-J21_core|<=sqrt(E_e)*Eps+b(h_e)*sqrt(F11_core)+b(h_e)*Eps,
    F11_aux in F11_core+[-2sqrt(F11_core)Eps,2sqrt(F11_core)Eps]+[0,Eps^2].

The optional J11 wiring diagnostic uses the same formula with K_d,b(h_d).
It does not replace the retained original J11 in D5.

## Physical-field, interpolation and arithmetic payments

The inherited heat-semigroup lemma pays any complete analytic observable H by
BH*(beta/N)/(pi/4)^2 when |H|<=BH on |Im y|<=pi/4. In that strip rates have
magnitude <=1 and derivative <=1. Let

    Ld=160+4|p_d1|+12|p_d2|+2|q_d1|+2|q_d2|,
    Le=480+4|p_e1|+12|p_e2|+2|q_e1|+2|q_e2|,
    Kc=320+4|p_d1|+12|p_d2|,
    MA=40Ld+2beta*Kc+368beta+48beta^2.

The complete functions obey |w_e|<=Le+24beta, |w_d|<=Ld+8beta and
|A w_d|<=MA. The last bound includes |B K_d|<=2beta*Kc,
|C B h_d|<=320beta and |B^2 h_d|<=48beta+48beta^2, including its own-block
change. Thus physical payments are (Le+24beta)*MA*E0 for J21 and MA^2*E0
for F11, with E0=(beta/N)/(pi/4)^2. Pay these on the complete observables;
auxiliary conditional independence is not assumed for the physical law.

The complete core feature amplitudes are bounded by (2,2,4,12,160,480,6400)
throughout the interpolation ellipse and real tail. The largest Gram entry is
bounded by 40960000 times the original mass bound. The inherited grid has an
explicit new Chebyshev interpolation payment with numerator bound 1e8*Wbound;
the full omitted tail is paid entrywise. Only arithmetic on authenticated
Arb dyadics runs in C++; no floating transcendental is used. Round-to-nearest,
long-double precision >=64, no fast math/no FMA, 32-state blocks and binary merges
are required. A contribution path has fewer than 16384 rounding steps and at
most twelve cache factors. The absolute entrywise payment is conservatively

    mass * amplitude_i*amplitude_j * (4*gamma_16384+1000*2^-60).

The factor four covers expanded signed differences. Interpolation, full tail,
inherited source intervals and every new payment propagate to the source result.
