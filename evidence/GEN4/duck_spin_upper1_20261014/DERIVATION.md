# Original-source completion of T5 and the upper response

The original two new source operands J21=<w_e,A w_d> and F11=||A w_d||^2
are calculated with full original-source enclosures in
../spin_upper_source1_20261014/DERIVATION.md. Both values, including their signs
and errors, enter this Duck unchanged. These are source calculations, not fitted
receiver coordinates or algebraic extremizers from H002626.

Use H002626's retained scalar maps with j=J21 and f=F11:

    Q(j)=(a0+a1*j)^2,
    S(j,f)=f+s0+s1*j+s2*j^2,
    U5=U4-Q(j)/((xi+gamma)*S(j,f)).

Every interval endpoint and signed polynomial term remains. For each original
history report S, the gain, normalized upper xi*U5/Var(d), inherited L5, and
the fraction of the old U4-L5 interval removed. Retain the minimum with prior
upper endpoints in final organization; the lower bound remains the completed L5.

The separately arranged direct route assembles the entire matrix

    T5=[[T4,t],[t^T,F11]], t=H^T k+E(J11,J21)^T,
    K5=T5+(xi-gamma)D5-xi*gamma*G5,
    r5=(D5-gamma*G5)e_d,
    U5=(Var(d)-r5^T K5^-1 r5)/(xi+gamma).

Source gamma and N/xi original site attempts are unchanged. Native solves and
products perform receiver arithmetic at 1024 bits. Independent source-core
checks, analytical payment reconstruction and high-precision receiver inversion
retain separate provenance from the primary source integration.
