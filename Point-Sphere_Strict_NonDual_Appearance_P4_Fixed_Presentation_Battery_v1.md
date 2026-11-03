# Point–Sphere Strict Non-Dual Appearance — P4 Fixed Presentation Battery v1

**Protocol parent:** `Point-Sphere_Strict_NonDual_Appearance_Presentation_Protocol_v1.md` (SHA-256 `88faa8ac4eea92e195ae5ce89e8fdafc39c1a48dac1bd863374f7bc7c60132aa`).  
**Prerequisites:** P1 (`37d7d91d1951a6c4578d167783c8520c78e910219d11eadd9d6bc9052b2e3867`), P2 (`5d4f6b7363de09024dbca94c897663fdb9a5944022ad627bcc122918f1912738`), and P3 (`b2dd9057376cf890662f3566df8e2bb42fd907c4135f8dab700fa5322537bd1f`).  
**Execution position:** Fixed six-case battery only.  
**Status:** Structural execution. No grammar, active-scope rule, plenitude rule, or presentation bridge has been changed. The results are structural classification results, not validation of consciousness, truth, prophetic revelation, horror, or a zero-residue framework.

---

## 1. Fixed grammar and shared support

All predicates retain the P1 meanings. In particular, the following are formal diagram labels only:

\[
\mathsf{Clear}_0,
\quad
\mathsf{Authenticates}_0,
\quad
\mathsf{Miraculous}_0,
\quad
\mathsf{Defeats}_0,
\quad
\mathsf{Harm}_0.
\]

They do not establish actual clear disclosure, authentication, miracle, deception, suffering, or historical prophecy.

All six cases use the frozen support:

\[
V_{\Box}=
\{\ell:\mathbf L,e:\mathbf E,c:\mathbf C,q:\mathbf Q,o:\mathbf O,i:\mathbf I,r:\mathbf R\}.
\]

The shared signed-literal base is:

\[
S_{\rm base}=
\{
\mathsf{Dep}_0(\ell,\mathsf g),
\neg\mathsf{Part}_0(\ell,\mathsf g),
\mathsf{Undergoes}_0(\ell,e,i),
\mathsf{Presents}_0(e,c),
\mathsf{Has}_0(\ell,q,i),
\mathsf{Observes}_0(\ell,o,i),
\mathsf{CountsFor}_0(\ell,r,i)
\}.
\tag{Base}
\]

For every compatible signed seed \(S\), define the frozen completion operation:

\[
\mathsf{CompDiag}(S):=
\left\langle
V_{\Box},
S\cup
\{\neg A:A\in\mathsf{Atom}_{\Sigma_{\rm pres}}(V_{\Box}),\ A\notin S,\ \neg A\notin S\}
\right\rangle.
\tag{CompDiag}
\]

No diagram has any positive or negative literals beyond those fixed by its seed plus this completion operation.

---

## 2. Fixed six diagrams

### B1. Ordinary presentation form

\[
S_{\rm ordinary}:=
S_{\rm base}\cup
\{\mathsf{Supports}_0(e,c)\},
\qquad
m_{\rm ordinary}:=\mathsf{CompDiag}(S_{\rm ordinary}).
\tag{Ord}
\]

### B2. Silent presentation form

\[
S_{\rm silent}:=
S_{\rm base}\cup
\{\neg\mathsf{Clear}_0(\ell,c,i),\neg\mathsf{Authenticates}_0(e,c)\},
\qquad
m_{\rm silent}:=\mathsf{CompDiag}(S_{\rm silent}).
\tag{Sil}
\]

### B3. Clear-disclosure presentation form

\[
S_{\rm clear}:=
S_{\rm base}\cup
\{\mathsf{Clear}_0(\ell,c,i),\mathsf{Authenticates}_0(e,c),\mathsf{Supports}_0(e,c)\},
\qquad
m_{\rm clear}:=\mathsf{CompDiag}(S_{\rm clear}).
\tag{Clr}
\]

### B4. Prophetic/miraculous presentation form

\[
\begin{aligned}
S_{\rm prophetic}:={}&
S_{\rm base}\cup
\{\mathsf{Clear}_0(\ell,c,i),\mathsf{Authenticates}_0(e,c),\\
&\mathsf{Supports}_0(e,c),\mathsf{Miraculous}_0(e)\},\\
&m_{\rm prophetic}:=\mathsf{CompDiag}(S_{\rm prophetic}).
\end{aligned}
\tag{Pro}
\]

### B5. Deceptive/error presentation form

