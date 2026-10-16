# Radial geometry as a possible selector of the quarter shift

This is a source-selection continuation of the native-energy Wildfowl. The
owner asks whether one native energy could represent SAM light speed. The
quarter-shift spectrum is a candidate to investigate, not a physical premise.

## Source actually retained

`GEN4/vol_i_activation_selection1/NETWORK_METHOD.md`, `network.py` and
`RESULT.md` define and execute a proposed conservative receiver network.
Its shell conductance is `c_(i,i+1)=i(i+1)`, with the common4*pi*D factor
placed in transport units. Native traffic solves give
`rho(r)=J(1/r-1/L)` with a finite absorbing exterior, and J/r in its limit.
The source explicitly proposes isotropic three-dimensional transport and a
continuum Poisson balance. It does not derive the microscopic carrier,
source/service normalization, an angular completion, or physical elapsed
time. Workload rho, mean queued work, and clock duty remain distinct.

The new calculation extends that retained monopole geometry to separated
scalar harmonic boundary responses. That extension and the boundary
conditions are explicit hypotheses. The actual Write spectrum0,2,6 and
the angular Casimir motivate the comparison; they are not automatically
identified with spatial harmonic fields.

## 1. Where the quarter comes from

In d spatial dimensions the separated scalar Laplace equation is

```
r² f'' +(d-1)r f' - kappa f = 0.
t=log(r/R), a=(d-2)/2, f=e^(-a*t) u.
u_tt=(kappa+a²)u.
```

Let y=(f,f_t), F=[[0,1],[kappa,-(d-2)]], and
S=[[1,0],[a,1]]. The transformed generator is
`S F S^-1+aI=[[0,1],[kappa+a²,0]]`.
Native rational matrix multiplication evaluates this for kappa0,2,6,12
and d2,3,4. Kappa is an independent separation parameter in this comparison;
only d3 with these kappa values corresponds to l0,1,2,3 of the actual
three-dimensional sphere. In general dimension, the scalar-sphere spectrum
is kappa=l(l+d-2). The resulting shift is0,1/4,1 for d2,3,4.

The variable t is **log radius**, not elapsed time. Its generator is
hyperbolic: u grows or decays radially. This derivation does not turn an
elliptic field equation into an oscillating clock.

## 2. One-sided responses, balanced energy and the offset ambiguity

At a sphere of radius R in three dimensions, regular interior harmonic
extension is `(r/R)^l`, and decaying exterior extension is `(R/r)^(l+1)`.
Using the outward normal of each domain gives

```
Lambda_in=l/R,
Lambda_out=(l+1)/R,  where the exterior outward normal at r=R is -d/dr,
B=R*(Lambda_in+Lambda_out)/2=l+1/2,
B²=C+I/4, C_l=l(l+1).
```

For a common boundary trace a_lm*Y_lm and a field with the same stiffness D
on both sides, the minimized positive Dirichlet energy is

```
U=(D/2)*integral_all_space |grad(phi)|² dV
 =D*R*sum_lm (l+1/2)|a_lm|²,
```

where Y is normalized on the unit sphere. If boundary harmonics are instead
normalized using physical surface measure, the coefficient is D/R. The
surface measure and field normalization must accompany the energy formula.
The boundary Hessian is the DtN sum; the conventional half in the quadratic
energy supplies the balanced operator coefficient. Fixed interior sources
can add an affine forcing and source self-energy while leaving this
homogeneous second variation, provided the stated interior/exterior field
problem is selected.

The current receiver network alone selects neither the regular interior
field nor equal two-sided stiffness. Also, l, l+1 and l+1/2 have the same
adjacent gaps. They differ only by scalar offsets, so their closed unitary
density propagation cannot distinguish them after a common normalization.
Weighted one-sided sums likewise retain equal spacing. Native probes return
the balanced spectrum, the exterior-minus-interior identity, the squared
Casimir residual and equality of one-sided adjacent-gap responses.

Thus antipodal recurrence alone cannot select the quarter. Source boundary
energy, flux, an external phase reference, or finite-boundary dependence
must provide additional information.

## 3. Finite absorbing exterior: solve the actual boundary problem

Set R=1 for the native finite probes, with L=2,4,8 and l0..3. The exterior
annulus solution is `f(r)=a*r^l+b*r^(-l-1)`. For each mode the native inverse
solves the coefficients and response together:

```
a+b=1,
L^l*a+L^(-l-1)*b=0,
lambda_out+l*a-(l+1)*b=0,
2*B_L-lambda_out=l.
```

Additional rows solve `gap_l=B_(l+1)-B_l`. All57 unknowns (48 coefficient/
response variables plus9 gaps) are solved by installed `GEN2_READOUT_INVERSE`.
No exterior response or gap formula is inserted as the answer vector.

The separately derived analytic comparison, not a supplied inverse solution,
is

```
q=(R/L)^(2l+1),
Lambda_out=[l+1+l*q]/[R*(1-q)],
B_L=R*(Lambda_in+Lambda_out)/2=(l+1/2)/(1-q).
```

It approaches the infinite-boundary result, but its finite-radius correction
depends on l and therefore changes the gaps. At l0, the integrated response
with the common4*pi*D removed is
`R²*Lambda_out=1/(1/R-1/L)`, exactly the reciprocal series resistance of
the retained receiver network. This is the source bridge; higher angular
modes are the newly declared continuation.

## 4. Positive boundary energy does not choose physical time

For the same candidate boundary form
`E=(q^T B q+pi^T B pi)/2`, two temporal completions are compared:

```
Hamiltonian: d(q,pi)/ds=[[0,B],[-B,0]](q,pi),
gradient:    d(q,pi)/ds=-diag(B,B)(q,pi).
```

Native words evaluate `F^T W+W F` with W=diag(B,B), preserving the two
results in separate blocks. The first conserves the quadratic energy; the
second dissipates it. The doubled real field/canonical bracket and both
temporal laws are explicit candidate completions. They are not supplied by
the stationary receiver-network solve. A native action scale, physical time,
receiver interaction and spatial readout remain to be selected.

## Execution

`build_radial_cases.py` compiles exact rational operands and the full shared-web
proposal schema into `radial_cases.json`. It performs no local research
execution. The root agent owns native dispatch, source intake and custody.
Actual returned results must be read before classifying any tested concept.
