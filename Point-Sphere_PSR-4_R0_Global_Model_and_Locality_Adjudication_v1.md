# PSR-4 R0 Global-Model and Finite-Locality Adjudication v1
## Independent determination of the submitted R0 audit

**Candidate:** \(F_{\rm PSR\text{-}4}\)  
**Frozen packet:** `uploads/Plural_Structural_Realism_Entry_Packet_v4.md`  
**Packet SHA-256:** `d326b9fe2276c472cdc1558d1c4cc669a479c01c8563fe32e77ac4e47b04b6b7`  
**Submitted R0 audit:** `uploads/Point-Sphere_PSR-4_R0_Global_Model_and_Locality_Audit_v1.md`  
**Audit SHA-256:** `0e26bb0c786f53cdfcb3cf36f53e4a3b185c6c92de747d54bff360c1ac4a57c4`  
**Scope:** R0 only. R1, R2, R3.a, R3.b, and R3.c are not executed.

---

## 0. Source-static result

The submitted audit is valid UTF-8 and passes display-pair and TeX-grouping checks:

\[
\mathsf{AuditSourceStaticValid}.
\tag{Audit-Static-Pass}
\]

That source-level result does not establish the semantic R0 requirements:

\[
\mathsf{AuditSourceStaticValid}
\not\Rightarrow
\mathsf{R0Pass}.
\tag{Static-Not-Semantic}
\]

---

## 1. The submitted raw-carrier partition is ill typed

The audit declares:

\[
\mathcal S_{\rm raw}
=
\mathsf{MacroRecords}
\cup
\mathsf{GENRecords}
\cup
\mathsf{RejectedStrings}.
\tag{Submitted-Raw-Partition}
\]

But rejected strings are explicitly noncandidate strings, whereas \(\mathcal S_{\rm raw}\) is the carrier that is then quotiented by structural isomorphism:

\[
\overline{\mathcal S}
=
\mathcal S_{\rm raw}/\cong_{\rm str}.
\tag{Submitted-Quotient}
\]

No structural record, signature, or \(\cong_{\rm str}\)-relation is supplied for a rejected string. Therefore the quotient is not typed on the carrier asserted by the audit:

\[
\boxed{
\neg\mathsf{WellTyped}
\left(
\mathcal S_{\rm raw}/\cong_{\rm str}
\right)
\quad\text{under (Submitted-Raw-Partition).}
}
\tag{Raw-Carrier-Failure}
\]

A coherent construction would have required a separately typed code universe and a decode map, for example:

\[
\{0,1\}^{*}
=
\mathsf{AcceptedCodeStrings}\sqcup\mathsf{RejectedStrings},
\qquad
\mathcal S_{\rm raw}
=
\mathsf{Decode}(\mathsf{AcceptedCodeStrings}).
\tag{Required-Separation-Not-Supplied}
\]

This is displayed only to identify the missing typed separation. It is not imported as a repair to the frozen packet or audit.

---

## 2. The generic parser remains underdetermined for the claimed global universe

The R0 audit repeats the packet's assertion that the generic branch is fully specified, but it does not close two grammar interfaces required for the purported universal decode relation.

First, the content branch permits a nested “complete finite pattern body”:

\[
\mathsf{ContentCode}
=
1\mathsf N(|B|)B,
\qquad
B=\text{a complete nested finite pattern body}.
\tag{Pattern-Body-Clause}
\]

No production rule specifies the bit grammar or decoder for a `pattern body`. This differs from the successor clause, which at least identifies \(B\) as a nested \(\mathsf{GEN}\) body. Hence an arbitrary generic string using the content-body branch has no determined parse or decoded content value.

Second, the declared \(\mathsf{ValueKey}\) table includes:

\[
\mathsf{instrumentalized},
\quad
\mathsf{quality},
\quad
\mathsf{content},
\quad
\mathsf{time},
\quad
\mathsf{field},
\tag{Declared-Value-Keys}
\]

while the only \(\mathsf{ValueCode}\) cases are instrumentalization and quality/intensity. No value-code case, validity condition, or rejection clause is supplied for the latter three keys. Therefore the asserted generic parser and its accepted-record set remain incomplete:

