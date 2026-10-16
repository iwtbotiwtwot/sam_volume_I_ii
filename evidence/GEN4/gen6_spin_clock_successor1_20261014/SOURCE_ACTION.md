# GEN6 Spin-Clock Successor Source/Action Map

Date: 2026-10-14  
Status: source-analysis note; no numerical successor run performed here  
Authority: H002616 source-first continuation and R000039 source map

## Purpose

This note maps the source material available for a spin-informed H02--H06
clock successor. It is not a new live authority entry and does not alter the
frozen H02--H06 record. It separates source statements from Codex deductions so
the next implementation can receive source-derived quantities before comparing
them with the frozen GEN6 action family.

The productive route is:

```text
original evolution / update rules
 -> source operator, metric and readouts
 -> retained projection plus complete hidden dynamics
 -> received action / response
 -> comparison with the frozen GEN6 family
```

Finding a source that already writes the final unified action is useful but not
required. Separately composable typed laws are enough to build the source-side
functional and then compare.

## Direct source inventory

| Source | Type | Use in this map |
|---|---|---|
| `GEN4/gen6_spin_source_transfer1_20261014/REPORT.md` | current result | Current H002616 continuation, H02 one-stroke clock transfer, source-first route and spin-method transfer. |
| `SAM_RETRIEVAL/packets/R000039_SUPPORT_RECURRENCE_TEMPORAL_FIELD_MAP/INDEX.md` | retrieval map | Support recurrence, temporal A exposure, G679c/G643c/V4.2, q_A carrier route and open comparison items. |
| `GEN4/gen6_original_challenge2_20261013/SOURCE_DERIVATION.md` | retained derivation | Signed Write phase/action, contact coefficients, canonical one-form, source energies, proper-time phase, static A functional and frozen-family comparison rows. |
| `/home/lilhelper/SAM_Research_Overflow/The_Courtroom/SAM_NATIVE_ACTION_ENGINE_V4_2.md` | original Courtroom source | A-kernel, typed A-exposure route, support-flow split, time/action readout and recurrence/write-depth constraints. |
| `/home/lilhelper/SAM_Research_Overflow/The_Courtroom/SAM_NATIVE_MASTER_FORMULA_V4_2.md` | original Courtroom source | Formal `Exp_c[A_L]` exposure syntax and symbol table. |
| `volume_IV/SAM_VOLUME_IV_INFORMATION_BRIDGE_TECHNICAL_SPINE.md` and `SAM_HISTORY/entries/H000185_2026-08-12_AFC4_MATTER_QA_BOUNCE_INTERSECTION_SUPPORT.md` | frozen bridge / history | Matter-side q_A support, normalized support demand and relative velocity/common A account. |
| `/home/lilhelper/SAM_Research_Overflow/The_Courtroom/16_THE_LAST_CAMPAIGN/LC03_result.md` | Courtroom mechanism result | Closed matter write -> q_A -> 1/8 carrier -> ledger compression -> A readout. |
| GitHub `iwtbotiwtwot/STAM_Model-A.v.1.0`, commit `822f8f4241c1b0b7fb272eb30c1022dd860ea18c`, `tests/Substrate/G679c_SUPPORT_FLOW_ACTION_SPLIT_SELECTOR/` | original selector payload | Selects scoped support-flow split and records its boundaries. |
| `GEN4/spin_hidden_direction1/REPORT.md` and `GEN4/spin_hidden_direction1/NEXT.md` | completed spin source result | Retained/hidden operator method, source metric, residual composition and two-scalar continuation formulas. |

## Source statements

These are statements directly recovered from the sources above.

1. Signed Writes carry a phase/action increment

   ```text
   Delta phi_Write = sigma*pi/2
   Delta S_Write = hbar*Delta phi_Write
   sigma = +/-1
   ```

2. The native contact recovery gives exact source coefficients

   ```text
   E_B = 6 - 2 B cos(phi_a - phi_p) + 2 B cos(phi_b - phi_p)
   ```

   The coefficient origin is the recovered source contact table, not a fit to
   H01 or H02.

3. G286/G286b supply the canonical two-channel action one-form

   ```text
   dS = p dx - E dt
   ```

   with the original baseline subtraction retained in gravitational exposure.

