# Actual Si29 source effects, a finite localized account and its spatial field

Sean Brady is originator and conceptual director. OpenAI ChatGPT and Codex are
research collaborators. The source recovery is retained project work; the explicit
ball localization, physical unit assignments and the conditional field coupling
below are Codex constructions for the authorized Chapter III continuation.

## Outcome

The actual retained Si29 source supplies a complete positive excitation-energy
decomposition and an exactly calculable finite cube example. Every summed site
effect is **H0/8**. Species and coherence can evolve while this scalar spatial
share remains fixed. Its gravitational interpretation therefore has a precise
next interface: the physical local energy/stress coupling and a common energy
reference. The existing scalar record minimum is not substituted for that account.

The chosen finite localization gives a worked source with eight equal masses,
finite binding energy and an explicit, bounded departure from a spherical exterior.
Its first nonspherical term has degree four. The calculation keeps the adopted
Poisson receiver, energy-to-mass conversion and physical length assignment visible.

For the recovered source-to-space account and its finite-source mathematical
consequences: **The test result suggests strong contact with the concept.**
This classification concerns that construction. A physical gravitational coupling
and an absolute mass/length calibration remain open source assignments.

## 1. Exact source recovery and native tasks

The controlling route is `GEN4/voli_recent_source_recovery1/REPORT.md`, followed
by `GEN4/volii_duck_expansion2/REPORT.md`, sections 1, 2 and 6. Exact operands are
retained in `GEN4/volii_duck_expansion1/Q01_RESULT.json`: the incoming occupations
Ntx, every coherent spatial Gram Gtx, their denominator 240, and

    Q = [[128,8,0,8], [8,136,0,0], [0,0,128,8], [8,0,8,128]].

`EXACT_INPUTS.json` freezes these operands without converting mathematical values
to machine floats. Independently retained `OBSERVABLE_CLOSURE.json` in expansion2
reconstructs all 24 rational seeds and the same companion Q. `verify.py` checks
that agreement and all principal minors of each spatial Gram. It also checks all
eight incoming and outgoing sum identities, the finite cube geometry and moments,
and the regularized energy coefficients. **2,040 independent exact checks pass.**

`DUCK_R1_TASKS.json` contains two proposed `GEN3_SOURCE_OPERATOR_WORD` calls.
Each uses a 32 by 32 block diagonal matrix to check all eight sites at once:

    sum_t Ntx - I = 0;           sum_t Gtx - 240 Q = 0.

These are source-bound operands for the parent's Duck run, not a native execution
performed by this subtask. Actual acceptance, execution and fresh receipts belong
to that run. The expected outputs are complete zero matrices.

The earlier NPZ copies are absent in the current T500 directories. No absent
binary has been represented as an original recovered file. The exact retained
JSON supplies the operands used here. Old native references remain historical:
expansion2 Q01 retained root
`e004a48c2b327e79249a4f8d86d44464d39d5edd64e813e886e2d3147c9bd360`,
Q13 root `86f9bbc2f94d2a003503f2693c87870f3107f52cf6502b14cdc9a7e39ae121a0`.
Its `VERIFY.json` records source session
`ATOM3D_6bec0a12f43946d3b50fa38b6a4e923c`, Q01 call
`c28410f8ef1441b2b235419d8efc6f2f` and Q13 call
`053b4bbb93ba4c208b31c433fb8c2a60`; the original absolute receipt paths refer
to the earlier host. Those historical reports are preserved under `retained/`;
they are not claimed as newly recovered call directories.

## 2. Which energy and which evolution?

Let h be the positive square root of Q. Its positive-definiteness follows from
the leading principal minors 128, 17344, 2220032 and 281939968. In the orthonormal
eight-dimensional bright representation, the retained coherent generator and
the declared positive excitation account are

    Hgen = [[0,h],[h,0]],       H0 = diag(h,h) = |Hgen|.

They commute. H0 is not obtained from Hgen by adding a scalar constant: it replaces
the signed bright spectrum by its magnitude. It is the inherited positive account
used by the conserving transfer construction. It should not be silently renamed
the complete rest energy of the source, its gravitational mass, or an extra term
to add to Hgen and count twice.

Define the effects and energy effects exactly as in the retained source:

    Otx = diag(Ntx, h^-1 (Gtx/240) h^-1)/8,
    Etx = sqrt(H0) Otx sqrt(H0).

Every Ntx is a nonnegative diagonal occupation operator and every Gtx is a
positive semidefinite Gram. Congruence therefore makes every Otx and Etx positive.
The exact incoming and outgoing identities give, at every site x,

    sum_t Otx = I/8,       Ex := sum_t Etx = H0/8,
    sum_x Ex = H0,        [Hgen,Ex] = 0.

