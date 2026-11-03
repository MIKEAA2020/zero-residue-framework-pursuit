# PSR-5 R3.a Phenomenal-Interface Audit v1
## Executed after independently adjudicated R2 pass

**Candidate:** \(F_{\rm PSR\text{-}5}\)  
**Packet SHA-256:** `b0d2a0fe6c72f19437aa1804230d0c2ba41c26a878a26deffbf50bd93d901321`  
**Controlling R2 adjudication:** `Point-Sphere_PSR-5_R2_Presentation_Truth_and_Error_Adjudication_v1.md`  
**Scope:** R3.a only. No R3.b or R3.c stage is executed or credited.

---

## 0. Frozen R3.a controls

The positive and negative controls are the two actual orbit-token loci:

\[
\iota_{[S_\Sigma],[a]_{S_\Sigma}},
\qquad
\iota_{[S_\Sigma],[d]_{S_\Sigma}}.
\tag{R3A-CONTROL-LOCI}
\]

Both are actual finite loci because \([S_\Sigma]\) is instantiated, both \([a]\) and \([d]\) are finite, and \(a,d\) have type \(Ag\):

\[
\mathsf{ActualLocus}(\iota_{[S_\Sigma],[a]_{S_\Sigma}})
\land
\mathsf{ActualLocus}(\iota_{[S_\Sigma],[d]_{S_\Sigma}}).
\tag{R3A-ACTUAL-LOCI}
\]

R3.a tests the frozen conjunction of actual locus, integrated structural condition, and a separately typed actual realization relation. It does not identify phenomenality with a graph label, an \(Ph\)-role name, or a quality field.

---

## 1. Positive structural and experience controls

At \(a\), the two hosted \(Ph\)-roles \(x_1,x_2\) both have quality \((\mathsf{pain},2)\). Their coaccess edges form a strongly connected pair, \(x_1\) strictly precedes \(x_2\), the distinct event roles \(e_1,e_2\) respectively input to them, and \(x_1\) outputs to the hosted action role \(n\). Therefore:

\[
\mathsf{IntegratedRec}(S_\Sigma,a,\mathsf{pain}),
	ag{POSITIVE-INTEGRATION}
\]

and hence:

\[
\mathsf{PhenStruct}([S_\Sigma],[a]_{S_\Sigma},\mathsf{pain}).
\tag{POSITIVE-PHEN-STRUCT}
\]

The independent experiential bearer is exactly declared:

\[
\xi_a
=
\xi_{[S_\Sigma],[a]_{S_\Sigma},\mathsf{pain}},
	ag{EXPERIENCE-TOKEN}
\]

\[
\mathsf{ActualExperience}(\xi_a)
\land
\mathsf{Qualia}(\xi_a,\mathsf{pain})
\land
\mathsf{ExpRealizes}
\left(
\xi_a,
\iota_{[S_\Sigma],[a]_{S_\Sigma}},
\mathsf{pain}
\right).
\tag{POSITIVE-REALIZATION}
\]

Together these frozen conditions yield:

\[
\mathsf{Phenomenal}_{\rm PSR}
\left(
\iota_{[S_\Sigma],[a]_{S_\Sigma}},
\mathsf{pain}
\right).
\tag{R3A-POSITIVE}
\]

---

## 2. Actual negative control

The negative control at \(d\) is not excluded by nonactuality: it is an actual locus. But the \(Ph\)-roles \(y_1,y_2\) have no coaccess edges, so the integrated structural condition fails:

\[
\neg\mathsf{IntegratedRec}(S_\Sigma,d,\mathsf{pain}),
	ag{NEGATIVE-INTEGRATION}
\]

and therefore:

\[
\neg\mathsf{PhenStruct}([S_\Sigma],[d]_{S_\Sigma},\mathsf{pain}).
\tag{NEGATIVE-PHEN-STRUCT}
\]

In addition, the actual experience extension contains no experiential bearer realizing pain at \(d\):

\[
\neg\exists\xi\,[
\mathsf{ActualExperience}(\xi)
\land
\mathsf{ExpRealizes}
(\xi,\iota_{[S_\Sigma],[d]_{S_\Sigma}},\mathsf{pain})].
\tag{NEGATIVE-REALIZATION}
\]

Hence the negative control is fixed by two independent failures of the frozen conjunction:

\[
\neg\mathsf{Phenomenal}_{\rm PSR}
\left(
\iota_{[S_\Sigma],[d]_{S_\Sigma}},
\mathsf{pain}
\right).
\tag{R3A-NEGATIVE}
\]

---

## 3. Restricted-interface boundary and R3.a verdict

The packet openly retains the realization relation as a psychophysical residual:

\[
\mathsf{DeclaredResidual}(\mathsf{ExpRealizes})
\not\Rightarrow
\mathsf{DerivedFromStructure}(
\mathsf{ExpRealizes}
).
\tag{PSYCHOPHYSICAL-RESIDUAL}
\]

Accordingly, this audit does not confirm consciousness, derive phenomenal character from graph topology, discharge selector residue, or establish a public bridge.

The frozen positive and actual-negative controls are both satisfied:

\[
\boxed{
R3.a(F_{\rm PSR\text{-}5})
=
\mathsf{Pass}_{\rm restricted\ formal}.
}
\tag{R3A-PASS}
\]

Only R3.b is authorized next:

\[
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R3.b)
\land
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R3.c).
\tag{NO-LATER-EXECUTION}
\]