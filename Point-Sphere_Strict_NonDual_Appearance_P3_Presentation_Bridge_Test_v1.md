# Point–Sphere Strict Non-Dual Appearance — P3 Presentation-Bridge Test v1

**Protocol parent:** `Point-Sphere_Strict_NonDual_Appearance_Presentation_Protocol_v1.md` (SHA-256 `88faa8ac4eea92e195ae5ce89e8fdafc39c1a48dac1bd863374f7bc7c60132aa`).  
**Prerequisites:** P1 Presentation Grammar v1 (SHA-256 `37d7d91d1951a6c4578d167783c8520c78e910219d11eadd9d6bc9052b2e3867`) and P2 Context/Manifestation/Plenitude v1 (SHA-256 `5d4f6b7363de09024dbca94c897663fdb9a5944022ad627bcc122918f1912738`).  
**Execution position:** P3 only.  
**Status:** Executed structural test of a non-substantial presentation bridge. The bridge is satisfiable as a formal presentation-index construction; it is not a derivation of consciousness, a real finite subject, public objectivity, or phenomenal adequacy.

---

## 1. Fixed P3 target

P3 does not add a realization bridge. It tests only:

\[
\boxed{
\mathsf{AA}^{\rm pres}_G(m,c,d)
\land
\mathsf{ExperientialForm}(m)
\to
\exists\phi\,
\mathsf{GenuinePresentation}_G(\phi,m,c,d).
}
\tag{PB}
\]

The bridge must be profile-faithful, non-substantial, invariant, non-selector-based, and non-vacuous in the restricted structural sense below.

The following remain prohibited:

\[
\mathsf{ActualFiniteMode},\quad
\mathsf{Realizes},\quad
\mathsf{Subjecthood},\quad
\mathsf{IndependentWitness},\quad
\mathsf{ExternalTime},\quad
\mathsf{PublicObjectivity},\quad
\mathsf{SecondaryCause}.
\]

---

## 2. Presentation indices and formal profile content

For every \(\simeq_{\rm pres}\)-class of P1 diagrams having experiential form, introduce one presentation index:

\[
\Phi_{\rm pres}:=
\{\phi_{[m]_{\simeq_{\rm pres}}}:
\mathsf{CandMode}_{\rm pres}(m)
\land
\mathsf{ExperientialForm}(m)
\}.
\tag{Phi}
\]

A presentation index is not a new object in a second ontological realm. It is a metalinguistic index for a profile-equivalence class. It bears no existential predicate, causal role, agency predicate, or observer relation.

Define its formal profile content by:

\[
\mathsf{Code}(\phi_{[m]_{\simeq_{\rm pres}}})
:=[m]_{\simeq_{\rm pres}}.
\tag{Code}
\]

The formal presentation bridge is:

\[
\begin{aligned}
\mathsf{GenuinePresentation}^{\rm str}_G(\phi,m,c,d)
\iff{}&
\mathsf{AA}^{\rm pres}_G(m,c,d)\\
&\land
\mathsf{ExperientialForm}(m)\\
&\land
\phi=\phi_{[m]_{\simeq_{\rm pres}}}.
\end{aligned}
\tag{GP-str}
\]

The superscript \(\mathsf{str}\) is essential: at P3, “genuine presentation” means a faithful structural presentation-index relation only. It does not yet establish phenomenality in the robust sense.

---

## 3. P3 bridge conditions

### 3.1 Profile faithfulness

\[
\mathsf{GenuinePresentation}^{\rm str}_G(\phi,m,c,d)
\to
\mathsf{Code}(\phi)=[m]_{\simeq_{\rm pres}}.
\tag{F}
\]

No unrecorded profile content may be added to \(\phi\).

### 3.2 Non-substantiality

\[
\phi\in\Phi_{\rm pres}
\not\Rightarrow
\mathsf{Exists}_{\rm strict}(\phi),
\qquad
\phi\notin\mathbf L,
\tag{NS}
\]

and no predicate in P1–P3 makes \(\phi\) a finite subject, entity, part, cause, or observer.

### 3.3 Non-selector condition

