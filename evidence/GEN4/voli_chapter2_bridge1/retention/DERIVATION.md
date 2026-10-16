# Retained histories in the achieved interacting phase

Sean Brady is originator and conceptual director. OpenAI ChatGPT and Codex
are AI research collaborators. The transport and finite receiving results below
are new Codex deductions for the Chapter II bridge. Their algebra is independently
checked here; no new native source evolution has run.

## 1. The three inherited sources and the proposed interface

The native J4 history experiment has 16 reachable predictive states, eight
immediate sphere/action/phase outputs, and a completed-Write index. Its exact
transition table and stored histories control that result. The observed-history
experiment has a different, source-bound covariance receiver and an exact
two-past-coordinate repair. Chapter I has six separately prepared interacting
source/field lanes, each with an achieved positive actual phase rate on its
retained interval. These are three distinct sources, with three distinct
receiving constructions.

The new common interface is this: supply a retained-label record on the same
time interval as an admitted positive phase clock. The results below describe
exactly which histories, weights and receiver coefficients survive a change to
that clock. Assigning a J4 event schedule to a Chapter I preparation would be
an additional physical coupling; it is not asserted by this interface.

Let tau be the source time, let theta(tau) be the absolutely continuous
unwrapped actual phase, and
write nu(tau)=dtheta/dtau. On the admitted interval assume

    0 < nu_minus <= nu(tau) <= nu_plus.

The Chapter I certificate supplies such bounds for its six stated preparations
on 0<=tau<=573049*pi. Each preparation has its own actual theta and bounds.
All references to that certificate here preserve its radius, hard-coherent
preparation, free soft vacuum and full continuum/source action. A clock for a
general coherent sixteen-state preparation is not supplied by this citation.

## 2. Exact transport of history measures

**Claim 1.** The actual phase is strictly increasing and has an absolutely
continuous inverse tau(theta). For any integrable scalar receiver r,

    integral r(tau) dtau
      = integral r(tau(theta))/nu(tau(theta)) dtheta,                (R1)

    integral r(tau) nu(tau) dtau
      = integral r(tau(theta)) dtheta.                             (R2)

For a supplied event record (tau_n,j_n), the atomic measure transports as

    sum_n a_n delta_(tau_n,j_n) -> sum_n a_n delta_(theta(tau_n),j_n).
                                                                    (R3)

Its event masses a_n are unchanged. They acquire no extra nu factor.

*Derivation.* The lower rate bound gives
nu_minus*(b-a)<=theta(b)-theta(a)<=nu_plus*(b-a); hence strict ordering,
an inverse, and d tau/d theta=1/nu almost everywhere. Substitution gives
R1-R2. The pushforward definition gives R3 directly. No constant-rate or
stationary-source assumption is used.

Thus completed-Write count, elapsed source duration, and elapsed interacting
phase are three different measures. An occupation count is not converted into
an actual phase exposure merely by relabeling its index.

**Immediate enclosure.** For a retained label j, define

    H_j=integral 1[j(tau)=j] dtau,
    P_j=integral 1[j(tau)=j] dtheta.

Then nu_minus H_j <= P_j <= nu_plus H_j. Conversely,
P_j/nu_plus <= H_j <= P_j/nu_minus. These are useful when the actual clock
has a certified rate interval but its detailed phase samples are unavailable.
`verify.py` reads the six achieved native intervals and checks the premises and
these exact enclosure operations. This consumes existing clock evidence; it
does not evaluate a new joint microscopic record.

## 3. A finite monitor for variable-rate phase exposures

Let j(tau) be piecewise constant in a finite label set J. On a segment
[a,b), label j, admit the actual phase endpoints alpha=theta(a), beta=theta(b).
Maintain three counters per label:

    H_j += b-a,
    P_j += beta-alpha,
    Q_j += (beta^2-alpha^2)/2.                                     (R4)

Also maintain event count C_j and event phase moment E_j by

    C_j += 1,
    E_j += theta(tau_n)                                            (R5)

when a declared event with label j occurs. Event counters do not use R4.

**Claim 2.** For every prescribed receiver affine in the actual phase,

    R_phase = integral a_j(theta) dtheta,
    a_j(theta)=u_j+v_j theta,

