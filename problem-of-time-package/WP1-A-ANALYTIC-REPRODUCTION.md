# WP1-A analytic reproduction: bounded-band clock and TO/PM protocols

**Status:** the bounded-band response, smooth-pulse same-task TO/PM meter, normalized probabilities and channel comparison are derived. The free pre-pulse rigging map, weak-coupling conditional-series convergence, self-adjoint interacting constraint, an interacting rigging map on its absolutely continuous scattering test space, the source reconstruction’s incoming-state match/nonzero normalized readout support, its identification with the incoming Kato representative and induced physical norm, and physical-fiber gauge consistency for the special one-pulse meter are checked. The noncommuting two-pulse benchmark has exact weak-coupling state construction, scalar sequential normalization, Born-rule physical-fiber POVMs, and an analytic order witness. WP1-A therefore passes its declared analytic gate in the weak-coupling/supported-slot domain; no causal-order or Level C claim is made. No code, parameter scan, or numerical campaign was run.  
**Primary source:** Hausmann, Schmidhuber & Castro-Ruiz, *Measurement events relative to temporal quantum reference frames*, arXiv:2308.10967 v4, §§2–4, especially Eqs. (2)–(23). [3](https://arxiv.org/abs/2308.10967)

## 1. Bounded-band clock: normalization and resolution

Set \(\hbar=1\) in the derivation. The source clock has

\[
\mathcal H_C=L^2([-E,E]),\qquad
\hat H_C=\int_{-E}^{E}de\,e|e\rangle\langle e|,
\]

and generalized time states

\[
|\phi_t\rangle_C=\frac{1}{\sqrt{2E}}\int_{-E}^{E}de\,e^{-iet}|e\rangle_C.
\]

Directly integrating gives

\[
\langle\phi_t|\phi_{t'}\rangle_C
=\frac{1}{2E}\int_{-E}^{E}de\,e^{ie(t-t')}
=\frac{\sin(E(t-t'))}{E(t-t')}.
\]

The covariant POVM density is \(\hat\phi_t=|\phi_t\rangle\langle\phi_t|\), with normalization \(N_C=E/\pi\):

\[
N_C\int_{\mathbb R}dt\,|\phi_t\rangle\langle\phi_t|=I_C,
\qquad
N_C\langle\phi_t|\phi_{t'}\rangle_C
=\frac{\sin(E(t-t'))}{\pi(t-t')}.
\]

The first nonzero-separation zero is \(|t-t'|=\pi/E\) (restore \(\pi\hbar/E\)). It is a feature of this covariant time-state overlap, not a universal clock-error bound. Operational error still requires a normalized clock packet, a readout, and a chosen distance or decision task.

## 2. TO baseline: constraint, relational observables, and order resource

For the TO model the free constraint is

\[
(\hat H_C+\hat H_S)|\Psi\rangle=0.
\]

For a system operator \(\hat F_S\), the source constructs its constraint-invariant relational extension by a group twirl. In the ideal-clock notation it is

\[
\hat F_{CS}(\tau)=\int_{\mathbb R}dt\,
 e^{-it\hat H_C}|\tau\rangle\langle\tau|_C e^{it\hat H_C}
 \otimes e^{-it\hat H_S}\hat F_S e^{it\hat H_S}.
\]

For projectors \(\Pi_S^k,\Pi_S^q\) and an initial state \(|\psi_0\rangle_S\), the ideal-clock two-measurement probability is

\[
P_{TO}(k,q|\tau_1,\tau_2)
=\left\|\Pi_S^q e^{-i(\tau_2-\tau_1)\hat H_S}
  \Pi_S^k e^{-i\tau_1\hat H_S}|\psi_0\rangle\right\|^2.
\]

For a finite-spectrum clock the source restricts the physical system support to
\(\sigma(\hat H_S)\cap(-[-E,E])\); within that allowed support its TO relational evolution remains unitary. The crucial protocol resource is that the experimenter externally supplies which invariant operation is applied and in what order. The clock’s finite bandwidth does not itself select that order. The source describes TO and PM as different operational event models, even though their predictions agree in the ideal-clock regime.

## 3. PM model and the exact non-ideal response kernel

The PM construction puts the measurement interaction into the constraint, with an ancilla \(A\):

\[
\left(\hat H_C+\hat H_S+N_C\int dt\,
 |\phi_t\rangle\langle\phi_t|_C\otimes\hat K_{SA}(t)\right)|\Phi\rangle_{CSA}=0.
\]

Conditioning on the clock POVM gives \(|\psi(t)\rangle_{SA}=\langle\phi_t|_C|\Phi\rangle_{CSA}\). The source derives

\[
i\frac{d}{dt}|\psi(t)\rangle_{SA}
=\hat H_S|\psi(t)\rangle_{SA}
+N_C\int dt'\,\langle\phi_t|\phi_{t'}\rangle_C
  \hat K_{SA}(t')|\psi(t')\rangle_{SA}.
\]

For the symmetric band, define the response function

\[
F(t)=N_C\int_{-\infty}^{t}dt'\,\langle\phi_{t'}|\phi_0\rangle_C.
\]

Using the overlap above and \(N_C=E/\pi\), set \(u=Et'\) to obtain the explicit result

\[
F(t)=\frac12+\frac{1}{\pi}\operatorname{Si}(Et),
\qquad
\operatorname{Si}(x)=\int_0^x du\,\frac{\sin u}{u}.
\]

Thus \(F(0)=1/2\), \(F(t)\to0\) as \(Et\to-\infty\), and \(F(t)\to1\) as \(Et\to+\infty\). In the ideal limit it approaches \(\Theta(t)\) away from the step. The source’s perturbative solution is a time-nonlocal Dyson-type series weighted by products of \(F\); it becomes the usual time-ordered unitary evolution when \(F\to\Theta\). The source also cautions that a time-nonlocal equation alone does not establish nonunitary evolution; unitarity must be checked for the actual channel/protocol.

## 4. Finite-duration analytic correction: smooth compact pulse

Use a finite-duration envelope that vanishes at both endpoints rather than relying only on a delta pulse. Let

\[
\hat K_{SA}(s)=k(s)\hat K,\qquad \hat H_S=0,\qquad \hat K=\hat K^\dagger,\quad \hat K^2=I,
\]

with the dimensionless pulse area \(\gamma\), duration \(T>0\), and profile

\[
k(s)=\frac{\gamma}{T}w(s/T),\qquad
w(x)=\begin{cases}
C\exp\!\left[-\frac{1}{(x+1)(-x)}\right],&-1<x<0,\\
0,&\text{otherwise,}
\end{cases}
\]

where \(C^{-1}\) is the integral of the displayed exponential over \((-1,0)\). This standard compact bump is \(C^\infty\), vanishes with all derivatives at the endpoints, is symmetric about \(x=-1/2\), and obeys
\(W:=\int_{-1}^{0}w(x)dx=1\) and \(B:=\int_{-1}^{0}(-x)w(x)dx=1/2\).
At the end of the pulse \(t=0\), the first two terms of the source’s PM series are

\[
\begin{aligned}
A_1&=\int ds\,k(s)F(-s),\\
A_2&=\int ds_2\,ds_1\,k(s_2)k(s_1)F(-s_2)F(s_2-s_1),\\
U(0)&=I-iA_1\hat K-A_2\hat K^2+O(\gamma^3).
\end{aligned}
\]

For \(\epsilon=ET\ll1\), use \(F(z)=\tfrac12+Ez/\pi+O((Ez)^3)\). Changing variables \(s_j=Tx_j\) gives

\[
A_1=\gamma\left(\frac{W}{2}+\frac{\epsilon B}{\pi}+O(\epsilon^3)\right)
=\gamma\left(\frac12+\frac{\epsilon}{2\pi}+O(\epsilon^3)\right),
\]

and, since
\(F(-Tx_2)F(T(x_2-x_1))=\tfrac14-\epsilon x_1/(2\pi)+O(\epsilon^2)\),

\[
A_2=\gamma^2\left(\frac{W^2}{4}+\frac{\epsilon WB}{2\pi}+O(\epsilon^2)\right)
=\gamma^2\left(\frac14+\frac{\epsilon}{4\pi}+O(\epsilon^2)\right).
\]

Therefore the leading conditional-map norm defect is

\[
U^\dagger U-I=(A_1^2-2A_2)I+O(\gamma^3)
=-\frac{\gamma^2}{4}I+O(\gamma^2\epsilon^2,\gamma^3).
\]

This is a finite-duration analytic correction for a smooth, bounded pulse when \(|\gamma|\ll1\) and the clock bandwidth cannot resolve the pulse (\(ET\ll1\)). The envelope is genuinely smooth and has compact support. It is still only the conditioned channel expansion: the outcome probabilities require the declared ancilla/readout instrument and the PM clock-conditioned denominator below. The approximation is not a numerical fit, and no parameter sweep was run.

## 5. Exact formal pulse check: nonunitarity and its scope

For an analytic stress test, the source sets \(\hat H_S=0\) and takes the formal sharp interaction \(\hat K_{SA}(t)=\hat K_{SA}\delta(t-\tau)\). Its closed-form conditioned map is

\[
U_F=I-F(t-\tau)\frac{i\hat K_{SA}}{I+i\hat K_{SA}/2}.
\]

To check this result’s nonunitarity, take any Hermitian coupling whose eigenvalues are \(\pm\kappa\). On either eigenvector, with \(F=F(t-\tau)\),

\[
u_\pm=\frac{1\pm i\kappa(1/2-F)}{1\pm i\kappa/2},
\qquad
|u_\pm|^2=\frac{1+\kappa^2(1/2-F)^2}{1+\kappa^2/4}.
\]

Hence

\[
U_F^\dagger U_F-I
=-\frac{\kappa^2F(1-F)}{1+\kappa^2/4}\,I,
\]

which is strictly negative for \(0<F<1\) and \(\kappa\ne0\), and vanishes at the endpoints \(F=0,1\). For example, at the pulse center \(t=\tau\), the symmetric-band kernel gives \(F=1/2\), so the defect is \(-\kappa^2/(4+\kappa^2)\,I\). This reproduces a direct finite-band diagnostic from the source’s formal sharp-pulse solution.

**Scope warning:** a delta-function interaction is not a finite-duration, finite-resource apparatus that a bounded-band clock can trigger sharply. The source itself requires taking the ideal-clock limit before the instantaneous-interaction limit, so the exact delta-pulse formula must not be substituted for the finite-pulse calculation above. It remains an analytic diagnostic of the PM kernel, not evidence of fundamental nonunitarity for every protocol. The smooth-pulse result is finite-duration but perturbative and does not by itself complete the operational benchmark. PM probabilities also use the clock-conditioned denominator

\[
P(a|\tau)_t=
\frac{\langle\Phi|\hat E_C(t)\otimes I_S\otimes|a\rangle\langle a|_A|\Phi\rangle}
 {\langle\Phi|\hat E_C(t)\otimes I_S\otimes I_A|\Phi\rangle},
\qquad \hat E_C(t)=N_C|\phi_t\rangle\langle\phi_t|,
\]

so a nonunitary conditioned map is not a probability-normalization failure; the denominator must be retained and checked for the declared outcome instrument.

## 6. Operational comparison and outstanding pass conditions

- **TO event:** the external experimenter applies constraint-invariant observables and supplies their order; the clock label does not provide that control resource.
- **PM event:** an internal observer uses the clock reading to trigger a system–ancilla interaction; the clock/interaction dynamics supplies event ordering.
- Finite-clock TO and PM predictions need not agree because these are distinct protocols. A nonzero order cross-term is a protocol statistic, not by itself a violation of a causal inequality. The source does not establish a causal-inequality violation.
- The discrete-time PM construction is conditional on its orthogonal sampled clock states and chosen unitary update; it is not evidence for fundamental discreteness.

## 7. Same-task two-outcome meter: normalized probabilities and channel comparison

This is a deliberately narrow one-event benchmark: estimate the conserved system observable \(Z\) with a calibrated ancilla meter at relational reading \(0\). It isolates clock-triggering effects; it is not a multi-event ordering witness.

To match the source’s exactly tractable PM case, set \(H_S=H_A=0\) for this one-event pulse benchmark and take \(K=Z\otimes Y_A\), with \(K=K^\dagger\), \(K^2=I\). This isolates the bounded-clock trigger response rather than free system evolution. Use the same relational input for both protocols,

\[
\rho_S=\frac12\left(I+\frac{X+Z}{\sqrt2}\right),\qquad
\rho_A=|0_z\rangle\langle0_z|,
\]

and read the ancilla in the \(X_A\) basis, \(\Pi_a^X=|a_x\rangle\langle a_x|\), \(a=\pm1\). Thus \(\mu:=\operatorname{Tr}(Z\rho_S)=1/\sqrt2\). The clock energy required by the free constraint is zero, which lies inside \([-E,E]\). With \(\alpha^2=(1+1/\sqrt2)/2\) and \(\beta^2=(1-1/\sqrt2)/2\), a formal free-constraint representative is \( |0\rangle_C\otimes(\alpha|+z\rangle_S+\beta|-z\rangle_S)\otimes|0_z\rangle_A\); the group-averaging norm for this state is checked in §9. It is a pre-pulse state, not the physical solution of the interaction-modified PM constraint.

### TO: externally scheduled, ideal-calibrated instrument

For the target calibrated meter, use \(V_\gamma=e^{-i\gamma Z\otimes Y_A}\). The TO experimenter applies the constraint-invariant meter operation and supplies the event schedule. Since \(K\) commutes with the free constraint generator, its relational twirl is time-independent for this task; the clock does not trigger the operation. The outcome Kraus operators are

\[
M_a^{TO}=\langle a_x|V_\gamma|0_z\rangle
=\frac{1}{\sqrt2}(\cos\gamma\,I+a\sin\gamma\,Z).
\]

They obey \(\sum_a(M_a^{TO})^\dagger M_a^{TO}=I\), giving

\[
P_{TO}(a)=\operatorname{Tr}(M_a^{TO}\rho_S(M_a^{TO})^\dagger)
=\frac12(1+a\sin(2\gamma)\mu),\qquad \sum_aP_{TO}(a)=1.
\]

The nonselective system channel is

\[
\mathcal E_{TO}(\rho)=\cos^2\gamma\,\rho+\sin^2\gamma\,Z\rho Z.
\]

This instrument defines the same ideal-meter calibration used for PM: in the ideal-clock limit the finite pulse of area \(\gamma\) generates \(V_\gamma\). It is a benchmark extension to a weak ancilla instrument, not a claim that the source paper used this specific meter.

### PM: clock-triggered smooth pulse and its conditional instrument

Use the compact bump profile of §4, \(K_{SA}(s)=\gamma T^{-1}w(s/T)K\), and evaluate the clock-conditioned state at \(t=0\). In the source probability rule, the clock factor \(N_C\) cancels between numerator and denominator, leaving the normalized SA state \(|\psi(0)\rangle/\|\psi(0)\|\). Through second order in \(\gamma\), define \(c=1-A_2\), \(d=A_1\), and \(q=c^2+d^2\). The ancilla-outcome Kraus operators induced by the truncated PM map are

\[
\widetilde M_a^{PM}=\langle a_x|U(0)|0_z\rangle
=\frac{1}{\sqrt2}(cI+a d Z)+O(\gamma^3).
\]

For the second-order truncated map,

\[
\sum_a(\widetilde M_a^{PM})^\dagger\widetilde M_a^{PM}=qI,
\qquad
q=c^2+d^2=1-2A_2+A_1^2+A_2^2
=1-\frac{\gamma^2}{4}+O(\gamma^2\epsilon^2,\gamma^3).
\]

Thus the clock-conditioned, normalized outcome probabilities are

\[
P_{PM}(a|t=0)
=\frac{\operatorname{Tr}(\widetilde M_a^{PM}\rho_S(\widetilde M_a^{PM})^\dagger)}{q}
=\frac12\left(1+a\eta_{PM}\mu\right)+O(\gamma^3),
\qquad
\eta_{PM}:=\frac{2cd}{q}.
\]

The displayed truncated probabilities sum to one exactly; they are nonnegative because \(2|cd|\le c^2+d^2=q\) and \(|\mu|\le1\). For the fixed input \(\mu=1/\sqrt2\), this gives \(P_{PM}(a|0)=\tfrac12(1+a\eta_{PM}/\sqrt2)+O(\gamma^3)\). Using §4,

\[
\eta_{PM}=\gamma\left(1+\frac{\epsilon}{\pi}+O(\epsilon^3)\right)+O(\gamma^3),
\qquad
\eta_{TO}=\sin(2\gamma)=2\gamma+O(\gamma^3).
\]

In the unresolved-pulse regime \(ET=\epsilon\ll1\), the PM pointer contrast is therefore approximately half the TO calibrated contrast at leading order in \(\gamma\). This is a protocol-specific result for the stated smooth pulse and conserved observable, not a universal clock error.

After summing over pointer outcomes and conditioning on the clock reading, the PM system channel through this order is

\[
\mathcal E_{PM}^{cond}(\rho)
=\frac{c^2\rho+d^2Z\rho Z}{q}+O(\gamma^3)
=\rho+\gamma^2\left(\frac14+\frac{\epsilon}{2\pi}+O(\epsilon^2)\right)(Z\rho Z-\rho)+O(\gamma^3).
\]

Comparison with TO yields the channel-level difference

\[
(\mathcal E_{PM}^{cond}-\mathcal E_{TO})(\rho)
=\gamma^2\left(-\frac34+\frac{\epsilon}{2\pi}+O(\epsilon^2)\right)(Z\rho Z-\rho)+O(\gamma^3).
\]

For fixed smooth \(w\), taking \(E\to\infty\) first gives \(A_1\to\gamma\), \(A_2\to\gamma^2/2\) at this order, and the full source series becomes the time-ordered unitary \(V_\gamma\); consequently the PM instrument recovers the TO calibration. This limit keeps \(T>0\) fixed and does not exchange the ideal-clock and sharp-pulse limits.

**Scope of this calculation.** It supplies normalized outcomes and a channel correction for one same-task, one-event meter in the source’s conditional-state framework. The free pre-pulse norm, interacting group average on an absolutely continuous scattering test space, conditional-rule normalization, source-reconstructed incoming state/nonzero readout support, Kato representative/physical-norm identification, and special-meter physical-fiber gauge consistency are checked in §§8–13; §14 extends the construction to a noncommuting sequential benchmark, and §15 supplies its exact scalar normalization and physical-fiber POVMs.


## 8. All-orders PM meter form and convergence for the chosen pulse

The same commuting meter admits an all-orders treatment without numerically solving the memory equation. Let \(J_0(t)=1\), set \(s_{n+1}=t\), and define the scalar coefficients from the source series (Eq. 17) by

\[
J_n(t)=\int_{[-T,0]^n}\prod_{j=1}^n ds_j\,k(s_j)
\prod_{j=1}^n F(s_{j+1}-s_j),\qquad n\ge1.
\]

Because \(F\) is bounded for the symmetric finite band, let \(F_{\max}:=\sup_x|F(x)|<\infty\). The nonnegative normalized bump has \(\int|k(s)|ds=|\gamma|\), so

\[
|J_n(t)|\le(F_{\max}|\gamma|)^n.
\]

Consequently the source series converges absolutely and uniformly in \(t\) whenever \(r:=F_{\max}|\gamma|<1\):
For \(n\ge1\), the outermost factor in \(J_n(t)\) is \(F(t-s_n)\), with \(s_n\in[-T,0]\). Hence, defining \(m_t:=\sup_{x\le t+T}|F(x)|\to0\) as \(t\to-\infty\),

\[
|J_n(t)|\le |\gamma|^nF_{\max}^{n-1}m_t,
\qquad
\|U(t)-I\|\le\frac{|\gamma|m_t}{1-r}\longrightarrow0.
\]

Thus the normalized \(|\psi_0\rangle_{SA}\) in the source series is precisely the incoming clock-conditioned state for this compact pulse, not the output at \(t=0\).


\[
U(t)=\sum_{n=0}^{\infty}(-i)^nJ_n(t)K^n
=a(t)I-i b(t)K,
\]

where \(a(t)=\sum_{m\ge0}(-1)^mJ_{2m}(t)\) and \(b(t)=\sum_{m\ge0}(-1)^mJ_{2m+1}(t)\) are real. Since \(K=K^\dagger\), \(K^2=I\),

\[
U(t)^\dagger U(t)=q(t)I,\qquad q(t):=a(t)^2+b(t)^2.
\]

For \(r<1/2\), \(|a(t)-1|\le r^2/(1-r^2)<1/3\), hence \(q(t)>4/9\) uniformly. This both gives a nonzero clock-conditioned denominator in the declared weak-coupling domain and bounds the full series, for this one-pulse model only.

The exact convergent-series ancilla Kraus operators and normalized PM outcome law are therefore

\[
\widetilde M_{\xi}^{PM}(t)=\frac{1}{\sqrt2}\big(a(t)I+\xi b(t)Z\big),\qquad
P_{PM}(\xi|t)=\frac12\left(1+\xi\frac{2a(t)b(t)}{q(t)}\mu\right),
\quad \xi=\pm1.
\]

They sum to one and are nonnegative because \(2|ab|\le a^2+b^2=q\). The exact normalized nonselective channel for this special meter is

\[
\mathcal E_{PM,t}^{cond}(\rho)
=\frac{a(t)^2\rho+b(t)^2Z\rho Z}{q(t)},
\]

which is completely positive and trace preserving. The map \(U\) itself is generally nonunitary; here its norm defect is scalar, so conditioning normalizes it to a unitary on S+A before pointer readout. This special simplification must not be generalized to arbitrary interactions.

At \(t=0\), \(J_1=A_1\), \(J_2=A_2\), \(a=1-A_2+O(\gamma^4)\), and \(b=A_1+O(\gamma^3)\), recovering §7’s perturbative probabilities and channel. The source reconstruction in §10 matches the incoming conditional state and gives nonzero readout support; §12 identifies it with the incoming Kato representative and induced physical norm, and §13 gives its physical-fiber gauge-consistent readout.

## 9. Free pre-pulse group average and exact probability normalization

A concrete free-constraint input can be specified as the incoming reference for the interacting construction in §10. Let \(C_0=H_C+H_S+H_A=H_C\), with \(H_S=H_A=0\), on the clock space \(L^2([-E,E])\). Choose a test packet \(g\in C_c^\infty((-E,E))\), normalized in \(L^2\), with nonzero value \(g_0=g(0)\). For the pure system input in §7, write \(|\chi\rangle=\alpha|+z\rangle+\beta|-z\rangle\) and \(|f\rangle=|g\rangle_C|\chi\rangle_S|0_z\rangle_A\).

Use the explicitly declared group-averaging convention

\[
\eta(f)=\int_{\mathbb R}d\lambda\,e^{-i\lambda C_0}|f\rangle,
\qquad
\langle\eta(f)|\eta(h)\rangle_{phys}=2\pi\langle f|\delta(C_0)|h\rangle.
\]

For test vectors with smooth compactly supported energy components \(f_j(e)\) in a basis of the four-dimensional S+A space, the induced form is

\[
\langle f|\delta(C_0)|h\rangle
=\sum_{j=1}^{4}\overline{f_j(0)}h_j(0).
\]

It is finite and positive semidefinite, and the group-average integral converges on this test space because its matrix coefficients are Fourier transforms of smooth compactly supported functions. Quotienting the null vectors gives the stated free physical sector. For the chosen input, the induced norm is

\[
\|\eta(f)\|_{phys}^2
=2\pi|g(0)|^2\langle\chi|\chi\rangle
=2\pi|g_0|^2>0.
\]

The associated generalized-energy representative is proportional to \(g_0|0\rangle_C\otimes|\chi\rangle_S\otimes|0_z\rangle_A\). Since \(\langle\phi_t|0\rangle=(2E)^{-1/2}\), conditioning gives the same \(|\chi\rangle_S|0_z\rangle_A\) up to a common factor at every clock reading. This verifies a positive, finite physical norm and the chosen relational input for the **free pre-pulse constraint** under the stated rigging-map convention. Section 10 constructs the interacting group average abstractly; §12 identifies its incoming physical vector with the source-reconstructed conditional state.

Two further exact probability checks are available. In TO, the chosen \(M_a^{TO}\) and pointer effects preserve the free constraint: \([M_a^{TO},H_S+H_A]=0\), and \(\sum_a(M_a^{TO})^\dagger M_a^{TO}=I\). In PM, for any state representative \(|\Phi\rangle\) on which the source’s probability-rule matrix elements are defined and whose clock-conditioned denominator is positive, the source rule

\[
P_{PM}(a|t)=
\frac{\langle\Phi|E_C(t)\otimes I_S\otimes\Pi_a^X|\Phi\rangle}
 {\langle\Phi|E_C(t)\otimes I_S\otimes I_A|\Phi\rangle}
\]

is nonnegative and normalized: \(E_C(t)\ge0\), \(\Pi_a^X\ge0\), and \(\sum_a\Pi_a^X=I_A\), so summing the numerators gives the denominator. This proves normalization of the stipulated conditional probability rule for any interacting physical state with positive denominator. It does not prove positive clock-readout support for the specific calibrated rigging-map vector, nor covariance of the full readout instrument under the interaction-modified constraint.

## 10. Interaction-modified constraint: self-adjointness, zero spectrum, and rigging map

For this finite-band, finite-duration benchmark, the full PM constraint in Eq. (15) is a concrete bounded operator. On \(\mathcal H_C\otimes\mathcal H_{SA}\), write

\[
V_C=N_C\int_{-T}^{0}ds\,k(s)|\phi_s\rangle\langle\phi_s|,
\qquad
C_{PM}=H_C\otimes I_{SA}+V_C\otimes K.
\]

The clock states are normalized, so each rank-one projector has trace norm one. The integral is a trace-class Bochner integral and

\[
\|V_C\|_1\le N_C\int_{-T}^{0}|k(s)|ds=N_C|\gamma|.
\]

Thus \(V_C\) is bounded, compact, and self-adjoint; with bounded \(H_C\) and finite-dimensional \(S+A\), \(C_{PM}\) is self-adjoint on the whole kinematical Hilbert space. Moreover, zero lies in its essential spectrum. To see this, choose normalized clock wavefunctions \(\xi_n(e)\) supported in \([-\delta_n,\delta_n]\), where \(\delta_n\downarrow0\), and a fixed normalized \(|v\rangle_{SA}\). Then \(x_n=|\xi_n\rangle\otimes|v\rangle\) is weakly null, \(\|H_C\xi_n\|\le\delta_n\), and compactness gives \(\|V_C\xi_n\|\to0\). Hence \(\|C_{PM}x_n\|\to0\); the Weyl criterion places \(0\) in the essential spectrum.

Because \(C_{PM}-C_0=V_C\otimes K\) is trace class, the Kato–Rosenblum theorem gives complete wave operators and unitary equivalence of the absolutely continuous (a.c.) parts of these self-adjoint operators (Pushnitski & Volberg, Theorem 1.1; [source](https://arxiv.org/html/1211.6694)). Here \(C_0=H_C\otimes I_{SA}\) is purely a.c. on \([-E,E]\). Let \(W_\pm\) be either wave operator, defined using the group parameter (not a physical clock time), and take the test space

\[
\mathcal T_\pm=W_\pm\big(C_c^\infty((-E,E))\otimes\mathbb C^4\big).
\]

The intertwining relation carries the free test-space group average to the interacting constraint:

\[
\langle W_\pm f|e^{-i\lambda C_{PM}}|W_\pm h\rangle
=\langle f|e^{-i\lambda C_0}|h\rangle.
\]

The right-hand side is a rapidly decaying Fourier transform, so the rigging-map integral converges on this scattering test space, with

\[
\langle\eta_{PM}(W_\pm f)|\eta_{PM}(W_\pm h)\rangle_{phys}
=2\pi\langle f|\delta(C_0)|h\rangle
=2\pi\sum_{j=1}^{4}\overline{f_j(0)}h_j(0).
\]

Thus an interacting group-averaged physical sector with a positive semidefinite induced form is available on the a.c. scattering test space; quotienting its zero-norm vectors gives the physical fiber at constraint value zero. The following reconstruction subsection supplies the conditional state and denominator; §12 identifies that reconstructed state with this Kato representative and computes its induced physical norm, and §13 gives the special meter’s physical-fiber readout observable.

### Conditional-state reconstruction and nonzero readout support

The convergent solution \(|\psi(t)\rangle=U(t)|\psi_0\rangle\) is the source’s PM solution with the incoming boundary just established. Hausmann et al., Appendix E.2, Eqs. (91)–(96) ([source](https://arxiv.org/html/2308.10967v4#A5)), reconstruct the corresponding distributional state as

\[
|\Phi_{PM}\rangle=N_C\int_{\mathbb R}dt\,|\phi_t\rangle_C\otimes|\psi(t)\rangle_{SA},
\]

and show that it satisfies the interaction-modified constraint and obeys \({}_C\langle\phi_t|\Phi_{PM}\rangle=|\psi(t)\rangle\). For the present weak-coupling domain, the source probability-rule denominator at the pulse end is therefore

\[
D(0)=\langle\Phi_{PM}|E_C(0)\otimes I_{SA}|\Phi_{PM}\rangle
=N_C\|\psi(0)\|^2=N_Cq(0)\|\psi_0\|^2>\frac49N_C\|\psi_0\|^2>0.
\]

This closes the incoming conditional-state match and nonzero readout support **within the source’s conditional-state reconstruction**; §12 identifies that reconstruction with the incoming Kato representative and gives its induced physical norm. The source’s Appendix F also leaves the exact relation between its PM conditional rule and the TO physical inner product open; the probability-ratio normalization alone does not settle that issue.

## 11. Clock-origin covariance of the finite-pulse readout

The PM readout is covariant under a common translation of the pulse centre and clock-reading label. For \(k_\tau(s)=k(s-\tau)\), define

\[
V_\tau=N_C\int ds\,k(s-\tau)|\phi_s\rangle\langle\phi_s|,
\qquad C_{PM,\tau}=H_C\otimes I_{SA}+V_\tau\otimes K.
\]

The clock POVM covariance \(|\phi_{s+\tau}\rangle=e^{-iH_C\tau}|\phi_s\rangle\) gives

\[
V_\tau=e^{-iH_C\tau}V_0e^{iH_C\tau},
\qquad C_{PM,\tau}=U_C(\tau)C_{PM,0}U_C(\tau)^\dagger,
\quad U_C(\tau)=e^{-iH_C\tau}.
\]

If \(|\Phi_0\rangle\) solves the zero-centred constraint, then \(|\Phi_\tau\rangle=U_C(\tau)|\Phi_0\rangle\) solves the translated one. Since \(U_C(\tau)^\dagger E_C(t+\tau)U_C(\tau)=E_C(t)\), the source conditional probability rule obeys

\[
P_\tau(a|t+\tau)=P_0(a|t)
\]

whenever the denominator is positive. Equivalently, the convergent-series coefficients depend on \(t-\tau\). This verifies clock-origin translation covariance of the chosen pulse/readout family. It is **not** a proof that the kinematical clock-conditioned effect \(E_C(t)\otimes\Pi_a^X\) itself commutes with \(C_{PM}\). Section 13 instead establishes the special meter’s gauge-consistent physical-fiber effect; the exact all-orders sequential gate is assessed separately.

## 12. Kato representative identification and induced physical norm

The Appendix E.2 reconstructed state can now be identified with an incoming state selected by the Kato scattering construction. Use the spectral projectors

\[
P_\kappa=\frac{I+\kappa K}{2},\qquad \kappa=\pm1.
\]

Since \(K^2=I\), the interaction block on \(\operatorname{ran}P_\kappa\) is

\[
C_\kappa=H_C+\kappa V_C,
\]

and \(C_\kappa-H_C\) is trace class. Let \(W_-^{(\kappa)}\) denote the Møller wave operator in the incoming convention

\[
W_-^{(\kappa)}=\operatorname*{s-lim}_{\sigma\to-\infty}
 e^{i\sigma C_\kappa}e^{-i\sigma H_C}P_{\rm ac}(H_C).
\]

The clock spectral kets \(\{|e\rangle\}_{e\in[-E,E]}\) are delta-normalized. At the constraint value zero, set

\[
c_E:=\langle\phi_t|0\rangle=(2E)^{-1/2},
\qquad
|0,\psi_0;\mathrm{in}\rangle
:=\sum_{\kappa=\pm1}W_-^{(\kappa)}
 \big(|0\rangle\otimes P_\kappa\psi_0\big),
\]

where the last action is understood through the standard generalized spectral/Lippmann–Schwinger representative of the wave operator. This prescription selects the state that asymptotes to the free constraint state \(|0\rangle\otimes\psi_0\) before the pulse.

Write \(R_{H_C}(z)=(H_C-z)^{-1}\). The boundary-value identity is

\[
\begin{aligned}
\langle\phi_t|R_{H_C}(0+i0)|\phi_s\rangle
&=\frac{1}{2E}\int_{-E}^{E}de\,\frac{e^{ie(t-s)}}{e-i0}\\
&=\frac{i\pi}{E}\left[\frac12+\frac{1}{\pi}\operatorname{Si}(E(t-s))\right]
=iN_C^{-1}F(t-s).
\end{aligned}
\]

Using the incoming Lippmann–Schwinger representative for the full constraint,

\[
|\Psi_{\rm in}\rangle
=|0\rangle\otimes\psi_0
-\big(R_{H_C}(0+i0)\otimes I_{SA}\big)(V_C\otimes K)|\Psi_{\rm in}\rangle,
\]

define \(X(t):=\langle\phi_t|\Psi_{\rm in}\rangle\). Substitution of \(V_C=N_C\int ds\,k(s)|\phi_s\rangle\langle\phi_s|\) and the resolvent identity gives

\[
\begin{aligned}
X(t)
&=c_E\psi_0
-N_C\int ds\,k(s)\,
\langle\phi_t|R_{H_C}(0+i0)|\phi_s\rangle\,KX(s)\\
&=c_E\left[\psi_0-i\int ds\,k(s)F(t-s)K\frac{X(s)}{c_E}\right].
\end{aligned}
\]

Thus \(y(t)=X(t)/c_E\) obeys the same incoming integral equation as the source conditional solution \(\psi(t)\) in §8. In the weak-coupling domain \(r=F_{\max}|\gamma|<1\), that equation’s integral operator is a contraction for the uniform norm, so its solution is unique for fixed incoming \(\psi_0\). Consequently

\[
\langle\phi_t|0,\psi_0;\mathrm{in}\rangle=c_E\psi(t)
\]

for the convergent PM solution already constructed.

For a free test packet \(f=|g\rangle\otimes|\psi_0\rangle\), with \(g\in C_c^\infty((-E,E))\), \(g(0)\ne0\), and \(\psi_0\in\mathbb C^4\), intertwining gives

\[
\eta_{PM}(W_-f)=2\pi g(0)|0,\psi_0;\mathrm{in}\rangle,
\qquad
\langle\phi_t|\eta_{PM}(W_-f)\rangle
=2\pi g(0)c_E\,\psi(t).
\]

The normalized rigging-map state

\[
\widetilde\Phi_{PM}
:=\frac{1}{2\pi g(0)c_E}\eta_{PM}(W_-f)
\]

therefore has conditional overlap \(\psi(t)\). It coincides with the source reconstruction \(\Phi_{PM}=N_C\int dt\,|\phi_t\rangle\otimes|\psi(t)\rangle\): their difference has vanishing clock-conditioned overlap and no free \(e=0\) component; its Lippmann–Schwinger equation is homogeneous, and \(V_C\) couples only through \(\langle\phi_s|\cdot\rangle\), so the difference vanishes. Hence the source reconstruction is not an additional state prescription. Up to the fixed source normalization, it is the incoming Kato rigging-map representative.

The induced physical norm from §10 is

\[
\|\eta_{PM}(W_-f)\|_{\rm phys}^2
=2\pi|g(0)|^2\,\|\psi_0\|^2.
\]

Since \(c_E^2=(2E)^{-1}\),

\[
\|\Phi_{PM}\|_{\rm phys}^2
=\frac{2\pi|g(0)|^2\|\psi_0\|^2}
 {|2\pi g(0)c_E|^2}
=\frac{1}{2\pi c_E^2}\|\psi_0\|^2
=N_C\|\psi_0\|^2.
\]

Thus the interacting source state has a finite, positive norm under the stated rigging-map convention. Moreover, at the pulse end,

\[
\frac{D(0)}{\|\Phi_{PM}\|_{\rm phys}^2}
=\frac{N_Cq(0)\|\psi_0\|^2}{N_C\|\psi_0\|^2}
=q(0)>\frac49
\]

for \(r<1/2\). This upgrades the nonzero readout-support check from an unnormalized distributional statement to a normalized statement in the induced physical inner product.

This construction concerns the a.c. incoming channel at the interior constraint value zero. The finite-rank perturbation can in principle create discrete eigenvalues outside the clock band, but those spectral components do not contribute to the zero-energy group average used here. The identification does **not** make the fixed kinematical effect \(E_C(t)\otimes\Pi_a^X\) constraint-commuting. Section 13 instead exhibits the gauge-consistent physical-fiber effect that reproduces the conditional ratio for the special meter; §14 treats the noncommuting sequential benchmark through its first order-sensitive term, leaving only its all-orders fiber check open.

## 13. Physical-fiber readout observable and gauge consistency

The Kato identification in §12 supplies a concrete zero-constraint physical fiber for this one-pulse model: incoming data are \(\psi_0\in\mathbb C^4\), and the induced norm of the reconstructed state is \(N_C\|\psi_0\|^2\). The conditional probability ratio can therefore be represented as an ordinary Born rule on that fiber without identifying the bare kinematical effect with a constraint-commuting operator.

Let \(\widehat\psi_0=\psi_0/\|\psi_0\|\). For the fixed ancilla preparation \(|0_z\rangle_A\), the exact pointer Kraus operators of §8 give the system effects

\[
\mathsf F_{\xi,t}
:=\frac{(\widetilde M_\xi^{PM}(t))^\dagger\widetilde M_\xi^{PM}(t)}{q(t)}
=\frac12\left[I_S+\xi\frac{2a(t)b(t)}{q(t)}Z_S\right],
\qquad \xi=\pm1.
\]

They are positive because \(2|a(t)b(t)|\le q(t)\), and

\[
\mathsf F_{+,t}+\mathsf F_{-,t}=I_S,
\qquad q(t)>\frac49\quad(r<1/2).
\]

On the normalized incoming physical data,

\[
\operatorname{Tr}(\rho_S\mathsf F_{\xi,t})
=\frac12\left(1+\xi\frac{2a(t)b(t)}{q(t)}\mu\right)
=P_{PM}(\xi|t).
\]

Thus the PM conditional ratio is exactly the Born expectation of a state-independent linear POVM on the physical zero-energy fiber. The fixed test packet \(g\) cancels from the ratio by §12; clock-origin covariance in §11 gives the correspondingly shifted effect for a shifted pulse. On the quotient physical fiber the constraint is zero, so these fiber effects trivially commute with the reduced constraint. This closes the gauge-consistency check **for the declared special meter**, whose conditioned propagation satisfies \(U(t)^\dagger U(t)=q(t)I\).

This result should not be confused with commutation of the bare conditional effect before reduction. In fact

\[
[C_{PM},E_C(t)\otimes\Pi_\xi^X]
=[H_C,E_C(t)]\otimes\Pi_\xi^X
+N_C\int ds\,k(s)
 [|\phi_s\rangle\langle\phi_s|,|\phi_t\rangle\langle\phi_t|]
 \otimes K\Pi_\xi^X,
\]

which is generally nonzero. The physical-fiber POVM above is the relational extension whose statistics reproduce the source ratio; it does not make \(E_C(t)\otimes\Pi_\xi^X\) itself constraint-commuting.

The argument is special to this one-pulse instrument. For arbitrary interactions with several noncommuting coupling operators, \(U^\dagger U\) need not be scalar, so the clock-conditioned denominator can depend on the incoming state. Sections 14–15 nevertheless show that the declared anticommuting two-pulse benchmark retains exact scalar normalization and admits state-independent physical-fiber effects.

## 14. Noncommuting two-pulse benchmark and order witness

The final analytic gate for the current WP1-A task is a sequential task with two noncommuting couplings. Keep \(H_S=0\) and enlarge the ancilla to two qubits \(A_1,A_2\), prepared as \(|0_z0_z\rangle\). Set

\[
K_1=Z_S\otimes Y_{A_1}\otimes I_{A_2},
\qquad
K_2=X_S\otimes I_{A_1}\otimes Y_{A_2}.
\]

Each operator is Hermitian and squares to one, and they anticommute:

\[
K_1^2=K_2^2=I,
\qquad
\{K_1,K_2\}=0.
\]

Let \(A\) denote an early pulse slot and \(B\) a later pulse slot, with \(\operatorname{supp}\bar k_A\) strictly before \(\operatorname{supp}\bar k_B\). Take \(k_j(s)=\gamma_j\bar k_j(s)\) for \(j=A,B\), where each \(\bar k_j\) is a nonnegative normalized compact bump. Sequence \(12\) applies \(K_1\) at \(A\) and \(K_2\) at \(B\); sequence \(21\) applies \(K_2\) at \(A\) and \(K_1\) at \(B\). Thus

\[
\widetilde K_{SA}^{12}(s)=k_A(s)K_1+k_B(s)K_2,
\qquad
\widetilde K_{SA}^{21}(s)=k_A(s)K_2+k_B(s)K_1.
\]

The pulse envelopes, slot positions, ancilla preparations, and readout calibration are held fixed. Both supports precede the reading time \(t_R=0\), with a positive gap after slot \(B\).

### Convergence, physical state, and readout support

Because \(\|K_1\|=\|K_2\|=1\) and \(\int|k_j(s)|ds=|\gamma_j|\) for \(j=A,B\), the \(n\)-th source-series term is bounded by

\[
(F_{\max}\Gamma)^n,\qquad \Gamma:=|\gamma_A|+|\gamma_B|.
\]

Hence the conditional solution converges uniformly for \(r:=F_{\max}\Gamma<1\). Both profiles have compact support, so the same incoming-boundary estimate as §8 gives \(U(t)\to I\) and identifies \(\psi_0\) as the incoming state. The clock-side perturbation is a finite sum of rank-one Bochner integrals, with

\[
\left\|N_C\int ds\,[k_A(s)|\phi_s\rangle\langle\phi_s|\otimes K^{(A)}
+k_B(s)|\phi_s\rangle\langle\phi_s|\otimes K^{(B)}]\right\|_1
\le N_C\Gamma,
\]

where \(K^{(A)},K^{(B)}\) are the two operators assigned by the selected sequence.

It is therefore trace class. The Kato–Rosenblum construction and the unique-contraction argument of §12 apply unchanged, with \(K\psi(s)\) replaced by \(\widetilde K_{SA}(s)\psi(s)\). The source-reconstructed sequential state is again the incoming Kato representative, with induced norm \(N_C\|\psi_0\|^2\).

For \(r<1/2\), \(\|U-I\|\le r/(1-r)<1\), so \(U\) is invertible and

\[
D(t)\ge N_C\left(1-\frac{r}{1-r}\right)^2\|\psi_0\|^2
=N_C\left(\frac{1-2r}{1-r}\right)^2\|\psi_0\|^2>0.
\]

Thus the two-pulse conditional rule has positive support in the stated weak-coupling domain even though \(U^\dagger U\) need not be scalar.

### Second-order joint Kraus operators

At \(t_R=0\), define the real slot coefficients

\[
\beta_A=\int ds\,k_A(s)F(-s),\qquad
\beta_B=\int ds\,k_B(s)F(-s),
\]

and

\[
\lambda_{jl}=\iint ds\,ds'\,
k_j(s)k_l(s')F(-s)F(s-s'),
\qquad j,l\in\{A,B\}.
\]

For sequence \(12\),

\[
U_{12}(0)=I-i(\beta_AK_1+\beta_BK_2)
-\sum_{j,l\in\{A,B\}}\lambda_{jl}K^{(j)}K^{(l)}+O(\Gamma^3),
\]

where \(K^{(A)}=K_1\) and \(K^{(B)}=K_2\). The anticommutation relation gives

\[
\lambda_{AB}K_1K_2+\lambda_{BA}K_2K_1=i(\lambda_{AB}-\lambda_{BA})Y
\]

in the two-record amplitude. Define

\[
c=1-\lambda_{AA}-\lambda_{BB},
\qquad d=\lambda_{AB}-\lambda_{BA}.
\]

For \(X\)-basis records \(a_1,a_2=\pm1\) at the early and late slots, respectively, the sequence Kraus operators are

\[
L_{a_1a_2}^{(12)}
=\frac12\left[cI+a_1\beta_AZ+a_2\beta_BX+i\,a_1a_2d\,Y\right]+O(\Gamma^3),
\]

\[
L_{a_1a_2}^{(21)}
=\frac12\left[cI+a_1\beta_AX+a_2\beta_BZ-i\,a_1a_2d\,Y\right]+O(\Gamma^3).
\]

Because \(K_1\) and \(K_2\) anticommute, the clock-conditioned denominator is scalar through this order and is the same for the two sequences:

\[
q_{\rm seq}
=1+\beta_A^2+\beta_B^2-2(\lambda_{AA}+\lambda_{BB})+O(\Gamma^3).
\]

Let \(x\) and \(z\) be the \(X_S\) and \(Z_S\) components of the incoming system Bloch vector. Tracing the Kraus products against \(\rho_S\) gives

\[
P_{PM}^{12}(a_1,a_2)-P_{PM}^{21}(a_1,a_2)
=\frac{1}{2q_{\rm seq}}\Big[
(z-x)c(a_1\beta_A-a_2\beta_B)
+(x-z)d(a_2\beta_A+a_1\beta_B)
\Big]+O(\Gamma^4).
\]

The first term is a slot-calibration effect; the second is the noncommuting order cross term. To isolate the latter at the retained analytical order, choose calibrated equal effective pulse areas

\[
\beta_A=\beta_B=\beta
\]

(the nominal slot areas are adjusted by the factor \(\int\bar k_jF(-s)\)) and take \(a_1=a_2=+1\). The calibration term then vanishes exactly at this order, leaving

\[
W_{++}^{\rm seq}
:=\left|P_{PM}^{12}(+,+)-P_{PM}^{21}(+,+)\right|
=\frac{\sqrt2\,|\beta d|}{q_{\rm seq}}+O(\Gamma^4)
\]

for the Bloch input

\[
\rho_S=\frac12\left(I+\frac{X_S-Z_S}{\sqrt2}\right),
\qquad x=\frac1{\sqrt2},\quad z=-\frac1{\sqrt2}.
\]

Write \(d=\beta^2\Delta_v\) with \(\Delta_v=v_{AB}-v_{BA}\), where the \(v\)'s are the profile-normalized cross integrals. Then

\[
W_{++}^{\rm seq}
=\sqrt2\,|\beta|^3|\Delta_v|
+O(\Gamma^4).
\]

When the gap between pulse supports is \(G\gg E^{-1}\), and slot \(B\) ends a distance \(R\gg E^{-1}\) before the reading, the large-argument asymptotics of \(\operatorname{Si}\) give

\[
|\beta|=|\gamma|\left[1+O\!\left(\frac1{ER}\right)\right],
\qquad
|\Delta_v|=1+O\!\left(\frac1{EG},\frac1{ER}\right).
\]

Consequently

\[
W_{++}^{\rm seq}
=\sqrt2\,|\gamma|^3
+O\!\left(\gamma^4,\frac{|\gamma|^3}{EG},\frac{|\gamma|^3}{ER}\right),
\]

which is nonzero for sufficiently small \(|\gamma|>0\) and sufficiently large pulse/readout separations relative to the clock resolution \(E^{-1}\). In the ideal-clock limit at fixed smooth profiles, \(\beta\to\gamma\) and \((v_{AB},v_{BA})\to(0,1)\), and the PM law recovers the externally scheduled TO sequence with the same witness at this order.

This witness compares the statistics of two explicitly declared event orders. It is an order-sensitivity statistic, not evidence by itself of indefinite causal order or of a causal-inequality violation. In TO, event order remains an external scheduler resource; in PM, it is supplied by the placement of constraint interactions relative to the clock readout. Both resources are logged separately.

**Exact closure of this benchmark.** The state reconstruction, incoming Kato representative, positive support, and scalar normalization are exact in the weak-coupling domain. Section 15 uses the anticommuting couplings’ quaternionic reduction to construct exact all-orders physical-fiber POVMs for both event sequences; the second-order formulas above are used only to evaluate the order witness. This closes the sequential gauge gate for the declared model.

## 15. Exact sequential normalization and physical-fiber POVM

For the two anticommuting couplings in §14, the apparent all-orders obstruction has an exact algebraic resolution. Write \(A=K_1\), \(B=K_2\), and \(C=AB\). Their multiplication rules are

\[
A^2=B^2=I,\qquad AB=-BA=C,\qquad C^2=-I,
\]

and \(A\), \(B\), and \(C\) are pairwise anticommuting. Consequently, every word in \(A\) and \(B\) reduces to one of \(I,A,B,C\): an odd-length word reduces to \(A\) or \(B\), while an even-length word reduces to \(I\) or \(C\).

In the source PM series, an odd word carries the pure imaginary prefactor \((-i)^n\), while an even word carries the real prefactor \((-i)^n\). Therefore the uniformly convergent sequential map has the real quaternionic form

\[
U(t)=x(t)I+i\big(y(t)A+z(t)B\big)+w(t)C,
\qquad x,y,z,w\in\mathbb R.
\]

Using the multiplication table, all mixed terms in \(U^\dagger U\) cancel pairwise, leaving

\[
U(t)^\dagger U(t)=q(t)I,
\qquad
q(t)=x(t)^2+y(t)^2+z(t)^2+w(t)^2.
\]

Thus the sequential conditional propagation is also scalar times a unitary for the anticommuting Pauli couplings used here; this is exact, not a second-order approximation.

Coefficient bounds follow from the word reduction and the series bound \(r=F_{\max}\Gamma<1\):

\[
|x(t)-1|\le\sum_{\substack{n\ge2\\n\ {\rm even}}}r^n
=\frac{r^2}{1-r^2},
\]

so for \(r<1/\sqrt2\),

\[
q(t)\ge x(t)^2
\ge \left(1-\frac{r^2}{1-r^2}\right)^2
=\left(\frac{1-2r^2}{1-r^2}\right)^2.
\]

In the previously used domain \(r<1/2\), this gives \(q(t)>4/9\), independently of the incoming state. This is the exact sequential analogue of the one-pulse denominator bound.

Let

\[
L_{a_1a_2,t}^{(\omega)}
:=\langle a_1,a_2|_X U_\omega(t)|0_z0_z\rangle,
\qquad \omega\in\{12,21\}.
\]

Since \(U_\omega^\dagger U_\omega=q_\omega I\), define physical-fiber effects

\[
\mathsf F_{a_1a_2,t}^{(\omega)}
:=\frac{(L_{a_1a_2,t}^{(\omega)})^\dagger L_{a_1a_2,t}^{(\omega)}}{q_\omega(t)}.
\]

They are positive and satisfy

\[
\sum_{a_1,a_2=\pm1}\mathsf F_{a_1a_2,t}^{(\omega)}
=I_S.
\]

Moreover,

\[
\operatorname{Tr}\!\left(\rho_S\mathsf F_{a_1a_2,t}^{(\omega)}\right)
=\frac{\operatorname{Tr}\!\left[(L_{a_1a_2,t}^{(\omega)})^\dagger
 L_{a_1a_2,t}^{(\omega)}\rho_S\right]}{q_\omega(t)}
=P_{PM}^{(\omega)}(a_1,a_2|t).
\]

Hence both sequential conditional laws are Born expectations of state-independent linear POVMs on the physical zero-constraint fiber. Together with the Kato identification and induced norm from §12, this closes the exact all-orders sequential gauge check for the declared anticommuting benchmark. The order witness in §14 is therefore a comparison of two Born probability laws, not a postselected or state-dependent rule. This closure is special to the declared anticommuting pair; merely noncommuting couplings without this quaternionic reduction would require a separate normalization analysis.

**WP1-A analytic gate: passed in its declared domain.** The smooth-pulse same-task instrument and normalized second-order TO/PM probabilities and channel correction are recorded in §7. The free pre-pulse norm, interacting rigging map on the absolutely continuous scattering test space, weak-coupling PM-series convergence, and conditional-rule positivity/normalization are checked. The incoming conditional-state match, nonzero normalized readout support, Kato representative identification, induced physical norm, clock-origin covariance, and special-meter physical-fiber gauge consistency are established. The noncommuting two-pulse benchmark has exact weak-coupling state construction/support, exact scalar sequential normalization, state-independent physical-fiber POVMs, and an analytic order witness through the first order where order sensitivity appears. The result is restricted to the bounded continuous-band clock, compact supported pulses, anticommuting Pauli couplings, and the stated weak-coupling/supported-slot domain. It is a model-specific Level A analytic benchmark, not a Level B/C closure or an indefinite-causal-order claim. No numerical campaign was run or authorized.
