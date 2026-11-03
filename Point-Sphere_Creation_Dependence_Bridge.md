# Creation–Dependence Bridge v1
## A modal, non-competitive model of real creation and an exact C-Nec/C-Cont fork

## Result in one sentence

This bridge does not prove that creation occurs. It establishes a cleaner result: **real, distinct, dependent creatures can be modelled without making the ground a competing physical cause; and any such model must state where the determination of the created totality comes from.** Under explicit assumptions, the options are necessary realisation, a further contingent selector, or rejection of real numerical distinctness.

That is a genuine improvement over treating “creation,” “expression,” “emanation,” and “appearance” as interchangeable words.

---

## 1. The problem to solve

A creation claim must meet four conditions simultaneously.

1. **Reality:** creatures are not merely apparent or fictitious.
2. **Distinctness:** creatures are numerically distinct from the ground and are not parts that complete it.
3. **Dependence:** creatures have no independent actuality; their existence depends asymmetrically on the ground.
4. **Non-competition:** ground-level dependence does not become a second physical cause alongside creaturely causes, and therefore does not overwrite established causal models.

A fifth issue then arises:

5. **Determination:** what makes this derivative totality actual rather than another admissible totality, or rather than none?

The first four can be given a coherent two-sorted semantics. The fifth produces the exact fork between **necessary creation** and **contingent creation**.

---

## 2. Two-sorted modal semantics

Let
\[
\mathfrak M=(W,\mathcal R,w_*,g,\{D_w,\mathsf C_w,\mathsf G_w,\sigma_w\}_{w\in W})
\]
be a modal creation model.

- \(W\) is a non-empty set of metaphysically admissible worlds, with accessibility \(\mathcal R\). Nothing below requires a particular modal logic beyond the inferences explicitly stated.
- \(w_*\) is the actual world.
- \(g\) is a distinguished ground individual, present in every world:
  \[
  \forall w\in W\quad g\in D_w.
  \]
- \(D_w^C\subseteq D_w\setminus\{g\}\) is the domain of derivative creatures or creaturely bearers at \(w\).
- \(\mathsf C_w\) is the intraworld causal structure: a structural causal model, process theory, or other physical causal account defined only over derivative variables.
- \(\mathsf G_w\) is a **grounding relation**, typed differently from \(\mathsf C_w\). It relates ground-level facts to existential facts, not one event in spacetime to another.
- \(\sigma_w\) is a world-level realisation parameter: it specifies which admissible derivative totality is realised at \(w\). It may be necessary, contingent, primitive, or itself grounded; the model must say which.

Let \(\mathcal T\) be a class of admissible derivative totalities. Write
\[
T_w=\operatorname{Realise}(\sigma_w)\in\mathcal T.
\]
A totality includes its derivative entities, events, laws, and causal organisation at the relevant description level.

### 2.1 Conditions for literal participatory creation

A model has **literal participatory creation** when the following conditions hold.

**R1 — Ground necessity.** The ground exists in every admissible world:
\[
\Box\operatorname{Ex}(g).
\]

**R2 — Creature distinctness.** For every \(x\in D_w^C\),
\[
x\neq g.
\]
Creatures are not identical with the ground, nor merely parts whose existence composes the ground.

**R3 — Asymmetric existential dependence.** For every creature \(x\) and its existence fact \(\operatorname{Ex}_w(x)\),
\[
\mathsf G_w\bigl(g,\operatorname{Ex}_w(x)\bigr),
\]
and no creature or creaturely totality grounds \(\operatorname{Ex}(g)\).

**R4 — Non-competitive causation.** \(\mathsf G_w\) is not an edge, variable, or intervention in \(\mathsf C_w\). Creaturely causal queries are evaluated inside \(\mathsf C_w\); grounding answers why that causal model and its bearers are actual at all.

**R5 — Creaturely reality.** Creaturely variables have genuine causal roles in \(\mathsf C_w\), including under the model’s ordinary interventions. The framework does not make them merely apparent because they are dependent.

R1–R5 make creation an asymmetric dependence relation rather than a temporal change in the ground.

---

## 3. Coherence result: non-competitive creation is a conservative extension

### Theorem 1 — Conservative creation extension

Let
\[
\mathcal S=(V,U,F,\mu)
\]
be any consistent finite structural causal model for a derivative domain. There exists a two-sorted modal creation model \(\widehat{\mathcal S}\) satisfying R1–R5 such that every observational or intervention distribution expressible solely in the original vocabulary \(V\) is identical in \(\mathcal S\) and \(\widehat{\mathcal S}\).

#### Construction

For each world carrying \(\mathcal S\), retain the same \(V,U,F,\mu\) as \(\mathsf C_w\). Add a new ground individual \(g\), a grounding relation \(\mathsf G_w\), and existential facts for every bearer, power, and event-token represented by \(V\). Stipulate that \(g\) grounds these existential facts, but do not add \(g\) as a variable or parent in any structural equation in \(F\). Let the derivative variables retain exactly their original domains and intervention semantics.