4. G470/G471 supply role-selected source rates and energies

   ```text
   lambda_j = (A0^2 k_j / 2^n_j) / (1 + (A0/2)(q_j/2^D))
   E_j = hbar*lambda_j/t_SW
   S_A = E_j*T_A
   Delta phi_A = S_A/hbar
   ```

5. G406 supplies the weak-field slow-motion kinetic/potential reading

   ```text
   L_NR = (1/2) m_j v_j^2 + (1/2) E_j A
        = (1/2) m_j v_j^2 - m_j Phi_N
   m_j = E_j / c_physical^2
   ```

6. G481 supplies the proper-time phase readout

   ```text
   d phi_j = (lambda_j/t_SW) d tau_A
   d tau_A/dt = sqrt(1 - A)
   ```

7. V4.2 starts from the source-over-distance A-kernel

   ```text
   A(r) = r_s/r
   r_s = 2GM/c^2 = 2GE/c^4
   A_L(x) = sum_i r_s,i / |x - x_i|
   ```

8. V4.2 routes `A_L` through typed exposure and ledger readout

   ```text
   Exp_c[A_L] -> O_SAM[p,c] -> W_SAM[p,c]
   ```

   and its time/action subcase is

   ```text
   Delta_phi_A[p,c] = epsilon_p * T_c[A] / t_SW
   epsilon_p = lambda_p
   ```

9. G679c/V4.2 select the support-flow split

   ```text
   A_total = A_environment + A_support + A_velocity
   A_environment = A_L
   A_support = burden required to keep a matter closure open
   A_velocity = relative-motion wake burden
   v_rel = v_matter - v_substrate_support
   A_velocity(0) = 0
   ```

   The original G679c payload is a scoped typing gate. It records
   `engine_update_status = NOT_APPLIED_BY_THIS_GATE`.

10. The G679c dependency chain records rest support as forced standing
    SW/eigenmode recurrence and rejects static zero-write rest. The local SAMA
    index names G643c as:

    ```text
    PASS_REST_EIGENMODE_RECURRENT_PROPAGATION_REQUIRED_NOT_STATIC_PLACEMENT
    ```

11. V4.2 recurrence/write-depth rules are discrete constraints:

    ```text
    depth does not create extra A
    memory overlay cannot create extra A
    recurrence must conserve A
    recurrence variants require route-distinct and ownership-valid status
    recurrence may not alter radix-R closure
    recurrence may not violate weighted route-depth conservation
    ```

12. Volume IV/H000185 install the normalized support account

    ```text
    A0 = 1/(12*pi)
    A_total = A_environment + A_support + 2*beta_rel^2
    D_bounce(A)/D_bounce(A0) = A/A0
    q_A_required(A)/q_A_required(A0) = A/A0
    ```

    These are relative support demands, not joules.

13. LC03/QP092C route matter-side support into the field readout through
    carrier compression:

    ```text
    closed matter write
      -> q_A source support
      -> 1/8 unresolved tensor carrier
      -> ledger compression
      -> A(r)=r_s/r
      -> force/clock/road readout
    ```

14. The later spin source uses the inherited reversible single-site Gibbs
    heatbath with uniform site selection. Its generator is source-local:

    ```text
    L = N(I - P)
    ```

    where `P` is the heatbath transition. H002616 preserves that provenance:
    spin methods are reusable source-operator techniques, not a relabeling of
    the heatbath as signed-Write dynamics.

## Codex deductions from the source statements

These are technical deductions for the successor design. They are not new
source claims.

### 1. Independent variables versus readouts

The recovered source record supports this working separation:

| Quantity | Current source status | Successor implication |
|---|---|---|
| Signed Write phase/action | independent source event increment | Keep signed orientation and event work; do not replace by unsigned elapsed time. |
| Source positions/momenta | independent once incidence is supplied | Pull into GEN6 coordinates before selecting `M=I` or any other mass metric. |
| `A_L` | source-over-distance field account | Build field account before readout; do not let q_A update A directly as mass. |
| `Exp_c[A_L]` | typed exposure/readout | Choose channel and support domain before using phase/action formula. |
| `A_support` | typed support burden / recurrence lane | Treat as constrained recurrence/support demand unless a source supplies an independent inertia. |
| `A_velocity` | relative-motion wake readout | Use `2 beta_rel^2` lane where source-selected; do not double count potential and kinematic readings. |
| `q_A` | matter-side source support | Route through 1/8 carrier and ledger compression before A readout. |
| `Lambda` / frozen reservoir | frozen-family comparison variable | Do not assume it is a source-independent degree of freedom; receive or replace after source mapping. |
| Spin `L=N(I-P)` | heatbath source operator | Reuse response/elimination method with spin provenance preserved. |

