# WP0-A first-pass reproduction: DEHK §8.1 gravitational interferometer

**Status:** source-equation reconstruction and analytical consistency checks completed for the main §8.1 chain, and a concrete Gaussian/finite-matrix state-level **control gate** is now passed below. The general DEHK group-averaging, QFT modular-domain, and regional common-algebra questions remain open; this is not a full independent proof audit or a same-observable clock comparison.  
**Primary source:** De Vuyst, Eccles, Höhn & Kirklin, *Crossed products and quantum reference frames: on the observer-dependence of gravitational entropy*, arXiv:2412.15502 v3, §8.1 and Appendix F, especially Eqs. (294)–(309), (508)–(520). [1](https://arxiv.org/abs/2412.15502)

## 1. Comparison object and its scope

The example places clocks C1 and C2 in the same subregion \(\mathcal U\), and complementary clock C3 in \(\mathcal U'\). It uses two perspective reductions of one physical state. The target is the entropy assigned to the regional QFT/graviton degrees of freedom by each clock-dressed algebra—not a change in the total entropy of the whole patch.

The source explicitly states that the two regional algebras are inequivalent,

\[
 r(\mathcal A^{H}_{\mathcal U C_1})\ne r(\mathcal A^{H}_{\mathcal U C_2}),
\]

and that their overlap may be trivial when the modular action on the regional algebra is ergodic (Eq. 294 and the cited overlap result). Thus §8.1 is a same-state, same-region comparison of clock-relative **algebra/entropy constructions**. It is not, without a nontrivial common algebra or matched relational task, a comparison of predictions for the same observables. The source also distinguishes this restricted regional entropy from the full-patch/generalized entropy, which is observer-independent under its assumptions.

## 2. Same-state perspective map

In the C1 perspective the source takes the projected product-form state

\[
 |\phi_{\vert 1}\rangle
 =\sqrt{N}\,\Pi_{\vert 1}
   (|\phi_S\rangle\otimes|f\rangle_2\otimes|g\rangle_3),
 \tag{295}
\]

where \(|f\rangle_2\) and \(|g\rangle_3\) are normalized clock states and \(N\) normalizes the projected state. The C2 perspective is obtained by the source’s QRF transformation, not by choosing a new physical state:

\[
 |\phi_{\vert 2}\rangle
 =V_{1\to2}(0,0)|\phi_{\vert 1}\rangle
 =\sqrt{2\pi N}\,f(-H_S-H_1-H_3)\Pi_{\vert 2}
   (|\phi_S\rangle\otimes|0\rangle_1\otimes|g\rangle_3).
 \tag{296}
\]

Appendix F gives the corresponding projected-state decomposition and the frame-change calculation (Eqs. 508–520). The no-explicit-entanglement description in the C1 perspective is qualified: the non-ideal-clock projector prevents a simple tensor-product factorization of the reduced physical Hilbert space. The apparent entanglement difference is therefore relative to the chosen perspective/factorization and projector.

## 3. Finite-C3 density operators: retain the complementary clock

Write the spectral projectors as \(\Pi(\mathcal O,\sigma)\), restricting \(\mathcal O\) to spectrum \(\sigma\), and define

\[
 \bar H'_1=H_S-H_2-H_3,\qquad
 \bar H'_2=H_S-H_1-H_3,\qquad
 \bar H_2=-H_S-H_1-H_3,
\]

with the source’s constraint-equivalent Hamiltonians and perspective projectors \(\Pi_{\vert i}\). Let \(\Delta=\Delta_{\phi_S\vert\psi_S}\) be the relative modular operator for the declared regional QFT reference state pair. The exact source expressions before the ideal-C3 simplification are

\[
\begin{aligned}
\rho_{\phi\vert1}={}&2\pi N e^{-S_{0,1}-\beta(H_2+H_3)}\Pi_{\vert1}\Delta^{1/2}
  \left[\int_{\sigma_2}d\epsilon_2\,
  \Pi(\bar H'_1+\epsilon_2,-\sigma_3)
  |f(\epsilon_2)|^2|g(-\bar H'_1-\epsilon_2)|^2\right]
  \Delta^{1/2}\Pi_{\vert1},\\[3pt]
\rho_{\phi\vert2}={}&2\pi N e^{-S_{0,2}-\beta(H_1+H_3)}\Pi_{\vert2}f(\bar H_2)\Delta^{1/2}
  \left[\int_{\sigma_1}d\epsilon_1\,
  \Pi(\bar H'_2+\epsilon_1,-\sigma_3)
  |g(-\bar H'_2-\epsilon_1)|^2\right]
  \Delta^{1/2}f^*(\bar H_2)\Pi_{\vert2}.
\end{aligned}
\tag{297–298}
\]

These expressions keep the spectral-support projectors and finite clock wavefunction \(g\). The factors \(S_{0,i}\) encode trace-normalization conventions. The equations are densities for different algebras, so equality of their numerical traces or absolute entropies must not be presumed.

### Check: controlled ideal-C3 simplification

Let \(L_i=\|\sigma_i\|\) denote the spectral width when finite. In the source’s effectively ideal-C3 approximation, \(|g(E_3)|^2\) is constant over the relevant support, with value \(L_3^{-1}\) in the finite-window normalization, and the projectors involving \(-\sigma_3\) act as identity on the support of interest. With \(\int_{\sigma_2}|f(\epsilon_2)|^2d\epsilon_2=1\), the bracket in \(\rho_{\phi\vert1}\) reduces to \(L_3^{-1}\). In \(\rho_{\phi\vert2}\), the remaining \(\epsilon_1\)-integral gives \(L_1L_3^{-1}\). This yields the source’s Eqs. (299)–(300):

\[
\begin{aligned}
\rho_{\phi\vert1}&\approx 2\pi N L_3^{-1}e^{-S_{0,1}-\beta(H_2+H_3)}
  \Pi_{\vert1}\Delta\Pi_{\vert1},\\
\rho_{\phi\vert2}&\approx 2\pi N L_1L_3^{-1}e^{-S_{0,2}-\beta(H_1+H_3)}
  f(\bar H_2)\Pi_{\vert2}\Delta\Pi_{\vert2}f^*(\bar H_2).
\end{aligned}
\tag{299–300}
\]

This is an approximation to the reduced density operators, not an exact finite-C3 result. In an unbounded ideal-clock limit the clock state is not normalizable as an ordinary factor state; the limit and normalization must be taken together, as the source notes.

## 4. Shapiro-delay superposition and normalization check

The source chooses C2’s state in the C1 perspective as a superposition of two clock-orientation states separated by \(\Delta\tau\). For a clock spectrum interval of width \(L_2=\epsilon_2^{\max}-\epsilon_2^{\min}\), it writes

\[
 f(E)=\sqrt{\frac{N_2}{2\pi}}e^{-i\tau_2E}(1+e^{-iE\Delta\tau}),
 \qquad \alpha=L_2\Delta\tau.
 \tag{301}
\]

The normalization follows directly from \(\int_{\sigma_2}|f(E)|^2dE=1\):

\[
\begin{aligned}
1&=\frac{N_2}{\pi}\left[L_2+
   \frac{\sin(E\Delta\tau)|_{E=\epsilon_2^{\min}}^{\epsilon_2^{\max}}}{\Delta\tau}\right],\\
N_2&=\frac{\pi}{L_2\left[1+
  \dfrac{\sin(\alpha\epsilon_2^{\max}/L_2)-\sin(\alpha\epsilon_2^{\min}/L_2)}{\alpha}\right]}.
\end{aligned}
\]

As \(\alpha\to0\), \(N_2\to\pi/(2L_2)\), and \(f(E)\) reduces to the normalized single-orientation clock state. This independently checks the normalization quoted in Eq. (302).

## 5. Entropy expansion and the two sources of entropy relativity

For C1, the source obtains (Eq. 305)

\[
S[\phi_{\vert1}]=S_{0,1}-\log(2\pi N L_3^{-1})
 +\beta\langle H_2+H_3\rangle_{\phi_{\vert1}}
 -\left\langle\log(\Pi_{\vert1}\Delta\Pi_{\vert1})\right\rangle_{\phi_{\vert1}}.
\]

For C2, the exact logarithm of the noncommuting product in \(\rho_{\phi\vert2}\) is not simplified by assuming that \(H_S\) commutes with \(\Delta\). The source instead expands for \(|\alpha|\ll1\), where the symmetric BCH formula gives the first-order commutator term (Eq. 308), and obtains Eq. (309):

\[
\begin{aligned}
S[\phi_{\vert2}]={}&S_{0,2}-\log(2\pi N L_1L_2^{-1}L_3^{-1})
 +\beta\langle H_1+H_3\rangle_{\phi_{\vert2}}\\
&-\frac12\left[
 \left\langle\log(\Pi_{\vert2}\Delta_{\phi_S(-\tau_2)\vert\psi_S}\Pi_{\vert2})\right\rangle_{\phi_{\vert2}}
 +\left\langle\log(\Pi_{\vert2}\Delta_{\phi_S(-\tau_2-\Delta\tau)\vert\psi_S}\Pi_{\vert2})\right\rangle_{\phi_{\vert2}}
 \right]+O(\alpha^2).
\end{aligned}
\]

The source identifies two distinct effects:

1. **Non-isomorphic clocks:** different clock spectra produce different projected/coarse-grained modular operators, even at the leading semiclassical level.
2. **Different perspective entanglement:** for isomorphic spectra, a nonzero clock superposition changes the C2-relative state and adds the commutator/BCH contribution; this is a first-order-in-\(\alpha\) effect in the stated small-\(\alpha\) regime.

This does not imply that the total patch or generalized entropy changes with observer. The source distinguishes the restricted regional QFT algebras from the full patch algebra containing all relevant clocks; the full-patch descriptions are unitarily related under the stated framework.

## 6. Physical-inner-product status

DEHK §2.3 defines the physical inner product by group averaging and explicitly states that its convergence and positive-semidefinite character are unknown in general; the authors assume both in the remainder of the paper. [1](https://arxiv.org/abs/2412.15502) The §8.1 reconstruction below is therefore conditional on that framework assumption. It does not establish the physical inner product for the general theory or for every state in the example family.

For a state-level gate, specify a test space closed under the constraint action, the spectral behavior near zero, and the rigging map/regularization; then demonstrate that the group-averaged norm is finite and nonnegative for the chosen state. If that cannot be done, report the comparison as conditional on the source’s assumed physical inner product rather than treating it as independently verified.

## 7. Concrete state-level control gate

The most tractable nontrivial check uses a one-dimensional absolutely continuous constraint scaffold. Its role is deliberately limited: it tests a fully specified state, domain, and common-algebra calculation without claiming to reconstruct DEHK’s full multi-clock gravitational model or its type-III/crossed-product region theory.

### 7.1 Continuous constraint scaffold and rigging map

Let

\[
\mathcal H_{\rm kin}=L^2(\mathbb R,dE)\otimes \mathbb C^2,
\qquad
C=E\otimes I_R.
\]

The continuous variable \(E\) represents one declared total-constraint spectral coordinate after a linear clock/system change of variables. Define the test space

\[
\mathcal D=\{E\mapsto f(E)r_0:\ f\in C_c^\infty(\mathbb R),\ r_0\in\mathbb C^2\}.
\]

For \(\Psi=f r_0\) and \(\Phi=g s_0\) in that space,

\[
\langle\Psi,e^{itC}\Phi\rangle
=\langle r_0|s_0\rangle\int dE\,\bar f(E)g(E)e^{itE}.
\]

Using a symmetric regulator \(L\to\infty\), interchange integrals only at finite \(L\) and apply the standard sinc limit \(\int dE\,\bar f(E)g(E)\,2\sin(LE)/E\to2\pi\bar f(0)g(0)\). Equivalently, \(\int dt\,e^{itE}=2\pi\delta(E)\) distributionally. The group-averaged pairing is therefore finite:

\[
(\Psi,\Phi)_{\rm GA}
:=\int_{\mathbb R}dt\,\langle\Psi,e^{itC}\Phi\rangle
=2\pi\,\bar f(0)g(0)\langle r_0|s_0\rangle.
\]

The corresponding rigging map satisfies \(\eta\Psi=2\pi f(0)\,\delta(E)r_0\) in the spectral representation. Vectors with \(f(0)=0\) lie in the kernel of the induced sesquilinear form and are quotiented out. On the quotient the form is positive definite.

For the explicit normalizable Gaussian and regional vector

\[
f_a(E)=\frac{1}{(\pi a^2)^{1/4}}e^{-E^2/(2a^2)},
\qquad
\|f_a\|_{L^2}=1,
\qquad
\Psi_a=f_a(E)\otimes
\frac{|0\rangle+|1\rangle}{\sqrt2},
\]

the exact physical norm is

\[
\boxed{\ \|\Psi_a\|_{\rm GA}^2
=2\pi|f_a(0)|^2
=\frac{2\sqrt\pi}{a}\ }.
\]

It is finite and strictly positive for every finite \(a>0\). This closes the physical-inner-product convergence/positivity check **for this concrete state and scaffold**. It does not prove convergence or positivity for DEHK’s general U(1) family, for nonintegrable energy densities, or for a model whose zero-frequency Jacobian vanishes.

The scaffold has an explicit source-style multi-clock realization. Take

\[
\mathcal H_{\rm kin}=\mathbb C^2\otimes
\bigotimes_{i=1}^{3}L^2(\mathbb R,d\varepsilon_i),
\qquad
C=H_S+\sum_{i=1}^3\varepsilon_i I,
\]

with \(H_S=0\) on \(\mathbb C^2\), and choose the factorized clock–system test state

\[
\Psi_{\rm mc}=r_0\otimes f_a(\varepsilon_1)f_a(\varepsilon_2)f_a(\varepsilon_3).
\]

Define \(p=\varepsilon_1+\varepsilon_2+\varepsilon_3\), \(q=\varepsilon_1-\varepsilon_2\), and \(v=\varepsilon_2-\varepsilon_3\). The Jacobian is \(d\varepsilon_1d\varepsilon_2d\varepsilon_3=\frac13dp\,dq\,dv\), hence the group-averaged norm is a physical-slice integral,

\[
\|\Psi_{\rm mc}\|_{\rm GA}^{2}
=\frac{2\pi}{3}\int dq\,dv\,
|\Psi_{\rm mc}(p=0,q,v)|^2.
\]

On \(p=0\), the equivalent energy coordinates have squared sum

\[
\varepsilon_1^2+\varepsilon_2^2+\varepsilon_3^2
=\frac23\left(q^2+qv+v^2\right),
\]

so the Gaussian integration gives exactly

\[
\boxed{\ \|\Psi_{\rm mc}\|_{\rm GA}^{2}
=\frac{2\sqrt{\pi}}{\sqrt3\,a}\ }.
\]

This is a fully specified normalizable multi-clock kinematical state with a finite, strictly positive group-averaged norm. It still uses three ideal continuous one-parameter clock Hamiltonians and a finite-dimensional system, not DEHK’s unrestricted non-ideal finite-spectrum/QFT state family; its purpose is to close the tractable convergence/positivity gate without pretending to solve the general source model.

### 7.2 Modular-domain control

Use \(\mathcal H_R=\mathbb C^2\), \(h=\operatorname{diag}(0,1)\), and two full-support commuting regional reference states

\[
\omega_\phi=\frac{e^{-\beta h}}{Z_\beta},
\qquad
\omega_\psi=\frac{e^{-\beta' h}}{Z_{\beta'}}
\]

in a finite-dimensional standard representation. The relative modular operator has positive, nondegenerate support and is diagonal on the modular operator basis with eigenvalues
\((\omega_\phi)_i/(\omega_\psi)_j\). There are no nontrivial weak-closure, dense-domain, logarithmic-branch, or trace-class issues to solve in this finite-dimensional control: \(\Delta^{1/2}\), \(\log\Delta\), and every relevant density-matrix trace are well defined.

This verifies the domain/logarithm/trace gate for the selected matrix model only. It does not settle those questions for the unrestricted regional QFT algebra in DEHK §8.1.

### 7.3 Common-algebra control

Let \(Z=\operatorname{diag}(1,-1)\) and \(X=\sigma_x\). Model two inequivalent clock-dressed regional matrix algebras by

\[
\mathcal A_1=\operatorname{span}\{I,Z\},
\qquad
\mathcal A_2=\operatorname{span}\{I,X\}.
\]

Pauli-matrix independence gives immediately

\[
\boxed{\ \mathcal A_1\cap\mathcal A_2=\mathbb C I\ }.
\]

Thus this concrete control has no nontrivial common regional observable and therefore no shared same-task prediction comparison. Its outcome is entropy-functional/construction relativity only, not evidence that two clocks agree or disagree on a common observable. This direct trivial-intersection calculation closes the common-algebra gate for the control; it does not prove ergodicity of the source’s particular modular action and cannot be inserted back into DEHK §8.1 as if the source had supplied this pair of algebras.

### 7.4 Source-specific conditional common-algebra classification

The source itself gives a conditional intersection result. At the kinematical level, its Eq. (62) states that if the regional algebra is a Type III\(_1\) von Neumann algebra and the modular Hamiltonian \(H_S\) has an ergodic action on it, then

\[
\mathcal A_{SC_1}^{H}\cap\mathcal A_{SC_2}^{H}
=\mathbb C\,\mathbf 1_{S12}.
\]

Section 8.1 applies this possibility to the physical representations in Eq. (294), and §8.2 later summarizes the §8.1 example as having a trivial overlap “when \(H_S\) has an ergodic action.” [1](https://arxiv.org/abs/2412.15502) Therefore, for the explicitly declared ergodic modular-action case—such as the source’s de-Sitter-type static-patch setting—the common regional algebra is scalar-only and the CEH comparison is unambiguously **entropy-functional/algebra relativity, not a same-observable prediction test**.

This records the source’s stated classification rather than an independent proof for every background named in §8.1. For Schwarzschild or more general region constructions, the chosen modular action must be named and its ergodicity checked before importing the scalar-intersection conclusion. The common-algebra gate is therefore:

- **passed as a conditional source classification** in the declared Type III\(_1\)+ergodic-modular-flow case; and
- **open** for any alternate §8.1 background whose modular action is not shown to satisfy the same condition.

**Control-gate outcome:** for \((C,\Psi_a,\omega_\phi,\omega_\psi,\mathcal A_{1,2})\) above, the physical-inner-product convergence/positivity, modular-domain/log/trace, and common-algebra checks pass exactly. The independent source-general group-averaging and QFT-domain gates remain open and conditional on DEHK’s assumptions.

## 8. Reproduction checks completed and remaining gates

**Checked in this first pass**

- The state in the C2 perspective is obtained by the frame-change map from the C1-perspective state; the comparison is not made by selecting two unrelated physical states.
- Appendix F’s derivation chain (508)–(520) leads to the finite-C3 density operators; the main-text simplification is postponed until after those expressions.
- Normalization of the two-branch clock amplitude reproduces Eq. (302), including the \(\alpha\to0\) limit.
- The ideal-C3 limit produces the factors \(L_3^{-1}\) and \(L_1L_3^{-1}\) in Eqs. (299)–(300), subject to its support and normalization conditions.
- The comparison is between inequivalent regional algebras; the shared algebra must be computed, not assumed. Cross-algebra additive trace constants remain state-independent but can shift absolute entropy values.

**Not passed yet**

- Independently reconstruct the general group-averaged physical inner product and verify convergence/positivity for a fully specified normalizable \(f,g,\phi_S\) and clock spectra. The symbolic source family is not itself a concrete state-level convergence proof.
- Extend the relative modular operator domain and logarithm/trace verification from the finite matrix control to a source-specified regional QFT state.
- Evaluate any chosen alternate §8.1 background outside the source’s declared Type III\(_1\)+ergodic-modular-flow case; in that source case the recorded intersection is scalar-only, so no same-observable prediction task exists. The finite control has a directly proved trivial intersection, but it is not evidence about a nonergodic background.
- Match trace normalizations before any numerical comparison of absolute entropies. If this cannot be done canonically, restrict comparison to state dependence, within-algebra differences, or relative entropy.

**Gate:** WP0-A remains *in progress* for the source-general thesis, but the declared concrete state-level control now passes, and the source-specific common-algebra classification is scalar-only in the stated Type III\(_1\)+ergodic-modular-flow case. The worksheet reconstructs the source’s calculation, checks its normalization/limit structure, and closes a separate Gaussian/finite-matrix control for group average, modular domains, and a trivial common-algebra intersection. Do not begin a quantitative scan, describe WP0-A as fully closed for the DEHK source family, infer an intersection for nonergodic backgrounds, or call either result a same-observable clock-equivalence result.
