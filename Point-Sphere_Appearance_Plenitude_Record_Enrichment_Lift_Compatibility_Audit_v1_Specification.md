# AP4D2 Record-Enrichment / Lift-Quotient Compatibility Audit v1
## Which explicit record enrichments preserve the minimal lift quotient, and which make lift data substantive?

## Purpose

With \(\mathsf{IFG}_{\rm P1}\) adopted, AP4D1 established that no record law is entailed. This audit compares explicit added record laws rather than searching for an upstream derivation.

The common base has 16 lift functions:
\[
f:S=\mathbb Z_2^2\to\mathbb Z_2,
\qquad
\beta_f(a,b,c)=(a,b,c\oplus f(a,b)),
\]
and Q-fibre coordinate transformations:
\[
f\mapsto f+h,
\qquad h\in H_{\rm full}\cong(\mathbb Z_2)^4.
\]

## Three explicit enrichment types

### R-trace — AP4C1-style trace-only record

Witnesses redundantly record only the shared ordered trace \((a,b)\). No record contains free-fibre relation \(c\oplus d\) or cross-sector Q relation. Since every Q-fibre translation fixes \((a,b)\), it is compatible with full minimal lift gauge.

### R-J — within-component comparator record

Add a recordable intrinsic relation:
\[
J_s=c\oplus d=f(s).
\]
A transformation changes it by \(J_s\mapsto J_s\oplus h(s)\). If the record is intrinsic, only \(h=0\) preserves it. The 16 lifts become distinct record-enriched classes.

### R-I — cross-sector relative record

Add a global relational signature, for reference sector \(s_0\):
\[
\rho(f)=\bigl(f(s_0)\oplus f(s)\bigr)_{s\ne s_0}.
\]
It is preserved by uniform complement but not generic sector-dependent flips. It produces eight record-enriched classes.

## Common component count

The grammar-level phase/successor components remain the eight \(\theta=(a,b,c)\) components in all three cases. These enrichment choices change the **lift description quotient**, not the P1 graph-component count.

## Interpretation rule

No enrichment is selected merely by its mathematical availability. `R-trace` is compatible with AP4C1’s established added trace-record law. `R-J` and `R-I` are permitted only if their added observables have independent content warrant. If a non-gauge enriched class is typed as a genuine aspect, conditional plenitude co-realizes it rather than selecting a winner.