the exact answer is sum_j(u_j P_j+v_j Q_j). The corresponding atomic receiver
sum_n(u_jn+v_jn theta(tau_n)) is sum_j(u_j C_j+v_j E_j). For a prescribed
phase gate [g0,g1), replace each segment by its overlap
[max(alpha,g0),min(beta,g1)) in R4. A fixed finite number of gates requires a
fixed number of additional counters.

*Derivation.* Integrate 1 and theta on each segment and add. The actual
within-segment variation of nu cancels by R2. A gate crossing is unique by
Claim 1, so clipping in phase is exact. Summing atomic masses gives R5.
This closes the specified receiver family; arbitrary retrospective gates,
nonlinear weights and higher correlations need their own statistics.

The number of counters stays fixed for the prescribed finite family. Counter
precision and bit length may grow with the record. The monitor does not claim
a finite total information capacity for arbitrarily long exact histories.

A physical-time integral over a phase gate additionally needs tau(g0),tau(g1)
and any internal event boundaries, or the R1 Jacobian. Phase endpoints alone
do not determine a physical-time-weighted integral. Changing an endpoint
reference must transport its gates and all receiver weights with it.

## 4. Exact variable-clock example

This example is a new rational receiving fixture, not a computed microscopic
phase trajectory. Use theta(tau)=tau+tau^2/2 on 0<=tau<=2, so nu=1+tau>0.
Compare A then B on the two unit intervals with B then A. Both have the same
physical-time occupation (H_A,H_B)=(1,1), the same total phase4, and one event
of each label. Yet

    A then B: (P_A,P_B)=(3/2,5/2), (Q_A,Q_B)=(9/8,55/8),
    B then A: (P_A,P_B)=(5/2,3/2), (Q_A,Q_B)=(55/8,9/8).

An A-only phase receiver separates the records by1. The phase gate [1,3)
gives (P_A,P_B)=(1/2,3/2) versus (3/2,1/2). Physical-time occupations alone
cannot supply these actual-phase observations under a variable clock.

For an affine clock with theta_n=alpha+beta*n at event n, R5 reduces exactly to
E_j=alpha*C_j+beta*m_j, where m_j is the inherited native Write-index moment.
For a variable clock, E_j must be accumulated from its actual endpoints.
`verify.py` checks the count/moment invariants on all twelve retained native
summaries, then replays the two grouped words through the retained transition
table to verify the affine reduction independently of their original streaming
implementation. It does not rerun the microscopic source engine.

## 5. Covariance memory survives a positive change of clock

Let X(tau) have mean m and centered covariance C(tau,sigma). Reparametrize the
same readings by X_theta(theta)=X(tau(theta)). Then

    C_theta(theta,eta)=C(tau(theta),tau(eta)).                       (R6)

Consequently any finite Gram at matched physical nodes is unchanged; so are
its exact predictive-memory recipient and Schur residual. If C is stationary
in tau, it need not be stationary in a nonlinear theta. Replacing its physical
lag by a phase difference without the inverse map changes the receiver.

For the retained observed-history Gram on its local normalized nodes
u=(0,3/2,9/4,5/2), let P=(0,1)
and F=(2,3). Its exact linear second-moment recipient is

    B=G_FP G_PP^-1
      =[[-11/744,44/93],[-8/1023,256/1023]],
    Sigma=G_FF-B G_PF
      =[[4621/5952,19039/23808],[19039/23808,959/1023]].

The anchor-only cross-block defect is [-121/8192,-1/128]. Both the older
coordinate and the anchor therefore matter to this receiver. Evaluating the
same Gram at a strictly increasing relabeling of u_i leaves B,Sigma and the
defect unchanged. The fixture uses the declared synthetic relabeling from
Section 4; u is not identified with Chapter I's source time. This is a
new transport deduction from the completed exact memory construction. It
does not introduce a distributional conditioning law or a microscopic reset.

**Compatible centering/gain monitor.** If measured mean and second moment are
Am and A(G+mm^T)A at the matched nodes, with an admitted invertible positive
diagonal gain A and H=A^-1, then

    H[A(G+mm^T)A-(Am)(Am)^T]H=G.                                 (R7)

