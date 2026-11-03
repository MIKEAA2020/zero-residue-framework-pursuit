# Plural Structural Realism PSR-3 Entry Review v1
## Critical admission review of the submitted frozen restricted-formal candidate

**Reviewed source:** `uploads/Plural_Structural_Realism_Entry_Packet_v3.md`  
**Candidate:** \(F_{\rm PSR\text{-}3}\), a fresh lineage distinct from PSR-1 and PSR-2  
**Source SHA-256 verified:** `60b03d369511df37d93e0d78af3371e0e21a0a0d81165f13352ed6f40746dadb`  
**Scope:** entry review only. No R0–R3 stage is executed.

---

## 0. Source and normalization controls

PSR-3 repairs the PSR-2 grouping defect. Its UTF-8 source, display delimiters, and non-literal TeX grouping delimiters are balanced:

\[
\mathsf{SourceStaticValid}(F_{\rm PSR\text{-}3}).
\tag{Static-Pass}
\]

The packet also supplies the family-required structural normalizations:

\[
\begin{array}{c|l}
\textbf{requirement} & \textbf{entry finding}\\
\hline
\text{isomorphism transport for orbit individuals} & \mathsf{Declared}\\
\text{quotient-native local-pattern transport} & \mathsf{Declared}\\
\text{actual plurality reading} & \mathsf{Declared}\ \bigl([S_\Sigma],[S_\Phi]\bigr)\\
\text{primitive selector disclosure} & \mathsf{Declared}\ \bigl(\mathsf{Instantiates},\mathsf{ExpRealizes}\bigr)\\
\text{actual truth/error bearer} & \mathsf{Declared}\ \bigl([S_\Sigma],[a]\bigr)\\
\text{typed experiential bearer} & \mathsf{Declared}\ \bigl(\xi_a\bigr)
\end{array}
\tag{Normalization-Record}
\]

In particular, the repaired experiential tuple is well formed. It gives the restricted formal interface a separate actual-experience token and realization predicate, rather than inferring phenomenality from a \(Ph\) label or graph pattern alone:

\[
\mathsf{PhenStruct}
\not\Rightarrow
\mathsf{GenuinePhenomenality},
\qquad
\mathsf{GenuinePhenomenality}
\text{ is asserted only through the declared }
\mathsf{ActualExperience}/\mathsf{Qualia}/\mathsf{ExpRealizes}
\text{ extension}.
\tag{Phenomenal-Scope}
\]

This is a restricted formal resource with an expressly primitive psychophysical residual. It is neither a nonbrute discharge nor a consciousness bridge pass:

\[
\mathsf{Declared}(\mathsf{ExpRealizes})
\not\Rightarrow
\mathsf{NoSelectorResidue},
\qquad
\mathsf{Declared}(\mathsf{ExpRealizes})
\not\Rightarrow
\mathsf{GenuinePhenomenalityCredit}.
\tag{No-Experience-Credit}
\]

---

## 1. The asserted explicit-infinite global codec is not fully specified

The finite macro codes establish a useful bounded fixture vocabulary and a concrete proposed bound \(N_\star=3\). But PSR-3 declares an **explicit-infinite** model containing every raw structural string and its decoded operations. That declaration requires a fully parsable generic codec.

The generic-code paragraph does not supply one. It says there are “six” length-prefixed tables while listing only five:

\[
\kappa,\ \eta,\ \alpha,\ \nu,\ \Phi.
\tag{Five-Listed-Tables}
\]

More fundamentally, the only displayed symbol tables code role types and relation types. They do not code the values or recursive objects needed by the asserted generic parser, including:

\[
\begin{array}{c|l}
\textbf{field} & \textbf{missing generic decoding interface}\\
\hline
\kappa & \text{content-object grammar and content values}\\
\eta & \text{encoding of integer-valued local indices}\\
\alpha & \text{finite successor-record grammar and its boundary rule}\\
\nu & \text{value-key and value grammar, including quality/value pairs}\\
\Phi & \text{field-domain, field-index, and field-value grammar}
\end{array}
\tag{GEN-Gaps}
\]

The phrase “indices and values under the same fixed symbol table” cannot fill these gaps, because that displayed table contains no codes for the listed value kinds. Consequently, the source does not determine the generic parser, the set of all decoded raw structures, or the asserted global model:

\[
\boxed{
\neg\mathsf{Defined}
\left(
\mathcal S_{\rm raw}^{\mathsf{GEN}},
\overline{\mathcal S}^{\mathsf{GEN}},
\mathfrak M_{\rm PSR}^{\rm ExplicitInfinite}
\right).
}
\tag{Global-Codec-Incomplete}
\]