This is a short operator proof, valid for every state, rather than a fit to a few
trajectories. Each site receives exactly one eighth of the declared excitation
energy. Consequently the summed scalar energy is spatially flat and stationary
under this isolated source evolution. Species currents and coherence are retained
in the 36-coordinate closure; they are not erased by saying the scalar sum is flat.

The old retained energy evaluations illustrate the amplitude distinction:

| Preparation | Total relative excitation energy | Energy at every site |
|---|---:|---:|
| e0 | 11.302793352678457 | total / 8 |
| plus | 11.82826622637241 | total / 8 |
| minus | 11.131220607210203 | total / 8 |
| phase | 11.479743416791305 | total / 8 |

These decimals are retained evaluations, not newly certified square-root values.
The spatial fraction is the exact rational 1/8 in every row. Thus different
preparations can change total energy while preserving the same normalized spatial
shape. Gravity is not required here to distinguish every internal phase; the
specific conclusion is that this summed effect cannot supply a changing spatial
profile on its own.

## 3. A complete explicit localization, with its assignments stated

Use the retained cube-edge graph, whose 12 edges have source-coordinate length
two. A faithful embedding, fixing an arbitrary rigid orientation, is

    xi_x,j = +1 when bit j of x is 1, otherwise -1;
    Xx = ell * xi_x,             x = 0,...,7.

We explicitly choose this orthogonal cube realization. The edge graph alone
does not fix its angles. The physical length ell and physical orientation are
new assignments; the unavailable original coordinate JSON is not represented
as recovered. Choose a nonnegative normalized spatial
smearing zx(z), and an excitation-energy unit eu. The explicit candidate account is

    rho_exc(z) = (eu/c^2) sum_x <Ex> zx(z-Xx)
               = (M/8) sum_x zx(z-Xx),
    M = eu <H0>/c^2,             integral rho_exc dz = M.

Here the normalization of zx and the E/c^2 conversion are stated physical inputs.
This expression localizes the chosen positive excitation energy. It does not
assert that it already includes rest energy, source-field interaction energy,
counterterms, supports, pump, clock reference, receiver or apparatus.

For a finite-energy worked case, choose each zx to be a uniform ball of physical
radius delta, with 0 < delta < ell:

    zx(z) = 3/(4 pi delta^3) for |z|<=delta, and 0 otherwise.

The eight balls are disjoint, because the shortest center distance is 2 ell.
Each has mass m=M/8. This smoothing is a declared model choice; neither delta nor
ell is derived from the source effect algebra. The finite source, unlike an
unregularized point source, has a finite Newtonian self-energy.

## 4. Conditional receiving field and its calibration

Adopt the Chapter III isolated Poisson law and normalization,

    Laplacian a = -(8 pi G/c^2) rho_exc,       a(infinity)=0.

For a field point outside every ball, the shell theorem gives the exact field

    a(z) = (2GM/c^2) Kcube(z),
    Kcube(z) = (1/8) sum_x 1/|z-Xx|.

This is a worked finite source-to-field map once the receiving law is declared.
It does not identify the finite cube with a spherical source. Its flux through
any enclosing surface is -8 pi GM/c^2. At distances outside all eight balls the
same potential follows from eight point masses, while their interiors and their
finite binding energy continue to depend on delta.

Writing z=ell y exposes the remaining dimensional coefficient:

    a(ell y) = [2 G eu/(c^4 ell)] <H0>
               * (1/8) sum_x 1/|y-xi_x|.

Thus the retained relative source matrices do not determine the dimensionless
gravitational strength 2G eu/(c^4 ell). Assigning a physical eu, even if related
to Chapter I's epsilon by a separately justified common coupling, does not fix
ell or this coefficient by itself. The physical action unit and theta-to-time
conversion also remain distinct: the retained source permits theta=eu t/Iu.
Its source ruler edge 2 ell and its clock rates alone do not establish c.

A concrete candidate weak coupling consistent with this account is

    delta Hphys[a] = -(eu/2) sum_x abar_x Ex,
    abar_x = integral a(z) zx(z-Xx) d^3z.

This spatially averaged coupling yields the assigned finite-ball source density
under variation with respect to a. The point evaluation a(Xx) instead gives a
point source; it is a long-wavelength approximation to this chosen finite
smearing, not its exact variation. This
constructs a coupling; the source effects do not uniquely select it. A deformation
or lapse-dependent microscopic Hamiltonian would have to supply that choice.
Only a uniform lapse derivative is fixed by the total account; couplings with
additional differences between neighboring lapse values can redistribute local
response while leaving the uniform total response unchanged.

## 5. The finite cube's first departure from the spherical kernel

