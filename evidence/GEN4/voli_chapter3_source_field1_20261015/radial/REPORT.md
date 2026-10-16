# Exact finite radial source, field, flux and boundary account

## Source and executable question

The retained `GEN4/native_energy_source1/RADIAL_METHOD.md` and
`GEN4/vol_i_activation_selection1/NETWORK_METHOD.md` select radial edge
conductances `c_i=i(i+1)`, with the common transport factor placed in units.
The retained interpretation proposes isotropic three-dimensional transport.
The present construction keeps those conductances and supplies an explicit
extended source and the complete energy/force account. It is a conditional
monopole receiving model. Neither concentric shells nor angular isotropy are
identified with the actual cube sites or the physical Chapter I clock.

Native operands are in `DUCK_R1_TASKS.json` (source inverse) and
`DUCK_R2_TASKS.json` (three flux/energy identities). The parent owns native
execution and receipt readback. `verify.py` is a separate portable rational
check: 312 assertions pass. Its one pre-execution syntax correction is
retained in `IMPLEMENTATION_LOG.md`.

## 1. Finite source problem, including the outer boundary

Let `r_i=i h`, `i=1,...,L`, with `a_L=0`. There is no inner sink:
`c_0=0`. Source shells have masses `M_unit m_i`, and

    kappa = 2 G M_unit/(c^2 h),
    q_i = kappa m_i,
    (Ka)_i = c_i(a_i-a_(i+1)) + c_(i-1)(a_i-a_(i-1)) = q_i.

`K=B^T C B`, where `B` takes outward edge differences and
`C=diag(c_i)`. Every nonzero vector has positive `v^T K v`, since its
edge differences cannot all vanish while the outer endpoint is zero.
The source boundary problem therefore has a unique solution.

The exterior exit is essential. Remove its conductance from the last
diagonal to obtain the closed conservative graph `K_closed`. Its row sums
vanish, so `K_closed*1=0` and `1^T K_closed a=0`. A positive-total source
has `1^T q>0` and cannot satisfy that closed static problem. The absorbing
boundary is thus an explicit flux account, not a numerical convention
that can be silently omitted.

The exactly solved example has `L=9`, eight unknowns,

    m = (0, 1/5, 0, 3/10, 1/10, 0, 2/5, 0),
    sum m_i = 1,     kappa = 1/50.

The field is obtained from `Ka=q`; no desired `1/r` field enters the right
side. The chosen rational mass fractions are a declared source fixture, not
an inferred mass spectrum or a physical assignment of the microscopic sites.

## 2. Exact Green kernel and enclosed flux

Summing the source balance through node `i` gives

    c_i(a_i-a_(i+1)) = kappa M_i,   M_i=sum_(j<=i) m_j.

The telescoping edge resistance is

    1/c_i = 1/i - 1/(i+1).

Summing from node `i` to the absorbing boundary gives

    H_ij = 1/max(i,j) - 1/L,
    a_i = kappa sum_j H_ij m_j,
    K H = I.

Thus source injection, field and flux come from one operator. On the open
interval `r_i<r<r_(i+1)`, use its exact harmonic interpolation. Then

    a'(r) = -2 G M_unit M_i/(c^2 r^2),
    g(r) = -G M_unit M_i/r^2,
    -c^2 r^2 a'(r)/(2G) = M_unit M_i.

Outside shells produce a constant interior potential and zero interior
acceleration. Across a shell the derivative jump carries exactly its mass.
On an ideal shell itself, specify the one-sided field or the mean-field
virtual-work convention; they are distinct from the open-interval formula.

## 3. What is exact about the continuum connection

For the declared concentric shell source, this finite network is exactly the
radial continuum shell solution sampled at `r_i`. Indeed,

    a_L(r) = (2G/c^2) sum_j [M_unit m_j/max(r,r_j)
                                      - M_unit m_j/(Lh)].

The subscript denotes the finite outer reference, not a partial source.
The continuum interpretation uses the pre-existing spherical receiving
geometry; it is not a derivation of angular isotropy or microscopic spatial
incidence from a finite-state spin generator.

The isolated field differs by one known constant:

    a_infinity(r) = a_L(r) + 2 G M_total/(c^2 Lh).

Consequently every acceleration and flux agrees, while potential and escape
to infinity require this correction. Treating `a_L=0` as a zero-at-infinity
potential would retain a finite bias even if the mesh were arbitrarily fine.

