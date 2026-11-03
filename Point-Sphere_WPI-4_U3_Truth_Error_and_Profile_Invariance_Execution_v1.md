# WPI-4 U3 — Truth, Error, and Profile-Invariance Execution v1
## Execution of the actual-correct, actual-error, and carrier-renaming controls

**Frozen candidate:** `Weak_Simplicity_Positive_Immanent_Explicit_Infinite_Constructive_Entry_Packet_v4.md`  
**Required predecessors:** WPI-4 U0 and U1/U2 execution records.  
**Scope:** U3.a, U3.b, and U3.c only. U4 is not executed.  
**Result:** The fixed canonical correct and error controls pass. The carrier-renaming invariance control fails because canonical-only actualization makes a permitted noncanonical representative nonactual and reverses its correct verdict to error.

---

## 0. Frozen truth/error rules

For a presentation node \(j\) hosted by \(b_{p,i}\), the candidate declares:

\[
\mathsf{Anchor}(s_{p,j},a_q)
\iff
\mathsf{ActPres}(s_{p,j})
\land q=p
\land\mathsf{ActArt}(a_p)
\land\mathsf{RefTag}(s_{p,j},\mathsf{HostArt})
\land\mathsf{Profiles}(a_p,b_{p,i}).
\tag{ANCHOR2}
\]

\[
\mathsf{Matches}(\lambda,a_p,b_{p,i})
\iff
\lambda\approx_{\rm WPI4}\mathsf{ObsProj}(p,i).
\tag{MATCH}
\]

\[
\mathsf{Fit}(s_{p,j},\lambda)
\iff
\mathsf{Claims}(s_{p,j},\lambda)
\land\exists i[
\mathsf{PresOf}(s_{p,j},b_{p,i})
\land\mathsf{Anchor}(s_{p,j},a_p)
\land\mathsf{Matches}(\lambda,a_p,b_{p,i})].
\tag{FIT2}
\]

\[
\mathsf{Correct}(s,\lambda)
\iff
\mathsf{Claims}(s,\lambda)\land\mathsf{Fit}(s,\lambda),
\qquad
\mathsf{Error}(s,\lambda)
\iff
\mathsf{Claims}(s,\lambda)\land\neg\mathsf{Fit}(s,\lambda).
\tag{TE2}
\]

The actualization rule retains the canonical-only condition:

\[
a_p\in A_H
\Longrightarrow
p=\operatorname{can}(p).
\tag{CAN-ACT}
\]

Equivalence, however, identifies all carrier-renamed records with the same canonical code:

\[
p\approx_{\rm WPI4}q
\iff
\operatorname{can}(p)=\operatorname{can}(q).
\tag{EQ2}
\]

U3.c requires that corresponding presentation/claim verdicts survive this permitted equivalence.

---

## 1. U3.a — actual correct control

The fixed positive fixture has:

\[
q^+=\mathsf{ObsProj}(p_0,3),
\qquad
\mathsf{Content}(s^+,q^+),
\qquad
\mathsf{ObsProj}(p^+,3)=q^+.
\tag{Positive-Fixture}
\]

The outer code \(p^+\) is canonical, rooted, admissible, and has no structural predecessor. It therefore enters at the first articulation stage; its entity and presentation enter at subsequent finite stages:

\[
\mathsf{ActArt}(a_{p^+}),
\qquad
\mathsf{FiniteEnt}(b_{p^+,3}),
\qquad
\mathsf{ActPres}(s^+).
\tag{Positive-Actual}
\]

Its reference field is the fixed tag \(\mathsf{HostArt}\), and the relevant articulation profiles the host entity. Therefore:

\[
\mathsf{Anchor}(s^+,a_{p^+}).
\tag{Positive-Anchor}
\]

Since \(q^+\approx_{\rm WPI4}\mathsf{ObsProj}(p^+,3)\), match and fit hold:

\[
\mathsf{Matches}(q^+,a_{p^+},b_{p^+,3}),
\qquad
\mathsf{Fit}(s^+,q^+).
\tag{Positive-Fit}
\]

Thus:

\[
\boxed{
\mathsf{ActPres}(s^+)
\land
\mathsf{Correct}(s^+,q^+).
}
\tag{U3a-Pass}
\]

---

## 2. U3.b — actual error control

The negative fixture \(p^-\) is canonical, rooted, admissible, and predecessor-free. Its corresponding presentation \(s^-\) is therefore actual:

\[
\mathsf{ActPres}(s^-).
\tag{Negative-Actual}
\]

Its content \(\lambda^-\) is the fixed observational code in which a retained \(Pr\)-node is altered to \(Ev\). It remains \(\mathsf{ObsWF}\), but is not equivalent to the host observation projection:

\[
\lambda^-
\not\approx_{\rm WPI4}
\mathsf{ObsProj}(p^-,3).
\tag{Negative-Mismatch}
\]

The actual anchor remains intact, but the match conjunct fails. Hence:

\[
\neg\mathsf{Fit}(s^-,\lambda^-),
\tag{Negative-NoFit}
\]

and:

