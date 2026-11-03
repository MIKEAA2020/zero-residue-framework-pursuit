# PSR S2 Witness-Package Preparation Specification v1
## Post-PTB preparation only — not a B2 bridge preregistration and not a bridge execution

**Context:** \(B^{(1)}_{\rm PSR\text{-}S2}\) is frozen at its bridge-entry-incomplete disposition.  
**Purpose:** state the concrete materials that must exist before any future fresh S2 bridge preregistration can be assessed for preflight.  
**Status:** no new bridge docket, no \(F_{\rm PSR\text{-}6}\) EntryPacket, no witness package, and no bridge operation is authorized.

---

## 0. Boundary

This preparation specification does not amend \(B^{(1)}_{\rm PSR\text{-}S2}\), PSR-5, or any earlier packet. It neither registers \(B^{(2)}_{\rm PSR\text{-}S2}\) nor supplies a witness by template alone.

\[
\neg\mathsf{BridgePreregistered}(B^{(2)}_{\rm PSR\text{-}S2})
\land
\neg\mathsf{WitnessPresented}(\mathcal W_{S2})
\land
\neg\mathsf{AuthorizeExecution}(B^{(2)}_{\rm PSR\text{-}S2}).
\tag{PREPARATION-ONLY}
\]

A future package cannot execute merely because it fills textual fields. It must contain actual, independently checkable artifacts and pass a later frozen preflight.

---

## 1. Required concrete witness package

A future proposed witness package must provide one complete finite tuple:

\[
\mathcal W_{S2}=
\langle
\mathcal T,
\Gamma,
\mathcal A,
\Pi,
I,
r,
H,
\mathsf{PubPattern},
\lambda,
\mathsf{Decide},
E_1,E_2,
\mathcal R,
\mathcal C
\rangle.
\tag{WITNESS-TUPLE}
\]

Nothing in this document stipulates any component into existence. The following sections state what the supplier must furnish for each component.

---

## 2. Independent public target and reference provenance

### 2.1 Public subject matter \(\mathcal T\)

Provide a finite, typed public target \(\mathcal T\), including:

\[
\langle
\text{target identifier},
\text{carrier and relation vocabulary},
\text{target boundary},
\text{public location/access route},
\text{target-independent provenance source}
\rangle.
\tag{TARGET-REQUIREMENTS}
\]

The target must exist independently of PSR labels, the desired verdict, the PSR truth/error patterns, and the bridge's eventual decision rule.

### 2.2 Reference source \(\Gamma\)

Supply an independently public derivation route:

\[
\Gamma:
\mathcal T
\longrightarrow
\mathcal A,
\tag{REFERENCE-SOURCE}
\]

where \(\mathcal A\) is a finite typed assertion subject matter. \(\Gamma\) must identify the source artifacts, extraction method, relevant timestamps, access rights, and provenance chain. It may not be chosen after viewing the bridge verdict or by decoding PSR content labels.

The following are insufficient on their own:

\[
\mathsf{PreRegistered}(\lambda)
\land
\neg\mathsf{PSRGenerated}(r)
\not\Rightarrow
\mathsf{IndependentTargetProvenance}(\lambda,\mathcal T).
\tag{NO-DECODER-SHORTCUT}
\]

---

## 3. Typed claim/aboutness channel

For every proposed PSR presentation/content pair \((p,o)\), supply a typed assertion token \(a\) and an explicit reference relation:

\[
\mathsf{ClaimsAbout}(p,o,a,\mathcal T)
\subseteq
\mathbf P\times\mathbf O\times\mathbf A\times\mathbf T.
\tag{CLAIM-CHANNEL-TYPE}
\]

The package must specify, before acquisition, at least these two records:

\[
\begin{array}{c|c|c|c}
\textbf{presentation} & \textbf{content} & \textbf{assertion token} & \textbf{public subject matter}\\
\hline
p_t & o_{\rm true} & a_t & \mathcal T\\
p_e & o_{\rm false} & a_e & \mathcal T
\end{array}
\tag{CLAIM-CHANNEL-TABLE}
\]

For each row, specify the assertion's exact finite content and the independently derived condition on \(\mathcal T\) under which it is correct. Neither a presentation label nor the PSR-internal \(\mathsf{Matches}_{\rm PSR}\) relation may serve as the assertion or reference channel.

