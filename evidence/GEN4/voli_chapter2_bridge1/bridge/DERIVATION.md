# Original Write one-form, occupied source, and clock-coherent preparations

Sean Brady is originator and conceptual director; OpenAI ChatGPT and Codex are
AI research collaborators. The phase incidence, source operators and completed
clock preparations below are inherited. The compatibility decomposition,
preparation-class comparison and exact residual identities are new Codex
derivations for the Chapter II continuation. No physical coefficient is fitted.

## 1. Sources and conventions

Use the finalized Chapter I, §§2–3, 5–7, and
`GEN4/duck_write_tensor1_20261014/sources/ACTION_UNIT_MAP.md`. The retained
inverse is

    phi_a=(gamma+delta)/2+chi,
    phi_b=(gamma-delta)/2+chi, phi_p=chi,
    omega_W=hbar(dgamma+3dchi).

This is the original signed legal-Write ledger. The canonical state one-form
is `i hbar <Psi|dPsi>`; the signed Hilbert phase has the opposite sign.
The action-unit identification `I_*=hbar` receives the same physical quantum
phase convention; it assigns neither a numerical time unit nor a length.

Retain the actual whole sixteen-state operators

    S=Swap, N_s=(I+S)/2,
    H_pair=S+Q_L+Q_R+Q_L Q_R=2N_s+K,
    K=Q_L+Q_R+Q_L Q_R-I,
    D=Q_L-Q_R, C=i S D.

Here `K` is the even source operator, not the positive interacting field form
also denoted K in Chapter I §5. Write the latter as `K_field` here.
Exactly `[K,N_s]=[K,D]=[K,C]=0` and `{S,D}={S,C}=0`.
All six unequal-occupation lanes and four equal-occupation states remain.

`gamma`, `delta`, `chi` and the ordered Write word remain separate coordinates
in the retained source record. The current recipient depends on gamma; that
does not make delta or the word absent. The native full endpoint Hilbert action
has a retained nonzero residual against the pair-current recipient. No full
Hilbert intertwiner between these distinct source representations is asserted.

## 2. Exact occupied receiving lift

Fix a normalized source vector `psi0` and its expectation `n=<N_s>_0`. The
declared current/common-phase receiving lift is

    Psi_W(gamma,chi)=exp(-i3chi) exp(-i gamma N_s) psi0.

It has exactly

    i hbar <Psi_W|dPsi_W>=hbar(n dgamma+3dchi),
    omega_W-i hbar <Psi_W|dPsi_W>=hbar(1-n) dgamma.       (B1)

Since N_s is a projector, equality for arbitrary nonzero dgamma holds precisely
on its occupied subspace `N_s psi0=psi0`. This gives an exact, specified
preparation class in which the original scalar ledger is the pullback of the
canonical receiving connection. It is a receiving construction using the
retained pair generator; it does not change the original endpoint action.

The coordinate delta is still carried by the source incidence and history.
No independent quantum delta generator is supplied by this two-coordinate
recipient. An actual full source-channel lift must state its delta incidence.

## 3. Full energy and the even complement

The source energy lift at the same current angle is

    Psi_H(gamma)=exp[-i gamma H_pair/2] psi0
                =exp(-i gamma N_s) exp(-i gamma K/2) psi0.

Its generator retains the full even energy, while its D/C conjugation is the
same current rotation as the N_s lift. The relative operator is exactly

    Psi_W=exp[-i(3chi I-gamma K/2)] Psi_H.                (B2)

On a fixed K eigenspace with eigenvalue k, the relative factor is the scalar
phase `exp[-i(3chi-k gamma/2)]`. Its differential is retained; removing that
factor from a state representative requires retaining the associated common
phase/reference-energy account. If the preparation coherently occupies
different K eigenspaces, the relative factor carries their actual different
phases and is not a single scalar state phase.

At the level of scalar canonical one-forms alone,

    i hbar<Psi_H|dPsi_H>=hbar(n+kbar/2)dgamma,
    omega_W-i hbar<Psi_H|dPsi_H>
      =hbar[(1-n-kbar/2)dgamma+3dchi].                  (B2a)

