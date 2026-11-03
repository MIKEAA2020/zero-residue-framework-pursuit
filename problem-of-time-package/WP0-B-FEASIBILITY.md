# WP0-B feasibility dossier: JT+CFT York clock and a proposed second dynamical clock

**Status:** two WP0-B second-clock admissibility attempts are recorded and neither passes. The localized finite-band probe gate is written below; the CFT-internal repair gate in `WP0-B-CFT-INTERNAL-GATE.md` is a restricted uniqueness result for the tested free-scalar/Majorana mode class, not a model-wide uniqueness theorem. A different closed-Milne rolling-matter model has been separately specified as WP0-B₂ in `WP0-B2-ROLLING-MATTER.md`; it passes only action/constraint and rolling-branch kinematics, not full quantum admissibility. No entropy, algebra-type, or prediction comparison is made. This dossier uses the fixed-topology subregion construction of Blommaert–Chen only. It does not splice that model with the separate York-time wavefunction construction in arXiv:2505.19231.

**Base source:** Blommaert & Chen, *Time in gravitational subregions and in closed universes*, arXiv:2602.22153 v1, especially §§3–4 ([source](https://arxiv.org/html/2602.22153#S4)). The base model excludes topology-changing contributions and is nonperturbative in \(G_N\) within that fixed topology sector. It is not a background-independent fundamental completion: the AdS\(_2\) asymptotic/boundary data, topology, subregion definition, and conformal-matter state remain fixed structure.

## 1. Fixed base model and comparison contract

The fixed base model is:

- AdS\(_2\) JT gravity on a fixed topology;
- conformal matter in the declared state, with the source’s thermal/modular \(s\)-flow assumptions;
- one causal-diamond subregion \(\mathcal U\), fixed by boundary dilaton data and anchors;
- no topology-changing path-integral sectors;
- the York/extrinsic-curvature clock associated with conformal-time slices;
- the same physical state and physical inner product for every proposed clock reduction.

Blommaert–Chen parameterize the diamond phase space so that the conformal-time/slicing coordinate \(S\) is conjugate to a gravitational constraint. Their symplectic form has the announced block form ([Eq. 3.13](https://arxiv.org/html/2602.22153#S3.E13))

\[
\varpi=dK_{\rm grav}\wedge dS+dB\wedge dP,
\]

and for conformal matter their projected Einstein equation gives ([Eq. 4.5](https://arxiv.org/html/2602.22153#S4.E5))

\[
K_{\rm grav}+K_{\rm matter}=0.
\]

A second-clock comparison must preserve the action, topology, subregion, boundary dilaton, anchors, CFT state, normalization conventions, and target task. A boundary time or changed matter theory is an external control or a different model, not a second internal clock.

## 2. First candidate: localized probe clock

The first candidate investigated here is a localized relativistic probe clock \(Q\), coupled to the same JT geometry as a matter defect. It carries an internal WP1-type finite-band clock Hilbert space

\[
\mathcal H_Q=L^2([-E,E])\otimes\mathbb C^{d_{\rm int}},
\qquad
\operatorname{spec}(H_Q)\subset[-E,E],
\]

with the covariant finite-band time POVM used in WP1-A. This choice has a declared finite energy resource and a controlled time-state overlap. The remaining question is whether embedding it as dynamical matter yields a valid gravitational clock comparator.

The probe has worldline embedding \(X^\mu(\lambda)\), worldline momentum \(P_\mu(\lambda)\), lapse \(\mathcal N\), and internal wavepacket \(|\Pi\rangle\in\mathcal H_Q\). A first-quantized action is

\[
S_Q=\int d\lambda\left[
P_\mu\dot X^\mu+\langle\Pi|i\partial_\lambda|\Pi\rangle
-\mathcal N\,\mathcal H_Q
\right]+S_{Q,\rm bdy},
\]

with

\[
\mathcal H_Q=
\frac{g^{\mu\nu}(X)P_\mu P_\nu}{2M}+\frac{M}{2}
+H_Q+\lambda_X H_{\rm int}(X).
\]

Here \(M\) is the probe mass parameter, \(H_Q\) is the internal clock Hamiltonian, and \(H_{\rm int}(X)\) is a declared coupling/readout potential. The endpoint term \(S_{Q,\rm bdy}\) must fix the worldline reparametrization endpoints and internal canonical boundary conditions before this proposal is operationally complete.

The probe’s backreaction is represented by its localized stress tensor. In one consistent convention for the constraint above,

\[
T_Q^{\mu\nu}(x)=\int d\lambda\,\frac{1}{\mathcal N\sqrt{-g}}
\left[\frac{P^\mu P^\nu}{M}
-g^{\mu\nu}\big(H_Q+\lambda_XH_{\rm int}(X)\big)\right]
\delta^{(2)}(x-X(\lambda)).
\]

The sign of the localized potential term follows the convention chosen for \(\mathcal H_Q\); it must be fixed in the final action. What matters for admissibility is that \(Q\) carries stress energy and therefore changes the dilaton/constraint data; it cannot be treated as stress-free once the same combined constraint is required.

## 3. Complete candidate action

Let \(\Gamma\) be the fixed JT spacetime topology, with boundary data that define the diamond and its asymptotic/cutoff boundary. A candidate total action is

\[
S_{\rm tot}
=S_{\rm top}+S_{JT}+S_{\partial,\rm GHY}+S_{\rm ct}
+S_{\rm CFT}+S_Q,
\]

with a convention-independent topological term

\[
S_{\rm top}=\frac{\Phi_0}{16\pi G}
\left[\int_\Gamma d^2x\,\sqrt{-g}\,R
+\int_{\partial\Gamma}d\lambda\,\sqrt{|h|}\,2\mathcal K\right],
\]

and, up to the sign/detail conventions that must be fixed in a quantitative derivation,

\[
S_{JT}=\frac{1}{16\pi G}\int_\Gamma d^2x\,\sqrt{-g}\,\Phi(R+2),
\qquad
S_{\partial,\rm GHY}=\frac{1}{8\pi G}\int_{\partial\Gamma}d\lambda\,\sqrt{|h|}\,\Phi\mathcal K,
\]

and a renormalization counterterm \(S_{\rm ct}\) fixed by the chosen boundary/cutoff scheme. Here \(\mathcal K\) denotes extrinsic curvature in the GHY boundary term; it should not be confused with the York-clock label \(K\).

For \(c\) conformal scalar sectors one may use

\[
S_{\rm CFT}=-\frac12\sum_{i=1}^{c}\int_\Gamma d^2x\,\sqrt{-g}\,g^{\mu\nu}
\partial_\mu\chi_i\partial_\nu\chi_i
+S_{\rm anom}[g].
\]

The induced nonlocal term \(S_{\rm anom}\), normal ordering, and central-charge data must be specified whenever the matter stress tensor is quantized. The source’s subregion calculation uses conformal matter and its thermal \(s\)-flow state; changing that matter content or state changes the comparison object.

The subregion is fixed by the same boundary dilaton and anchor data as in the base model. Any entropy comparison would have to retain these data rather than compare a probe-corrected diamond with the uncorrected source diamond as if they were one geometry.

## 4. Combined constraint

With lapse/shift data \((N,Y)\), the smeared total constraint is

\[
\underline C[N,Y]
=
\underline C_{\rm grav}[N,Y]
+\underline C_{\rm CFT}[N,Y]
+\underline C_Q[N,Y],
\]

with

\[
\underline C_{\rm grav}[N,Y]
=\int_\Sigma d x\,\sqrt h\,N^\mu Y^\nu
\left(\nabla_\mu\nabla_\nu\Phi-g_{\mu\nu}\Box\Phi+g_{\mu\nu}\Phi\right),
\]

up to the convention for the nonsmearing term; the Blommaert–Chen formula for the CKV smearing is the relevant specialization. Matter contributions are

\[
\underline C_{\rm CFT}[N,Y]
=\int_\Sigma d x\,\sqrt h\,N^\mu Y^\nu\mathcal T_{\mu\nu}^{\rm CFT},
\]

where \(\mathcal T^{\rm CFT}\) includes the declared renormalization/anomaly prescription, and

\[
\underline C_Q[N,Y]
=\int_\Sigma d x\,\sqrt h\,N^\mu Y^\nu T_{\mu\nu}^{Q}.
\]

For the conformal-time vector \(\xi=\partial_s\) used by the source, \(N^\mu Y^\nu\) means the normal/normal and normal/tangential projections appropriate to the smearing. The specialized constraint would be

\[
\boxed{\ C_{s,\rm tot}
=K_{\rm grav}+K_{\rm CFT}+K_Q\approx 0\ }
\]

on physical states. A corresponding momentum/remainders constraint must also be retained if the candidate is formulated before the source’s minisuperspace reduction.

This is the **combined** constraint required for a fair clock comparison. The York/extrinsic-curvature clock is part of the gravitational canonical data. The probe Hamiltonian \(H_Q\) is not added as an unconstrained external Hamiltonian; it enters \(T_Q^{\mu\nu}\) and therefore shifts the physical constraint surface and can shift the phase-space measure and clock-conditioned state.

## 5. First-probe admissibility-gate assessment

| Gate | Status | Finding |
|---|---|---|
| 1. Complete action, canonical variables, boundary terms | **Partial / not passed** | The candidate total action and variables are recorded, but the worldline endpoint term, CFT anomalous action/normal ordering, and all dilaton/counterterm conventions are not yet fixed to one quantitative scheme. |
| 2. Combined constraint closure | **Not passed** | The formal total constraint is written. Closure with the CFT anomaly, localized probe stress tensor, and minisuperspace/CKV reduction has not been proved. The source’s simple \(K_{\rm grav}+K_{\rm matter}=0\) relation does not automatically survive a nonconformal localized clock. |
| 3. Probe-clock POVM validity on the model support | **Not passed** | The internal finite-band clock has a covariant POVM as a standalone WP1 model. Its relational transformation along the JT worldline, its allowed turning/interaction domain, and its validity on a nonzero physical-state sector have not been established. |
| 4. Nonzero common physical-state sector | **Not passed** | No simultaneous zero sector for \(C_{s,\rm tot}=0\) has been constructed that retains both York-slicing data and the probe clock’s support. |
| 5. Physical inner product and trace properties of both clock-dressed algebras | **Not passed** | Group averaging/Dirac quantization of the probe-corrected constraint has not been shown convergent or positive; the Q-dressed algebra and its trace are therefore undefined at this gate. |
| 6. Nonperturbative target | **Not passed** | A test-particle or \(G_N\to0\) treatment could neglect backreaction, but that is only a perturbative semiclassical simplification and does not satisfy the fixed-topology nonperturbative target. |

**First-probe decision outcome:** **no admissible comparator from this candidate.** This is a feasibility obstruction, not evidence for either clock independence or physical clock dependence. Consequently, no entropy functional, algebra intersection, or same-task prediction comparison is licensed by this candidate at present.

## 6. Repair history and remaining routes

### 6.1 Repair route 1 tested: CFT-internal clock

The CFT-internal route is analyzed in `WP0-B-CFT-INTERNAL-GATE.md`. It tests a Majorana two-level mode and a free-scalar positive-energy band in the same fixed diamond. The band’s standalone covariant POVM is exact, but the autonomous bounded clock does not survive as an admissible subsystem of the undeformed continuum CFT: the two-level projection is nonunitary on the absolutely continuous geometric flow, while the full bosonic band Fock sector loses the bounded spectrum. A hard one-particle/band truncation is a regulator or a different model, not the same source CFT. **Route 1 therefore passes no admissible comparator.** Its permissible positive classification is restricted uniqueness within this tested mode class, conditional on the admissibility criteria—not model-wide uniqueness. A rolling-matter WP0-B₂ scope is separately recorded in `WP0-B2-ROLLING-MATTER.md`; it is a different closed-Milne model and does not alter this WP0-B result.

### 6.2 Remaining admissibility attempts

The next feasibility work should choose one of the following routes and prove the stated item before any comparison:

1. **Rolling-matter WP0-B₂:** the closed-Milne scope in `WP0-B2-ROLLING-MATTER.md` passes only the action/constraint and positive-momentum rolling-branch kinematics. Its quantum group average, branch readout, and both clock-dressed traces must be checked before any comparison.
2. **Probe clock with exact backreaction:** retain the localized probe and derive the full JT+defect constraint algebra and physical inner product from first principles, including endpoint terms and renormalized defect stress. This is eligible for one bounded scoping attempt only; if it becomes a sustained perturbative or numerical effort, stop and record intractability.
3. **Modified-CFT or perturbative offshoot:** introduce a lattice/finite-mode/doubly holographic CFT or run only at \(G_N	o0\) as a clearly labeled WP0-B′ model. It must not be reported as the nonperturbative fixed-subregion WP0-B target.

## 7. Scope discipline

- This dossier does **not** combine Blommaert–Chen’s fixed-topology subregion geometry with equations from the separate York-time wavefunction paper.
- York conformal-time dressing is a relational-clock construction, but fixed topology and fixed boundary/subregion data mean it is not by itself a background-free fundamental resolution of time.
- The source’s bulk entropy conclusion depends on its York-clock algebra and the fact that the gauged CKV flow is a conformal rather than actual isometry. That is not yet a comparison between two independent clocks.
- The localized-probe and CFT-internal no-go outcomes are model-specific and may be removed by one of the remaining repair routes above, or by a clearly modified CFT/topology offshoot.
