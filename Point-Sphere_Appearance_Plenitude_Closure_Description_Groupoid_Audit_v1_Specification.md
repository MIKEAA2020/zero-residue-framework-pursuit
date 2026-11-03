# AP3P2J Closure, Description-Class, and Lift-Groupoid Audit v1
## Evaluation of four proposed strengthenings of the minimal-fibre gauge result

## Aim

This audit tests four proposals:

1. derive no-hidden-coordinate-content (NCC) from essential/no-brute closure;
2. classify declared-structure isomorphism (SI_decl) as definitional rather than substantive;
3. identify \(H_{\rm full}\) with the full automorphism group; and
4. obtain component boundaries from AP3L maximality.

It separates what is valid at the description level from what would require a new grammar-adequacy or mode-identity bridge.

## 1. Essential closure does not by itself imply grammar exhaustiveness

Let \(\operatorname{Cont}(x)\) mean genuine intrinsic content, \(\operatorname{Grounded}_G(x)\) mean non-brutely grounded in the one ground, and \(\operatorname{Rep}_\Sigma(x)\) mean represented in the currently declared finite grammar \(\Sigma\).

The relevant closure thesis has shape:
\[
\operatorname{Cont}(x)\Rightarrow \operatorname{Grounded}_G(x).
\]
NCC requires:
\[
\neg\operatorname{Rep}_\Sigma(x)\Rightarrow\neg\operatorname{Cont}(x),
\]
or contrapositively:
\[
\operatorname{Cont}(x)\Rightarrow\operatorname{Rep}_\Sigma(x).
\]

The latter is a **grammar-adequacy/completeness bridge**. It does not follow from common grounding: an unrepresented relation can be grounded but not yet captured by a provisional/revisable grammar. A countermodel with an intrinsic, grounded \(J_s\) absent from minimal \(\Sigma\) satisfies essential closure and violates NCC.

A weaker valid methodological rule remains:
\[
\neg\operatorname{Rep}_\Sigma(x)
\Rightarrow
\text{do not count }x\text{ as established content of the minimal grammar merely from its code notation.}
\]

## 2. SI_decl is definitional at description-class level only

Define:
\[
[\mathcal M]_{\Sigma}:=
\{\mathcal N:\mathcal N\cong_\Sigma\mathcal M\}.
\]
Then isomorphic declared structures are in the same **description class** by definition. This does not alone entail that they are the same genuine mode/aspect; that additional identification depends on the grammar-to-mode bridge.

## 3. Correct group-theoretic target: an isomorphism groupoid

Let \(\mathcal M_f\) be the phase-successor graph for lift \(f:S\to\mathbb Z_2\). A sector-preserving P/Q-type-preserving isomorphism \(\mathcal M_f\to\mathcal M_g\) has:
\[
P(s,c)\mapsto P(s,c\oplus k(s)),
\]
\[
Q(s,d)\mapsto Q(s,d\oplus \ell(s)),
\qquad \ell(s)=k(s)\oplus f(s)\oplus g(s).
\]
Thus every Hom-set has \(2^4\) members.

The previously used \(H_{\rm full}\) maps are the canonical subfamily \(k=0\): they are Q-chart translations between \(\mathcal M_f\) and \(\mathcal M_{f+h}\). They are **not** \(\operatorname{Aut}(\mathcal M_f)\) for nonzero \(h\), because they map between different lift presentations. Instead:
\[
\operatorname{Aut}(\mathcal M_f)\cong(\mathbb Z_2)^4
\]
is represented by simultaneous P/Q translations with \(\ell=k\).

The groupoid is connected, so there is one isomorphism description class in the minimal signature. This is stronger and more accurate than the false equation \(H_{\rm full}=\operatorname{Aut}(\mathcal M_f)\).

## 4. Maximality versus component boundaries

AP3L maximality concerns maximal mutually compatible **phase contexts**. AP3P1 mode components are maximal connected subgraphs only relative to the stipulated successor relation. Graph-theoretic connected components are canonical once that relation is fixed, but AP3L does not derive that successor-connected components are genuine finite modes. A new component-to-mode bridge would still be needed.

## Registered conclusions

- Essential closure alone does not derive NCC; grammar adequacy would be an additional bridge.
- SI_decl is analytic for description classes, not automatically for genuine mode identity.
- The correct canonical structure is a connected lift-isomorphism groupoid, not one automorphism group equated with \(H_{\rm full}\).
- Maximality can sharpen boundaries only after the successor/component-to-mode bridge is independently warranted.