Thus scalar action compatibility on this fixed preparation requires
`3dchi=(n-1+kbar/2)dgamma`. It is an expectation identity and does not require
K variance to vanish. The following whole-vector comparison is a separately
identified stronger question; it is not an additional condition imposed on the
original scalar ledger or on the completed interacting clock.

For differentiable gamma and chi, define the exact even-generator residual

    R_even=(gamma_dot K/2-3chi_dot I) Psi_W.

Let `kbar=<K>_0` and `V_K=<K^2>_0-kbar^2`. Then

    ||R_even||^2=(gamma_dot^2/4) V_K
                 +(gamma_dot kbar/2-3chi_dot)^2.        (B3)

This is an orthogonal mean/complement balance. A scalar common phase can
receive the mean; the variance is the retained operator complement. Literal
vector-generator compatibility requires both terms to vanish. A single K
eigenspace removes the variance term, while `3chi_dot=k gamma_dot/2` is the
remaining path condition. These are conditions to compare with the original
path, not rules selected to adjust its outcome.

For the original placement calibration vector `|e0 e0>`, N_s=1 exactly but K
is not scalar on its occupied spectral support. Direct exact source identities
give `<K>=573047` and `Var(K)=14384109824`. Thus the occupied one-form (B1)
is exact for this actual retained source vector, while (B3) retains a nonzero
full-energy complement whenever gamma_dot is nonzero. Its placement-state
preparation remains distinct from the six interacting clock preparations.

## 4. Legal role tangents and the original path condition

A legal pure active role has `dphi_j=s d ell`, with signed s and positive
progress ell. The retained incidence gives

| Active role | dgamma/(s d ell) | ddelta/(s d ell) | dchi/(s d ell) |
| --- | ---: | ---: | ---: |
| a | 1 | 1 | 0 |
| b | 1 | -1 | 0 |
| partner p | -2 | 0 | 1 |

Consequently the scalar condition in (B3), for a K eigenpreparation, requires
`k=0` on a/b strokes and `k=-3` on partner strokes. The actual unit-strength Q
is positive and has all four roots greater than 600 (the exact matrix
`Q-600I` is strictly diagonally dominant with positive diagonal). Hence

    K=(I+Q_L)(I+Q_R)-2I > (601^2-2)I=361199 I.

Neither required value belongs to this actual source spectrum. This locates
the precise missing receiving input: the original signed one-form and the full
positive source-energy evolution have different per-stroke common-phase
payments. Their current-angle agreement remains exact. A reference-phase
ledger, different physical incidence or additional received source channel
must be stated if they are to describe one vector evolution. A positive
elapsed clock does not turn a signed inverse stroke into a negative duration.

The fixed-preparation scalar comparison (B2a) can be stated without the
stronger vector criterion: it requires `kbar=2(1-n)` on a/b strokes and
`kbar=-1-2n` on partner strokes. For `0<=n<=1` these ranges are [0,2] and
[-3,-1], respectively, while the actual K expectation exceeds 361199.
Consequently this direct full-energy one-form identification also has a
specific retained reference/channel payment to supply on the original legal
tangents. This is the comparison for the unshifted actual H_pair/2 and the
fixed preparation specified above; the general changing-state connection is
retained in (B6a).

For the bare Hamiltonian `epsilon H_pair`, matching its current angle to
model time requires `gamma_dot=2epsilon`. This is its completed free-source
current equation. It is not the original path's generally variable signed
gamma_dot, nor the interacting clock's actual nu. A separate time map is
required to identify these coordinates physically.

## 5. The nontrivial interacting clock preparation has a different class

On one fixed unequal-occupation lane, put S=sigma_x and
`Z=sigma_z+i sigma_y`. For any source marginal, including a marginal of an
entangled source–field state, write `n=<N_s>` and `z=<Z>`. Bloch positivity
gives exactly

    |z|^2 <= 1-<S>^2 = 4n(1-n).                         (B4)

Therefore nonzero clock amplitude requires `0<n<1`. The occupied N_s=1
class of §2 has z=0 and is not the Chapter I clock preparation. If the achieved
amplitude bound gives `|z|>=m>0`, then

    (1-sqrt(1-m^2))/2 <= n <= (1+sqrt(1-m^2))/2.         (B5)

