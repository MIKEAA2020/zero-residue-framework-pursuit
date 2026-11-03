# PPA-6 Z0 Global-Model and Slice-Locality Audit v1
## Executed only after restricted-formal entry admission

**Candidate:** \(F_{\rm PPA\text{-}6}\)  
**Packet:** `Public_Primitive_Actuality_Constructive_Entry_Packet_v6.md`  
**Packet SHA-256:** `2ac75e75c9bdfb7cc1b1701bc2c35616cc1e58ac315b45cfa2b65a82c2111e3b`  
**Entry decision relied upon:** `Point-Sphere_PPA-6_Restricted_Physical_Successor_Entry_Review_v1.md`  
**Scope:** Z0 only. No Z1, Z2, or Z3 test is executed or credited.

---

## 0. Authorized question

PPA-6 fixes Z0 as a test of the explicit-infinite quotient model, a *finite* \(N_\star\)-slice, its typed primitive actuality/attestation interpretation, and the declared locality condition. Its frozen failure trigger includes a missing carrier, relation, slice, or locality premise.

The present audit therefore distinguishes the global interpretation from the claimed finite induced substructure. It does not repair a failed definition by supplying new carrier conventions.

---

## 1. Global structure: sufficient at the stated abstract level

The packet explicitly supplies the infinite raw-code carrier

\[
\mathbf C_{\rm raw}=\{0,1\}^{*},
\qquad
\overline{\mathbf C}=\mathbf C_{\rm raw}/\cong_{\rm raw},
\]

and gives quotient-native articulation tokens, the primitive finite actual extension, withholding for all other applicable classes, and nonapplicability outside the applicability condition. In particular, its declared actuality extension is finite:

\[
\mathsf{Act}_0^{\mathfrak G}
=
\{a_{[p_{\rm act}]},a_{[p^-]},a_{[p_{\rm phen}]},a_{[p_{\rm phen}^{\rm disc}]},a_{[p_{\rm norm}]},a_{[p_\star]}\}.
\]

The packet also states that every applicable class has exactly one public attestation. Nothing in this Z0 audit challenges the class-native status of actuality or the stated global \(\mathsf{Act}_0\)/\(\mathsf{Withheld}\) split.

---

## 2. What the stated slice actually defines

PPA-6 defines only a set of quotient classes:

\[
\mathsf{Slice}_N
=
\{[p]:|\operatorname{can}([p])|\le N\}
\cup
\{\text{reachable shorter content, successor, predecessor, and observation classes}\}.
\]

This class set is finite: there are finitely many binary strings of length at most \(N\), hence no more quotient classes of that bounded canonical length; strict length decrease preserves finiteness under the stated closure operations.

However, \(\mathsf{Slice}_N\subseteq\overline{\mathbf C}\) does not define carriers for the other sorts of the declared multi-sorted signature.

---

## 3. Missing finite multi-sorted restriction

The packet's signature contains, among other sorts,

\[
\begin{aligned}
\mathbf B&=\{G\}\cup\{b_{[p],i}:[p]\in\overline{\mathbf C},\ i\in\mathbb N\},\\
\mathbf S&=\{s_{[p],j}:[p]\in\overline{\mathbf C},\ j\in\mathbb N\},\\
\mathbf R&=\{r_{[p],j}:[p]\in\overline{\mathbf C},\ j\in\mathbb N\},\\
\mathbf W&=\text{finite public attestation records},
qquad
\mathbf T=\mathbb Z.
\end{aligned}
\]

No frozen definition specifies the corresponding finite carriers for

\[
\mathfrak G_{\rm PPA6}\upharpoonright N_\star.
\]

In particular, the packet does not state any of the needed restrictions, such as:

\[
\begin{aligned}
\mathbf B_{N_\star}&\subseteq\mathbf B, &
\mathbf S_{N_\star}&\subseteq\mathbf S, &
\mathbf R_{N_\star}&\subseteq\mathbf R,\\
\mathbf W_{N_\star}&\subseteq\mathbf W, &
\mathbf T_{N_\star}&\subseteq\mathbb Z.
\end{aligned}
\]

nor a typed induced-relation convention over such carriers. Merely taking all tokens with a slice class index is not a finite remedy: \(i,j\in\mathbb N\) remain unrestricted. Nor may this audit insert post hoc restrictions to decoded node slots, presentational slots, action slots, attestation records, or displayed times; those would be new frozen slice operations.

Consequently, the assertion that

\[
\mathfrak G_{\rm PPA6}\upharpoonright N_\star
\text{ is a finite induced fixture slice}
\]

is not derivable from the frozen packet.

---

## 4. Locality consequence

PPA-6's physical-locality biconditional has a global left-hand side but an underdefined right-hand side:

\[
\mathfrak G_{\rm PPA6}\models\varphi_{\rm phys}
\iff
\mathfrak G_{\rm PPA6}\upharpoonright N_\star\models\varphi_{\rm phys}.
\]

The finite physical data and the Pulse-125 certificate remain valid as data about \(p_\star\). But they cannot establish the stated model/slice locality bridge until the multi-sorted restricted structure itself is specified. A locality proof cannot supply the missing carrier map.

---

## 5. Z0 result and freeze consequence

The global quotient model and primitive roster are not refuted. The Z0 finite-slice conjunct, however, fails at its frozen carrier/slice requirement:

\[
\boxed{
\neg\mathsf{FiniteTypedSliceCertified}
(\mathfrak G_{\rm PPA6}\upharpoonright N_\star).
}
\]

Hence:

\[
\boxed{
Z0(F_{\rm PPA\text{-}6})=\mathsf{Fail}_{\rm missing\ finite\ multi\text{-}sorted\ slice\ carriers}.
}
\]

No later battery stage is authorized:

\[
\neg Z1.a\text{ executed}
\land\neg Z1.b\text{ executed}
\land\neg Z2\text{ executed}
\land\neg Z3.a\text{ executed}
\land\neg Z3.b\text{ executed}
\land\neg Z3.c\text{ executed}.
\]

Under PPA-6's expiry rule, a slice-carrier or attestation-domain addition cannot amend the frozen candidate. The appropriate disposition is:

\[
\boxed{
\mathsf{Disposition}(F_{\rm PPA\text{-}6})
=
\mathsf{Closed}_{\rm frozen\ Z0\ slice\ carrier/locality\ failure}.
}
\]

A successor, if proposed, must be a distinct candidate and explicitly fix all multi-sorted slice carriers and their induced relations before entry review. This audit claims neither a physical-battery failure nor a zero-residue result.