## 4. Controlled uniform-ball limit

For a ball of radius `b`, place the mass of each radial cell on its outer
endpoint: `h=b/n`, `r_j=jh`,

    m_j/M = [j^3-(j-1)^3]/n^3,    j=1,...,n.

Let `eta=GM/(c^2 b)`. Write the reduced lift `alpha=a/eta`.
The continuous uniform ball is `alpha=3-x^2` inside and `2/x` outside,
where `x=r/b`. The sampled isolated lift obeys, at every radius,

    0 <= alpha_uniform-alpha_shell
       <= 3/n - 2 H_n/n^2 < 3/n,
    H_n=sum_(j=1)^n 1/j.

The upper bound is the exact central error. Moving a mass element from `s`
to its cell endpoint `s_j>=s` changes the kernel by a nonnegative amount
no larger than `1/s-1/s_j`; integration gives the stated expression.
At each noncentral mesh node the outer one-sided enclosed mass is exactly
`M x^3`, so the reduced acceleration is exactly `-x`. Exterior acceleration
is exact for every radius outside the source.

At a finite absorbing radius `R=Lh`, there is the additional exact reduced
lift offset `2b/R`. The uniform-ball binding account satisfies

    0 <= U_shell/(GM^2/b) + 3/5
       <= 3/(2n) - H_n/n^2,
    U_finite = U_shell + GM^2/(2R).

For the energy inequality, write the pair kernel as
`1/max(s,t)=min(1/s,1/t)`. When both radii are moved outward, its nonnegative
decrease is at most `(1/s-1/s_j)+(1/t-1/t_k)`. The two pair integrals
therefore give twice the central potential-kernel error, and the energy's
factor `1/2` leaves the stated bound.

An isolated continuum limit therefore requires both `h/b -> 0` and
`b/R -> 0`. Refining at fixed `R/b=2` leaves reduced lift bias `1` and
binding-energy bias `1/4`. This exact separation is a useful computational
breadcrumb: small discretization error does not imply small boundary error.

## 5. Energy and force in one account

Put `u=a/kappa` and measure energy in `G M_unit^2/h`. The finite functional is

    F[u;m] = (1/2) u^T K u - m^T u.

It has stationary equation `Ku=m` and exact minimum identity

    F[u_*+v;m]-F[u_*;m] = (1/2) v^T K v.

On its solution,

    U_L/(G M_unit^2/h) = -(1/2) m^T H m,
    U_infinity = U_L - G M_total^2/(2R).

For the executed fixture's independent exact check,

    U_L/(G M_unit^2/h)        = -9427/252000,
    U_infinity/(G M_unit^2/h) = -2603/28000.

The missing exterior gradient energy is positive `G M_total^2/(2R)`.
The infinite-reference source coupling changes by twice this amount with
the negative sign, so the full on-solution binding change is negative once.

For a shell of radius `r_j` that moves while shell ordering is unchanged,

    -dU/dr_j = -G M_j [M_(<j)+M_j/2]/r_j^2.

Outer shells exert no radial work on it. The half self term is the mean
of the two one-sided self fields and agrees with differentiating the shell's
own energy `-G M_j^2/(2r_j)`. In the small test-shell limit the usual inward
force `-G M_j M_(<j)/r_j^2` is recovered. A shell force is a derivative with
respect to its spherical radius, rather than the net vector force on its
center, which is zero by symmetry.

## 6. Exact native targets and independent controls

1. Solve the eight source equations by installed `GEN2_READOUT_INVERSE`.
2. Evaluate `B^T C B-K`, `KH-I`, `HKH-H` with the installed source-operator
   word. The blocks should each be zero.
3. The independent checker reconstructs the solution by exact Gaussian
   elimination, checks all eight source fluxes, signed energy and the shell
   virtual-work derivative, and bounds six uniform-ball refinements.
4. Two exact controls fail the intended identities: omitting the `-1/L`
   Green correction, and adding an invented central sink. They expose wrong
   boundary and inner-flux assumptions without adding new empirical gates.

For the conditional finite shell receiving construction, the independent
test result suggests strong contact with the concept. The physical mass
assignment, angular completion, kinetic law and elapsed-time calibration
remain separate source interfaces; this calculation does not select them.