The upper and lower bounds exclude both projector endpoints. These formulas
can consume the completed lane-specific amplitude certificates, without
substituting a newly chosen preparation.

For the actual joint Hamiltonian of Chapter I §5, the exact form Ehrenfest
identity also gives

    dn/dtau=g <sigma_y phi_+ - sigma_z phi_cross>,
    d<N_+ - N_->/dtau=-dn/dtau.                         (B6)

The second identity follows from the retained conserved charge
`Q_ch=N_s+N_+-N_-`. Both circular polarizations and the joint correlations
remain. Thus n is a dynamical occupation, not a coefficient that may be set
to one for the clock state.

More generally an abstract smooth normalized joint-state path can be
written in the original phase frame as

    Psi=exp(-i3chi) exp(-i gamma N_s) eta,
    a_eta=i<eta|d eta>, n=<eta|N_s|eta>.

The exact connection and its original-ledger difference are

    i hbar<Psi|dPsi>=hbar(n dgamma+3dchi+a_eta),
    omega_W-i hbar<Psi|dPsi>=hbar[(1-n)dgamma-a_eta].     (B6a)

This retains the internal joint-state Berry form, including source–field
entanglement and changing n. Equation (B1) is the fixed-eta class; replacing
its n by n(t) while dropping a_eta would change the account.

For the actual continuum trajectory, finite energy means membership in the
closed Hamiltonian form domain, and does not require a strongly differentiable
Hilbert-space vector. Let H be the retained self-adjoint semibounded joint
Hamiltonian, Psi in its form domain, and mu_Psi its spectral measure. Then

    a_H(Psi)=lim_{h->0} i<Psi,(exp(-iHh)-I)Psi>/h
            =integral lambda d mu_Psi(lambda)=q_H[Psi]. (B6b)

The form-domain hypothesis gives `integral |lambda|d mu_Psi<infinity` for
semibounded H. The spectral integrand is bounded by |lambda| because
`|exp(-i lambda h)-1|<=|lambda h|`; dominated convergence establishes the
displayed overlap derivative. No D(H) assumption or Hilbert-vector derivative
is used. The spectral measure, and therefore this energy-form value, is
constant under the actual unitary evolution. Along that orbit the notation
`i<Psi|dPsi>=q_H[Psi]d tau` denotes this overlap/form connection. Source
rotations preserve the common form domain; factoring the smooth bounded
gamma/chi rotations gives the same decomposition (B6a) in overlap form.
Comparing the original path to that trajectory requires its actual
phase/time/preparation incidence.

A scalar rephasing can always add a specified exact phase differential to the
canonical connection. Its Schrodinger Hamiltonian acquires the same scalar
time derivative, so `a-<H>d tau` is unchanged. Such a common phase is retained
reference data; by itself it does not select the physical energy normalization
or supply the original-source-to-clock preparation map.

## 6. A completed hard-coherent clock provides an explicit phase/action example

The inherited hard reference uses orthogonal exact charge eigenbranches
`Q_ch Phi0=0`, `Q_ch Phi1=Phi1`, with preparation

    Psi_ref(0)=(Phi0+Phi1)/sqrt(2),
    <Phi0|Z|Phi1>=2M, M>0.

It follows exactly that `<Q_ch>=1/2`, `Var(Q_ch)=1/4`. On this branch span,
the charge orbit `exp(-i gamma Q_ch)` has

    z(gamma)=M exp(-i gamma),
    i hbar <Psi|dPsi>=(hbar/2) dgamma.                  (B7)

The clock's phase rotates by gamma, while its canonical charge-orbit action
has coefficient one half. The transition charge difference and the prepared
charge expectation have different roles. An exact rational two-state
representation is supplied to the test operands; the arbitrary positive M
is retained as its original transition weight rather than set by the algebra.

For the actual hard reference evolution with branch energies E0,E1 and
Omega=E1-E0, the source record supplies

    z(tau)=M exp(-i Omega tau),
    i hbar <Psi_ref|dPsi_ref>=hbar(E0+Omega/2) dtau.     (B8)

The common E0 remains in its energy/action ledger, while the observed phase
reads the gap Omega. The completed actual clock then differs from this
reference through its already bounded joint soft dynamics. Its inverse
coordinate is d tau=d theta/nu; it is not inferred by setting gamma=theta.

