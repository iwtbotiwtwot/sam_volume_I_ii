# Exact evolution of a retained source account

This Codex analytical continuation uses the finite original spin heat operator
A=N(I-P_transition), the original Gibbs inner product, and an explicitly
selected orthogonal retained-source projection Pi. P_transition and Pi have
different meanings. It changes neither the operator nor the attempt clock.

Put Q=I-Pi. For a finite source u'(t)=-Au(t), set p=Pi u and q=Q u. The exact
block equations are

    p'=-Pi A Pi p-Pi A Q q,
    q'=-Q A Pi p-Q A Q q.

Variation of constants within the complementary subspace gives

    q(t)=exp(-Q A Q t)q(0)
         -integral_0^t exp[-Q A Q(t-s)] Q A Pi p(s) ds.

Substituting, the closed retained equation is

    p'(t)=-Pi A Pi p(t)-Pi A Q exp(-Q A Q t)q(0)
          +integral_0^t K(t-s)p(s) ds,
    K(t)=Pi A Q exp(-Q A Q t)Q A Pi.                     (M1)

This is an identity for every finite source vector and every original time;
it is not a fitted reset, exponential approximation, or new Markov law. The
initial-hidden-state term retains preparation. The memory integral retains
the source evolution that leaves and reenters the observed span. Dropping
either changes the receiving equation unless its actual source contraction
vanishes. A sufficient exact closure condition is Pi A Q=0; self-adjoint A
then also has Q A Pi=0. For nonzero cross blocks a particular observable
or preparation can still annihilate the terms; that is a source-specific
condition, not a general state reduction.

For self-adjoint A>=0, K(t) is positive semidefinite on the retained space:
it is C* exp(-Q A Q t) C with C=Q A Pi and a positive complementary
semigroup. This positivity does not permit dropping signed cross terms
when the final physical energy uses another operator B.

The completed spin basis b5=(d,e,u_d,u_e,w_d), G5,D5,T5, and its successor
r_next=A w_d-P_b5(A w_d) supply an actual source-bound direction for a
larger retained span. The completed projection floor Ffloor instead uses
b6=(d,e,u_d,u_e,w_d,w_e). Their two residuals remain distinct. No fresh
J21/F11 integration or next Dirichlet scalar was evaluated here.

An achieved phase coordinate theta may transport this equation. Write
t=t(theta) and multiply every right-hand term by 1/nu(t(theta)); retain
the kernel argument t(theta)-t(vartheta) and replace ds by
d vartheta/nu(t(vartheta)). This preserves both clock factors and the
original time-difference kernel. Replacing the kernel argument by a raw
phase difference would introduce another evolution law.
