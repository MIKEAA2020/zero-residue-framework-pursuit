# Modal Necessary-Existence Bridge v1
## From an actual non-derivative ground entity to necessary existence—under an explicit contingency principle

## Result in one sentence

An actual ground entity does not become necessary merely by being ungrounded. Necessary existence follows once one adds a modal-dependence bridge saying that every actual entity capable of failing to exist has a distinct external ontological ground for its actuality; without this or some comparably strong modal bridge, the inference fails. The premise excludes brute modal contingency and is the substantive cost of the result.

---

## 1. The exact modal gap

The bearer–truthmaker bridge yields, conditionally, an actual entity \(G\) that bears the unique foundation fact and has no **distinct external entity-ground** of its actuality. This is an actual-world conclusion:
\[
\mathsf{ActEnt}(G).
\]
It does not entail
\[
\Box\mathsf{ActEnt}(G).
\]

An entity can be actual and externally ungrounded in the actual world while absent from another possible world, unless a principle connects possible nonexistence to present ontological dependence. Calling an ungrounded entity “necessary” without that principle simply redescribes the conclusion sought.

---

## 2. Modal setting and distinctions

Fix an intended accessibility range \(R\) over possible worlds. All modal claims below are relative to it. At a world \(w\), write \(E_w(x)\) for “\(x\) is actual at \(w\)” and \(\mathsf{EG}_w(y,\mathsf{Ex}(x))\) for “the being or nature of \(y\) grounds the actuality of \(x\) at \(w\).”

Define:
\[
\mathsf{Cont}_R(x,w)
\quad\Longleftrightarrow\quad
E_w(x)\land\exists v\,(wRv\land\neg E_v(x)),
\]
\[
\mathsf{ExtDep}_w(x)
\quad\Longleftrightarrow\quad
\exists y\,[E_w(y)\land y\ne x\land\mathsf{EG}_w(y,\mathsf{Ex}(x))].
\]

Three propositions must not be conflated:

- \(\Box\exists x\,\mathsf{Ground}(x)\): every possible world has some ground;
- \(\exists x\,\Box\mathsf{Ground}(x)\): one individual is ground in every possible world;
- \(\Box E(G)\): this individual \(G\) exists in every possible world.

The first does not entail the second. A different foundation entity can occupy the ground role in each world.

---

## 3. Modal-dependence bridge

The bridge adds one substantive principle.

### MD — Explanatory contingency
\[
\forall x\,\bigl[\mathsf{Cont}_R(x,w)\ \Rightarrow\ \mathsf{ExtDep}_w(x)\bigr].
\]

If an actual entity could fail to exist somewhere in the intended modal range, its actuality is externally ontologically dependent here. MD is not a theorem of modal logic. It is a restricted principle of sufficient reason for **existential contingency**.

The bearer bridge supplies the companion premise:

### ND — External non-derivativeness of the ground bearer
\[
\neg\mathsf{ExtDep}_w(G).
\]

ND does not deny that \(G\)'s nature explains its own actuality in some immanent sense. It denies that another, distinct entity grounds \(G\)'s actuality.

---

## 4. Conditional theorem

### Theorem — Necessary existence from modal dependence

At the actual world \(w_0\), assume:

1. \(E_{w_0}(G)\);
2. \(\neg\mathsf{ExtDep}_{w_0}(G)\);
3. MD holds at \(w_0\).

Then
\[
\Box_R E(G).
\]

#### Proof

Assume instead \(\Diamond_R\neg E(G)\) at \(w_0\). Together with \(E_{w_0}(G)\), this gives \(\mathsf{Cont}_R(G,w_0)\). By MD, \(\mathsf{ExtDep}_{w_0}(G)\). This contradicts premise 2. Hence \(\neg\Diamond_R\neg E(G)\), equivalently \(\Box_R E(G)\). \(\square\)

No S5 principle is needed for this inference; it uses only the ordinary duality of \(\Box\) and \(\Diamond\) relative to the stipulated accessibility range. Changing the range changes the necessity claim.

---

## 5. What MD costs—and alternative modal routes

MD rules out an important rival: an entity whose existence is brute in the actual world but modally optional. A critic may accept the actual ground entity and reject MD, holding that possible nonexistence requires no actual external ground. The conditional theorem then does not apply.

A stronger fact-first version may replace external entity-grounding by a full factual explanation:
\[
\mathsf{Cont}_R(x,w)\Rightarrow
\exists f\,[\mathsf{Fact}(f)\land\mathsf{FG}_w(f,\mathsf{Ex}(x))\land f\text{ is external to }x].
\]
It requires a correspondingly stronger no-external-factual-ground premise for \(G\). This route blocks primitive modal facts but is more demanding than the entity-only bridge.

A different route uses a necessary fundamental nature \(N\):
\[
\Box_R\exists!x\,N(x),
\qquad
\Box_R\forall x\,[N(x)\Rightarrow x=G].
\]
These premises entail \(\Box_R E(G)\). But the second is a cross-world identity/rigidity premise, and the first is a necessary-instantiation premise. Together they do not derive necessary existence; they encode it in a different form. They remain useful only when independently defended—for example by an essence theory with a clear account of why the relevant nature cannot be uninstantiated.

---

## 6. Necessary existence is not modal collapse

From \(\Box E(G)\) alone, no arbitrary derivative truth follows necessarily. Consider two accessible worlds containing the same \(G\), in which \(G\) grounds each world’s concrete order, but a derivative fact \(p\) obtains in one world and not the other. Then:
\[
\Box E(G)\ \land\ \Diamond p\ \land\ \Diamond\neg p
\]
is consistent. A further principle connecting the ground’s necessary nature, will, explanatory sufficiency, or act to every derivative fact is needed to produce modal collapse.

This distinction matters for creation. Necessary existence of a ground entity does not entail necessary creation. C-Nec, C-Cont, and strict non-dual alternatives retain their separate costs.

---

## 7. Countermodels and failure points

| Model | Actual ground entity? | Necessary existence? | Failed premise | Lesson |
|---|---:|---:|---|---|
| Brute contingent foundation | Yes | No | MD | Actual non-derivativeness alone is insufficient. |
| Each world has a different ground entity | Yes, world-relative | No individual is necessary | Cross-world identity | \(\Box\exists x\,\mathsf{Ground}(x)\) is only de dicto necessity. |
| Necessary fundamental nature, contingently instantiated | Potentially | No | Necessary instantiation | Essence talk alone is insufficient. |
| Same necessarily existing G; contingent derivatives | Yes | Yes | None | Necessary ground need not mean modal collapse. |

---

## 8. Assessment

The bridge delivers a clean conditional result:

\[
\text{actual external non-derivativeness}
+\text{ explanatory contingency}
\quad\Rightarrow\quad
\text{necessary existence}.
\]

Its strength is also its price. It does not pretend that an actual ungrounded entity is automatically necessary; it identifies the precise premise—MD—that excludes ungrounded modal contingency. The result remains relative to the intended modal range and does not establish aseity-through-itself, simplicity, awareness, personhood, goodness, or necessary creation.
