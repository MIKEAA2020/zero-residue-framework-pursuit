# WPI-5 U3 — Class Truth, Error, and Representation-Invariance Execution v1
## Execution of the actual-correct, actual-error, and raw-representation controls

**Frozen candidate:** `Weak_Simplicity_Quotient_Native_Productive_Constructive_Entry_Packet_v5.md`  
**Required predecessors:** WPI-5 U0, U1, and U2 execution records.  
**Scope:** U3.a, U3.b, and U3.c only. U4 is not executed.  
**Result:** The actual correct and actual error controls pass, and profile invariance passes because carrier-renamed raw records denote the same class-level bearer rather than distinct constructor tokens.

---

## 0. Frozen class truth/error rules

For a profile class \(\pi\), presentation slot class \(\upsilon\), host entity slot \(\epsilon\), and observational class \(o\):

\[
\mathsf{Anchor}(s_{\pi,\upsilon},a_\kappa)
\iff
\mathsf{ActPres}(s_{\pi,\upsilon})
\land\kappa=\pi
\land\mathsf{ActArt}(a_\pi)
\land\mathsf{RefTag}(s_{\pi,\upsilon},\mathsf{HostArt}).
\tag{Anchor}
\]

\[
\mathsf{Matches}(o,a_\pi,b_{\pi,\epsilon})
\iff
o=\mathsf{ObsProjProf}(\pi,\epsilon).
\tag{Match}
\]

\[
\mathsf{Fit}(s_{\pi,\upsilon},o)
\iff
\mathsf{Claims}(s_{\pi,\upsilon},o)
\land\exists\epsilon[
\mathsf{PresOf}(s_{\pi,\upsilon},b_{\pi,\epsilon})
\land\mathsf{Anchor}(s_{\pi,\upsilon},a_\pi)
\land\mathsf{Matches}(o,a_\pi,b_{\pi,\epsilon})].
\tag{Fit}
\]

\[
\mathsf{Correct}(s,o)
\iff
\mathsf{Claims}(s,o)\land\mathsf{Fit}(s,o),
\qquad
\mathsf{Error}(s,o)
\iff
\mathsf{Claims}(s,o)\land\neg\mathsf{Fit}(s,o).
\tag{Truth-Error}
\]

All arguments of these predicates are quotient objects. A raw code is not an argument of \(\mathsf{ActArt}\), \(\mathsf{ActPres}\), \(\mathsf{Correct}\), or \(\mathsf{Error}\).

---

## 1. U3.a — actual correct class control

Let:

\[
\pi^+=[p^+],
\qquad
\epsilon^+=[p^+,3],
\qquad
\upsilon^+=[p^+,4],
\qquad
o^+=[q^+].
\tag{Positive-Objects}
\]

The fixed fixture supplies:

\[
\mathsf{Content}(s_{\pi^+,\upsilon^+},o^+),
\qquad
o^+=\mathsf{ObsProjProf}(\pi^+,\epsilon^+).
\tag{Positive-Content}
\]

The positive profile class is candidate, rooted, and predecessor-free. Its entity and presentation satisfy the realized conditions established by the U0–U2 rule pattern:

\[
\mathsf{ActArt}(a_{\pi^+}),
\qquad
\mathsf{FiniteEnt}(b_{\pi^+,\epsilon^+}),
\qquad
\mathsf{ActPres}(s_{\pi^+,\upsilon^+}).
\tag{Positive-Actual}
\]

The \(\mathsf{HostArt}\) tag is fixed and the anchor holds:

\[
\mathsf{Anchor}(s_{\pi^+,\upsilon^+},a_{\pi^+}).
\tag{Positive-Anchor}
\]

Hence:

\[
\boxed{
\mathsf{ActPres}(s_{\pi^+,\upsilon^+})
\land
\mathsf{Correct}(s_{\pi^+,\upsilon^+},o^+).
}
\tag{U3a-Pass}
\]

---

## 2. U3.b — actual error class control

Let:

\[
\pi^-=[p^-],
qquad
\epsilon^-=[p^-,3],
\qquad
\upsilon^-=[p^-,4],
qquad
o^-=[\lambda^-].
\tag{Negative-Objects}
\]

The outer negative profile remains candidate, rooted, and predecessor-free, so its presentation is actual and anchored:

