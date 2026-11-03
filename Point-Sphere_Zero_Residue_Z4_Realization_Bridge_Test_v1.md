# Point–Sphere Zero-Residue Search — Z4 Realization-Bridge Test v1

**Protocol parent:** `Point-Sphere_Zero_Residue_Whole_Reality_Search_Protocol_v1.md`  
**Prerequisites:** Z1 (SHA-256 `3f67848a3c2ed4b3d836019185ae1cfe008fb48a94ad55f740459fb713058c59`), Z2 (SHA-256 `923b49ce4ed3ace9779d2edfe3bb9c52b8d692a4935ce720e4bed3ba15137abb`), and Z3 (SHA-256 `053feb47563609bfe42ef361954ca07f531dcc0575076859d13780656f605f5a`).  
**Execution position:** Z4 only.  
**Status:** Executed restricted realization-bridge test. The frozen candidate architecture fails this Z4 test through an empty-diagram countercase. This is not a no-go for plenitude, modal monism, Appearance, or whole-reality frameworks generally.

---

## 1. Z4 bridge obligation

The Z3 manifestation result deliberately did not license real finite modes. The fixed Z4 obligation is a faithful realization bridge:

\[
\mathsf{AA}_G(m,c,d)
\to
\exists!x[
\mathsf{Realizes}(x,m,c,d)
\land
\mathsf{ActualFiniteMode}(x)
].
\tag{MR}
\]

For this bridge to count as realization rather than an unrelated extra existence claim, it must satisfy the following minimal faithfulness condition:

\[
\mathsf{Realizes}(x,m,c,d)
\to
\mathsf{ProfileOf}(x,c,d)\simeq_1m.
\tag{Faith}
\]

The right side permits only profile-conservative re-encoding. It does not permit unrecorded content to be inserted into a finite mode merely because an actual articulation has been stipulated.

A positive finite profile requires a nonempty typed profile support and at least one nonstructural positive relation literal:

\[
\begin{aligned}
\mathsf{PosProf}(m)\iff{}&
V_m\cap
(\mathbf P\cup\mathbf E\cup\mathbf K\cup\mathbf F\cup\mathbf O\cup\mathbf N\cup\mathbf I)
\neq\varnothing\\
&\land
\exists A\in L_m\,[
A\text{ is a positive relation literal other than }\mathsf{Dep}_0\text{ or }\mathsf{Part}_0
].
\end{aligned}
\tag{PP}
\]

Thus the relevant Z4 requirement is:

\[
\mathsf{AA}_G(m,c,d)
\to
\exists!x[
\mathsf{Realizes}(x,m,c,d)
\land
\mathsf{ActualFiniteMode}(x)
\land
\mathsf{PosProf}(m)
].
\tag{MR+}
\]

This is not a demand for independent substancehood, external time, cross-articulation injectivity, agency, causal efficacy, or subjecthood. It is the minimal requirement that a claimed finite mode be realized from a positive finite profile rather than from an empty syntactic placeholder.

---

## 2. Empty candidate countercase

Z1 permits the empty finite signed diagram:

\[
m_{\varnothing}:=\langle\varnothing,\varnothing\rangle.
\tag{E1}
\]

It is well formed under the frozen Z1 rule \((\mathrm{WF})\). Its existential translation is the tautology:

\[
\llbracket m_{\varnothing}\rrbracket=\top.
\tag{E2}
\]

Hence:

\[
\mathsf{Coh}_{T_{\rm base}}(m_{\varnothing}).
\tag{E3}
\]

Its active scope is empty:

\[
\mathsf{ActSig}(m_{\varnothing})=\varnothing.
\tag{E4}
\]

Therefore the determinacy condition holds vacuously:

\[
\mathsf{Det}(m_{\varnothing}).
\tag{E5}
\]

So the frozen Z1 candidate rule gives:

\[
\boxed{
\mathsf{CandMode}(m_{\varnothing}).
}
\tag{E6}
\]

By Z2, its singleton formal context is admissible:

\[
c_{\varnothing}:=
\langle
\{m_{\varnothing}\},
\operatorname{id}_{\varnothing}
\rangle,
\qquad
\mathsf{CandCtx}(c_{\varnothing})
land
\mathsf{At}_0(m_{\varnothing},c_{\varnothing}).
\tag{E7}
\]

By the frozen Z3 plenitude postulate:

\[
\mathsf{MPlen}^{\rm fin}_G
\to
\exists d\,
\mathsf{AA}_G(m_{\varnothing},c_{\varnothing},d).
\tag{E8}
\]

But \((\mathrm{PP})\) fails:

\[
\neg\mathsf{PosProf}(m_{\varnothing}).
\tag{E9}
\]

Combining \((\mathrm{E8})\) and \((\mathrm{E9})\), the realization bridge \((\mathrm{MR+})\) fails for the empty candidate:

\[
\boxed{
\mathsf{MPlen}^{\rm fin}_G
\not\Rightarrow
\mathsf{MR+}
\quad\text{under the frozen Z1 candidate grammar.}
}
\tag{Z4-F}
\]

---

## 3. Why the countercase cannot be silently repaired here

Three apparent responses are unavailable in this protocol.

### 3.1 Exclude the empty diagram

Adding:

\[
V_m\neq\varnothing
\quad\text{or}\quad
\mathsf{PosProf}(m)
\]

to \(\mathsf{CandMode}\) would alter the frozen Z1 grammar after plenitude had been stated. It is a candidate-grammar amendment, not an execution of Z4.

### 3.2 Add unrecorded positive content to \(x\)

One might let \(x\) have a rich finite profile despite realizing \(m_{\varnothing}\). That violates faithfulness:

\[
\mathsf{ProfileOf}(x,c,d)\not\simeq_1m_{\varnothing}.
\]

The added content would be an undeclared actual-profile completion rule and a new selector/dependency item.

### 3.3 Treat an empty profile as a positive finite mode

This would empty “positive profile,” individuation, and difference-making of their stated role. In particular, it would not provide a profile that can bear finite experience, silence, disclosure, privation, agency, or causal structure.

---

## 4. Restricted conclusion

The result is not that finite modes are impossible, that actual articulations cannot be real modes, or that plenitude is false.

It is exactly:

\[
\boxed{
\text{The frozen finite grammar admits a vacuous candidate which restricted plenitude manifests,}\
\text{but which cannot satisfy the required faithful positive finite-mode realization bridge.}
}
\]

Therefore the candidate has not reached later gates:

\[
Z4\text{ failure}
\Rightarrow
\neg\text{execution of Z5, }\mathcal B_\Phi, Z6, Z7
\text{ in this protocol.}
\tag{Stop}
\]

Under the parent protocol’s stop rule, the correct classification is:

\[
\boxed{
\mathsf{Status}(\mathcal A_{\rm NP}^{\rm fin})=
\mathsf{Open\;with\;a\;restricted\;Z4\;failure}.
}
\tag{Result}
\]

No amendment, relaxed realization condition, modified candidate grammar, or successor limitation theory is permitted in this project. A distinct new protocol would be required to examine a nonempty-profile grammar or another candidate architecture.