---

## 4. Nonvacuous prediction and target-derived representation

The package must state a target-derived representation procedure:

\[
\mathsf{TargetPattern}_{\Gamma}:
\mathcal A\to\mathbf P_{\rm pub},
\tag{TARGET-PATTERN}
\]

and a content/reference map whose provenance is shown rather than merely declared:

\[
\lambda_{\Gamma}:
\{o_{\rm true},o_{\rm false}\}
\to
\mathbf P_{\rm pub}.
\tag{REFERENCE-MAP}
\]

The supplier must demonstrate, using \(\Gamma\), why:

\[
\lambda_{\Gamma}(o)
=
\mathsf{TargetPattern}_{\Gamma}(a)
\quad
\text{for the asserted }a\text{ associated with }(p,o),
\tag{PROVENANCE-IDENTITY}
\]

rather than assigning a preferred public pattern to a PSR label.

A prediction is nonvacuous only if its negation has a determinate, predeclared possibility:

\[
\begin{aligned}
&\mathsf{Predicts}(a_t,\mathsf{match})
\land
\mathsf{Predicts}(a_e,\mathsf{mismatch}),\\
&\mathsf{PossibleUnderProtocol}(\mathsf{mismatch}\text{ for }a_t)
\land
\mathsf{PossibleUnderProtocol}(\mathsf{match}\text{ for }a_e).
\end{aligned}
\tag{NONVACUITY}
\]

A bridge whose target is stipulated to mirror the desired answer fails this requirement.

---

## 5. Acquisition, actual evidence, archive, and public access

Provide the frozen protocol \(\Pi\), its complete typed input bundle \(I\), and the resulting actual finite record \(r\):

\[
\mathsf{Acquire}_{\Pi}:I\to\mathbf R_{\rm pub},
\qquad
r=\mathsf{Acquire}_{\Pi}(I).
\tag{ACQUISITION}
\]

The package must include the input artifacts, acquisition timestamps, instrumentation or collection description, integrity checks, and a provenance chain showing why \(r\) bears on \(\mathcal T\).

Before any evaluator sees a bridge verdict, the package must supply a public archive record \(H\):

\[
H=
\langle
\mathsf{Hash}(r),
\mathsf{Timestamp},
\mathsf{ArchiveLocation},
\mathsf{AccessMethod},
\mathsf{VersionHistory}
\rangle.
\tag{ARCHIVE-RECORD}
\]

The archive must make the raw record, protocol, target-source artifacts, and precommitment accessible to independent review. A nonpublic report about an alleged record is not an actual public finite entity.

---

## 6. Public projection and total decision procedure

The supplier must provide a complete public relation vocabulary and a total, deterministic projection:

\[
\mathsf{PubPattern}_{\Pi}:
\mathbf R_{\rm pub}	o\mathbf P_{\rm pub}.
\tag{PUBLIC-PROJECTION}
\]

It must list every allowed input form and state an outcome for malformed, missing, ambiguous, and out-of-domain data. It may not invoke PSR's internal matching/correctness predicates.

Provide a total decision procedure:

\[
\mathsf{Decide}_{\Pi}:
\mathbf P_{\rm pub}\times\mathbf P_{\rm pub}
\to
\{\mathsf{match},\mathsf{mismatch},\mathsf{inconclusive}\}.
\tag{TOTAL-DECISION}
\]

The package must define the composite control predicate rather than leave it as prose:

\[
\begin{aligned}
\mathsf{ControlsPass}_{\Pi}(\mathcal W_{S2})
\iff{}&
C_1\land C_2\land C_3\land C_4\land C_5\\
&\land C_6\land C_7\land C_8\land C_9\land C_{10},
\end{aligned}
\tag{CONTROLS-PASS}
\]

where each \(C_i\) has an explicit typed input, expected output, and failure disposition.

---

## 7. Independent reconstruction roles

Name two non-overlapping audit teams \(E_1,E_2\), and provide evidence for their independence relative to the acquisition team and each other:

\[
\mathsf{Independent}(E_1,E_2,\Pi)
\land
\mathsf{Independent}(E_1,\mathsf{AcquisitionTeam},\Pi)
\land
\mathsf{Independent}(E_2,\mathsf{AcquisitionTeam},\Pi).
\tag{AUDITOR-INDEPENDENCE}
\]

