# GA1 — Coherence / Non-Contradiction Boundary Audit v1
## Formal specification

## Status and question

GA0 has fixed genuine aspecthood as a semantic/metaphysical target predicate rather than realization, grammar membership, a gauge quotient, or context membership. GA1 asks a narrower question:

> What exactly does coherence/non-contradiction exclude, and why is it necessary but insufficient for a genuine finite determination of the ground?

This is an exclusion and non-entailment audit. It neither supplies \(\mathsf{Det}_{G}\) nor revises the protected identity package.

## 1. Typed finite-content semantics

Fix a declared finite content language \(\mathcal L\), an interpretation class \(\mathfrak I\), and a finite proper context \(c\). A candidate \(a\) has a finite asserted content set \(\Gamma_c(a)\subseteq\mathcal L\). The subscript matters: the same formula token in a different typed context need not have the same role.

The primary coherence predicate is semantic satisfiability:

\[
\mathsf{Coh}_{\mathcal L,\mathfrak I,c}(a)
\;:\\Longleftrightarrow\;
\exists I\in\mathfrak I\;\bigl(I\models \Gamma_c(a)\bigr).
\tag{Coh}
\]

The audit uses a finite classical bivalent fragment only as an executable witness class. In that fragment, a direct contradiction is a pair \(p,\neg p\) at the **same declared content position** (same predicate, arguments, index, respect, and context). A change in time, context, relata, or sense is not silently collapsed into a contradiction.

For a sound and complete proof calculus for \(\mathfrak I\), satisfiability can be checked syntactically:

\[
\mathsf{Coh}(a)
\Longleftrightarrow
\Gamma_c(a)\not\vdash \bot.
\]

Without a stated soundness/completeness bridge, the syntactic condition is only a fallible or partial test, not the definition of coherence.

## 2. Scope of the coherence filter

Under (Coh), an incoherent candidate is excluded precisely when its asserted finite content cannot be jointly satisfied in the declared interpretation class and context. In the executable fragment, this excludes:

1. direct incompatible determinations, \(p\land\neg p\), at one content position;
2. contradictions reached through declared constraints, not only visibly adjacent formula pairs; and
3. an alleged finite articulation whose declared content has no interpretation in the allowed typed class.

It does **not** by itself exclude a coherent but merely formal construction, a coherent fiction, a coherent rival ontology, a coherent restricted domain, a coherent content with an ungrounded selector, or a coherent description that fails to determine the one ground’s nature.

Coherence is therefore a negative admissibility filter. It is not an actuality rule, an identity bridge, a realization rule, or a criterion of \(\mathsf{Det}_{G}\).

## 3. Necessity bridge, stated rather than smuggled in

GA1 tests the following explicit framework-level bridge:

\[
\mathsf{NCD}:\qquad
\mathsf{GA}(a)\Rightarrow
\exists I\in\mathfrak I\;\bigl(I\models\Gamma_c(a)\bigr).
\tag{NCD}
\]

Its rationale is limited. A genuine finite determination in complete non-representational self-knowledge must be determinately articulable *as that finite content*; it cannot both assert and deny one identical determination in one respect and context. From NCD and (Coh):

\[
\mathsf{GA}(a)\Rightarrow\mathsf{Coh}(a).
\tag{GA-Coh}
\]

NCD is not derived from bare formal logic, nor does it ban ambiguity, finite partiality, tension between different contexts, or the use of non-classical calculi. It says only that a candidate counted as one determinate finite content must be satisfiable under its own explicitly declared content semantics.

A paraconsistent or dialetheic rival may reject NCD or replace the satisfaction relation. Such a move is a live rival semantic architecture, not a contradiction established by this audit. It must then state what makes a contradictory content one determinate self-presentation rather than an inconsistent description.

## 4. Structural base and independence target

Let the GA1 structural reduct be

\[
B=(A,\Gamma,\mathsf{Coh},\mathsf{NG},\mathsf{Ctx}),
\]

where \(A\) is a finite candidate set. Neither \(\mathsf{GA}\) nor \(\mathsf{Det}_{G}\) is in \(B\). GA0 establishes that these are not to be identified with any coordinate of that reduct.

The required executable witnesses are:

| Witness | Candidate content | \(\mathsf{Coh}\) | \(\mathsf{NG}\) | \(\mathsf{Ctx}\) | Intended audit role |
|---|---|---:|---:|---:|---|
| \(a_{\bot}\) | \(\{p,\neg p\}\) | no | yes | no | incoherence is rejected by NCD; it also cannot enter an admissible proper context |
| \(a_{d}\) | \(\{p\}\) | yes | yes | yes | coherent structural candidate that may be determinate |
| \(a_{f}\) | \(\{q\}\) | yes | yes | yes | matched coherent structural candidate with no determination bridge |
| \(a_{g}\) | \(\{r\}\) | yes | no | yes | coherence does not discharge gauge criterion |
| \(a_{x}\) | \(\{s\}\) | yes | yes | no | coherence does not discharge context criterion |

The two target expansions have the same reduct \(B\) and same \(\Gamma\), \(\mathsf{Coh}\), \(\mathsf{NG}\), and \(\mathsf{Ctx}\) facts:

\[
\begin{array}{c|cc}
 & \mathsf{Det}_{G} & \mathsf{GA}\\
\hline
M_{+} & \{a_d\} & \{a_d\}\\
M_{-} & \varnothing & \varnothing
\end{array}
\]

Both satisfy NCD. Thus the structural data do not entail that *any* candidate is a genuine aspect, and in particular:

\[
\mathsf{Coh}(a)\land\mathsf{NG}(a)\land\mathsf{Ctx}(a)
\not\models
\mathsf{Det}_{G}(a),
\qquad
\mathsf{Coh}(a)\land\mathsf{NG}(a)\land\mathsf{Ctx}(a)
\not\models
\mathsf{GA}(a).
\tag{GA1-NE}
\]

This is a logical non-entailment result about the typed structural base. It does not establish that \(M_-\) is the true metaphysics, nor that \(a_f\) is actually a fiction; it shows that a semantic determination bridge cannot be recovered from the structural predicates alone.

## 5. Assertions

The executable audit must verify:

1. \(a_{\bot}\) is unsatisfiable in the declared finite semantics.
2. Each of \(a_d,a_f,a_g,a_x\) is satisfiable.
3. NCD excludes \(a_{\bot}\) from \(\mathsf{GA}\) in every listed expansion.
4. Both expansions preserve the entire structural reduct and satisfy NCD.
5. \(a_d\) has \(\mathsf{Coh}\land\mathsf{NG}\land\mathsf{Ctx}\) in both expansions but is genuine only in \(M_+\).
6. Coherence alone also fails to imply \(\mathsf{NG}\) or \(\mathsf{Ctx}\), via \(a_g\) and \(a_x\).
7. No assertion treats coherence as realization, persistence, public-record structure, phenomenality, physical law, or a general all-world possibility principle.

## 6. Pass criterion and limits

GA1 passes if it establishes the exact conditional necessity result (GA-Coh), the stated semantic scope of the coherence filter, and the matched-expansion non-entailments (GA1-NE).

It fails if it: (i) defines genuine aspecthood by coherence; (ii) silently adds \(\mathsf{Det}_{G}\) to the structural base; (iii) claims that a finite countermodel settles metaphysical truth; (iv) treats classical consistency as the only possible logic; or (v) reopens realization selection, directedness, persistence, public records, or physics.

A successful GA1 leaves GA2 as the load-bearing positive task: give and defend the semantic content of \(\mathsf{Det}_{G}\) without reifying \(G\), treating formal grammar as ground structure, or defining aspecthood by realization.
