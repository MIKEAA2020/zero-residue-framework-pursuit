# PSR-5 R2 Presentation, Truth, and Error Audit v1
## Executed after independently adjudicated R1 pass

**Candidate:** \(F_{\rm PSR\text{-}5}\)  
**Packet SHA-256:** `b0d2a0fe6c72f19437aa1804230d0c2ba41c26a878a26deffbf50bd93d901321`  
**Controlling R1 adjudication:** `Point-Sphere_PSR-5_R1_Instantiation_and_Isomorphism_Adjudication_v1.md`  
**Scope:** R2 only. No R3.a, R3.b, or R3.c stage is executed or credited.

---

## 0. Frozen R2 case

R2 examines the actual orbit \([a]_{S_\Sigma}\) and the two presentation roles \(p_t,p_e\) of \(S_\Sigma\). It must establish a correct presentation and an error presentation at the same actual locus without making tokenhood, actual bearer status, or a label alone sufficient for fit.

\[
\mathsf{Instantiates}^{\mathfrak M}
=
\{[S_\Sigma],[S_\Phi]\}.
\tag{R2-ACTUAL-EXTENSION}
\]

Since \(a\) has type \(Ag\), its orbit is finite, and \([S_\Sigma]\) is actual:

\[
\mathsf{ActualLocus}
\left(
\iota_{[S_\Sigma],[a]_{S_\Sigma}}
\right).
\tag{R2-ACTUAL-LOCUS}
\]

This is an orbit-token locus, not the raw carrier spelling \(a\).

---

## 1. Presentations and their contents

Both \(p_t\) and \(p_e\) are \(Pr\)-roles hosted by \(a\) in the actual structure. Their frozen presentation/content clauses are:

\[
\begin{aligned}
\mathsf{Presents}_{\rm PSR}
\left(p_{[S_\Sigma],p_t},\iota_{[S_\Sigma],[a]_{S_\Sigma}},o_{\rm true}\right),
&\qquad
\mathsf{Content}(p_{[S_\Sigma],p_t},o_{\rm true}),\\
\mathsf{Presents}_{\rm PSR}
\left(p_{[S_\Sigma],p_e},\iota_{[S_\Sigma],[a]_{S_\Sigma}},o_{\rm false}\right),
&\qquad
\mathsf{Content}(p_{[S_\Sigma],p_e},o_{\rm false}).
\end{aligned}
\tag{R2-PRESENTS}
\]

The content-pattern operation is total on the frozen three-member content domain:

\[
\mathsf{Pat}(o_{\rm true})
=
\mathsf{LocalPattern}(S_\Sigma,[a]_{S_\Sigma}),
\tag{TRUE-PATTERN}
\]

while \(\mathsf{Pat}(o_{\rm false})\) is the same typed local pattern except that it lacks the two coaccess triples between \(x_1\) and \(x_2\). Therefore:

\[
\mathsf{Pat}(o_{\rm false})
\not\cong_{\rm str}
\mathsf{LocalPattern}(S_\Sigma,[a]_{S_\Sigma}).
\tag{FALSE-NONMATCH}
\]

---

## 2. Correct and error determinations

The true content matches the actual orbit-local pattern:

\[
\mathsf{Matches}_{\rm PSR}
\left(o_{\rm true},[S_\Sigma],[a]_{S_\Sigma}\right).
\tag{TRUE-MATCH}
\]

Together with the actual locus and presentation clause, this yields:

\[
\mathsf{Correct}_{\rm PSR}
\left(p_{[S_\Sigma],p_t},o_{\rm true}\right).
\tag{R2-CORRECT}
\]

The false content is nevertheless presented at the same actual locus, but fails the matching condition. Hence:

\[
\neg\mathsf{Correct}_{\rm PSR}
\left(p_{[S_\Sigma],p_e},o_{\rm false}\right),
\tag{FALSE-NOT-CORRECT}
\]

and, using its declared content:

\[
\mathsf{Error}_{\rm PSR}
\left(p_{[S_\Sigma],p_e},o_{\rm false}\right).
\tag{R2-ERROR}
\]

The contrast controls precisely the required non-entailment:

\[
\mathsf{ActualLocus}
\land
\mathsf{Presents}_{\rm PSR}
\land
\mathsf{Content}
\not\Rightarrow
\mathsf{Correct}_{\rm PSR}.
\tag{NO-TOKENHOOD-FIT}
\]

All operations are transported through structural isomorphism by the packet's orbit-token and local-pattern transport rules, so the result does not depend on a raw representative or a presentation label.

---

## 3. R2 verdict and boundary

\[
\boxed{
R2(F_{\rm PSR\text{-}5})
=
\mathsf{Pass}_{\rm restricted\ formal}.
}
\tag{R2-PASS}
\]

R2 validates only this defined presentation/matching interface. It does not establish correspondence theory in general, semantic realism, a consciousness result, objective normativity, empirical physical adequacy, nonbrute instantiation, public-bridge success, or zero residue.

Only R3.a is authorized next:

\[
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R3.a)
\land
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R3.b)
\land
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R3.c).
\tag{NO-LATER-EXECUTION}
\]