### 2. Static A-field functional and coefficient origin

From the V4.1 A-kernel and G406 coupling, the source-side static functional is

```text
S_static = integral dt d^3x [
  - c_physical^4/(32*pi*G) |grad A|^2
  + rho*c_physical^2*A/2
]
```

The coefficient `c_physical^4/(32*pi*G)` is source-derived from the Green
equation `nabla^2 A = -8*pi*G*rho/c_physical^2` and the source coupling
`+rho*c_physical^2*A/2`.

If a normalized chart uses

```text
x = ell_* x_N
t = t_* s_N
A = A_* phi_N
S = S_* S_N
```

then the received spatial coefficient is

```text
kappa_N = (c_physical^4/(16*pi*G)) * (A_*^2 t_* ell_* / S_*)
```

This gives a concrete comparison route for frozen `kappa=2`; it does not by
itself select `kappa=2`.

### 3. Source-potential Hessian route for the GEN6 quadratic block

The frozen comparison term has the structure

```text
-(q_can*g/2) (y - r - a v)^T B68 (y - r - a v)
```

Let `U=(y,r,a)` and `z=y-r-a v`. The source side should first receive the
whole source potential into `V_src(U)`. The quadratic comparison is then through
the actual source Hessian

```text
H_src = nabla_U^2 V_src
```

and the GEN6 frozen form corresponds to a block structure

```text
g * J^T B68 J,   J = [I, -I, -v]
```

including the `a^2` counterterm and mixed blocks. Therefore `g` is not selected
by reading the frozen fixture. It must be compared against the source Hessian
after coordinate, field-boundary and unit reception.

### 4. Recurrence/support contributes constraints before inertia

The support recurrence sources currently give:

```text
rest support = recurrent standing SW/eigenmode propagation
recurrence conserves A
recurrence does not create extra A
recurrence respects weighted route-depth
```

This supports a constrained-route contribution to the action/account. It does
not yet require a separate term of the form

```text
(eta/2) dot(Lambda)^2
```

Such a term remains a comparison candidate only if a source-side evolving
coordinate and kinetic coefficient are identified. A source-derived action may
omit it, replace it by a constrained readout, or map it to another variable.

### 5. Time/action exposure is channel-specific

V4.2 gives

```text
Delta_phi_A[p,c] = epsilon_p*T_c[A]/t_SW
```

for declared time exposure. This is a time/action readout law, not a generic
wave-field Lagrangian. For the clock successor, this means source stroke
durations should be derived from the declared event/channel exposure and then
fed to the native logarithm/clock receiver. A separate wave term

```text
(kappa/2) integral [ (partial_t phi)^2/(q c_N^2) - q |grad phi|^2 ]
```

requires a source dynamic field operator and receiving map before comparison.

### 6. Spin response functional as reusable source method

For the spin transfer, keep the spin generator distinct from the A field:

```text
L = N(I - P)
```

For `xi > 0`, the source-derived quadratic response functional is

```text
J_xi(h) = (1/2)<h,(L+xi)h> - <f,h>
```

In a source basis `b_i`, its coefficients are

```text
G_ij = <b_i,b_j>
D_ij = <b_i,L b_j>
j_i  = <b_i,f>
J_xi(c) = (1/2)c^T(D + xi G)c - j^T c
```

If `K = D + xi G` is split into retained/hidden blocks, exact hidden
elimination gives

```text
K_eff = K_rr - K_rh K_hh^-1 K_hr
```

with the full hidden block retained. In a nonorthogonal basis the off-diagonal
blocks include `xi G_rh`. Finite retained approximations must carry the
remaining certified residual instead of dropping it.

This is directly useful for H02--H06 successor work because it explains how to
reuse source-derived metric/operator blocks while preserving unrepresented
dynamics.