Let r=|z|, n=z/r, and q=sqrt(3) ell/r < 1. Every center has radius sqrt(3) ell.
The Legendre expansion of each Coulomb kernel converges absolutely for this r.
The cube's inversion symmetry kills every odd multipole. Its second moment is

    mean_x Xi Xj = ell^2 delta_ij,

so the traceless quadrupole vanishes as well. For the fourth moment,

    mean_x (n dot X)^4 = ell^4 [3-2 sum_j n_j^4].

Substitution into P4(u)=(35u^4-30u^2+3)/8 gives

    Kcube(r n) = 1/r
        + [7 ell^4/(4 r^5)] [3-5 sum_j n_j^4] + R6(r,n),
    |R6| <= q^6/[r(1-q^2)].

The remainder follows directly from |Pl|<=1 and the geometric sum over even
degrees l>=6. The simpler monopole error bound is

    |Kcube-1/r| <= q^4/[r(1-q^2)].

The degree-four coefficient is -7 ell^4/(2r^5) on a cube axis and
+7 ell^4/(3r^5) along a body diagonal. These are source-shape consequences of
the declared receiver and equal site energies. They are not fitted amplitudes.
Finite cube symmetry is sufficient for low-order isotropy, and does not make the
entire exterior exactly spherical. The bounds concern the region r>sqrt(3)ell;
for the ball model also require the observation point to lie outside every ball.

## 6. Finite binding energy and the shared reference

The self-energy of each uniform ball is -3Gm^2/(5delta), giving

    Uself = -3GM^2/(40delta).

There are 12 unordered center pairs at distance 2ell, 12 at 2sqrt(2)ell and four
at 2sqrt(3)ell. Because the balls do not overlap, each pair's exact mutual energy
equals its point-center value. Hence

    Umutual = -GM^2/(64ell) [6+3sqrt(2)+2/sqrt(3)].

Uself+Umutual is the negative on-solution Newtonian field/source binding account
under the Chapter III convention, including the exterior field. Restricting the
field integral to the eight balls would omit part of it. Counting both this
on-solution binding energy and the same source-field coupling again would double
count. M in the displayed Poisson equation is the declared prescribed excitation
mass. Re-inserting U/c^2 as an additional source would be a further self-gravity
completion, not an automatic part of the linear calculation.

The remaining full account is schematic until its source terms are specified:

    Efull = Eexc + Eother_fields + Einteraction + Ecounterterm
            + Ereference/apparatus,      all relative to one declared reference.

Each term needs a physical spatial incidence. Interaction terms can be carried
on bonds or fields; they need not admit an arbitrary positive on-site split.
The positive Gram-based excitation decomposition is therefore useful without
being promoted to a decomposition of every term in Efull. Chapter I's continuum
Hamiltonian/counterterm and Chapter II's paid reference supply templates for
retaining such accounts, not a direct identification with this Si29 source.

## 7. Why clock data alone leave the source baseline open

For a closed source, replacing Hgen by Hgen+kI multiplies every amplitude by the
same phase exp(-ik theta). Density evolution, relative frequencies and recurrence
of the density are unchanged. A phase comparison with an external reference can
resolve a relative common phase only through its specified coupling and paid
reference protocol. It does not establish an absolute mass baseline by itself.

Independently replacing the positive account H0 by H0+kI, when it remains positive,
changes the candidate total excitation mass by eu k/c^2 for a normalized state.
Using the corresponding congruence still gives every summed site effect
(H0+kI)/8. Thus density clock data do not select the mass offset. This is distinct
from recomputing |Hgen+kI|, which is generally not H0+kI because Hgen has both
spectral signs. Keeping these operations separate prevents phase invariance from
being used to erase an assigned gravitational source or an actual reference cost.

## 8. Next physically useful question

Specify the actual source Hamiltonian's dependence on a local lapse, spatial
deformation or receiver coordinate. Its derivative should return the proposed
local energy/stress operator, including the interaction and reference terms that
are active in that experiment. Then calculate the receiver's low-frequency,
long-wavelength susceptibility and its memory correction. The target is a
massless isotropic k^2 leading term with a source-derived coefficient, under one
shared calibration. This source question precedes assigning metric gamma or
equating a relaxed stiffness with a high-frequency propagation speed.

The finite cube result supplies a complete worked calibration and shape control
for that next calculation. It preserves the source's actual finite geometry and
its 36-coordinate species/current/coherence evolution while showing exactly what
additional physical relation is being proposed.

## Reproduction

Run `python3 -B source/verify.py` from the campaign directory, or run the script
by its absolute path. It uses the Python standard library and only files under
this source directory. `prepare.py` is the retained original task builder and
requires the project paths; offline replay uses the frozen exact inputs/tasks
and local retained source snapshots. No native process, old campaign or physical
experiment is relaunched by the independent verifier.
