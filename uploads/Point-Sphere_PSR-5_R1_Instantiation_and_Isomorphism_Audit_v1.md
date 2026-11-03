# PSR-5 R1 Instantiation and Isomorphism Audit v1
## Executed after independently adjudicated R0 pass

**Candidate:** \(F_{\rm PSR\text{-}5}\)  
**Packet SHA-256:** `b0d2a0fe6c72f19437aa1804230d0c2ba41c26a878a26deffbf50bd93d901321`  
**R0 adjudication:** `Point-Sphere_PSR-5_R0_Global_Model_and_Locality_Adjudication_v1.md`  
**Scope:** R1 only. No R2, R3.a, R3.b, or R3.c stage is executed or credited.

---

## 0. Frozen R1 controls

The fixed R1 control classes are:

\[
[S_\Sigma],
\qquad
[S_\Phi],
\qquad
[S_{\rm with}],
\qquad
[S_{\rm noncand}].
\tag{R1-CONTROLS}
\]

R1 checks class-native actual/nonactual status and isomorphism invariance. It does not attempt to derive the primitive instantiation extension.

---

## 1. Actual, nonactual, and noncandidate status

The global primitive extension is frozen as:

\[
\mathsf{Instantiates}^{\mathfrak M}
=
\{[S_\Sigma],[S_\Phi]\},
\qquad
\mathsf{ActualStruct}([S])
\iff
\mathsf{Instantiates}([S]).
\tag{ACTUALITY-RULE}
\]

Thus:

\[
\mathsf{ActualStruct}([S_\Sigma]),
\qquad
\mathsf{ActualStruct}([S_\Phi]).
\tag{R1-ACTUAL}
\]

The withheld structural candidate is a decoded and well-formed record but is not instantiated:

\[
\mathsf{StructCand}([S_{\rm with}])
\land
\neg\mathsf{Instantiates}([S_{\rm with}])
\land
\neg\mathsf{ActualStruct}([S_{\rm with}]).
\tag{R1-WITH}
\]

The noncandidate macro decodes to a raw record with an untyped relation endpoint. It belongs to the raw-record carrier but fails the candidate grammar and is absent from the actual extension:

\[
\neg\mathsf{StructCand}([S_{\rm noncand}])
\land
\neg\mathsf{ActualStruct}([S_{\rm noncand}]).
\tag{R1-NONCAND}
\]

These results depend on neither macro labels, generic-code branch, code length, local pattern, observation, target satisfaction, nor structural elegance.

---

## 2. Isomorphism invariance

Actuality has quotient-class domain. For every signature-preserving isomorphism \(h:S\cong_{\rm str}T\):

\[
S\cong_{\rm str}T
\Longrightarrow
[S]=[T]
\Longrightarrow
\left(
\mathsf{ActualStruct}([S])
\leftrightarrow
\mathsf{ActualStruct}([T])
\right).
\tag{ACTUALITY-INVARIANCE}
\]

The generic alias branch makes this nonvacuous: a valid alias \(1110\,\mathsf N(i)\mathsf N(r)\) decodes to a carrier-renamed macro record \(\pi_r(S_i)\), and therefore denotes the same structural class as \(S_i\).

\[
[\pi_r(S_\Sigma)]=[S_\Sigma],
\qquad
[\pi_r(S_{\rm with})]=[S_{\rm with}].
\tag{ALIAS-CLASS-ID}
\]

Consequently, aliases preserve the corresponding actual or nonactual status. The orbit and local-pattern transport clauses provide the matching role-level invariance:

\[
\iota_{[S],[u]_S}
=
\iota_{[T],[h(u)]_T},
qquad
\mathsf{LocalPattern}(S,[u]_S)
\cong_{\rm str}
\mathsf{LocalPattern}(T,[h(u)]_T).
\tag{ROLE-TRANSPORT}
\]

---

## 3. Residual boundary and R1 verdict

R1 verifies transparency and representation invariance of the stipulated extension only:

\[
\mathsf{R1Pass}
\not\Rightarrow
\mathsf{NonBrute}(\mathsf{Instantiates}),
\qquad
\mathsf{R1Pass}
\not\Rightarrow
\mathsf{NoSelectorResidue}.
\tag{NO-RESIDUE-CREDIT}
\]

All frozen R1 conditions are satisfied:

\[
\boxed{
R1(F_{\rm PSR\text{-}5})
=
\mathsf{Pass}_{\rm restricted\ formal}.
}
\tag{R1-PASS}
\]

Only R2 is now authorized. No later case is executed here:

\[
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R2)
\land
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R3.a)
\land
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R3.b)
\land
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R3.c).
\tag{NO-LATER-EXECUTION}
\]
