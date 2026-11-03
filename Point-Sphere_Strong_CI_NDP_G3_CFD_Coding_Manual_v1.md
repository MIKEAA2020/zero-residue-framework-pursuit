# G3/CFD Coding Manual v1
## Frozen translation from neutral local-experience reports to complete finite profiles

## Status

**Pre-registered coding manual. No report has been coded under this manual.** This manual implements the v2 calibration protocol and must be frozen before any confirmatory corpus is examined.

The manual translates only report-level information into a finite profile:

\[
\Pi=\langle\bar S,\bar E,Q,H,B\rangle.
\]

It does not identify metaphysical subjects, aspects, grounds, realization, nondual identity, or causal relations.

## 1. Two distinct input records

Each enrolled episode \(\alpha\) produces two records before analysis:

\[
R^{\rm raw}_{\alpha}
\quad\text{and}\quad
R^{\rm struct}_{\alpha}.
\]

### 1.1 Raw narrative record

\(R^{\rm raw}_{\alpha}\) is the participant's answer to the neutral narrative prompt:

> “Describe one brief, immediate experience in ordinary words. Include only what you experienced, any qualities that were present, and any changes or order you noticed.”

No framework vocabulary may be introduced by the interviewer.

### 1.2 Structured completion record

\(R^{\rm struct}_{\alpha}\) is a participant-completed neutral clarification form. It is required solely to determine whether a complete finite diagram is possible. It asks:

1. **Qualities:** “List the qualities you explicitly experienced in this episode, using your own ordinary words.”
2. **Phases:** “Was there one undivided moment, or distinguishable moments? If distinguishable, label them in the order you noticed them.”
3. **Perspective/locus:** “Did the report involve one experienced point of view, more than one explicitly distinct point of view, or were you unsure?”
4. **Quality-by-phase matrix:** for each participant-listed quality and phase: “Was this quality present in this moment? yes / no / unsure.”
5. **Order matrix:** for each pair of participant-listed phases: “Did the first occur before the second? yes / no / unsure.”
6. **Locus assignment:** for each affirmed quality-by-phase entry: “Was this presented at the same point of view as another affirmed entry, a distinct explicitly experienced point of view, or unsure?”
7. **Completeness check:** “Is there any reported quality, phase, or explicit point of view in this episode that the form has not represented? yes / no / unsure.”

The form must not mention graph, connectedness, Core, aspect, mode, nondual theory, participation, or a predicted classifier outcome.

## 2. Separation from phenomenal certification

The phenomenal classifier sees \(R^{\rm raw}_{\alpha}\) but not diagrams, field-profile labels, or CFD predictions. The diagram coder sees \(R^{\rm raw}_{\alpha}\) and \(R^{\rm struct}_{\alpha}\), but not the classifier's \(K1\)--\(K4\) answers or certification status.

The structured form is a coding instrument, not a field-certification instrument. In particular, the coder may not use any answer to “one local presentation rather than a list” because that question belongs only to the independent phenomenal-classification record.

## 3. Slot construction

### 3.1 Quality constants

For every distinct participant-listed quality expression, introduce one rigid active constant:

\[
q_i\in Q_A.
\]

The initial token is the normalized verbatim expression, not an inferred scientific, metaphysical, or colour-category translation. For example:

\[
\text{“bright red”}\mapsto \mathbf{bright\_red},
\qquad
\text{“warm pressure”}\mapsto \mathbf{warm\_pressure}.
\]

Synonym collapse is not permitted in confirmatory coding unless the participant explicitly identifies two expressions as the same quality. Otherwise, retain distinct constants and log the expressions.

### 3.2 Phase slots

If the participant reports one undivided moment, introduce one phase slot:

\[
e_1\in E_A.
\]

If the participant lists distinct moments, introduce one phase slot per listed moment in the stated order:

\[
e_1,\ldots,e_n\in E_A.
\]

Distinct named phases are coded as distinct only when the participant marks them distinct in the structured form. Any “unsure” response makes the episode incomplete/out of scope.

### 3.3 Presentation-locus slots

A subject-slot is used here only as a **reported presentation-locus role**. It is not a claim about a metaphysical self, ego, substance, observer, or external object.

If the participant reports one point of view or no explicit multiplicity of points of view, introduce one default local locus:

\[
s_1\in S_A.
\]

If the participant reports \(k>1\) explicitly distinct presentation loci, introduce:

\[
s_1,\ldots,s_k\in S_A.
\]

A default local locus does not certify that the episode is one phenomenal field. It is only the report-relative bearer role for entries in the structured quality-by-phase table. Field certification remains blinded and independent under the protocol.

If the participant is unsure whether two loci are same or distinct, the episode is incomplete/out of scope.

## 4. Literal coding rules

### 4.1 Positive and negative \(\mathsf{HasAt}\) entries

