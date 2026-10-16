"""Integrated reader draft: preserved core plus actual source and field work.

The completed computations retain their own source/check authority. A declared
coupling or physical unit assignment is identified at its first use.
"""
from base_content import TITLE, ABSTRACT, PAGES as CORE_PAGES

PAGES = list(CORE_PAGES) + [
(r'''
## 13. The actual spatial source

The retained Si29 construction supplies exact finite spatial effects. Its four-component Gram Q has diagonal (128,136,128,128). Its only nonzero off-diagonal entries are 8 on pairs 01, 03 and 23, with symmetric entries. Thus every original entry is retained. [3]

Write h=√Q. The orthonormal bright generator has zero diagonal blocks and h in both off-diagonal blocks. Its positive excitation account is

$$H_{\rm gen}^2=\operatorname{diag}(Q,Q),\quad H_0=\operatorname{diag}(h,h).$$

Here H0=|H<sub>gen</sub>|, and the two commute. The signed coherent generator and its positive excitation account have different roles. Replacing the signed spectrum by its magnitude is not a common scalar shift.

For species t at site x, let Ntx be the exact incoming occupation and Gtx the outgoing number Gram. Their retained denominator is 240. Define

$$O_{tx}=\frac{1}{8}\operatorname{diag}(N_{tx},W_{tx}),$$
$$W_{tx}=\frac{1}{240}h^{-1}G_{tx}h^{-1},$$
$$E_{tx}=H_0^{1/2}O_{tx}H_0^{1/2}.$$

Every Ntx is nonnegative and every Gtx is a positive Gram. Congruence makes Etx positive. Summing every species and site returns H0. The actual source evolution, energy transfer, current and coherence retain their original definitions. [3]

This account is an inherited excitation-energy choice. It is not added to H<sub>gen</sub> as another term or identified with complete rest energy. A spatial density also needs an embedding, physical energy conversion and a common reference.
''',r'''
## 14. An exact flatness identity

At each of the eight sites the retained matrices obey

$$\sum_tN_{tx}=I,\qquad \sum_tG_{tx}=240Q.$$

Since Q=h², substitution into the effects gives the short proof

$$\sum_tO_{tx}=\frac{I}{8},\qquad E_x:=\sum_tE_{tx}=\frac{H_0}{8}.$$

Consequently Ex commutes with H<sub>gen</sub>. Under H<sub>gen</sub>, every preparation has a stationary one-eighth share of this excitation energy at each site, although species and coherence evolve in the exact 36-coordinate closure.

The total amplitude can still change with preparation. Retained evaluations are:

| Preparation | Total relative energy |
|---|---:|
| e0 | 11.302793352678457 |
| plus | 11.828266226372410 |
| minus | 11.131220607210203 |
| phase | 11.479743416791305 |

Each site's energy is the displayed total divided by eight. The fractions are exact; these decimals are retained evaluations. This scalar receiver fixes a spatial shape and does not retain every changing source coordinate.

The independent checker verifies all spatial Gram principal minors, all eight flatness identities, and agreement with the separately retained observable closure. Two native operator words receive the complete incoming and outgoing identities. Their actual execution is recorded in the campaign receipt map.

The next density question is therefore precise: justify this uniform physical localization or derive a different local energy/stress coupling from the source. Species weights cannot be selected merely to obtain a desired field.
'''),
(r'''
## 15. A finite cube localization

Choose the orthogonal cube embedding Xx=ℓ times ξ<sub>x</sub>, with every component of ξ<sub>x</sub> equal to +1 or -1. It matches the retained cube-edge construction. The edge graph alone does not fix these angles. Its source-coordinate edge length is two; ℓ assigns a physical length.

Choose a normalized nonnegative spatial profile ζ<sub>x</sub> and an energy unit eu. The explicit excitation-mass account is

$$\rho_{\rm exc}(z)=\frac{e_u}{c^2}\sum_x\langle E_x\rangle\zeta_x(z-X_x),$$
$$M=\frac{e_u\langle H_0\rangle}{c^2},\qquad \rho_{\rm exc}=\frac{M}{8}\sum_x\zeta_x.$$

For the complete worked case, each profile is a uniform ball of radius δ<ℓ and volume 4π δ³/3. The balls are disjoint; each carries mass M/8. This specifies finite interiors and finite self-energy.

The embedding, smoothing radius and E/c² conversion are stated assignments. A compatible coupling uses the spatial average of a over each ball, not merely its center value. Other active fields, interactions and reference apparatus still need their own spatial account.

Under the declared Poisson receiver, a point outside every ball has

$$a(z)=\frac{2GM}{c^2}K_{\rm cube}(z),$$
$$K_{\rm cube}(z)=\frac{1}{8}\sum_x\frac{1}{|z-X_x|}.$$

The shell theorem makes this equality exact outside the balls. It does not make the cube spherical. The enclosing flux returns M, and the exterior profile retains shape information beyond its monopole.

Declare H<sub>gen</sub>(a)=H<sub>gen</sub>-aH<sub>0</sub>/2 for a uniform lift. For the actual incoming/outgoing contrast B=diag(I,-I), H<sub>0</sub> commutes with B and H<sub>gen</sub>, so its entire history is unchanged. Scaling H<sub>gen</sub> itself gives time dilation. This is the Si29 population clock; Chapter I uses a different, certified phase receiver.
''',r'''
## 16. Shape and a controlled remainder

Let r=|z|, n=z/r and q=sqrt(3)ℓ/r<1. The cube centers have common radius sqrt(3)ℓ. Inversion symmetry removes odd multipoles. Its second moment is ℓ² times the identity, so the traceless quadrupole also vanishes.

The fourth moment is

$$\frac{1}{8}\sum_x(n\cdot X_x)^4=\ell^4\left(3-2\sum_jn_j^4\right).$$

Insert this into P4(u)=(35u⁴-30u²+3)/8. The first surviving correction is

$$K_{\rm cube}(rn)=\frac{1}{r}+\frac{A_4(n)}{r^5}+R_6,$$
$$A_4(n)=\frac{7\ell^4}{4}\left(3-5\sum_jn_j^4\right).$$

Since |Pl|<=1, the remaining even Legendre series is bounded by

$$|R_6|\leq\frac{q^6}{r(1-q^2)}.$$

The monopole-only bound is q⁴/[r(1-q²)]. The degree-four correction is -7ℓ⁴/(2r⁵) on a cube axis and +7ℓ⁴/(3r⁵) along a body diagonal.

This is a source-shape control with no amplitude fit. Its domain requires r>sqrt(3)ℓ and an observation point outside every ball. The smearing changes the interior and self account while leaving this exterior center sum unchanged.

Low-order isotropy and an exactly spherical field are different conclusions. The finite cube supplies the former through degree three. A proposed macroscopic isotropic limit must specify how source orientations, placements or a graph family approach that limit, and bound the surviving shape terms.
'''),
(r'''
## 17. Finite cube binding energy

Eight uniform balls each have mass m=M/8 and radius δ. Their self energies sum to

$$U_{\rm self}=8\left(-\frac{3Gm^2}{5\delta}\right)=-\frac{3GM^2}{40\delta}.$$

The cube has 12 unordered pairs at distance 2ℓ, 12 at 2sqrt(2)ℓ, and four at 2sqrt(3)ℓ. Nonoverlap and spherical symmetry give each exact center-pair interaction. Thus

$$U_{\rm pair}=-\frac{GM^2}{64\ell}\left(6+3\sqrt{2}+\frac{2}{\sqrt{3}}\right).$$

The sum is the on-solution Newtonian binding account for this chosen density, using the whole field and one infinity reference. The source masses in the linear equation remain the prescribed M/8. Adding U/c² back into that source would introduce a further self-gravity completion.

This calculation also identifies which energy is missing from an excitation-only mass assignment. A complete account must include active field, interaction, counterterm and reference/apparatus energies under the same reference. Bond interactions need not possess an arbitrary positive site decomposition.

In particular, a positive minimum record cost and this negative binding account are different quantities. Counting the on-solution binding energy and then adding its source-field interaction a second time would double count the same coupling. The finite localization makes this distinction calculable rather than leaving an unregularized point-source self-energy implicit.
''',r'''
## 18. An exact radial receiver

The retained shell conductance is

$$c_i=i(i+1)=\left(\int_i^{i+1}\frac{du}{u^2}\right)^{-1}.$$

Use radii ri=ih, an outer boundary aL=0, and no inner sink, c0=0. Source shells have masses Munit mi. With kappa=2GMunit/(c²h), solve

$$Ka=\kappa m,\qquad K=B^TCB,$$

where B takes outward edge differences and C=diag(ci). Its ith row is

$$(Ka)_i=c_i(a_i-a_{i+1})+c_{i-1}(a_i-a_{i-1}).$$

For any nonzero v, vᵀKv is the positive sum of weighted squared edge differences. They cannot all vanish while the outer value is zero. K is therefore positive definite and the finite problem has a unique solution.

The outer exit carries an essential source flux. Removing it gives the closed graph Kclosed with Kclosed times 1 equal to zero. Summing its equations would require zero total injection. It cannot support this positive-total static source without an additional sink.

This is the retained spherical receiving geometry, with an explicit extended source and boundary. It is not an identification of concentric shells with Si29's eight cube sites. The two constructions answer distinct spatial questions while sharing a declared energy and receiver convention. [3]
'''),
(r'''
## 19. Green kernel and flux proof

Sum the source equations through shell i. Interior edge fluxes cancel, leaving

$$c_i(a_i-a_{i+1})=\kappa M_i,\quad M_i=\sum_{j\leq i}m_j.$$

The edge resistance telescopes:

$$\frac{1}{c_i}=\frac{1}{i}-\frac{1}{i+1}.$$

Summing the remaining differences to the outer boundary gives

$$H_{ij}=\frac{1}{\max(i,j)}-\frac{1}{L},$$
$$a_i=\kappa\sum_jH_{ij}m_j,\qquad KH=I.$$

No desired field values enter the right-hand side. The source and conductance determine them. Between shells use exact harmonic interpolation. On ri<r<ri+1 it gives

$$a'(r)=-\frac{2GM_{\rm unit}M_i}{c^2r^2},$$
$$g_r=-\frac{GM_{\rm unit}M_i}{r^2}.$$

The flux returns the same enclosed mass. Each shell produces its derivative jump and a constant interior potential. At the shell itself choose a one-sided acceleration or the mean self-field used in radial virtual work.

This network samples the exact continuum thin-shell solution. The finite outer reference differs from isolation by the known constant 2GMtotal/(c²Lh). Gradients and fluxes agree; potential values and escape to infinity require that correction. Refining the radial mesh cannot remove a boundary-reference error held fixed in physical units.
''',r'''
## 20. A complete rational example

Take L=9, kappa=1/50, and the shell masses shown below. Their total is one. These fractions specify a test source, not an inferred microscopic mass spectrum.

| i | mi | ai | Enclosed Mi |
|---|---|---|---|
| 1 | 0 | 1777/630000 | 0 |
| 2 | 1/5 | 1777/630000 | 1/5 |
| 3 | 0 | 1357/630000 | 1/5 |
| 4 | 3/10 | 1147/630000 | 1/2 |
| 5 | 1/10 | 52/39375 | 3/5 |
| 6 | 0 | 29/31500 | 3/5 |
| 7 | 2/5 | 1/1575 | 1 |
| 8 | 0 | 1/3600 | 1 |

Every outgoing flux is kappa Mi, including the final exit. Let u=a/kappa and measure energy in GMunit²/h. The finite functional is F=uᵀKu/2-mᵀu. Its minimum is -mᵀHm/2, giving

$$\frac{U_L}{GM_{\rm unit}^2/h}=-\frac{9427}{252000},$$
$$\frac{U_\infty}{GM_{\rm unit}^2/h}=-\frac{2603}{28000}.$$

The difference is the exact correction -GMtotal²/(2Lh). The exterior positive gradient term and the source-reference change combine into this signed on-solution result.

Varying a shell radius at fixed ordering gives

$$-\frac{dU}{dr_j}=-\frac{GM_j}{r_j^2}\left(M_{<j}+\frac{M_j}{2}\right).$$

The half self term is the mean of its two one-sided self-fields. This is radial work under spherical expansion, rather than net vector force on the shell center.
'''),
(r'''
## 21. A controlled continuum limit

For a uniform ball of radius b, divide radius into n cells with h=b/n. Move each cell's mass to its outer endpoint:

$$\frac{m_j}{M}=\frac{j^3-(j-1)^3}{n^3}.$$

Write eta=GM/(c²b), alpha=a/eta. The continuous profile is 3-x² inside and 2/x outside. The exact potential error obeys

$$0\leq\alpha_{\rm ball}-\alpha_{\rm shells}\leq\frac{3}{n}-\frac{2H_n}{n^2},$$

where Hn is the nth harmonic sum. The bound is attained at the center. Moving a mass element from s to its endpoint sj reduces its kernel by at most 1/s-1/sj. Integrating that difference gives the displayed bound.

For binding energy the corresponding bound is

$$0\leq\frac{U_{\rm shells}}{GM^2/b}+\frac{3}{5}\leq\frac{3}{2n}-\frac{H_n}{n^2}.$$

Use 1/max(s,t)=min(1/s,1/t) in the pair integral; outward motion changes that minimum by at most the sum of the two reciprocal-radius changes. The energy factor one-half yields the bound.

A finite absorbing radius R adds reduced lift offset 2b/R and energy offset GM²/(2R). Isolation therefore requires both h/b→0 and b/R→0. Refining while R/b=2 leaves lift bias one and reduced energy bias one-quarter. The radial continuum limit controls discretization; it does not derive the source graph's angular isotropy.
''',r'''
## 22. A Chapter I field density

Take the original static classical quadrupole field and average its positive free-field energy over angles. Write X² for the sum of the two squared source amplitudes. With kappa=4/5, its total free energy is Uf=X²/R. [1,5]

Conditionally assign Mf=Uf/c² to that free-field account and x=r/R. Its spherical density and enclosed mass are

$$\rho_{\rm in}=\frac{M_f r^2}{2\pi R^5},\quad \rho_{\rm out}=\frac{3M_fR^5}{4\pi r^8},$$
$$\frac{M(<r)}{M_f}=\frac{2}{5}x^5\quad (x\leq1),$$
$$\frac{M(<r)}{M_f}=1-\frac{3}{5}x^{-5}\quad (x\geq1).$$

Two-fifths of Uf lies inside R and three-fifths outside. Solving the same Poisson receiver, with x=r/R, gives

$$a_{\rm in}=\frac{2GM_f}{c^2R}\left(1-\frac{x^4}{10}\right),$$
$$a_{\rm out}=\frac{2GM_f}{c^2r}\left(1-\frac{x^{-5}}{10}\right).$$

Both a and a' match at R. The source field carries energy outside R; treating that energy as mass makes this region nonvacuum. Its exact correction is proportional to r^-6, rather than a pure vacuum 1/r profile.

At the commuting classical static minimum, each boundary amplitude equals half ε times its source current. Its free energy, interaction and counterterm satisfy

$$U_f+U_{\rm int}+U_{\rm ct}=U_f-2U_f+U_f=0.$$

This cancellation shows why the positive free-field sector alone is a conditional source choice. The quantum D and C do not commute on the nontrivial lanes; their joint local energy account still needs a derivation. R remains the original coupling radius, distinct from the cube scale and radial outer boundary.
'''),
(r'''
## 23. Energy unread by the clock

Retain the original sixteen-state source: S is Swap, D=Qleft-Qright, C=iSD, and Eeven=Qleft+Qright+Qleft Qright. Its unnormalized current is Zraw=D+iC. Exact multiplication gives

$$[S,Z_{\rm raw}]=-2Z_{\rm raw},$$
$$[E_{\rm even},Z_{\rm raw}]=[D^2+C^2,Z_{\rm raw}]=0.$$

The full Hamiltonian is Hs+Hf+Hint+Hct, with Hs=ε(S+Eeven), Hint=-ε(D phi_plus+C phi_cross), and Hct=ε²μ(D²+C²), μ=1/(4R). The free field, both polarizations and both counterterms are retained.

Eeven also commutes with the complete interacting Hamiltonian. Adding any bounded real function F(Eeven) therefore changes energy while leaving the entire current history unchanged for every initial state:

$$Z_{\mathcal{H}_0+F}(t)=Z_{\mathcal{H}_0}(t).$$

The four diagonal source states have D=C=0 yet distinct energies ε(1+qa)². They are current-dark energy controls, not clocks with a nonzero amplitude. Observing the current does not determine all source energy. [5]

A scalar addition kI supplies the simplest common-energy example. Density evolution and relative frequencies stay fixed while the common amplitude phase changes. An external phase reference can compare that phase through its stated coupling and payment; it does not choose a mass baseline by itself.

This distinction also applies to the Si29 account. Independently shifting its positive H0 by kI changes the candidate assigned mass by eu k/c². It does not follow from replacing H<sub>gen</sub> by H<sub>gen</sub>+kI and taking its absolute value. Reference energy, signed generator, positive account and actual clock receiver must retain their separate definitions.
''',r'''
## 24. The operational clock response

Supply a physical static-lift perturbation

$$\mathcal{H}(a)=\mathcal{H}_0+aV+O(a^2).$$

On lane l, let Z=(D+iC)/dl, z=<Z>, and nu=-Im(zdot/z), as in Chapter I. For a bounded V and a fixed preparation, Duhamel gives

$$\delta z(t)=i\int_0^t\langle[V_I(s),Z_I(t)]\rangle\,ds.$$

Where the baseline z0 stays away from zero, the actual phase-rate derivative is

$$\delta\nu=-\operatorname{Im}\left(\frac{\delta\dot z}{z_0}-\frac{\dot z_0\delta z}{z_0^2}\right).$$

A field-form perturbation needs common energy-form control and a dominated differentiated evolution. An a-dependent preparation supplies an additional state derivative. These requirements belong to the chosen V; the original sixteen-dimensional commutator is only its source algebra.

One exact full-continuum control is the declared coupling of the full interacting Hamiltonian:

$$\mathcal{H}(a)=n(a)\mathcal{H}_0+f(a)I.$$

It gives

$$z(t;a)=z(n(a)t;0),$$
$$\nu(t;a)=n(a)\nu(n(a)t;0).$$

At matched internal age the frequency ratio is n. At equal coordinate time, where nudot exists, its derivative also includes n'(0)t nudot(t;0). The actual retained clock is slightly nonstationary. Accumulated phase follows the time change without requiring an additional second derivative.

Thus a square-root n is an explicit coupling control. A first-order redshift test must specify matched age, a stationary reference, or the transient contribution at equal coordinate durations.
'''),
(r'''
## 25. Full scaling and ε

The complete scaling control multiplies Hs, Hf, Hint and Hct by the same n. Replacing only ε by n ε at a fixed field instead gives

$$\mathcal{H}_\epsilon=nH_s+H_f+nH_{\rm int}+n^2H_{\rm ct}.$$

For s=n'(0), its first-order difference from full scaling is

$$V_\epsilon-s\mathcal{H}_0=s(H_{\rm ct}-H_f).$$

For the source-only slope s=-1/2, the residual coefficients on (Hs,Hf,Hint,Hct) are (0,1/2,0,-1/2). This is not a scalar on the full field. The counterterm commutes with the full Hamiltonian and current, so its energy stays unread throughout this history. The free-field part of the residual can change the current.

The retained hard-branch second-order diagnostic is

$$\Omega_l^{(2)}=\Delta(1-4g_l^2J),\quad \Delta=2\epsilon,$$
$$\frac{d\log\Omega_l^{(2)}}{d\log\epsilon}=1-\frac{8g_l^2J+4g_l^2\Delta J'}{1-4g_l^2J}.$$

The hard split is held fixed in this perturbation. J and J' are positive, so the derivative is below one. The six original coupling squares differ, producing six disjoint derivative enclosures. These are second-order source diagnostics, not finite-lift full-field response certificates.

The actual physical V remains the question. A shared perturbation across six separately prepared lanes can test universality; fitting each lane's ε independently would change that test.

The energy unit e<sub>u</sub>, action I<sub>u</sub> and length ℓ<sub>phys</sub> must be shared between source, clock and field. They set the source time parameter and cube's lift coefficient:

$$\theta_{\rm source}=\frac{e_ut}{I_u},\qquad \frac{2Ge_u}{c^4\ell_{\rm phys}}.$$

A physical ε alone does not determine both conversions.
''',r'''
## 26. Correlated phase and precision

Under the declared full scaling, compare the same baseline phase history at T and nT. Within the common certified window, with ℓ≤ν<sub>0</sub>≤u,

$$\delta\theta(T)=-\int_{nT}^{T}\nu_0(s)\,ds,$$
$$-u(1-n)T\leq\delta\theta\leq-\ell(1-n)T<0.$$

For n=sqrt(1-a), 0<a<1, rational bounds on 1-n give

$$-\frac{uaT}{2-a}\leq\delta\theta\leq-\frac{\ell aT}{2}.$$

The signed shift exists for every positive a and T in this window. At the frozen Earth surface lift, all six one-bare-cycle shifts lie between -4.373898 and -4.373888 nanoradians. These are conditional source predictions, not achieved apparatus sensitivity. [5]

A separate comparison encloses the two phases independently. Those bands are disjoint only under the sufficient condition a>1-(ℓ/u)². Its conservatively rounded thresholds are:

| Lane | Sufficient a |
|---|---:|
| 01 | 2.84407 × 10<sup>-9</sup> |
| 02 | 1.22170 × 10<sup>-8</sup> |
| 03 | 1.89316 × 10<sup>-6</sup> |
| 12 | 3.27189 × 10<sup>-9</sup> |
| 13 | 1.74924 × 10<sup>-6</sup> |
| 23 | 1.60120 × 10<sup>-6</sup> |

These thresholds concern independent enclosures; they are not a minimum lift for the correlated phase sign. A phase error δ on each comparison needs

$$\ell(1-n)T>2\delta.$$

The physical coupling, common preparation and unwrapped phase branch remain explicit. Chapter II's fresh preparations, timing/error budgets, paid reference and turn counter supply the separate measurement protocol. [2]
'''),
(r'''
## 27. Frozen anchors and reproduction

The recovered CR004 premises retain the same declared gravitational parameters and radii. Recalculation gives the following spherical surface values; escape speeds are km/s. [4]

| Body | Lift a(b) | g, m/s² | Escape |
|---|---|---|---|
| Earth | 1.39225 × 10<sup>-9</sup> | 9.82025 | 11.1861 |
| Moon | 6.28226 × 10<sup>-11</sup> | 1.62490 | 2.37618 |
| Sun | 4.24501 × 10<sup>-6</sup> | 274.200 | 617.675 |

The formulas use the same frozen μ=GM and radius on both sides. These inputs preserve the intended Newtonian recovery; they do not determine mass from the microscopic account or select G. The digits expose arithmetic, rather than measured precision or corrections for shape and rotation.

The finite cube and shell controls add different information: a source-shape correction, exact source flux, boundary energy and quantified continuum error. The interacting-clock controls add the complete perturbation and a visible precision target.

Reproduction retains editable manuscript, exact operands, source snapshots, native receipts, independent code and content hashes. The source checker has 2,040 exact assertions, the radial checker 312, and the clock checker 822. The static-field checker adds 52 assertions, the kernel/frozen-arithmetic checker 45, the uniform-coupling certificate 23, and the correlated-phase supplement 47. Fresh native execution and custody are recorded separately in the campaign receipt map; retained historical calls are not counted as new work.

The old draft's 42 symbolic checks remain historical. They are not relabeled as the present verification. CR004, G224's retrieved index and LC03 retain their original evidence scopes. The original G224 derivation is still unrecovered; LC03 is an imported mechanism replay, and the current retained source route is the Si29 construction used here.
''',r'''
## 28. The next physical derivations

First derive the actual local energy/stress coupling, including field, interaction and reference terms. Carry its spatial density through one calibrated receiver.

Next derive a graph or field response with a massless isotropic k² leading term and bounded spatial/frequency error, retaining the radial boundary account.

Then apply one physical V to all six clocks, with matched-age or transient timing explicit. Derive causal kinetics and the spatial metric response, including γ, using the same source normalization.

Memory and closure methods control eliminated information. The spatial operator and metric coupling need their own derivations.

### References and retained sources

[1] Brady, ChatGPT and Codex. *Volume I, Chapter I*, final draft and `sam_volume_I_i` source/certificate, 15 October 2026.

[2] Same authors. *Chapter II: Retention, accumulation and the finite ledger*, 20-page physical development draft and this revision's companion source-to-space update.

[3] SAM Research Project. `volii_duck_expansion1/2`, Si29 effects; `native_energy_source1`, radial response; current source/radial reports and operands.

[4] SAM Research Project. CR004 declared premises, precommit and scoped weak-field result. Current arithmetic uses the frozen premises.

[5] Current clock/static-field derivations, certificates, checks and native receipt map, companion archive.

[6] SAM Research Project. `native_coupling_scale1` and `source_spatial_response1`: selected coupling and frequency-dependent source-response scopes.

[7] C. M. Will. *The Confrontation between General Relativity and Experiment*. Living Reviews in Relativity 17, 4 (2014), doi:10.12942/lrr-2014-4. Conventional metric notation.
''')]