\[
\boxed{
\mathsf{ActPres}(s^-)
\land
\mathsf{Error}(s^-,\lambda^-).
}
\tag{U3b-Pass}
\]

Neither tokenhood nor actual anchoring forces correctness.

---

## 3. U3.c — carrier-renaming invariance control

### 3.1 A permitted noncanonical representative

Take the canonical positive record \(p^+\), and apply a nonidentity carrier-slot renaming \(\sigma\) preserving all tags, edges, formality labels, intervals, content structure, and the \(\mathsf{HostArt}\) tag. Let the resulting finite code be:

\[
q^\sigma=\sigma(p^+).
\tag{Renamed-Code}
\]

Choose \(\sigma\) whose encoding is not lexicographically least among this finite carrier-renaming orbit. Then:

\[
q^\sigma\neq\operatorname{can}(q^\sigma)=p^+,
\qquad
q^\sigma\approx_{\rm WPI4}p^+.
\tag{Equivalent-Noncanonical}
\]

The grammar and rootedness conditions are invariant under the permitted renaming:

\[
\mathsf{Cand}(q^\sigma),
\qquad
\mathsf{RootedAtG}(q^\sigma).
\tag{Renamed-Structure}
\]

### 3.2 Canonical-only actualization destroys the required invariance

The frozen \((\mathrm{CAN\text{-}ACT})\) condition gives, for every closure stage \(H\):

\[
q^\sigma\neq\operatorname{can}(q^\sigma)
\Longrightarrow
a_{q^\sigma}\notin A_H.
\tag{Renamed-NoEntry}
\]

Consequently:

\[
a_{q^\sigma}\notin H_\omega,
\qquad
\neg\mathsf{ActArt}(a_{q^\sigma}).
\tag{Renamed-Nonactual}
\]

The corresponding entity and presentation cannot be actual:

\[
\neg\mathsf{FiniteEnt}(b_{q^\sigma,\sigma(3)}),
\qquad
\neg\mathsf{ActPres}(s_{q^\sigma,\sigma(4)}).
\tag{Renamed-NoPresentation}
\]

Thus the required anchor fails even if the local structural match is carried over by \(\sigma\):

\[
\neg\mathsf{Anchor}(s_{q^\sigma,\sigma(4)},a_{q^\sigma}).
\tag{Renamed-NoAnchor}
\]

Let \(\lambda^\sigma=\sigma(q^+)\) be the corresponding renamed claim content. The presentation constructor still has that content, so it claims \(\lambda^\sigma\), but it cannot fit it because the actual-anchor conjunct is false:

\[
\mathsf{Claims}(s_{q^\sigma,\sigma(4)},\lambda^\sigma)
\land
\neg\mathsf{Fit}(s_{q^\sigma,\sigma(4)},\lambda^\sigma).
\tag{Renamed-NoFit}
\]

The candidate's own total error definition therefore yields:

\[
\mathsf{Error}(s_{q^\sigma,\sigma(4)},\lambda^\sigma).
\tag{Renamed-Error}
\]

But the equivalent canonical presentation was correct:

\[
\mathsf{Correct}(s^+,q^+).
\tag{Canonical-Correct}
\]

Hence a permitted carrier renaming changes both actual-presentation status and the truth/error verdict:

\[
\boxed{
q^\sigma\approx_{\rm WPI4}p^+
\quad\land\quad
\mathsf{Correct}(s^+,q^+)
\quad\land\quad
\mathsf{Error}(s_{q^\sigma,\sigma(4)},\lambda^\sigma).
}
\tag{Invariance-Counterexample}
\]

This contradicts the frozen U3.c pass condition. Canonicalization can choose a representative for a quotient only if the actual-articulation and presentation predicates are then quotient-invariant. WPI-4 instead actualizes only the chosen syntactic representative while its declared equivalence treats the unchosen representative as profile-equivalent.

---

## 4. U3 result and expiry

\[
\boxed{
\begin{aligned}
&\mathsf{U3.aResult}(F_{\rm WPI\text{-}4})=\mathsf{Pass},\\
&\mathsf{U3.bResult}(F_{\rm WPI\text{-}4})=\mathsf{Pass},\\
&\mathsf{U3.cResult}(F_{\rm WPI\text{-}4})=\mathsf{Fail}_{\rm profile\ invariance}.
\end{aligned}
}
\tag{U3-Components}
\]

Because the truth/error bridge must pass all three controls:

\[
\boxed{
\mathsf{U3Result}(F_{\rm WPI\text{-}4})
=
\mathsf{Fail}_{\rm profile\ invariance}.
}
\tag{U3-Fail}
\]

The packet's expiry rule therefore closes its truth/error bridge claim:

\[
\boxed{
\neg\mathsf{TruthErrorBridgeClosed}(F_{\rm WPI\text{-}4}).
}
\tag{Truth-Expiry}
\]

No U4 phenomenal, normative, or physical test is authorized. Identifying constructor terms across the declared equivalence, actualizing every representative, or changing the equivalence relation would be a new candidate, not a repair of WPI-4.

This restricted failure does not refute weak simplicity, positive-immanent differentiation, explicit-infinite constructive regimes, or strict pure-negation.