For every active triple:

\[
(s_i,q_j,e_k)\in S_A\times Q_A\times E_A,
\]

enter:

\[
+\mathsf{HasAt}(s_i,q_j,e_k)
\]

only if the structured matrix says “yes” and the locus assignment associates the presentation with \(s_i\).

Enter:

\[
-\mathsf{HasAt}(s_i,q_j,e_k)
\]

only if the structured matrix says “no” for that phase and the locus assignment is determinate.

Any “unsure,” missing, or nonunique locus assignment makes the report incomplete/out of scope. The coder may not infer negatives from silence in the raw narrative.

### 4.2 \(\mathsf{Before}_{\Phi}\) entries

For each ordered pair of distinct active phases \((e_i,e_j)\), enter:

\[
+\mathsf{Before}_{\Phi}(e_i,e_j)
\]

only if the participant marks “yes.” Enter the negative literal only if the participant marks “no.” “Unsure” makes the report incomplete/out of scope.

Irreflexive negatives are supplied by the frozen background theory:

\[
-\mathsf{Before}_{\Phi}(e_i,e_i).
\]

If reported pairwise order assignments violate transitivity or irreflexivity, the item is recorded as semantically inconsistent and is excluded from confirmatory scoring. It may be retained, with no recoding, in an error log.

### 4.3 Equality and disequality

Use equality only for explicitly stated co-reference of active presentation loci or phases. The coding system must decide every active same-sort equality/disequality claim.

- An explicitly distinct listed phase/locus receives a disequality literal.
- Explicit co-reference receives an equality literal.
- An “unsure” same/different response makes the report incomplete/out of scope.

The coder may not identify slots merely because two descriptions resemble one another.

## 5. Completeness decision

A report receives a complete diagram only when all conditions hold:

\[
\begin{array}{ll}
C1 &: \text{all report-listed qualities, phases, and presentation loci are represented};\\
C2 &: \text{every active }\mathsf{HasAt}\text{ triple has yes/no coding};\\
C3 &: \text{every active phase-order pair has yes/no coding};\\
C4 &: \text{every active same-sort equality claim is decided};\\
C5 &: \text{the diagram is satisfiable under }T_A;\\
C6 &: \text{the coding uses no unreported enrichment.}
\end{array}
\]

If any condition fails:

\[
\mathsf{OutOfScope}_{\rm incomplete}(\alpha).
\]

An out-of-scope decision is neither a field nor a non-field prediction and is not a mismatch.

## 6. Profile extraction and classifier computation

For a complete diagram \(m\), form:

\[
\Pi(m)=\langle\bar S,\bar E,Q,H,B\rangle,
\]

by quotienting active locus and phase slots under forced equality. Set:

\[
H([s_i],q_j,[e_k])
\Longleftrightarrow
T_A\cup m\models\mathsf{HasAt}(s_i,q_j,e_k),
\]

and:

\[
B([e_i],[e_j])
\Longleftrightarrow
T_A\cup m\models\mathsf{Before}_{\Phi}(e_i,e_j).
\]

The automated verdict engine, not the coder, then computes:

\[
\mathsf{Core}^{\rm cmp}(m)=
\mathsf{Complete}(m)
\land
\mathsf{Supported}(m)
\land
\mathsf{Unified}(m).
\]

The coder is not told this result before the coding table is locked.

## 7. Global-context items

The atomistic-rival comparison is available only for reports that explicitly describe a jointly presented complex with separable subpresentations.

For those items, code a global complete context diagram:

\[
\delta_c
\]

which records all reported shared loci, shared phases, and cross-mode order relations. Do not create a global context merely by aggregating unrelated reports.

Each local submode and the global context must independently pass the complete-diagram rules. The global profile is extracted from \(\delta_c\), not from arbitrary model enrichment.

## 8. Reliability and audit trail

Every coded item must retain:

\[
\langle
\text{raw record},
\text{structured record},
\text{active frame},
\text{literal table},
\text{completeness result},
\text{exclusion result}
\rangle.
\]

For duplicate-coding reliability, second coders receive the same inputs and manual but no first-coder materials. All deviations, corrections, and version changes are logged. No rule change may enter the confirmatory analysis after the first valid item is coded.

## 9. Limits

This manual may create a high out-of-scope rate because it demands complete finite diagrams. That outcome is informative about the scope of the proposed G3 selector; it is not a warrant to relax the completion rule after seeing reports.

The default-locus convention is a declared formal choice. It does not prove that all local experience has one subject, nor that shared locus is sufficient for phenomenal unity. Those are precisely among the substantive adequacy questions the calibration tests.

## Nonclaims

This manual does not claim that raw reports directly reveal metaphysical aspecthood, that any quality token names an objective property, that phenomenality is reducible to this profile, or that a valid coding result establishes a correct framework of whole reality.
