# Shared-source signature, calibration and finite receiving record

ORIGINATOR / CONCEPTUAL DIRECTOR: Sean Brady. AI RESEARCH COLLABORATORS:
OpenAI ChatGPT and Codex. The matrices, pair Hamiltonian, protected subspace
and original six interacting clocks are inherited. The uniform bounds,
calibration inversion, finite-record certificates and placement exception
below are new source-bound Codex derivations for this authorized continuation.

## S1. Objects and source bindings

Retain the exact original four-component operands

```
T = [[84,8,8,0], [8,84,0,0], [8,0,84,8], [0,0,8,84]],
Kr= [[672,96,32,0], [96,2016,0,0],
     [32,0,672,32], [0,0,32,672]],
Q(g)=T+g Kr,                    g=g_H>=0.
```

`Kr` is the signed-response operator `K_response`, not the commuting
sixteen-state `K_even=Q_L+Q_R+Q_L Q_R-I`. The receiving comparison retains the
complete pair source `H_pair=Swap+Q_L+Q_R+Q_L Q_R` and its additive control
`H_add=Swap+Q_L+Q_R`. Both use the same positive physical frequency scale
`alpha=epsilon_phys/hbar`, field, counterterms, source incidence and declared
preparation. If model epsilon is used, `alpha=epsilon_model/t_u` when
`I_*=hbar`; numerical seconds are a separate calibration.

Source authority is `GEN4/duck_chapter1_lane1_20261015/sources/EXACT_INPUTS.json`,
containing exact matrices and inherited certified root enclosures at g=1.
`RESULTS.json` binds its SHA-256. The preceding comparison is
`GEN4/voli_chapter2_bridge1/comparison/DERIVATION.md`. Its completed current
clock results are inputs, not rerun here.

The protected diagonal span is `span{|q_a q_a>}`. The full D/C interaction
and counterterm annihilate it, so the field vacuum remains unchanged under
both full Hamiltonians. The state `( |q0q0>+|q1q1>+|q2q2> )/sqrt(3)` and
the sum of adjacent Hermitian coherences give

    y(t)=(2/3)[cos(omega10*t)+cos(omega21*t)],
    omega_ba=alpha(q_b-q_a)(q_b+q_a+2),              (S1)
    omega_ba_add=2alpha(q_b-q_a).                   (S2)

This is a specified complementary preparation/readout. D/C itself vanishes
on this subspace. Physical realization of the preparation and receiver is
not asserted by a mathematical assignment.

## S2. Uniform positive, simple spectrum

Theorem S2. For every g>=0 the four eigenvalues satisfy

    0 < 68+544g <= q0 < q1 < q2 < q3 <=100+2112g.   (S3)

Derivation. In placement order `(1,0,2,3)`, Q is a Jacobi matrix with diagonal
`(d+1344g,d,d,d)`, where `d=84+672g`, and successive positive links
`(a,b,b)`, where `a=8+96g` and `b=8+32g`. An eigenvector is fixed up to scale
by its first component through the three-term recurrence. That component
cannot vanish without every component vanishing. Each eigenspace therefore
has dimension one. Real symmetry gives four distinct real eigenvalues.

The four Gershgorin lower endpoints are

    68+544g, 76+1920g, 68+608g, 76+640g,

and every upper endpoint is at most `100+2112g`. This establishes (S3).
In addition `544I<=Kr<=2112I`; hence each ordered source root is increasing
with g, and Weyl's inequality gives

    |q_a(g+delta)-q_a(g)| <=2112|delta|.            (S4)

Both endpoints1 and3 of the reordered chain are cyclic for every g>=0:
every eigenmode has nonzero overlap with either endpoint placement.

## S3. Uniform separation of the pair and additive ratios

Define the ordered positive ratios

    R_add=(q2-q1)/(q1-q0),
    R_pair=R_add*(q2+q1+2)/(q1+q0+2).             (S5)

Theorem S3. Throughout g>=0,

    R_pair/R_add
      =1+(q2-q0)/(q1+q0+2)
      >=1+(8+32g)/(202+4224g)
      >1+1/132.                                  (S6)

On the declared diagnostic interval `0<=g<=2` the lower margin strengthens to

    R_pair/R_add >=1+36/4325.                     (S7)

Derivation. Delete original placement0. The remaining principal matrix has
eigenvalues `d-b,d+b,d+1344g`. Its smallest eigenvalue is `d-b` and its middle
eigenvalue is at least d. Cauchy interlacing gives `q0<=d-b` and `q2>=d`, so
`q2-q0>=b`. Bound the positive denominator by twice (S3)'s upper endpoint
plus2. The rational function in (S6) decreases with g and has limit1/132.
At g=2 it is36/4325.

