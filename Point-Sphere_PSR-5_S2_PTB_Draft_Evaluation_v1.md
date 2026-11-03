# PSR-5 S2 Public Truth Bridge (PTB) Draft Evaluation v1
## Gate review of the supplied pragmatist/predictive-correctness proposal

**Framework resource:** \(F_{\rm PSR\text{-}5}\), frozen SHA-256 `b0d2a0fe6c72f19437aa1804230d0c2ba41c26a878a26deffbf50bd93d901321`  
**Prior controlling B1 evaluation:** `Point-Sphere_PSR-5_S2_Public_Truth_Error_Bridge_Preregistration_Evaluation_v1.md`  
**Prior evaluation SHA-256:** `4d93da29f7878fa10ba4eafbfebc0ab707c638f0b54d450bd7f8e5db7a49d468`  
**Material reviewed:** the supplied unregistered PTB draft; no hash, freeze, concrete claim pair, target, protocol, or witness package was supplied  
**Scope:** gate review only. No S2 bridge is registered, authorized, or executed.

---

## 0. Relation to the B1 disposition

The first supplied block accurately retains the B1 nonauthorization boundary, with one file-location correction: the controlling evaluation is in the workspace root, not in `uploads/`. Its controlling result remains:

\[
\mathsf{BridgeRegistrationStatus}
\left(B^{(1)}_{\rm PSR\text{-}S2}\right)
=
\mathsf{EntryIncomplete}_{\rm claim/reference\ channel,\ independent\ target/decoder\ provenance,\ closed\ witness\ controls}.
\tag{B1-Controlling-Status}
\]

The PTB changes the proposed truth criterion, claim type, target interface, protocol, and scope. It is therefore not a repair to \(B^{(1)}_{\rm PSR\text{-}S2}\):

\[
\mathsf{PTB}\neq B^{(1)}_{\rm PSR\text{-}S2},
\qquad
\mathsf{PTB}\text{ would require a fresh bridge preregistration.}
\tag{Fresh-Bridge-Identity}
\]

---

## 1. What the PTB proposal contributes

The draft makes constructive improvements over bare pattern matching. It distinguishes an assertion marker, content structure, target, protocol, predicted observables, and verdict. It also proposes finite scope, protocol freezing, and representation invariance:

\[
c=\langle A_c,S_c,\pi_c\rangle,
\qquad
\mathsf{Correct}(c,t)
\text{ is proposed as predictive success under }\pi_c.
\tag{PTB-Resource}
\]

This is a potentially useful proposal for a **finite public predictive-score protocol**. It is not yet a public truth/error bridge, and its assertion that it “satisfies all six entry conditions” is not established.

\[
\boxed{
\mathsf{PTBStatus}
=
\mathsf{NotAdmittedAsS2TruthBridge}_{\rm target\ access/reference,\ predictive\ semantics,\ actual\ public\ witness,\ invariance/decision\ closure}.
}
\tag{PTB-Gate-Result}
\]

---

## 2. The protocol has no target-access or reference bridge

The proposal calls \(t\) a PSR-native quotient target while requiring an operational protocol:

\[
\pi_c:\mathcal T\to\mathcal V^n,
\qquad
\mathsf{ClaimsAbout}(c,t)
\iff
A_c=\mathsf{assert}
\land
\pi_c\text{ is applicable to }t
\land
S_c\text{ predicts under }\pi_c.
\tag{PTB-ClaimsAbout}
\]

But neither “applicable to” nor the application \(\pi_c(t)\) is typed. A procedure described in operational vocabulary does not automatically apply to a PSR quotient structure. The required measurement/access relation is the very bridge at issue:

\[
\mathsf{OperationalProtocol}(\pi_c)
\not\Rightarrow
\mathsf{PubliclyAnchoredAccess}(\pi_c,t),
\qquad
\mathsf{Target}(t)
\not\Rightarrow
\mathsf{ActualTarget}(t).
\tag{No-Target-Access}
\]

A public-practice vocabulary may be a legitimate independent resource, but it cannot be invoked as a self-authenticating anchor. A fresh preregistration would need a typed, quotient-invariant access/measurement map; an actual target-bearer condition; and public provenance showing why this map, rather than a stipulated decoder, links the target to the record.

---

## 3. Predictive success is not yet a noncircular correctness condition

The core proposed rule is:

