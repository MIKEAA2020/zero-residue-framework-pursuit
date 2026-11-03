# Strong CI Adjudication — CI0B Relation and Necessity Typing Audit v1
## Preventing equivocation before terminal-structure comparison

## Status

**CI0B completed as a vocabulary freeze.** It does not eliminate a framework. It specifies what every CI1–CI7 dossier must mean by “follows,” “requires,” “explains,” “necessary,” “real,” “aspect,” and “same framework.”

## 1. Typed relations

| Symbol | Typed role | It does not by itself establish |
|---|---|---|
| \(\Gamma\vdash_L p\) | Formal derivability in explicitly declared logic \(L\) | metaphysical grounding, actuality, truth of \(\Gamma\), or ontology |
| \(K\models p\) | Cross-model semantic entailment: every model of \(K\) satisfies \(p\) | that one named item occurs in a different theory, intrinsic explanation, or realization |
| \(p\prec_F q\) | Candidate-relative metaphysical grounding/dependence: \(p\) grounds \(q\) | logical entailment, temporal causation, or universal transitivity |
| \(\mathsf{Expl}_F(p,q)\) | \(p\) explains why \(q\) obtains under \(F\) | that \(p\) is ultimate or that no further explanation is required |
| \(\mathsf{Ess}_F(G)\) | Complete intrinsic nature claimed for an ultimate \(G\) | absolute simplicity, awareness, goodness, or a finite output |
| \(\mathsf{IntrReq}^{F,M}_G(a)\) | Given \(F\)'s fixed intrinsic nature in model \(M\), removing \(a\) changes that nature or makes its alleged self-presentation incomplete | cross-model necessity \(K\models a\), a particular grammar, or realization unless a separate identity bridge is stated |
| \(R_F(a)\) | \(a\) is real/realized in \(F\) | that \(a\) is genuine, intrinsic, a mode, or physically instantiated |
| \(\mathsf{GA}_F(a)\) | \(a\) is a genuine finite aspect/determination under \(F\) | that it is a grammar item, a gauge class, or selected by realization |
| \(a\sim_F b\) | \(a,b\) are the same framework-content under a declared representation/gauge/duality equivalence | literal syntactic identity or sameness merely because both share one ground |

No claim may move from one row to another without an explicitly named bridge.

## 2. Four different senses of necessity

The word “necessary” is a recurrent source of false derivations. The programme freezes four non-equivalent senses.

### N1 — formal necessity

\[
\vdash_L p.
\]

A theorem of the declared calculus. This cannot by itself entail that reality instantiates \(p\).

### N2 — theory-wide semantic necessity

\[
K\models p.
\]

Every model of a fully specified theory \(K\) satisfies \(p\). If the theory leaves finite contents open, completeness within each model does not imply that one fixed candidate occurs in all models.

### N3 — core-relative intrinsic necessity

\[
\mathsf{IntrReq}^{F,M}_G(a).
\]

A content is inseparable from the nature the candidate itself attributes to \(G\). This may be a legitimate internal identity claim, but it is not neutral: the candidate must disclose whether it is a core stipulation, a conceptual analysis, or a derived result.

### N4 — metaphysical necessity

\[
\Box_R p.
\]

\(p\) holds across the framework’s admissible reality space. A dossier must state that space and show why it is not merely a renamed list of actual facts.

These invalid inferences are prohibited unless bridges are supplied:

\[
K\models p\not\Rightarrow \mathsf{IntrReq}^{F,M}_G(p),
\]

\[
\mathsf{IntrReq}^{F,M}_G(p)\not\Rightarrow \Box_Rp,
\]

\[
\Box_Rp\not\Rightarrow \mathsf{Expl}_F(\mathsf{Ess}_F(G),p),
\]

\[
\mathsf{Expl}_F(\mathsf{Ess}_F(G),p)\not\Rightarrow R_F(p).
\]

## 3. Explanation versus grounding versus self-intelligibility

A framework may use grounding, explanation, or intrinsic intelligibility differently. It must choose and state its relation profile.

### 3.1 Grounding profile

If \(\prec_F\) is used, the dossier must say whether it is asserted to be asymmetric, irreflexive, transitive, hyperintensional, or non-monotonic. It may not call literal self-grounding an explanation where its own relation is irreflexive.