The length-three macro slice may be finite on its intended reading, but that does not establish the preregistered global-model premise or the displayed global-to-slice locality biconditional:

\[
\mathsf{MacroSliceFinite}(N_\star=3)
\not\Rightarrow
\mathsf{ExplicitInfiniteGlobalModel}
\not\Rightarrow
\mathsf{CertifiedGlobalToSliceLocality}.
\tag{Locality-Blocked}
\]

---

## 2. Normative operation remains incomplete and lacks locus typing

The normative value tuple contains an undeclared matching operation:

\[
\kappa_T(j)
\text{ matches its declared host-local pattern}.
\tag{Unspecified-Successor-Match}
\]

The only formal matching operation in PSR-3 is \(\mathsf{Matches}_{\rm PSR}\), whose domain is the two-member content set \(\mathbf O_\star\) and whose second argument is an isomorphism class and orbit. It does not apply to the successor record content specified for \(T_{\rm good}\):

\[
\kappa_{T_{\rm good}}(Pr)
=
\mathsf{LocalPattern}(T_{\rm good},[Ag]),
\qquad
\mathsf{LocalPattern}(T_{\rm good},[Ag])
\notin\mathbf O_\star.
\tag{Successor-Content-Mismatch}
\]

Hence the second coordinate of \(\mathsf{Val}_{\rm PSR}(T)\), including the asserted \(\langle1,1,1\rangle\) value for \(T_{\rm good}\), is not determined by a frozen typed operation:

\[
\boxed{
\neg\mathsf{Executable}
\bigl(
\mathsf{Val}_{\rm PSR},
\mathsf{LexMax}_{\rm PSR},
\mathsf{Ought}_{\rm PSR}
\bigr).
}
\tag{Normative-Value-Blocked}
\]

There is an independent locus-typing omission. The family preregistration requires an action-role at \([u]_S\), but the proposed \(\mathsf{Ought}\) clause connects any actual locus in \([S]\) to any lexicographically maximal action of \([S]\):

\[
\mathsf{Ought}_{\rm PSR}(\iota_{[S],[u]_S},a_{[S],j})
\iff
\mathsf{ActualLocus}(\iota_{[S],[u]_S})
\land
\mathsf{LexMax}_{\rm PSR}([S],j).
\tag{Ought-Rule}
\]

It lacks a requirement that \(j\) is hosted by, or belongs to, \([u]_S\). For the supplied fixture, \(g\) is hosted by \(a\), but the clause would also relate a lex-maximal \(g\) to the different actual locus \([d]\). The normative bearer is therefore not fixed by the formal rule:

\[
\neg\mathsf{LocusTyped}
\left(
\mathsf{Ought}_{\rm PSR}
\right).
\tag{Ought-Locus-Gap}
\]

This is an entry-interface diagnosis, not a conclusion that structural realism cannot formulate normativity.

---

## 3. Disposition

PSR-3 is a static improvement over PSR-2 and supplies useful formal resources for orbit transport, actual plurality, truth/error matching, and a separately typed primitive experiential extension. It does not yet meet the shared admission conditions for a globally explicit model/locality certificate and a fully typed finite normative fixture.

\[
\boxed{
\mathsf{EntryResult}(F_{\rm PSR\text{-}3})
=
\mathsf{EntryIncomplete}_{\rm generic\ global\ codec/locality,\ normative\ value\ and\ locus\ typing}.
}
\tag{Entry-Result}
\]

\[
\neg\mathsf{Established}
\left(
\mathsf{AdmittedForBattery}_{\rm restricted\ formal\ PSR}
(F_{\rm PSR\text{-}3})
\right).
\tag{No-Admission}
\]

\[
\bigwedge_{b\in\{R0,R1,R2,R3.a,R3.b,R3.c\}}
\neg\mathsf{Executed}(F_{\rm PSR\text{-}3},b).
\tag{No-Battery-Execution}
\]

This result is docket-bounded. It does not test or refute the PSR family, does not turn the declared residual into a selector failure, and does not support any rival framework:

\[
\mathsf{EntryIncomplete}(F_{\rm PSR\text{-}3})
\not\Rightarrow
\neg\mathsf{Viable}(\mathcal F_{\rm PSR}),
\qquad
\mathsf{EntryIncomplete}(F_{\rm PSR\text{-}3})
\not\Rightarrow
\mathsf{BridgeFailure}(\mathcal F_{\rm PSR}).
\tag{Scope-Boundary}
\]

Under the packet's freeze, this review makes no in-project repair. Any changed successor must be separately submitted and classified under its stated expiry rule.

\[
\exists![F]_{\simeq}\,\mathsf{ZeroResidue}(F)
\quad\text{remains unproved.}
\tag{Open-Objective}
\]
