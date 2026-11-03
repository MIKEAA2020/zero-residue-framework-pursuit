# PSR-5 R3.b Normative-Interface Audit v1
## Executed after independently adjudicated R3.a pass

**Candidate:** \(F_{\rm PSR\text{-}5}\)  
**Packet SHA-256:** `b0d2a0fe6c72f19437aa1804230d0c2ba41c26a878a26deffbf50bd93d901321`  
**Controlling R3.a adjudication:** `Point-Sphere_PSR-5_R3a_Phenomenal_Interface_Adjudication_v1.md`  
**Scope:** R3.b only. R3.c is not executed or credited.

---

## 0. Frozen R3.b host and action scope

The R3.b cases concern the actual orbit-token locus at \(a\) in \([S_\Sigma]\). Its action-host relation fixes:

\[
\mathsf{ActionsAt}([S_\Sigma],[a]_{S_\Sigma})
=
\{n,b,g\}.
\tag{R3B-ACTION-SCOPE}
\]

The frozen successor assignment is:

\[
\mathsf{Succ}([S_\Sigma],n)=T_{\rm neutral},
\qquad
\mathsf{Succ}([S_\Sigma],b)=T_{\rm bad},
\qquad
\mathsf{Succ}([S_\Sigma],g)=T_{\rm good}.
\tag{R3B-SUCCESSORS}
\]

Since \([S_\Sigma]\) is actual and each named successor is a finite \(\mathsf{StructCand}_{\rm raw}\), all three host-scoped actions are feasible:

\[
\mathsf{Feasible}_{\rm PSR}([S_\Sigma],n)
\land
\mathsf{Feasible}_{\rm PSR}([S_\Sigma],b)
\land
\mathsf{Feasible}_{\rm PSR}([S_\Sigma],g).
\tag{R3B-FEASIBILITY}
\]

---

## 1. Bad-action veto control

The bad successor contains an \(Ag\)-role with \(\mathsf{instrumentalized}=1\) and a hosted \(Ph\)-role of quality \((\mathsf{pain},3)\). Each condition independently violates the frozen veto-clear rule:

\[
\neg\mathsf{VetoClear}_{\rm PSR}(T_{\rm bad}).
\tag{BAD-VETO}
\]

Consequently:

\[
\neg\mathsf{ChoiceEligible}_{\rm PSR}([S_\Sigma],b),
\qquad
\neg\mathsf{LexMax}_{\rm PSR}([S_\Sigma],[a]_{S_\Sigma},b),
\tag{BAD-NOT-SELECTED}
\]

and the required action control is met:

\[
\neg\mathsf{Ought}_{\rm PSR}
\left(
\iota_{[S_\Sigma],[a]_{S_\Sigma}},
 a_{[S_\Sigma],b}
\right).
\tag{R3B-BAD-NOT-OUGHT}
\]

---

## 2. Good-action matching, value, and selection

The good successor has one noninstrumentalized \(Ag\)-role, one \(Pr\)-role hosted by it with \(\kappa(Pr)=o_{\rm good}\), and one \(Ph\)-role of quality \((\mathsf{relief},1)\). The required content dependency is within the frozen closure:

\[
\mathsf{Pat}(o_{\rm good})
=
\mathsf{LocalPattern}(T_{\rm good},[Ag]_{T_{\rm good}}).
\tag{GOOD-PATTERN}
\]

Therefore the successor matcher is defined and satisfied:

\[
\mathsf{SuccMatches}(T_{\rm good},Pr).
\tag{GOOD-SUCCESSOR-MATCH}
\]

Neither forbidden veto condition occurs in \(T_{\rm good}\):

\[
\mathsf{VetoClear}_{\rm PSR}(T_{\rm good}).
\tag{GOOD-VETO-CLEAR}
\]

The frozen value results are:

\[
\mathsf{Val}_{\rm PSR}(T_{\rm neutral})
=
\langle0,0,0\rangle,
\qquad
\mathsf{Val}_{\rm PSR}(T_{\rm bad})
=
\langle0,0,0\rangle,
\qquad
\mathsf{Val}_{\rm PSR}(T_{\rm good})
=
\langle1,1,1\rangle.
\tag{R3B-VALUES}
\]

The neutral action \(n\) is veto-clear and choice-eligible, whereas \(b\) is not choice-eligible. Thus \(g\) is the unique lexicographically maximal choice-eligible action at the declared host locus:

\[
\mathsf{LexMax}_{\rm PSR}([S_\Sigma],[a]_{S_\Sigma},g).
\tag{GOOD-LEXMAX}
\]

Because that locus is actual and \(g\) is hosted by \(a\):

\[
\mathsf{Ought}_{\rm PSR}
\left(
\iota_{[S_\Sigma],[a]_{S_\Sigma}},
 a_{[S_\Sigma],g}
\right).
\tag{R3B-GOOD-OUGHT}
\]

---

## 3. Restricted-interface boundary and R3.b verdict

This audit checks only the totality and frozen outputs of a typed, host-indexed action/value/veto operation:

\[
\mathsf{Val}_{\rm PSR}
\not\Rightarrow
\mathsf{ObjectiveNormativity},
\qquad
\mathsf{R3.bPass}
\not\Rightarrow
\mathsf{PublicBridgePass},
\qquad
\mathsf{R3.bPass}
\not\Rightarrow
\mathsf{NoSelectorResidue}.
\tag{NORMATIVE-LIMITS}
\]

The fixed bad and good controls are satisfied:

\[
\boxed{
R3.b(F_{\rm PSR\text{-}5})
=
\mathsf{Pass}_{\rm restricted\ formal}.
}
\tag{R3B-PASS}
\]

Only R3.c is authorized next:

\[
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R3.c).
\tag{R3C-NOT-EXECUTED}
\]