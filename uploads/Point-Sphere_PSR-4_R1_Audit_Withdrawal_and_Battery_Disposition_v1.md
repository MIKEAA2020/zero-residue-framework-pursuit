# PSR-4 R1 Audit Withdrawal and Battery Disposition v1
## Correction after independent R0 adjudication

**Candidate:** \(F_{\rm PSR\text{-}4}\)  
**Frozen packet SHA-256:** `d326b9fe2276c472cdc1558d1c4cc669a479c01c8563fe32e77ac4e47b04b6b7`  
**Earlier R0 audit:** `Point-Sphere_PSR-4_R0_Global_Model_and_Locality_Audit_v1.md`  
**Earlier R0 audit SHA-256:** `0e26bb0c786f53cdfcb3cf36f53e4a3b185c6c92de747d54bff360c1ac4a57c4`  
**Independent R0 adjudication:** `Point-Sphere_PSR-4_R0_Global_Model_and_Locality_Adjudication_v1.md`  
**Adjudication SHA-256:** `8d2177d7909533474b9bf353a8a4027a34600e4912de5a6a9616cdc0ef9d67fa`  
**Earlier R1 audit:** `Point-Sphere_PSR-4_R1_Instantiation_and_Isomorphism_Audit_v1.md`  
**Earlier R1 audit SHA-256:** `ebbb5dce62b5bd9a12e4f57bc97c527dbea5821d0b00d3f65324930c26054716`

---

## 0. Supersession and scope

The independent adjudication supersedes the earlier claimed R0 pass. It identifies three independent frozen R0 defects:

\[
\begin{array}{c|l}
\textbf{defect} & \textbf{frozen location}\\
\hline
\text{raw carrier/quotient typing} & \text{rejected strings were included in the quotiented structural carrier}\\
\text{generic global parser} & \text{content-body and value-key branches were underdetermined}\\
\text{content closure/locality} & \kappa_{T_{\rm good}}(Pr)\notin\{o_{\rm true},o_{\rm false}\}
\end{array}
\tag{R0-DEFECTS}
\]

Accordingly, the valid R0 result is:

\[
\boxed{
R0(F_{\rm PSR\text{-}4})
=
\mathsf{Fail}_{\rm raw\ carrier/quotient\ typing,\ generic\ global\ parser,\ content\ closure/locality}.
}
\tag{R0-FINAL}
\]

---

## 1. Withdrawal of the earlier R1 claim

The earlier R1 audit was generated on the erroneous premise that R0 had passed. Since the frozen battery requires R0 passage before R1 authorization, that audit is not a valid execution and its apparent result receives no credit:

\[
\boxed{
\mathsf{Status}
\left(
\texttt{Point-Sphere\_PSR-4\_R1\_Instantiation\_and\_Isomorphism\_Audit\_v1.md}
\right)
=
\mathsf{Void}_{\rm unauthorized\ after\ R0\ failure}.
}
\tag{R1-WITHDRAWN}
\]

In particular, the earlier statement

\[
R1(F_{\rm PSR\text{-}4})=\mathsf{Pass}_{\rm restricted\ formal}
\]

is withdrawn and must not be cited as an executed-stage result.

---

## 2. Frozen battery disposition

PSR-4 is closed at R0:

\[
\boxed{
\mathsf{BatteryStatus}(F_{\rm PSR\text{-}4})
=
\mathsf{Closed}_{\rm R0\ global\ model/locality\ failure}.
}
\tag{BATTERY-CLOSED}
\]

No later stage has a valid execution status:

\[
\bigwedge_{b\in\{R1,R2,R3.a,R3.b,R3.c\}}
\neg\mathsf{Executed}(F_{\rm PSR\text{-}4},b).
\tag{NO-LATER-STAGE}
\]

The closure does not refute the PSR family, discharge its instantiation/experience residual, establish a public-bridge failure for every PSR route, or support any rival by elimination:

\[
\mathsf{R0Fail}(F_{\rm PSR\text{-}4})
\not\Rightarrow
\neg\mathsf{Viable}(\mathcal F_{\rm PSR}),
\qquad
\mathsf{R0Fail}(F_{\rm PSR\text{-}4})
\not\Rightarrow
\mathsf{NoSelectorResidue},
\qquad
\mathsf{R0Fail}(F_{\rm PSR\text{-}4})
\not\Rightarrow
\mathsf{Confirmed}(\mathcal F_{\rm rival}).
\tag{SCOPE-BOUNDARY}
\]

---

## 3. Future boundary

A possible PSR successor would have to be a fresh candidate, not a repair, and would need to specify before review:

\[
\begin{aligned}
&\{0,1\}^*=\mathsf{AcceptedCodeStrings}\sqcup\mathsf{RejectedStrings},
\quad
\mathcal S_{\rm raw}=\mathsf{Decode}(\mathsf{AcceptedCodeStrings});\\
&\text{a total finite-pattern-body grammar and all value-key decoders;}\\
&\text{a closure including every successor content used by }\mathsf{SuccMatches}.
\end{aligned}
\tag{FRESH-PSR-REQUIREMENTS}
\]

No PSR-5 packet is initiated by this withdrawal. Any decision to pursue such a fresh route must occur separately.
