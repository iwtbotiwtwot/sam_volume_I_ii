"""Editable Chapter III core, reconstructed from the supplied development PDF.
The source PDF is preserved byte-for-byte in ../inputs; this is a successor.
"""
TITLE='The spherical accumulation kernel and the source-to-field interface'
ABSTRACT=('A retained energy account becomes a spatial field through a specified localization, coupling and receiving operator. This chapter develops the isolated Poisson kernel, its energy and force proofs, and two complete finite constructions: the actual retained eight-site source profile under a declared physical embedding, and an exactly solvable shell network with boundary and continuum errors. A static Chapter I field-energy example and an exact interacting-clock coupling criterion connect the construction to Chapters I and II. Source identities, physical assignments and computed results are stated separately. All earlier drafts remain preserved.')
PAGES=[
(r'''
## 1. The next source question

Chapter I supplies an interacting finite source and continuum field. Chapter II distinguishes a present output, a predictive state, a timed history and an unread energetic complement. Chapter III asks how their physical energy is located and received in space. [1,2]

The spherical lift is a static receiving profile:

$$a(r)=\frac{2GM}{c^2r},\quad A_{\rm tot}=A_0+a,\quad A_0=\frac{1}{12\pi}.$$

The physical mass M, source radius b, receiving radius r and Chapter I coupling radius R have different roles. G and c carry the declared physical units. The floor is dimensionless.

This revision carries exact source operands into finite field calculations. The mass/localization and coupling assignments are recorded at each step.
''',r'''
## 2. What enters the field

For a positive source form B and record r=Lᵀy, the ambient minimum is

$$\mathcal{C}(r)=r^T\mathcal{G}^+r,\quad\mathcal{G}=L^TB^{-1}L,$$

provided r belongs to the range of the receiver Gram. An infeasible record has no such source; its constrained infimum is +infinity. Allowed-state restrictions can raise the minimum. A change from an occupied reference also retains its cross term. [2]

This is a cost for a specified receiver. To form a physical density, specify the energy operator, physical conversion, reference and spatial incidence. The completed Chapter II now develops these requirements in its source-to-space interface.

The source and receiver below are static. Pressure, motion, retardation and nonlinear self-coupling require their own physical laws.
'''),
(r'''
## 3. The declared receiving law

For a supplied nonrelativistic mass density ρ, use

$$\Delta a=-\frac{8\pi G}{c^2}\rho,\qquad \Phi=-\frac{c^2}{2}a.$$

This is equivalent to Δ Φ=4π G ρ. The field normalization imports the Newtonian coupling. The sign makes a positive for a positive isolated mass when a tends to zero at infinity.

A test body with Lagrangian L=m|ẋ|²/2-m Φ has acceleration

$$\mathbf{g}=-\nabla\Phi=\frac{c^2}{2}\nabla a.$$

Equality of passive gravitational and inertial mass is part of this test-body coupling. The scalar profile by itself does not select that equality.

For bounded compact density the solution is

$$a(x)=\frac{2G}{c^2}\int\frac{\rho(y)}{|x-y|}\,d^3y.$$

The locally integrable kernel obeys Δ(1/r)=-4π delta. Linearity therefore gives the response to a sum of prescribed sources. Global regularity and isolated boundary data establish uniqueness; an exterior subproblem needs its inner data too.

All three displayed formulas have a fixed energy and time convention. A later rescaling of a must also rescale its source equation and its receiving laws.
''',r'''
## 4. Flux and exterior uniqueness

In a spherical vacuum exterior,

$$\frac{1}{r^2}(r^2a')'=0,\qquad a=C_0+\frac{C_1}{r}.$$

Decay fixes C<sub>0</sub>, while the enclosing source flux fixes C<sub>1</sub>:

$$M(<S)=-\frac{c^2}{8\pi G}\oint_S\nabla a\cdot d\mathbf{S}.$$

Thus C<sub>1</sub>=2GM/c<sup>2</sup> and g=-GM r̂/r<sup>2</sup>. Decay alone leaves the amplitude free. A regular vacuum ball containing the origin cannot carry a nonzero 1/r term.

For a nonspherical source, total mass fixes only the monopole. Higher multipoles carry shape information while contributing zero net enclosing flux. The cube construction below makes the first surviving shape term explicit.

A finite outer wall fixes a different boundary problem. Its correction must be included before comparing potential or clock values to the isolated profile. The shell example supplies that correction exactly, including its energy cost.

The spatially constant floor contributes no source flux. This statement is compatible with a nontrivial floor in an independently specified nonlinear clock receiver.
'''),
(r'''
## 5. Finite spherical sources

For a spherical source define its enclosed mass:

$$M(r)=4\pi\int_0^r\rho(s)s^2\,ds.$$

Regularity and the source equation give

$$a'(r)=-\frac{2GM(r)}{c^2r^2},$$
$$a(r)=\frac{2G}{c^2}\left[\frac{M(r)}{r}+4\pi\int_r^\infty\rho(s)s\,ds\right].$$

Exterior shells supply potential and zero interior acceleration. A thin shell of radius b and mass M has a=2GM/(c<sup>2</sup>b) inside and 2GM/(c<sup>2</sup>r) outside. Its derivative jump carries its surface mass. Values directly on a zero-thickness surface require a limiting convention.

For a uniform ball,

$$a(r)=\frac{GM}{c^2b}(3-r^2/b^2),\quad r\leq b,$$
$$a(r)=\frac{2GM}{c^2r},\quad r\geq b.$$

Both a and a' match at the surface. At the center a=3GM/(c<sup>2</sup>b) while g=0. Bounded compact density makes the central expression regular; finite mass alone does not. A central ρ proportional to r<sup>-2</sup> is a useful finite-mass, divergent-potential example.
''',r'''
## 6. Mechanical and tidal receivers

Circular motion differentiates the potential; escape compares it with a destination:

$$v_{\rm circ}^2=-\frac{c^2r}{2}a'(r),$$
$$v_{\rm esc}^2=c^2[a(r)-a(\infty)].$$

For the isolated spherical exterior they are GM/r and 2GM/r. A shell interior has zero circular-force field yet a nonzero escape energy relative to infinity. A truly global potential shift cancels when both endpoint values shift together.

For the exterior monopole, the tidal tensor is

$$T_{ij}=\frac{GM}{r^3}(3n_in_j-\delta_{ij}).$$

It has zero trace in vacuum, radial stretching 2GM/r<sup>3</sup>, and transverse compression -GM/r<sup>3</sup>. Inside a uniform ball it is -GM delta_ij/b<sup>3</sup>, including at the zero-acceleration center; its trace is -4π G ρ.

The tidal tensor here differentiates Newtonian acceleration. A relativistic spatial curvature or photon receiver requires additional structure. Chapter I's phase clock is another receiving operation, whose source coupling is derived below.
'''),
(r'''
## 7. Radial controls and scale

For a trial a_p=K r<sup>-p</sup> away from the origin,

$$\Delta a_p=p(p-1)Kr^{-p-2},$$
$$g_r=-\frac{c^2pK}{2}r^{-p-1},$$
$$M_{\rm flux}(r)=\frac{c^2pK}{2G}r^{1-p}.$$

A nonzero decaying spherical vacuum solution with constant source flux selects p=1. Positive attraction alone leaves many powers. The harmonic p=0 term is constant and carries no mass flux.

Compare powers using a reference radius: a_p=a<sub>∗</sub>(r<sub>∗</sub>/r)^p. Matching the potential at r<sub>∗</sub> gives a force p times the monopole force there. Dividing this profile by p matches that force but changes the potential to 1/p of its target. At other radii the force ratio is (r<sub>∗</sub>/r)^(p-1).

The coefficient K has units length<sup>p</sup>. Comparing its numerical value across powers without the reference radius changes the dimensional question. A matched datum at one radius therefore supplies less information than a radial profile, flux and potential reference together.
''',r'''
## 8. A finite-energy domain

For an isolated field, use the homogeneous Sobolev space D<sup>1,2</sup>(R³): the completion of compact smooth functions under ‖∇a‖<sub>2</sub>, represented in L<sup>6</sup>. This fixes the infinity reference and excludes a nonzero constant ambiguity.

A sufficient source class is ρ in L<sup>6/5</sup>; bounded compact density is an example. The pairing integral ρ a is then bounded by Holder and Sobolev. The functional

$$J[a;\rho]=\frac{c^4}{32\pi G}\int|\nabla a|^2$$
$$-\frac{c^2}{2}\int\rho a$$

has a unique weak minimizer. Its Euler equation is the declared Poisson problem. Existence follows from the bounded source functional and the positive gradient inner product; uniqueness follows from the same norm.

Compact smooth test variations give

$$\delta J=\int\left[-\frac{c^4}{16\pi G}\Delta a-\frac{c^2}{2}\rho\right]\delta a.$$

An ideal point source still has a distributional exterior solution, but has infinite self-energy. Thin spherical shells have a finite-energy potential with a derivative jump. The finite cube below uses regular balls to specify its self-energy.
'''),
(r'''
## 9. The minimum and binding energy

Let a<sub>∗</sub> be the weak solution and let v be an allowed variation with the same boundary reference. Expand J[a<sub>∗</sub>+v]. The linear terms cancel by the weak Poisson equation, leaving the exact identity

$$J[a_*+v]-J[a_*]=\frac{c^4}{32\pi G}\int|\nabla v|^2.$$

This proves the global minimum on the stated domain. Equality requires v=0 in D<sup>1,2</sup>. For a bounded Dirichlet region the same proof uses zero-trace variations.

Testing the weak equation against a<sub>∗</sub> gives

$$\int|\nabla a_*|^2=\frac{8\pi G}{c^2}\int\rho a_*.$$

Consequently,

$$U=J[a_*]=-\frac{c^2}{4}\int\rho a_*$$
$$=\frac{1}{2}\int\rho\Phi=-\frac{c^4}{32\pi G}\int|\nabla a_*|^2.$$

The positive penalty in J and the negative on-shell binding energy are different parts of the same calculation. For a uniform ball, integration over the whole field, including its exterior, gives U=-3GM²/(5b). Keeping only the material interior loses part of this energy.
''',r'''
## 10. Two sources and force

Let a_i be the isolated response to ρ_i and U_i its self-energy. Symmetry of the Green kernel gives

$$U[\rho_1+\rho_2]=U_1+U_2$$
$$-G\iint\frac{\rho_1(x)\rho_2(y)}{|x-y|}\,d^3x\,d^3y.$$

Proof: expand -c<sup>2</sup> integral(ρ_1+ρ_2)(a_1+a_2)/4. The two cross terms coincide and combine to the displayed pair interaction. The factor one-half in the self-energy removes double counting.

For spherical bodies whose enclosing balls are disjoint (d>b1+b2), the cross term is -GM1 M2/d, with d their center separation. Differentiation at fixed body shapes gives attraction of magnitude GM1 M2/d². This uses the same G, density reference and mass assigned to the field equation. The force follows from that common energy account.

For general disjoint compact bodies, differentiation under the integral gives the vector force directly. Positive separation bounds the differentiated kernel and justifies the step. Holding a source fixed while varying its field differs from translating that source and re-solving the field; this proof tracks the latter through the on-shell energy.
'''),
(r'''
## 11. The floor in a clock receiver

A constant floor has zero gradient. It also cancels from an ordinary endpoint subtraction. For the nonlinear diagnostic N_raw(a)=sqrt(1-A0-a), source-free normalization instead gives

$$\frac{N_{\rm raw}(a)}{N_{\rm raw}(0)}=\sqrt{1-\frac{a}{1-A_0}}.$$

Its logarithmic slope at zero is -1/[2(1-A0)]. With A0=1/(12pi), the residual scale factor is approximately 1.027248616.

The locally declared source-only lapse is

$$N_{\rm loc}(a)=\sqrt{1-a},\quad N_{\rm loc}'(0)=-\frac{1}{2}.$$

It gives the desired leading endpoint coefficient when a retains its Poisson normalization. Defining a_tilde=a/(1-A0) changes the source amplitude too; that redefinition must be carried through every equation.

These are explicitly different receiver prescriptions. The six-lane interacting-clock test below asks which perturbation of the full source Hamiltonian actually produces the source-only coefficient. Clock normalization alone supplies no density or absolute energy reference.
''',r'''
## 12. The weak metric interface

Fix static isotropic weak-field coordinates and write

$$ds^2=-[1-a+O(a^2)]c^2dt^2$$
$$+[1+\gamma a+O(a^2)]d\mathbf{x}^2.$$

The stationary clock coefficient is one-half. A null path in these coordinates instead has

$$c\,dt=\left[1+\frac{1+\gamma}{2}a+O(a^2)\right]d\ell.$$

The photon-road coefficient depends on the spatial response gamma. In conventional post-Newtonian notation gamma=1 gives coefficient one. These metric coefficients are additional physical input; static Poisson and an endpoint clock do not determine gamma. [7]

The coordinate convention also matters beyond first order. An exact square-root lapse must be tied to a specified time and radial coordinate before it is used as a nonlinear prediction.

Chapter IV can develop an actual endpoint receiver with reference and motion terms, and Chapter V a path receiver with spatial response. The following finite source constructions provide spatial inputs for both while retaining their separate receiving operations.
''')]
