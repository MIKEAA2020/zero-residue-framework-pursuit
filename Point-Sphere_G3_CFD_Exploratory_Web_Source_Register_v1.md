# G3/CFD Exploratory Web Source Register v1
## Archival-source scan after preregistration

## Status

**Exploratory source register only. These materials are not part of the frozen confirmatory corpus and have not been scored under the CFD protocol.**

The confirmatory protocol requires prospectively elicited, independently collected reports after 2026-10-21 with the protocol's neutral completion instrument. Web archival sources cannot satisfy that requirement retroactively.

## 1. Sources retrieved and inspected

| ID | Source | Public material retrieved | Use status |
|---|---|---|---|
| DES-Sadie-Index | `https://hurlburt.faculty.unlv.edu/ieo/sadie/sadie_sampling.html` | Public DES sampling-series page, interview links, sample summaries, and transcript links | Exploratory provenance/source map only |
| DES-Sadie-I1 | `https://hurlburt.faculty.unlv.edu/ieo/sadie/Sadie_interview_1_transcript_with_commentary.pdf` | Parsed public transcript of first DES sampling-day discussion, including several episode reports and method commentary | Exploratory stress-test candidate; not eligible for G3 confirmation |
| DES-Lena | `https://pmc.ncbi.nlm.nih.gov/articles/PMC8370856/` | Open article describing a complete, unabridged, pre-registered DES investigation and availability of transparent procedure materials | Exploratory source candidate only |
| Qwantify | `https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.1054292/full` | Open report describing app-based momentary desire reports, including open-ended, categorical, and continuous self-report elements | Exploratory structural comparison only |
| openESM | `https://openesmdata.org/` | Open experience-sampling database and metadata portal | Dataset-discovery source; no G3 eligibility assumed |

## 2. Immediate compatibility audit

### 2.1 DES material

The DES source is the closest available public material to the intended target because it records episode-level first-person descriptions and discusses temporal boundaries, simultaneous contents, uncertainty, and correction.

It still fails the frozen confirmatory eligibility rule because it is archival and did not use the G3 neutral structured completion record. In particular, a DES transcript ordinarily does not decide every active:

\[
\mathsf{HasAt}(s,q,e),
\quad
\mathsf{Before}_{\Phi}(e_i,e_j),
\quad
\text{and equality/disequality claim}.
\]

Therefore a transcript may not be completed by importing unreported negative facts merely to run the G3 classifier.

The retrieved first-day Sadie transcript also explicitly describes first-day DES sampling as primarily training and as normally discarded for substantive characterization. It should not be used even as a high-confidence exploratory validation case.

### 2.2 Qwantify and openESM

Qwantify includes in-the-moment self-report and open-ended desire descriptions, but its design does not supply the finite complete quality-by-phase and locus/equality matrix required by the G3 coding manual.

openESM is useful for locating open experience-sampling studies but, absent a dataset-specific audit, its metadata portal does not show that a given dataset supplies complete finite phenomenal profiles.

Thus neither is currently eligible to be coded as a G3 complete mode.

## 3. What archival sources can legitimately test

They can test the **practical burden** of the manual:

\[
\text{Can naturally available first-person data be translated into a complete G3 profile without illicit enrichment?}
\]

The presently inspected material already gives a preliminary reason to expect a high out-of-scope rate:

\[
\text{rich first-person description}
\not\Rightarrow
\text{complete finite diagram}.
\]

This is not a result against CFD. It is an exploratory feasibility observation requiring a separate, non-confirmatory coding log if pursued.

## 4. Prohibited uses

The following are prohibited under the frozen protocol:

\[
\begin{array}{ll}
P1 &: \text{Counting any archival source as one of the }N=80\text{ confirmatory reports};\\
P2 &: \text{Using DES interviewers' descriptive verdicts as }\mathsf{CertField};\\
P3 &: \text{Filling omitted profile facts from a theory or classifier prediction};\\
P4 &: \text{Treating transcript examples as independent support for }P_{\rm ND}\text{ or CFD};\\
P5 &: \text{Amending the completion threshold after archival coding proves difficult.}
\end{array}
\]

## 5. Next web-data action, if chosen

A separate exploratory pilot may be registered with its own manifest and use a small fixed set of publicly linked DES transcript episodes. Its only reportable outcomes would be:

\[
\text{complete-codeable},
\quad
\text{incomplete/out-of-scope},
\quad
\text{or semantically inconsistent}.
\]

It must not report CFD match rates, selector validation, rival defeat, or a framework conclusion.

## Nonclaims

This register does not claim that the archived sources are representative, that they are sufficiently independent for confirmation, that reports are false or unreliable, or that a high archival out-of-scope rate refutes the G3 complete-mode proposal.