## 7. Worked histories of the six actual interacting clocks

This example consumes the completed actual dynamics, not a selected rate
profile. For each original lane preparation let `[ell,u]` be its retained
uniform actual-rate enclosure on `0<=tau<=T0=573049 pi`. The completed
certificate gives `theta(0)=0`, nonzero amplitude and continuous positive nu.
The exact rational endpoints satisfy, separately in all six lanes,

    573049 ell > 3/2, 573049 u < 2.                    (B9)

Integrating the actual rate gives

    ell tau <= theta(tau) <= u tau,
    3pi/2 < theta(T0) < 2pi.

Consequently there are unique actual crossing times tau_k for
`theta(tau_k)=k pi/2`, k=1,2,3, before T0. A fourth crossing has not occurred
by T0. No claim about continuation beyond T0 is needed. The exact crossing
enclosures are

    k/(2u) <= tau_k/pi <= k/(2ell), k=1,2,3,            (B10)
    1/(2u) <= (tau_k-tau_(k-1))/pi <= 1/(2ell).

The retained intervals also have strictly ordered disjoint enclosures for
successive crossings. The third-crossing coefficients illustrate their actual
different lane histories (decimal endpoints rounded outward):

| Original lane | Lower tau_3/pi | Upper tau_3/pi |
| --- | ---: | ---: |
| 01 | 429786.750748927653 | 429786.751360098201 |
| 02 | 429786.753217082525 | 429786.755842418250 |
| 03 | 429787.248503309966 | 429787.655330598939 |
| 12 | 429786.750861586313 | 429786.751564693192 |
| 13 | 429787.210608853379 | 429787.586509288419 |
| 23 | 429787.171628775011 | 429787.515716566083 |

All eighteen crossing intervals, their original rational rate inputs, source
hashes and amplitude-to-occupation constraints are in
`ACTUAL_CLOCK_HISTORY.json`. These are clock quarter labels. They are distinct
from original legal Write events, the original gamma coordinate, and the eight
retained product addresses. An identification between those records needs its
explicit receiving map; no equality of their labels is used in (B9)–(B10).

Let E_total denote the actual conserved joint energy-form expectation of the
particular original preparation. It retains its even source energy, both
counterterms, field energy and joint correlations. On the fixed lane,
`H=epsilon e I+epsilon S+K_field>=epsilon(e-1)I>0`, so E_total is positive.
Using the finite-energy overlap identity (B6b), its dynamical energy-action
payment at a crossing is exactly

    J_k=hbar E_total tau_k,
    k/(2u) <= J_k/(hbar E_total pi) <= k/(2ell).         (B11)

E_total is not assigned a new numerical value here. The full variational
action separately retains

    S=hbar integral [B_theta-E_total/nu] dtheta.

Thus the clock history supplies a paid energy-action history while retaining
the Berry form and all source–field correlations. A physical seconds value
still uses the recorded time-unit assignment; the table is in model time.

`actual_clock_history.py` derives this packet from the original native
RESULTS.json and EXACT_INPUTS.json and passes 61 independent exact-rational
checks. It performs no rate simulation and launches no native calculation.

## 8. Exact scope and next receiving quantities

The derived bridge consists of: an exact occupied-class pullback, its even
operator residual, original legal tangent conditions, a strict distinction
between that class and the nonzero clock preparation, and a nontrivial
hard-coherent example in which phase slope and action weight are both explicit.
The eighteen newly deduced actual quarter-crossing intervals supply a worked
nontrivial clock/energy-action history on each completed interacting
preparation, separately from the occupied-class example.

Identifying the original action ledger with a quantum expectation requires a
physical rule selecting the preparation/channel and reference phase, together
with the gamma/delta/chi-to-model-time incidence. Those inputs have not been
chosen by the identities above. Preserving the whole variational action also
retains its Berry form, both field counterterms and the even source energy.
The occupied-class construction is therefore a completed mathematical
recipient; the actual original-source-to-interacting-preparation identification
is the remaining physical interface exposed by the calculation.

`exact_identities.py` provides independent exact-rational checks and complete
matrix operands for native reuse. Its own output identifies that independent
scope. No original campaign, installed core or native runtime is changed.