\[
\boxed{
\neg\mathsf{Defined}
\left(
\mathsf{Decode}_{\mathsf{GEN}},
\mathsf{GENRecords},
\mathcal S_{\rm raw}^{\rm global}
\right)
\quad\text{for all declared generic branches.}
}
\tag{Generic-Global-Underdetermination}
\]

This conclusion is not a no-go claim against structural coding. It is confined to PSR-4's frozen generic grammar.

---

## 3. The claimed content closure omits a live R3.b dependency

The submitted audit states that the content closure is exactly:

\[
\mathbf O_\star
=
\{o_{\rm true},o_{\rm false}\}.
\tag{Audit-Content-Closure}
\]

But the frozen packet assigns the good successor's presentation content as:

\[
\kappa_{T_{\rm good}}(Pr)
=
\mathsf{LocalPattern}(T_{\rm good},[Ag]).
\tag{Good-Successor-Content}
\]

The latter is neither \(o_{\rm true}\) nor \(o_{\rm false}\). It is also required by the frozen \(\mathsf{SuccMatches}\) operation used in the R3.b value and lexicographic clauses. Thus the audit's closure is false on the packet's own fixture data:

\[
\boxed{
\mathsf{ContentClosure}_{\rm audit}
\not\supseteq
\left\{
\kappa_{T_{\rm good}}(Pr)
\right\}.
}
\tag{Closure-Omission}
\]

As a result, the audit does not establish that every dependency of the declared R0–R3 formulas is contained in its displayed multi-sorted slice:

\[
\neg\mathsf{Certified}
\left(
\mathsf{Verdict}^{\mathfrak M_{\rm PSR}}(b)
\iff
\mathsf{Verdict}^{\mathfrak M_{\rm PSR}\upharpoonright N_\star}(b)
\right)
\quad
\left(b\in\{R0,R1,R2,R3.a,R3.b,R3.c\}\right).
\tag{Locality-Certificate-Failure}
\]

This does not assert the biconditional is false in every possible repaired formalization. It records that PSR-4's frozen R0 packet and submitted audit do not certify it.

---

## 4. R0 disposition and stop boundary

R0 requires a well-typed explicit-infinite global model and a certified finite local slice. The raw-carrier/quotient defect, generic-parser underdetermination, and omitted successor-content dependency each independently block that requirement:

\[
\boxed{
R0(F_{\rm PSR\text{-}4})
=
\mathsf{Fail}_{\rm raw\ carrier/quotient\ typing,\ generic\ global\ parser,\ content\ closure/locality}.
}
\tag{R0-Fail}
\]

This is an executed-stage failure, not entry incompleteness and not a family-level verdict:

\[
\mathsf{R0Fail}(F_{\rm PSR\text{-}4})
\not\Rightarrow
\neg\mathsf{Viable}(\mathcal F_{\rm PSR}),
\qquad
\mathsf{R0Fail}(F_{\rm PSR\text{-}4})
\not\Rightarrow
\mathsf{BridgeFailure}(\mathcal F_{\rm PSR}).
\tag{Scope-Boundary}
\]

The packet's expiry rule forbids in-project changes to the codec, global model, slice/locality bridge, fixture, or operation. Therefore this R0 docket is closed and no later battery operation is authorized:

\[
\boxed{
\mathsf{BatteryStatus}(F_{\rm PSR\text{-}4})
=
\mathsf{Closed}_{\rm R0\ global\ model/locality\ failure}.
}
\tag{Battery-Closed}
\]

\[
\bigwedge_{b\in\{R1,R2,R3.a,R3.b,R3.c\}}
\neg\mathsf{Executed}(F_{\rm PSR\text{-}4},b).
\tag{No-Later-Execution}
\]

The primitive instantiation and experience residual remains disclosed but unresolved:

\[
\mathsf{R0Fail}
\not\Rightarrow
\mathsf{NoSelectorResidue},
\qquad
\mathsf{R0Fail}
\not\Rightarrow
\mathsf{ZRPass}.
\tag{Residual-Boundary}
\]