Each team must reconstruct \(\mathsf{PubPattern}_{\Pi}(r)\) from archived materials, under blinded presentation names and before receiving the registered expected verdict. The package must contain their independently produced outputs and timestamps.

\[
\mathsf{PubPattern}^{E_1}_{\Pi}(r)
=
\mathsf{PubPattern}^{E_2}_{\Pi}(r)
=
\mathsf{PubPattern}_{\Pi}(r).
\tag{RECONSTRUCTION-AGREEMENT}
\]

Failure, disagreement, or unavailable independence evidence gives \(\mathsf{inconclusive}\), never a pass.

---

## 8. Minimum adversarial-control suite

The future package must define and execute these controls, plus any target-specific controls demanded by \(\mathcal T\):

\[
\begin{array}{c|l|l}
\textbf{control} & \textbf{manipulation} & \textbf{required disposition}\\
\hline
C_1 & \text{true assertion against target-derived record} & \mathsf{match}\\
C_2 & \text{false assertion against the same record} & \mathsf{mismatch}\\
C_3 & \text{swap public reference assignments} & \mathsf{fail}\text{ the prediction}\\
C_4 & \text{delete a target-relevant relation/input} & \mathsf{mismatch}\text{ or }\mathsf{inconclusive}\\
C_5 & \text{accepted PSR isomorphic alias} & \text{same result at the quotient class}\\
C_6 & \text{rejected code as articulation} & \text{typed rejection; no verdict}\\
C_7 & \text{blinded presentation names} & \text{unchanged reconstruction result}\\
C_8 & \text{missing archive/provenance/access} & \mathsf{inconclusive}\\
C_9 & \text{reference-source or decoder shift} & \mathsf{fail}\text{ unless a fresh docket is used}\\
C_{10} & \text{target-negating or prediction-reversing record} & \text{registered negative result}
\end{array}
\tag{MINIMUM-CONTROLS}
\]

---

## 9. Later preflight gate

A later fresh B2 preregistration may use the supplied package only if every component above is actual, typed, frozen, and source-statically verifiable. Its preflight must include at least:

\[
\begin{aligned}
\mathsf{Preflight}_{S2}(\mathcal W_{S2})
\iff{}&
\mathsf{TypedWitness}_{S2}(\mathcal W_{S2})
\land\mathsf{ActualPublicTarget}(\mathcal T)
\land\mathsf{IndependentTargetProvenance}(\Gamma,\mathcal T)\\
&\land\mathsf{ClaimsAboutDefined}(p_t,o_{\rm true},a_t,\mathcal T)
\land\mathsf{ClaimsAboutDefined}(p_e,o_{\rm false},a_e,\mathcal T)\\
&\land\mathsf{NonvacuousPredictionDefined}
\land\mathsf{ActualPublicEntity}(r)
\land\mathsf{ArchiveValid}(H,r)\\
&\land\mathsf{ProjectionTotal}(\mathsf{PubPattern}_{\Pi})
\land\mathsf{DecisionTotal}(\mathsf{Decide}_{\Pi})\\
&\land\mathsf{IndependentReconstructionEvidence}(E_1,E_2,r)
\land\mathsf{ControlsPassDefined}.
\end{aligned}
\tag{LATER-PREFLIGHT}
\]

No bridge is authorized merely because \(\mathsf{Preflight}_{S2}\) is syntactically stated. The later B2 packet must independently verify it on the actual submitted \(\mathcal W_{S2}\).

---

## 10. Residual boundary

Supplying a witness package would create a potential input for later review. It would not itself establish a public truth/error bridge, a general correspondence theory, nonbrute instantiation, selector discharge, or zero residue:

\[
\mathsf{WitnessPresented}(\mathcal W_{S2})
\not\Rightarrow
\mathsf{PreflightPass}_{S2}
\not\Rightarrow
\mathsf{S2Pass}
\not\Rightarrow
\mathsf{ZRPass}.
\tag{WITNESS-LIMITS}
\]

Any change to the eventual B2 claim channel, target, source/provenance, acquisition protocol, projection, decision rule, controls, or scope must occur before B2 is frozen. After B2 is frozen, such a change requires another fresh bridge preregistration.