\[
\mathsf{Correct}(c,t)
\iff
\mathsf{ClaimsAbout}(c,t)
\land
\forall o\in\mathsf{Pred}(S_c,\pi_c)
\,[\pi_c(t)\ni o].
\tag{PTB-Correctness-Rule}
\]

The predicates \(\mathsf{Predicts}\), \(\mathsf{Pred}\), the output-membership relation, and the protocol's application semantics remain undefined. In particular, it is not specified whether \(\mathsf{Pred}\) is independently derived from content, whether all relevant outcomes must be covered, or how false positives, false negatives, stochastic outcomes, and underprediction are distinguished.

The one-sided universal condition permits an underinformative prediction set. Finiteness does not exclude the empty set:

\[
\mathsf{Finite}(\mathsf{Pred}(S_c,\pi_c))
\not\Rightarrow
\mathsf{NonvacuousPrediction}(S_c,\pi_c).
\tag{Finite-Not-Nonvacuous}
\]

Thus a claim can pass merely by predicting too little. The proposed error rule inherits this defect. A finite predictive-score convention may still be valuable, but it is not yet an independently defined truth/error relation.

---

## 4. Assertion, public witness, and invariance are not closed

An assertion marker is presently another stipulated symbol:

\[
A_c=\mathsf{assert}
\not\Rightarrow
\mathsf{ActualPublicAssertion}(c).
\tag{Assertion-Marker-Insufficient}
\]

No actual target, measurement event, public record, archive, acquisition rule, auditor identities, independence evidence, or concrete finite claim pair is frozen. The proposal therefore lacks the required actual public witness package.

The proposed invariance clause also does not follow without definitions of conservative isomorphism for the compound claim/protocol and a quotient-respecting access rule:

\[
c\cong c'
\land t\cong t'
\not\Rightarrow
\mathsf{Verdict}(c,t)=\mathsf{Verdict}(c',t')
\tag{Invariance-Not-Derived}
\]

until the relevant isomorphism category, prediction extraction, protocol action, and record mapping are fixed. Merely freezing a protocol prevents a post hoc change; it does not establish that the frozen protocol is independently target-directed.

---

## 5. Scope correction

If fully specified, the PTB could at most establish a finite protocol-relative predictive score:

\[
\mathsf{ProtocolRelativePredictiveSuccess}(c,t,\pi_c).
\tag{Narrow-Potential-Result}
\]

Whether that score should be called `truth` is a substantive normative/semantic thesis, not a result of the protocol. It cannot be settled by declaring the account pragmatist or deflationary:

\[
\mathsf{PredictiveSuccess}
\not\Rightarrow
\mathsf{PublicTruthErrorBridge}
\quad\text{without an explicit, defended truth standard.}
\tag{Predictive-Not-Truth}
\]

The Newmannian, empirical-equivalence, theory-change, circularity, and relativism replies in the draft are therefore promissory responses, not completed controls. In particular, fixed finite observables do not independently prove that the target/reference relation is nonarbitrary.

---

## 6. Required fresh preregistration fields

A new \(B^{(2)}_{\rm PSR\text{-}S2}\) could be submitted only after it freezes:

\[
\begin{array}{c|l}
\textbf{field} & \textbf{minimum requirement}\\
\hline
\text{claim pair} & \text{two concrete finite actual-public assertions, contents, and assertion-bearing acts}\\
\text{actual target} & \text{typed actual target class plus public access/measurement relation}\\
\text{protocol} & \text{complete operational steps, finite domain/codomain, validity and failure cases}\\
\text{prediction map} & \text{independent finite extraction, nonempty/nontrivial coverage criterion, and outcome comparison rule}\\
\text{public witness} & \text{acquisition, record, archive, auditor identity/independence, and reproducibility evidence}\\
\text{reference provenance} & \text{non-PSR-label derivation of content-to-target and target-to-observable maps}\\
\text{invariance} & \text{relevant isomorphism category and proof of verdict preservation}\\
\text{semantic scope} & \text{whether the outcome is predictive success, deflationary truth, or a stronger truth claim}
\end{array}
\tag{PTB-Fresh-Requirements}
\]

Until a fresh bridge packet passes its own preflight:

\[
\neg\mathsf{AuthorizeExecution}(B^{(2)}_{\rm PSR\text{-}S2}),
\qquad
\neg\mathsf{Executed}(B^{(2)}_{\rm PSR\text{-}S2}).
\tag{No-PTB-Execution}
\]