\[
\begin{aligned}
S_{\rm deceptive}:={}&
S_{\rm base}\cup
\{\mathsf{Defeats}_0(e,c),\neg\mathsf{Supports}_0(e,c),\\
&\neg\mathsf{Clear}_0(\ell,c,i),\neg\mathsf{Authenticates}_0(e,c)\},\\
&m_{\rm deceptive}:=\mathsf{CompDiag}(S_{\rm deceptive}).
\end{aligned}
\tag{Dec}
\]

### B6. Horror/harm presentation form

\[
S_{\rm horror}:=
S_{\rm base}\cup
\{\mathsf{Harm}_0(\ell,e,i),\neg\mathsf{Clear}_0(\ell,c,i)\},
\qquad
m_{\rm horror}:=\mathsf{CompDiag}(S_{\rm horror}).
\tag{Hor}
\]

---

## 3. Structural classification method

For every battery diagram \(m\):

1. Coherence is established by a one-element-per-sort interpretation making exactly its positive seed atoms true and all remaining active atoms false.
2. This interpretation satisfies P1 axioms P1–P7: each seed includes the required \(\mathsf{Dep}_0\) and \(\neg\mathsf{Part}_0\); \(\mathsf{Harm}_0\) occurs only with \(\mathsf{Undergoes}_0\); \(\mathsf{Authenticates}_0\) occurs only with \(\mathsf{Presents}_0\) and \(\mathsf{Supports}_0\); and \(\mathsf{Supports}_0\) and \(\mathsf{Defeats}_0\) never co-occur positively.
3. Determinacy holds because \(\mathsf{CompDiag}\) assigns one sign to every active atom.
4. Experiential form holds because every seed includes:

\[
\mathsf{Undergoes}_0(\ell,e,i)
\land
\mathsf{Presents}_0(e,c).
\tag{EF}
\]

5. P2 plenitude supplies some \(c_m,d_m\) with \(\mathsf{AA}^{\rm pres}_G(m,c_m,d_m)\).
6. P3 supplies the structural presentation index:

\[
\mathsf{GenuinePresentation}^{\rm str}_G
(\phi_{[m]_{\simeq_{\rm pres}}},m,c_m,d_m).
\tag{GP}
\]

---

## 4. Fixed battery record

| Diagram | \(\mathsf{Coh}\) | \(\mathsf{Det}\) | \(\mathsf{CandMode}\) | \(\mathsf{AA}\) under MP | \(\mathsf{ExperientialForm}\) | Structural GP |
|---|---:|---:|---:|---:|---:|---:|
| \(m_{\rm ordinary}\) | Yes | Yes | Yes | Yes | Yes | Yes |
| \(m_{\rm silent}\) | Yes | Yes | Yes | Yes | Yes | Yes |
| \(m_{\rm clear}\) | Yes | Yes | Yes | Yes | Yes | Yes |
| \(m_{\rm prophetic}\) | Yes | Yes | Yes | Yes | Yes | Yes |
| \(m_{\rm deceptive}\) | Yes | Yes | Yes | Yes | Yes | Yes |
| \(m_{\rm horror}\) | Yes | Yes | Yes | Yes | Yes | Yes |

This record establishes only that all six frozen forms are admissible and structurally presented in the finite P1–P3 construction.

---

## 5. Adversarial reading and failure of stronger claims

The uniform structural result does not provide the required stronger bridges:

\[
\begin{array}{rcl}
\neg\mathsf{Clear}_0&\not\Rightarrow&\text{genuine experienced divine silence};\\
\mathsf{Clear}_0\land\mathsf{Authenticates}_0&\not\Rightarrow&\text{genuine unmistakable disclosure};\\
\mathsf{Miraculous}_0&\not\Rightarrow&\text{a miracle or a genuine prophet};\\
\mathsf{Defeats}_0&\not\Rightarrow&\text{truth, falsehood, bias, or error};\\
\mathsf{Harm}_0&\not\Rightarrow&\text{felt horror, suffering, evil, or a real sufferer.}
\end{array}
\tag{NoBridge}
\]

Moreover, the grammar permits all six diagram forms equally. P2 plenitude manifests each without a candidate-by-candidate selector. This removes no selector at the formal candidate-admission level only. It does not explain why the labels have the intended phenomenal or normative significance.

The battery therefore yields:

\[
\boxed{
\mathsf{BatteryResult}_{\rm P4}
=
\text{Structurally uniform; phenomenally and normatively unproved.}
}
\tag{P4-Result}
\]

No battery case may be repaired by changing its seed, the grammar, the presentation bridge, or the plenitude rule.

---

## 6. Fixed next task

The next permitted task is P5 only: a truth/error, privation, normativity, and evil audit using the unchanged P1–P4 structure. It may not introduce a real finite subject, independent witness, external time, a privileged scripture, a relaxed manifestation rule, or a revised presentation bridge.