\[
\mathsf{ActPres}(s_{\pi^-,\upsilon^-}),
\qquad
\mathsf{Anchor}(s_{\pi^-,\upsilon^-},a_{\pi^-}).
\tag{Negative-Actual}
\]

But the fixed retained \(Pr\mapsto Ev\) alteration gives distinct observational classes:

\[
o^-\neq\mathsf{ObsProjProf}(\pi^-,\epsilon^-).
\tag{Negative-Mismatch}
\]

Thus match and fit fail while the claim remains present:

\[
\mathsf{Claims}(s_{\pi^-,\upsilon^-},o^-)
\land
\neg\mathsf{Fit}(s_{\pi^-,\upsilon^-},o^-).
\tag{Negative-NoFit}
\]

Therefore:

\[
\boxed{
\mathsf{ActPres}(s_{\pi^-,\upsilon^-})
\land
\mathsf{Error}(s_{\pi^-,\upsilon^-},o^-).
}
\tag{U3b-Pass}
\]

---

## 3. U3.c — raw-representation invariance

Take a permitted carrier-slot renaming \(\sigma\) of \(p^+\), yielding a distinct raw string:

\[
q^\sigma=\sigma(p^+),
\qquad
q^\sigma\neq p^+,
\qquad
q^\sigma\cong p^+.
\tag{Renamed-Raw-Code}
\]

The quotient identification is immediate:

\[
[q^\sigma]=[p^+]=\pi^+.
\tag{Profile-Identity}
\]

Likewise the host, presentation, and content arguments are identical semantic terms:

\[
[q^\sigma,\sigma(3)]=\epsilon^+,
\qquad
[q^\sigma,\sigma(4)]=\upsilon^+,
qquad
[\sigma(q^+)]=o^+.
\tag{Slot-Content-Identity}
\]

Thus the renamed raw encoding does not introduce a second articulation or presentation constructor:

\[
a_{[q^\sigma]}=a_{\pi^+},
\qquad
s_{[q^\sigma,\sigma(4)]}=s_{\pi^+,\upsilon^+}.
\tag{Same-Bearers}
\]

The U3.a correct verdict is consequently exactly the same proposition, not merely a matching verdict assigned after the fact:

\[
\mathsf{Correct}(s_{[q^\sigma,\sigma(4)]},[\sigma(q^+)])
\iff
\mathsf{Correct}(s_{\pi^+,\upsilon^+},o^+).
\tag{Correct-Invariance}
\]

The analogous identity preserves the U3.b error verdict under a permitted raw representation change:

\[
\mathsf{Error}(s_{[\sigma(p^-) ,\sigma(4)]},[\sigma(\lambda^-)])
\iff
\mathsf{Error}(s_{\pi^-,\upsilon^-},o^-).
\tag{Error-Invariance}
\]

Therefore:

\[
\boxed{
\mathsf{U3.cResult}(F_{\rm WPI\text{-}5})
=
\mathsf{Pass}_{\rm quotient\ representation\ invariance}.
}
\tag{U3c-Pass}
\]

---

## 4. U3 result and next authorization

\[
\boxed{
\begin{aligned}
&\mathsf{U3.aResult}(F_{\rm WPI\text{-}5})=\mathsf{Pass},\\
&\mathsf{U3.bResult}(F_{\rm WPI\text{-}5})=\mathsf{Pass},\\
&\mathsf{U3.cResult}(F_{\rm WPI\text{-}5})=\mathsf{Pass}_{\rm quotient\ representation\ invariance}.
\end{aligned}
}
\tag{U3-Components}
\]

\[
\boxed{
\mathsf{U3Result}(F_{\rm WPI\text{-}5})
=
\mathsf{Pass}_{\rm fixed\ class\ truth/error\ battery}.
}
\tag{U3-Pass}
\]

This closes the candidate's declared internal truth/error bridge at the fixed battery scope. It does not establish that the class-level match relation supplies an adequate noncircular account of truth for all claims, nor does it establish phenomenal, normative, physical, comparative, or zero-residue adequacy.

No U4 phenomenal, normative, or physical result is entered here.

The sole next authorized operation is:

\[
U4.a:
\quad
\text{execute the integrated and disconnected phenomenal controls.}
\tag{Next-U4a}
\]