This is a common-calibration comparison: pair and additive predictions use
the same g. No finite sampling cadence is claimed to be nonaliased for every
unbounded g. The source-specific ratio comparison and a finite-record
experiment are different statements. At g=0 the source is equally structured
and still has a pair/additive separation; a negative g is outside this theorem.

## S4. An eight-sample certificate against a closed autonomous TLS

For a time-independent Hermitian two-state Hamiltonian, arbitrary fixed state
and fixed linear Hermitian readout, any equally spaced expectation record is

    y_k=c+A cos(k theta)+B sin(k theta).            (S8)

This includes the degenerate, constant and aliased cases. Set
`d_k=y_(k+1)-y_k` and form, from eight samples y0,...,y7,

    H_ij=d_(i+j),     i,j=0,1,2,3.                (S9)

Theorem S4. Every record (S8) has `rank(H)<=2`, so all its order3 minors and
its order4 determinant vanish. In contrast the protected record (S1) has
rank4 whenever its sampled exponentials
`exp(+/-i theta1),exp(+/-i theta2)` are distinct and none equals1.

Derivation. First differencing removes c. The remaining signal is a sum of
two exponentials for (S8), and four for (S1). Each exponential contributes a
rank-one Hankel matrix. In the four-exponential case the factorization
`H=V diag(c_j) V^T` has nonzero weights and a nonsingular Vandermonde V under
the stated nonalias conditions. For the protected cosine amplitudes, with
`a=cos(theta1)` and `b=cos(theta2)`, the real determinant is

    detH=(1024/81)(1-a)(1-b)(1-a^2)(1-b^2)(a-b)^4. (S10)

One obtains (S10) from weights `(z_j-1)/3` and the squared Vandermonde. The
resultant of `z^2-2az+1` and `z^2-2bz+1` is `4(a-b)^2`.

For the retained g=1 source choose `theta1=pi/3` and `theta2=R_pair*pi/3`.
Exact interval arithmetic yields

    detH >0.001284739647382393.                    (S11)

`check_signature.py` constructs pi bounds from the alternating Machin series
`pi=16 atan(1/5)-4 atan(1/239)`, then encloses cosine using a rational Taylor
series with explicit remainder and its 1-Lipschitz property. The Chebyshev
recurrence constructs all eight samples. It also checks the direct interval
determinant against (S10). Standard-library floating point appears only in
the printed convenience summary, never in a certificate.

The TLS comparison here is the autonomous closed two-state source with a
fixed linear receiver. A time-dependent receiver or a driven/open source has
additional degrees of freedom. A matching generic multilevel source can
reproduce (S1). The shared ledger's additional content is that it predicts
these quantities together with the same source calibration.

## S5. A larger certified sample-error tolerance

There is a useful efficiency improvement: retain the same eight samples but
receive one order3 minor rather than only detH. Choose the principal index
set `I={0,1,3}`. Its nominal source determinant is approximately

    det H[I,I] = -0.09600434808.                   (S12)

For an n-by-n matrix with entry size at most B and perturbation at most e,
expanding its determinant over permutations gives

    |det(A+E)-det A| <= n! n e (B+e)^(n-1).        (S13)

All protected samples lie in[-4/3,4/3], so B=8/3 bounds their differences.
If target and TLS predictions each agree with a measured record to
per-sample error eta, the two underlying sample records differ by at most
2eta and their Hankel entries by at most4eta. For n=3, their determinant
difference is bounded by

    72 eta (8/3+4eta)^2.                          (S14)

At `eta=1/10000` this bound is0.051215361152. The calibration intervals in S6
give, for a cadence fixed from independent source/scale calibration,

    det H[I,I] in
      [-0.106706899733662,-0.085302278620110].      (S15)

The entire interval lies outside the perturbation allowance around zero.
Thus the declared target and closed-TLS measurement-error sets are disjoint
at absolute per-sample tolerance1e-4. This tolerance is expressed in the
normalization of the stated observable; its measurement implementation is a
physical receiving assignment. It is not an experimentally measured precision.

The four-by-four witness also remains useful: (S10) establishes full rank4
without selecting a minor, and its simpler conservative certificate works
at sample error1e-7. The order3 minor improves that diagnostic tolerance by
three orders of magnitude without another sample or native evolution.

## S6. Independent calibration of g, scale and source offsets

Write physical signed lane coupling as `kappa_ab=epsilon_phys(q_a-q_b)` and
the common bare gap as `Delta=2epsilon_phys`. These are the source parameters;
the interacting clock's dressed gap is not substituted for Delta. Then

    Xi=sum_(a<b) kappa_ab^2/Delta^2
      =Tr(Q^2)-(Tr Q)^2/4
      =384+5120g+1377280g^2.                       (S16)

Theorem S6. On g>=0, Xi uniquely determines g. Its inverse has global
Lipschitz constant1/5120 and can be evaluated stably as

    g=2(Xi-384)/(5120+sqrt(5120^2
                                  +4*1377280*(Xi-384))). (S17)

