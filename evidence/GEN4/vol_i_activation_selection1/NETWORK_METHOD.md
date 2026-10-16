# Conservative queue network candidate

Nodes represent spherical shells at r=1,...,R-1; rho_R=0. The proposed isotropic
radial transport conductance is c_(i,i+1)=i(i+1), obtained from
1 / integral_i^(i+1) dr/r^2. The omitted common 4 pi D factor is a transport
unit. Thus the desired clock law is absent from the conductance definition;
isotropic transport in three spatial dimensions is an explicit proposal.
Source strength J=1/2 enters only the innermost shell.

For c_0=0, receiver service rate mu_i=c_(i-1,i)+c_(i,i+1) when nonempty;
routing probability P_ij=c_ij/mu_i, including exit at R. External arrivals are
Poisson, services exponential, all incoming jobs retained, and service is
work-conserving. This is an infinite-occupancy queue network; finite R is only
a spatial boundary. These dynamics are proposed, not read from QP092C.

Native exact inverse solves L rho=J e_1, with L diagonal mu and off-diagonal
-c. Native output rho_i is a utilization, not mean carrier count. The traffic
equations admit normalized product-form stationary weights
pi(n)=product_i (1-rho_i) rho_i^n_i for 0<=rho_i<1. The general-state balance
derivation is given in RESULT.md. Hence p_i=P(n_i=0)=1-rho_i; the clock's
exclusive access to this free state remains a proposed coupling rule.

Returned boundary corrections generate R=9,17,33. A final native inverse scales
all service and injection rates by1000, testing fixed rho with faster dynamics.
This is how the candidate can approach the retained fast-switching regime
without changing its duty. No absolute physical switching time is supplied.

The native solutions are compared after return with the analytic flux solution.
Postprocessing of the preceding native second-moment polynomials uses exact
rational bisection; this is identified readout analysis, not a new native call.
