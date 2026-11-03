# Zero-Residue Fixture-Actuality Preflight Protocol v1
## Prospective control after the WPI-5 phenomenal-fixture failure

**Status:** prospective methodology only; no prior candidate is reopened or reclassified.  
**Purpose:** ensure that a finite phenomenal, normative, physical, or truth/error fixture is an actual candidate case before its domain-specific adequacy predicate is credited.

---

## 1. Nonretroactivity

This protocol does not repair WPI-5:

\[
\mathsf{Disposition}(F_{\rm WPI\text{-}5})
=
\mathsf{Closed}_{\rm PhenomenalFixtureFailure}.
\tag{WPI5-Closed}
\]

A later packet must declare its fixture preflight before any battery outcome is known.

---

## 2. General preflight

For any candidate \(F\), finite fixture \(x\), and domain predicate \(\mathsf{Test}_D\), define:

\[
\mathsf{Preflight}_F(x;D)
\iff
\mathsf{TypedFixture}_F(x)
\land
\mathsf{ActualProfile}_F(x)
\land
\mathsf{DeclaredDependenciesActual}_F(x)
\land
\mathsf{DomainBearerActual}_F(x;D).
\tag{Preflight}
\]

A domain battery may be credited only if:

\[
\mathsf{Test}_D(x)
\Longrightarrow
\mathsf{Preflight}_F(x;D).
\tag{Preflight-Requirement}
\]

The preflight is not itself a phenomenal, normative, physical, or truth/error success.

---

## 3. Domain-specific bearer requirements

\[
\begin{array}{c|l}
\textbf{Domain} & \textbf{Additional required actual bearer}\\
\hline
\mathsf{Truth/Error} & \text{Actual presentation, actual host/anchor, and actual claim target where the candidate requires one.}\\
\mathsf{Phenomenal} & \text{Actual profile plus an actual entity or other explicitly typed phenomenal bearer.}\\
\mathsf{Normative} & \text{Actual deliberative bearer, actual feasible alternatives, and actual successor/outcome interface.}\\
\mathsf{Physical} & \text{Actual profile or explicitly declared physical bearer, with an actual recovery map domain.}
\end{array}
\tag{Bearer-Requirements}
\]

A syntactically finite graph, table, action, or presentation does not pass merely because its domain-specific graph calculation is defined:

\[
\mathsf{WellFormedFixture}(x)
\not\Rightarrow
\mathsf{Preflight}_F(x;D).
\tag{No-Formal-Shortcut}
\]

---

## 4. Fixture declaration and expiry

Every later EntryPacket must give, for every battery row:

\[
\langle
\text{raw/class fixture},
\text{typed bearer},
\text{actuality path},
\text{dependency witnesses},
\text{domain predicate},
\text{failure condition}
\rangle.
\tag{Fixture-Record}
\]

If preflight fails, the named fixture cannot establish that battery's pass condition:

\[
\neg\mathsf{Preflight}_F(x;D)
\Rightarrow
\neg\mathsf{FixturePass}_F(x;D).
\tag{Fixture-Expiry}
\]

This does not, without an exhaustive fixture argument, refute every possible test for that domain or every candidate in the family.

---

## 5. Status

\[
\boxed{
\mathsf{FixturePreflightStatus}
=
\mathsf{ProspectiveOnly}.
}
\tag{Status}
\]