#### Proof

All observational and intervention distributions over the original vocabulary are functions of \((V,U,F,\mu)\). The construction leaves these four components unchanged. Therefore every query formulated only with the original variables has the same value in both models. R1–R5 hold by construction: \(g\) is distinct from derivative variables, existential dependence is typed by \(\mathsf G_w\), and ordinary causal relations remain exactly those of \(\mathsf C_w\). \(\square\)

#### What this proves—and does not prove

It proves logical compatibility: a creation/dependence layer need not compete with finite empirical causal models. It does **not** prove that a ground exists, that the dependence relation is true, that all reality is covered by a finite SCM, or that creation makes any new empirical prediction.

This result solves one coherence problem: the framework can no longer treat “divine concurrence” as a rival physical mechanism while also claiming ordinary causal autonomy. It must be a typed, existential dependence relation or it is a different theory.

---

## 4. The determination problem

Real creation is not yet a full account. R1–R5 say that an actual derivative totality depends on the ground. They do not say why this totality is actual.

Let \(N_g\) denote the complete necessary nature of the ground as represented by a given theory. Let
\[
\mathsf{Act}(T)
\]
mean that derivative totality \(T\) is realised. The crucial question is whether \(N_g\) fully determines \(T\).

### Theorem 2 — Necessitating-selection lemma

If
\[
\Box N_g
\qquad\text{and}\qquad
\Box\bigl(N_g\rightarrow\mathsf{Act}(T)\bigr),
\]
then
\[
\Box\mathsf{Act}(T).
\]

#### Proof

In every accessible world, \(N_g\) holds. In every accessible world, \(N_g\) entails \(\mathsf{Act}(T)\). Hence \(\mathsf{Act}(T)\) holds in every accessible world. \(\square\)

This is elementary but decisive. If a necessary ground’s necessary, complete nature is claimed to be a sufficient contrastive explanation of one created totality, that totality is necessary. Calling the relation “identity,” “expression,” or “self-knowledge” does not avoid the result unless one of the modal premises is denied or qualified.

---

## 5. Three explicit creation models

### 5.1 C-Nec: necessary realisation

**C-Nec** adds a necessary realisation principle:
\[
\Box\forall T\in\mathcal A\,[\operatorname{Adm}(T)\rightarrow\mathsf{Act}(T)],
\]
or a different necessary rule selecting one totality \(T^*\) from \(\mathcal A\).

- If every admissible, compossible totality is realised, the model is a plenitude model.
- If one totality is necessarily selected, it is a determinate-necessity model.
- In either case, the totality-level result follows necessarily from the ground’s necessary nature and rule.

**Gain:** no unexplained contingent selector is added.

**Costs:** modal collapse pressure, a required admissibility/compossibility/measure theory, and—under plenitude—the actuality of every admissible finite harm. Contingency can survive only in a qualified sense: indexical location, internal conditional dependence, epistemic unpredictability, or non-fundamental descriptions. It does not survive as the metaphysical contingency of the totality fixed by the necessary rule.

### 5.2 C-Cont: contingent realisation

**C-Cont** denies the second premise of Theorem 2. The ground exists necessarily, but the realised derivative totality varies across admissible worlds:
\[
\Box N_g,
\qquad
\Diamond\mathsf{Act}(T_1),
\qquad
\Diamond\mathsf{Act}(T_2),
\qquad
T_1\neq T_2.
\]

A minimal semantic witness has two worlds, \(w_1,w_2\), with the same ground \(g\), but distinct realisation parameters:
\[
\sigma_{w_1}\neq\sigma_{w_2},
\qquad
T_{w_1}\neq T_{w_2}.
\]
At either world, R1–R5 can hold. Thus a necessary ground and genuinely contingent derivative reality are jointly consistent in this model.

The price is exact and unavoidable: \(\sigma_w\) must be accounted for.

1. If \(\sigma_w\) is a primitive contingent fact, the theory has a selection primitive.
2. If \(\sigma_w\) is a contingent act or relation of the ground, the theory must explain how this is compatible with simplicity, immutability, and any claim that the ground has no accidental states.
3. If \(\sigma_w\) is determined by reasons, values, or a free act, those are substantive additions that must not be relabelled as a derivation from bare completeness.
4. If \(\sigma_w\) has an independent source, the ground is no longer the sole full ground of the created totality unless the source is itself grounded or incorporated into the ground account.

C-Cont is therefore coherent, but it does not erase the contrastive question. It localises it in an explicit selector rather than hiding it behind “free creation.”

### 5.3 ND: strict numerical non-duality

A strict numerical non-dual model rejects R2 or R5 as applied to creatures. It does not posit genuinely distinct derivative beings in the same sense; plurality becomes perspectival, conventional, or appearance-like.

**Gain:** it avoids the selection and reception problem of literal real creation.

**Cost:** it assumes a different debt: explain bounded ignorance, stable public physics, intersubjective disagreement, suffering, agency, and the status of the apparent causal order without simply reinstating derivative reality under another name.