This follows from `Xi'(g)=5120+2754560g>=5120`. An interval for measured Xi
is inverted monotonically; no separate lane fitting is used. A measured
bare Delta determines `alpha=Delta/(2hbar)`. If model-chart quantities are
used, retain their action/time conversion before assigning physical alpha.
This calibration leaves the protected coherence ratio as a separate receiving
prediction. Extracting Xi requires the source/field coupling normalization;
measuring the six clock crossing times alone is not identified with that input.

For a diagnostic calculation, not a physical fit, take `Xi=Xi(1)+/-1`. Exact
rational bisection gives

    g in[0.999999637639081,1.000000362360788].        (S18)

Propagate (S4) from the inherited g=1 root intervals. The resulting source
predictions remain separated:

    R_pair in[1.156263996487890,1.156393795168546],
    R_add  in[1.072521411523748,1.072637448465540].  (S19)

For the finite record, choose a fixed cadence from the nominal calibration,

    h=pi/(3 alpha_nominal D_nominal),
    D_nominal=79355.8477726533875,

where D_nominal is an explicitly chosen rational approximation to nominal
omega10/alpha. Its small difference from the certified gap is retained in
the phase calculation. No target frequency is estimated from the eight measurements.
Allow both (S18) and `alpha/alpha_nominal in[1-1e-6,1+1e-6]`. Interval energies
`(1+q_a)^2`, phases at this h, cosine and Chebyshev recurrences yield (S15).
Thus the source-parameter and physical-scale uncertainties are included
separately from the stated1e-4 sample-error allowance. JSON stores rational
outward bounds; displayed decimals in this document are for reading.

The common root offset can also be recovered without assigning four separate
energies. Let `s_0=0` and `s_a=-2 kappa_0a/Delta=q_a-q_0`. The source trace gives

    q_a=84+1008g+s_a-(1/4)sum_b s_b.               (S20)

If each measured s1,s2,s3 has error at most sigma and g has error eta_g,

    |delta q0|<=1008 eta_g+(3/4)sigma,
    |delta qa|<=1008 eta_g+(5/4)sigma, a>0.        (S21)

These coefficients are the exact row absolute sums of the centered offset
map. They preserve the signed common orientation. Xi needs squared couplings;
(S20) additionally requires signed incidence. Independently fitting an
arbitrary common offset would discard the source trace relation being tested.

## S7. Placement access has an exact exceptional coupling

There is a useful preparation breadcrumb. Endpoint placements1 and3 are
cyclic for all g>=0 by S2. Original placement0 is cyclic except at exactly

    g=1/164.                                      (S22)

At this value a source eigenvector in original order `(0,1,2,3)` is

    v=(0,-b/a,1,1),     lambda=d+b=d+1344g.        (S23)

It has zero placement0 overlap. Conversely, any eigenvector with v0=0 must
have nonzero v1; the placement1 equation sets lambda=d+1344g. The remaining
two-state block requires lambda=d+/-b. With g>=0 only the plus sign is possible,
and `1344g=8+32g` gives (S22). Therefore this is the unique missed mode for
that placement family. The exception does not change the spectrum or S3;
it identifies an access condition relevant to building the shared instrument.
The exact source/eigenvector equation is included as a native operand.

## S8. Executable evidence and next use

Run `python3 check_signature.py`. The116 independent rational checks retain
the exact source, source-wide inequalities, inherited root intervals,
calibration inversion, both Hankel witnesses, a nontrivial rank-two TLS
control, fixed-cadence calibration uncertainties and the placement exception.
No native operation is run by this script.

`NATIVE_OPERANDS.json` supplies compact rational rounded H4/H3 matrices,
independent exact inverses/determinants, a nontrivial TLS control, T/Kr and
the exact blind-mode operands. The rational H4 entries are within1e-12 of
the actual nominal source Hankel matrix; `RESULTS.json` gives the entry and
determinant transfer bounds. A native check of these rounded matrices is a
native exact-arithmetic cross-check of the receiving certificate, not an
experimental trace or a fresh native evaluation of transcendental evolution.
Parent-owned receipts record whatever native operations are actually executed.

The completed Duck run `chapter2-signature-memory-20261015-01` supplied eight
signature-related native returns. `verify_native.py` independently checks
their bound payloads, Krylov bases, source-metric Grams, compressed operators,
zero leakage, receiving ranks and inverse enclosures:939 checks covering598
matrix entries pass. `NATIVE_VERIFICATION.json` binds every receipt hash.

These results supply the shared instrument with (i) a uniform source/control
comparison, (ii) independent calibration and stable reconstruction, (iii) a
finite receiving record and explicit error budget, and (iv) a source-access
choice that retains all modes. The test result suggests strong contact with
the concept.
