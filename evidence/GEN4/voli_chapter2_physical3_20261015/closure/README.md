# Actual spin closure

`DERIVATION.md` develops the exact finite-source generator, seven-dimensional
residual, its continued Krylov ranks, and an explicit invariant count-space
upper closure. `FINAL_CLOSURE.json` and `CERTIFICATE_TABLE.md` state the computed
coverage and depth; no rank cap is described as stabilization.

Offline replay, using Python's standard library only:

    python3 closure/reproduce.py

The source-law checker independently reconstructs physical Gibbs action
differences. It checks the full N-site heatbath rate and exact site
multiplicities, including mixed background occupancies. The point-certificate
checker uses exact rational interval elimination to verify the retained native
point minors and inverse-row residual witnesses. Every original preparation
has its source SHA-256 binding. The integer upper-bound checker constructs the
size of an exact invariant exchangeable source space.

`point_source.py` is the native source evaluator, and requires the qualified
scientific Python environment. It is not executed by offline reproduction.
Native session receipts and executed-code snapshots preserve which version
actually ran. In the current implementation, caches clear after each retained
exact configuration row to bound memory; no source term changes. Earlier
executed-code snapshots remain unchanged.

The seven-dimensional residual is certified through its explicit source
functions, exact rank and positive full-Gibbs norm bound. This does not assign
a numerical global higher-moment integral that has not been calculated. The
retained exact ranks give lower bounds on the smallest invariant closure. An
invariant-rank equality or source minimal-polynomial identity is required to
identify that minimum.