ND is not a version of C-Nec or C-Cont. It is an alternative to literal participatory creation.

---

## 6. A precise accounting result

### Proposition 3 — Creation accounting trilemma

Assume R1–R5, at least two admissible derivative totalities, and the demand that the realisation of the actual totality have a stated full ground. Then exactly one of the following must be supplied:

1. **Necessary determination:** the ground’s necessary nature plus a necessary realisation rule fully grounds the actual totality. This is C-Nec, and Theorem 2 makes its totality necessary.
2. **Further selector:** a contingent or non-necessitating selector co-grounds the actual totality with the ground. This is C-Cont, and the selector must be independently characterised and priced.
3. **Rejection of literal distinction:** derivative totalities are not genuinely distinct real beings in the R2/R5 sense. This is ND or another appearance ontology.

#### Why the trilemma is exhaustive under its assumptions

A full ground for the actual totality either is fully fixed by the necessary nature of \(g\), or it contains an element not so fixed. In the first case, necessary determination follows. In the second, that extra element is a selector in the broad sense: a fact, act, relation, reason, law, or co-ground distinguishing the realised totality. If the theory denies that there is a distinct derivative totality for the full-ground question to apply to, it has left literal creation.

The proposition does not prove one horn true. It prevents an equivocation: one cannot simultaneously claim (i) real distinct creation, (ii) no selection primitive or modal cost, and (iii) no necessary realisation rule.

---

## 7. Relevance to simplicity, concurrence, and freedom

### Simplicity

The semantics does not prove divine simplicity. It clarifies its pressure point. A C-Cont advocate who says that an immutable simple ground has different intrinsic volitions in different possible worlds owes an account of how those volitions are not accidental differentiations in the ground. A C-Nec advocate avoids that pressure by making the realised totality necessary, but accepts modal consequences.

A promising but unproved response is a **relational contingency model**: the ground is intrinsically invariant while contingent relational facts about creatures differ. That response still needs a theory of why a relation with no intrinsic change in the ground is sufficient to full-ground this rather than another creaturely totality. The model identifies the debt; it does not pay it by definition.

### Concurrence

The conservative extension theorem shows how concurrence can be non-competitive. Within a realised totality, creaturely powers and events retain their ordinary causal organisation. Grounding concerns existential actuality, not a second intervention in the same causal equations.

This gives a clean division:

- **existential question:** why is this causal system actual at all? — the grounding layer;
- **causal question:** why did this event occur rather than another under the system’s laws and inputs? — the intraworld model;
- **selection question:** why is this total causal system actual rather than another? — C-Nec or C-Cont’s additional bridge.

### Freedom

No creation model by itself supplies libertarian creaturely freedom.

- C-Nec is naturally compatible with compatibilist, structural, or indexical agency.
- C-Cont may create conceptual room for libertarian agency only if its selector and creaturely causal powers are formulated non-deterministically; it does not create that freedom automatically.
- ND relocates the question to conventional or perspectival agency.

This avoids an invalid inference from “the ground is not a competing cause” to “creatures originate themselves.”

---

## 8. Completion conditions

The creation bridge advances only when one of its horns is developed beyond vocabulary.

### To develop C-Nec

1. Define \(\mathcal A\), admissibility, and compossibility.
2. State the realisation principle without simply calling it symmetry or completeness.
3. Supply a measure if observer selection or probability is invoked.
4. State which modal notion of contingency survives.
5. Confront the distribution of harm and any benevolence claim.

### To develop C-Cont

1. State the ontology of \(\sigma\): fact, act, reason, law, relation, or co-ground.
2. Say whether \(\sigma\) is primitive, grounded, or necessarily connected to \(g\).
3. If it is an act of a simple ground, state how it avoids accidental multiplicity or temporal change.
4. Explain why the selector is not merely a renamed brute fact.
5. Show how the proposal differs from an ungrounded world plus an idle ground.

### To develop ND

1. Give identity conditions for apparent or conventional perspectives.
2. Explain public regularity, error, and intersubjective disagreement.
3. Preserve the ethical reality of finite suffering without smuggling back real derivative subjects.

---

## 9. What this bridge has achieved

1. **Creation is now typed.** Grounding, intraworld causation, and totality selection are distinct relations with distinct burdens.
2. **Non-competitive creation has a coherence model.** It can be added to any finite causal system without changing the system’s empirical causal consequences.
3. **Modal collapse is exact rather than rhetorical.** Necessary nature plus necessary sufficient selection yields necessary totality.
4. **C-Nec and C-Cont are no longer labels.** Each has explicit gains, costs, and proof obligations.
5. **Strict non-duality is preserved as a real alternative rather than an equivocation within literal creation.**

The bridge does not prove that the ground is real, simple, aware, personal, benevolent, or creative. It does something more disciplined: it makes a literal creation claim coherent, exposes the cost of each modal completion, and rules out the previous three-way equivocation between necessary creation, contingent creation, and non-dual appearance.