\[
\forall m,c,d[
\mathsf{AA}^{\rm pres}_G(m,c,d)
\land
\mathsf{ExperientialForm}(m)
\to
\exists\phi\,
\mathsf{GenuinePresentation}^{\rm str}_G(\phi,m,c,d)
].
\tag{NSc}
\]

The bridge applies uniformly to the predeclared syntactic class \(\mathsf{ExperientialForm}\). It does not select a favored diagram, context, or degree after inspection.

### 3.4 Invariance

\[
\begin{aligned}
&m\simeq_{\rm pres}m'\land
\mathsf{GenuinePresentation}^{\rm str}_G(\phi,m,c,d)\\
&\qquad\to
\exists c',d'[
\mathsf{GenuinePresentation}^{\rm str}_G(\phi,m',c',d')
].
\end{aligned}
\tag{Inv}
\]

The bridge therefore cannot distinguish re-encodings that preserve the P1 profile.

### 3.5 Restricted non-vacuity

The P1 witness has experiential form:

\[
\mathsf{CandMode}_{\rm pres}(m_\star)
\land
\mathsf{ExperientialForm}(m_\star).
\tag{NV1}
\]

P2 plenitude supplies a context and degree:

\[
\exists c_\star,d_\star\,
\mathsf{AA}^{\rm pres}_G(m_\star,c_\star,d_\star).
\tag{NV2}
\]

Thus:

\[
\exists\phi\,
\mathsf{GenuinePresentation}^{\rm str}_G(\phi,m_\star,c_\star,d_\star).
\tag{NV3}
\]

---

## 4. Satisfaction construction

Extend the canonical P2 manifestation structure \(\mathfrak N^{\rm can}_{\rm pres}\) by the class \(\Phi_{\rm pres}\), the code map \((\mathrm{Code})\), and the relation \((\mathrm{GP\text{-}str})\).

For every experiential candidate \(m\), P2 supplies:

\[
\mathsf{AA}^{\rm pres}_G(m,c_m,d_{[m]_{\simeq_{\rm pres}}}).
\]

Set:

\[
\phi_m:=\phi_{[m]_{\simeq_{\rm pres}}}.
\]

Then by \((\mathrm{GP\text{-}str})\):

\[
\mathsf{GenuinePresentation}^{\rm str}_G
(\phi_m,m,c_m,d_{[m]_{\simeq_{\rm pres}}}).
\tag{W}
\]

Therefore the P3 structural bridge is nonempty, faithful, non-substantial, non-selective over its declared class, and profile-invariant.

---

## 5. P3 result and limitation

The following restricted result is established:

\[
\boxed{
\mathsf{BridgePass}^{\rm structural}_{\rm P3}
(
\mathsf{GenuinePresentation}^{\rm str}_G
).
}
\tag{P3-Pass}
\]

This result means only that a P1 experiential-form diagram can be carried through the P2 plenitude/manifestation structure to a profile-faithful non-substantial presentation index, without a witness-subject, finite-mode realization, or representational selector.

It does **not** establish:

\[
\begin{aligned}
&\text{felt consciousness or a phenomenally real sufferer;}\\
&\text{truth, error, genuine silence, clear disclosure, prophetic revelation, or miracles;}\\
&\text{that \(\mathsf{ExperientialForm}\) is a correct theory of phenomenality;}\\
&\text{that the presentation-index construction avoids a hidden positive formal structure;}\\
&\text{that the strict presentation candidate is zero-residue, physically adequate, or correct.}
\end{aligned}
\]

Accordingly, P3 is a structural pass only. It leaves the decisive phenomenal adequacy burden for the fixed battery.

---

## 6. Fixed next task

The next permitted task is the fixed six-case battery only:

\[
\mathcal B_{\rm pres}=
\{m_{\rm ordinary},m_{\rm silent},m_{\rm clear},m_{\rm prophetic},m_{\rm deceptive},m_{\rm horror}\}.
\]

No alteration to \(\Sigma_{\rm pres}\), \(T_{\rm pres}\), \(\mathsf{ExperientialForm}\), \(\mathsf{MPlen}^{\rm fin,pres}_G\), or the P3 bridge is permitted while executing the battery.