R6 and R7 commute: either transport the full moments and monitor together,
or center/de-gain first and transport G. The same retained two-coordinate
recipient results. Time-varying gains are allowed at the sampled endpoints;
their matching monitor and noise law must still be supplied. Additive receiver
noise needs its own covariance correction and is not removed by this identity.

## 6. Predictive distinction and Chapter II interpretation

For a deterministic retained source with labelled transitions T_e and receiver
o, define q~q' when o(T_w q)=o(T_w q') for every finite allowed word w,
including the empty word. This is an equivalence relation preserved by every
T_e: apply the definition to the concatenated word ew. Its quotient is an
exact predictive state for this specified receiver/alphabet. Any deterministic
realization with fewer states would identify a pair separated by one of those
words. This is an operational meaning of a retained distinction.

The inherited J4 example realizes the distinction concretely: immediate output
classes8 refine to14 and then16. Every state pair has a separating word of
length at most2. A present address and a complete predictive state therefore
have different jobs. The numerical eight here is a source-specific output
count, separately typed from the eight Chapter II product addresses.

### A phase-compatible predictive quotient

Suppose an admitted finite event instrument supplies transitions T_e(q),
immediate outputs o(q), and positive actual phase increments

    phi_e(q)=integral_(event e at q) nu(tau) dtau.

For this finite representation phi_e must depend only on its declared state
and event. An instrument with additional hidden history must include that
history in its state, or admit a different representation. The occupied Write
source has not been assigned such a finite instrument by this package.

**Claim 3.** A quotient retaining both the output trace and accumulated actual
phase for every finite event word must preserve three things: o(q), every
phi_e(q), and the quotient successor under every T_e. Conversely these three
conditions suffice. The coarsest such quotient is obtained by partitioning on
(o(q),(phi_e(q))_e) and repeatedly refining by the vector of successor classes.

*Derivation.* Empty-word readings enforce the output condition. Reading phase
after one event enforces phi_e. Continuations enforce successor equivalence.
Conversely, induction on the word length gives the same output and same phase
increment at every step; their accumulated phases therefore agree. Finite
partition refinement terminates and retains every pair satisfying these
conditions. Any coarser deterministic quotient merges a distinguishable pair.

This is the precise clock qualification of an address reduction. A quotient
that preserves only present sphere images, or even untimed future images,
need not preserve the interacting phase. For example, two states can have
one constant output, alternate under one event, and carry increments1 and2.
Their untimed quotient has one state; their phase-compatible quotient has two.
After two events each accumulates phase3, while the first event reads1 versus2.
This is an exact receiving counterexample, with positive increments, rather
than an additional microscopic source calculation.

`phase_predictive_partition` implements this finite receiving construction.
It retains the inherited sixteen J4 predictive classes when every admitted
edge is assigned the same phase increment, and splits the two-state fixture
when the phase increment depends on its hidden state. A physical assignment
of phi_e from the actual Chapter I clock is the next source-bound operand.

New Claims 1-3 add the missing clock-weighted receiving statement: a retained
history can be compressed for an explicit family of future phase/time/event
observations, provided the same achieved positive phase and its measures are
carried throughout. A finished turn or equal endpoint does not erase a
receiver-visible distinction stored in these counters or predictive state.

## 7. Completed here and the next physical operand

Completed here: the exact transport identities, finite phase-gated/affine
monitor, event-versus-continuous measure distinction, rate-bound enclosures,
matched-node covariance/gain compatibility, and rational worked fixtures.
Existing native J4, observed-history and Chapter I clock results are reused
without rerunning them. `SOURCE_BINDINGS.json` hashes the exact consumed files;
`VERIFY.json` records the independent receiving checks.

The next physical operand is an admitted joint instrument/path/preparation
that supplies a Chapter II retained-label record and its phase endpoints from
the same occupied Write/source-field realization. That map must keep the
original common phase, commuting even energy, both currents and complete
action. R1-R7 give its receiving algebra; they do not assign J4 events to that
quantum preparation, a gravitational lapse, an SI rate, or the macroscopic
accumulation floor.
