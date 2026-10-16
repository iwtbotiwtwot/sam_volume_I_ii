# Native clock–geometry–receiver history reduction

The first ordered work package is complete. The native source needs16predictive
states even though it has only8immediate sphere/action/phase outputs. A fixed-size
streaming monitor then preserves the requested whole-history, timed-gate and
clock-weighted receiver statistics across12native histories and3888Writes.

**The test result suggests strong contact with the concept.** Scope: the admitted
native source, exact predictive-state distinction, and declared scalar receiver
observations tied to the completed-Write clock.

## What the source must remember

The source is the retained rho1 J4 block[1,4,7], initial[0,0,0], with W1+ andW7+.
All16reachable states and both outgoing labelled transitions were admitted through
32installed GEN2_RUN calls, each starting from the original reference. Native
fixed-sphere coordinates, action, wrapped phase and exact logarithms come directly
from the installed engine.

Grouping by immediate output gives8classes. Requiring the next Write's output
to agree refines this to14classes; another step gives16. All120distinct state
pairs have an explicit separating word of length at most2. An independent
relation-elimination calculation reaches the same result:38candidate ordered
pairs shrink to20, then16identity pairs.

For example,[0,0,0] and[0,0,3] share the same current output but separate after
W1+,W1+. The hidden source coordinate therefore carries predictive information
that an instantaneous sphere image omits. Within deterministic realizations of
this alphabet and output, all16states are needed. This is a source-specific
minimality result; the full64-state J4 alphabet and other output choices were
not part of this finite problem.

## Equal total occupancy can hide a timed response

Compare the grouped word W1+^196 W7+^128 with W7+^128 W1+^196. Both have324Writes,
endpoint[0,0,0], the same eight-bin sphere occupancy, and identical scalar
U,D,V,L,M logarithmic summaries. Their retained maximum-occurrence histories
remain distinct. The installed receiver at radius1, radial_fraction1/2 returns:

| X-direction readout | Grouped | Reverse grouped |
|---|---:|---:|
| Whole-history occupancy |0.2766532104|0.2766532104|
| First162Writes |0.1440964305|0.4063809938|
| Last162Writes |0.4092099904|0.1469254271|
| Weight proportional to completed-Write index |0.3563599761|0.1981822086|

The whole-history X/Y/Z requests recover the exact same retained native operands.
Each displayed timed contrast has a difference interval excluding zero at160bits.
The numbers above are rounded displays; RECEIVERS.json and COMPARISONS.json
retain the rational interval endpoints.

Each four-W1 and four-W7 block returns to the initial source state. Reordering
these closed blocks preserves additive total occupancy but moves that occupancy
between clock windows. That supplies an explicit mechanism for the distinction.
It is not necessary to postulate a different microscopic source.

## The resulting reusable state description

For quotient state q, completed-Write count n, point count h_j and first clock
moment m_j, the update is

    q' = T_event(q)
    n' = n + 1
    h_j' = h_j + 1[point(q') = j]
    m_j' = m_j + n' * 1[point(q') = j].

There are8point counters in h and8in m. The admitted timed gates add eight
counters per gate; each accumulates only while that gate is open. monitor.py
implements this update without retaining a history array. Counts grow in bit
length with the observation duration; the number of counters stays fixed for
the chosen readouts. Original full native histories and receipts are preserved
separately as research custody.

For any specified scalar angular kernel K_j, h determines its whole-history
mixture and m determines its first completed-Write-index-weighted mixture. The
installed angular operation evaluates those mixtures. This construction preserves
the declared readouts; arbitrary retrospective gates or higher time correlations
would require their corresponding statistics or the retained full history.

## New-ordering checks and native use

Two predecessor324-Write histories were reused. Ten new matched words include
reversal, three cyclic rotations, two shuffled closed-loop orders, and three
seeded event shuffles. All retain196W1+/128W7+ and the same final source state.
The monitor matches each actual installed sphere/action/phase output on all3888
steps. Its counts and moments also match independent complete-history aggregation.
The installed Write foundation verifies324completed Writes and81turns of absolute
phase variation on every arm.

There were42successful installed source executions and72installed certified
angular receiver calls, plus retained-result publication/export/checkpoint and
exact close/reopen recovery. Two source-bound combinatorial adapter calls perform
partition refinement and independent monitor verification. The menu has no
labelled-transducer minimization operation; this specific gap is documented in
DESIGN.md. No external math package or dependency was added. Native logarithms,
source dynamics and angular calculations use their existing installed handlers.

MATTER_SEARCH / GEN3-R4, SLC-GEN3-R4 and SLC-GEN3-CEV1-R4 were verified. Session,
RESOURCE.json and receipts are on T500; all computation used the local i9CPU4.
Prime Event, pods and paused research workers were not changed.

The first receiver request passed tuples where the installed contract requires
three-coordinate lists. Its failed receipt and original run.py are preserved.
resume.py corrects the handoff and reuses the completed source work. Its7.03s
receipt measures the resumed receiver stage, not total campaign runtime.

## Scientific meaning and next step

The completed-Write clock here and the earlier48-tick matter clock remain
separately typed. Sphere radius is the native chart radius. Equal nonnegative
per-Write injections and the timed receiver protocol are declared constructions;
this campaign does not assign a physical coupling between the two clocks.

The useful continuation within this branch is a source-supported receiver with
its own evolving state, for which a fixed finite set of occupancy moments may
no longer close. The new16-state source and counterexample provide the exact
starting point. The authorized work order next goes to negative-completion spin,
then the RH3Kcrossing estimate; see QUEUE.json.

Evidence and state: [T500 campaign](/home/sam/mnt/lilhelper-t500/GEN4/native_history_reduction1).
REDUCTION.json contains the transition table, quotient and separating words;
VERIFY.json contains independent qualification; RECOVERY.json records exact
restart. Completion archive and readback are routed by CUSTODY.json.

Sean Brady: originator/conceptual director. ChatGPT and Codex: research
collaborators. Quotient construction, streaming monitor, readout design and
interpretation in this campaign are Codex contributions.