### 7. Two-scalar spin continuation as an example of coefficient reuse

The completed spin source work already has the basis

```text
b4 = (d,e,u_d,u_e)
w  = (w_d,w_e)
b5 = (b4,w_d)
G  = <b4,b4>
D  = <b4,L b4>
W  = <w,w>
H  = G^-1 D
E  = [[0,0],[0,0],[1,0],[0,1]]
```

with identities

```text
<b4,w> = 0
L b4 = b4 H + w E^T
T4 = <L b4,L b4> = H^T G H + E W E^T
```

The proposed T5 upper response needs only

```text
J21 = <w_e,L w_d>
F11 = <L w_d,L w_d>
```

after reusing `J11`, `G5` and `D5`. This is a concrete coefficient-origin
pattern for the successor: calculate missing source contractions once, reuse
them across histories, and keep signs and cross terms.

## Source-to-frozen comparison table

| Frozen GEN6 term | Source-derived material now available | Exact remaining mapping |
|---|---|---|
| `dot X^T M dot X/(2q_can)` | G286 canonical one-form, G406 masses, G481 proper time | Pull source coordinates/momenta into 136 canonical positions; determine mass metric and the source status of `q_can`. |
| `q_can*g*z^T B68 z/2` | Contact coefficients `(6,-2,2)`, source A potentials, event-work Hessian route | Receive full potential Hessian including `a^2` and mixed blocks; compare derived block to `g J^T B68 J`. |
| `eta dot Lambda^2/2` | Support recurrence constraints and proper-time readouts | Identify whether `Lambda` is an independent source coordinate, a constrained readout, or absent/replaced; then compare any coefficient. |
| field spatial `-q |grad phi|^2` | Static A functional coefficient `c^4/(32*pi*G)` and normalized `kappa_N` formula | Supply `A <-> phi`, field measure, boundary/port and chart units. |
| field temporal `(partial_t phi)^2/(q c_N^2)` | V4.2 time/action exposure law; no generic wave operator selected yet | Locate/receive source dynamic field operator and its speed, or report source-selected absence/replacement. |
| clocks/logarithms | G481 endpoint lapse, H002616 certified source integral, native logarithm receiver | Generalize the successful source-bound clock adapter to all original strokes before full-trajectory successor comparisons. |
| support/velocity account | G679c/G643c/V4.2, Volume IV/H000185 | Keep support and velocity as typed lanes; do not double count potential and kinematic readings. |
| hidden dynamics | Spin retained/hidden source method | Use block elimination/residual certificates; keep heatbath provenance distinct from signed Writes. |

## Immediate successor implications

1. Generalize the H02 clock adapter by source stroke, not by frozen case label.
   Each stroke should expose its source energy, gradient, duration integral,
   signed orientation and outgoing clock/log receiver.

2. Treat the spin certified-integration method as a numerical and structural
   transfer: source-bound analytic integrals, explicit remainder/error
   accounting, retained/hidden block decomposition and reusable contractions.
   Do not relabel the spin heatbath generator as the signed-Write generator.

3. Preserve the frozen H02--H06 outcomes separately. A successor may improve
   the numerical execution path while the preserved 0/5 full-trajectory record
   remains the completed withheld-test result for the frozen construction.

4. When deriving coefficients, record the origin class:

   ```text
   source coefficient
   source-to-coordinate receiving factor
   chart/unit normalization
   frozen comparison value
   Codex deduction
   still open
   ```

5. The first full action comparison should accept differences as results. The
   source-selected action is not required to reproduce `g=0.1`, `eta=1/3`,
   `kappa=2`, `c_N=10` or `M=I`.

## Open questions for the next mapping pass

1. What is the exact source incidence from original Write/source coordinates
   into the 136 GEN6 canonical positions?
2. Does any source variable corresponding to `Lambda` evolve independently, or
   is the frozen reservoir a comparison coordinate for a constrained readout?
3. What source dynamic field operator, if any, supplies the temporal field
   term and propagation speed?
4. What boundary/port map receives `A` into `phi` and the frozen field boundary
   amplitude `a`?
5. Which source contractions are shared across H02--H06 strokes and can be
   computed once, as in the spin T5 pattern?

No scientific job was launched for this note.