### 3.2 Explanation profile

\(\mathsf{Expl}_F(p,q)\) must include an explanatory difference-maker. The following are not sufficient without further content:

- \(q\) because \(q\) is necessary;
- \(q\) because it is in the nature of \(G\);
- \(q\) because the whole explains itself;
- \(q\) because an ultimate agent freely chooses \(q\).

Each may become an explanation only after the candidate supplies a non-circular account of the necessity, nature, whole, or agency invoked.

### 3.3 Self-intelligibility profile

The permitted target is not reflexive grounding but:

\[
\mathsf{SelfInt}_F(G):
\quad
\mathsf{Ess}_F(G)
\text{ makes the existence/profile of \(G\) intelligible without an external ultimate source.}
\]

A framework claiming \(\mathsf{SelfInt}_F(G)\) must say what makes this more than a bare terminal label. This is CI1’s central burden.

## 4. The “all logic” clarification

“All logic” means every valid inference licensed by a declared logic \(L\). It does **not** silently add:

\[
\mathsf{PSR},
\quad
\mathsf{SCI},
\quad
\text{composition reflection},
\quad
\text{intelligibility}\Rightarrow\text{awareness},
\quad
\text{order}\Rightarrow\text{goodness},
\quad
\text{goodness}\Rightarrow\text{plenitude}.
\]

Those may be adopted and argued as metaphysical bridges. They are not demoted; they are made available for rigorous assessment rather than being treated as tautologies.

## 5. Source-tagging rule

Every nontrivial premise and conclusion in the programme must have one source tag:

| Tag | Meaning |
|---|---|
| **Core** | Explicit protected commitment of a candidate framework |
| **Logic** | Derived in declared calculus \(L\) |
| **Semantics** | Follows from a declared satisfaction or identity condition |
| **Bridge** | Metaphysical principle requiring independent defense |
| **Fidelity** | Supports fit to phenomenal or physical target only |
| **Empirical** | Supported by observation/experiment/data |

A Core claim can be used conditionally but cannot be advertised as Logic. A Bridge can be defended but cannot be silently treated as Core. This rule directly prevents both errors found in the updated transcript:

1. treating participatory creation as a consequence of CI; and
2. treating real finite modes as a derivation from a stripped theory that omits them.

## 6. Initial application to the leading rival families

| Family | Ultimate necessity claim requiring type | Relation claim requiring type |
|---|---|---|
| Contingent creator–creation | core-relative nature plus contingent act; not automatically necessary output | efficient creation / extrinsic act; selector bridge needed under SCI |
| Necessary determinate creation | \(\Box_R\) exact output must be shown essence-grounded | creation/production and exact-totality bridge |
| Neoplatonic emanation/plenitude | diffusive-goodness and all-possibilities-realized claims are Bridges unless defined as Core | necessary self-expression; hierarchy/domain/compossibility bridge |
| Leibnizian unique-best | unique-optimum claim is a Bridge | rational selection; proof of unique best required |
| Nondual real-aspect | intrinsic necessity may be Core within fixed nondual nature; cross-model necessity does not follow | identity/aspect relation; genuine-aspect and non-composition semantics required |
| Neutral/structural totality | necessity of ultimate structure requires intrinsic-intelligibility account | constitution/realization and phenomenal bridge required |
| Principled infinitism | whole-series principle must be typed as more than a restated totality | explanation of infinite pattern and its explanatory closure |

## 7. CI0B result

The phrase

\[
\text{“CI in its strongest sense plus all logic determines the framework”}
\]

is now usable only as a research hypothesis with a specified meaning:

\[
\text{Given SCI, declared bridges, an equivalence-controlled exhaustive rival space, and successful dossiers, a unique conditional survivor may be established.}
\]

It is not yet a theorem, and no candidate is selected at CI0B.

## Next node

**CI1 — terminal-structure audit** will test the claim that only a self-intelligible ultimate can meet SCI. It must consider brute, regress, circle, necessary totality, plural roots, and self-intelligible profiles under the same typed explanation rules. It may not assume in advance that self-intelligibility entails simplicity, awareness, goodness, or a creator/emanation/aspect relation.
