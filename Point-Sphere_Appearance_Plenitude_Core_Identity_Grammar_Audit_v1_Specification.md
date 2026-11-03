# AP3L Core-Identity Grammar Audit v1
## Apply immanence, partiality, non-objectification, and real-boundary constraints without IAR bias

## Purpose

This test implements the proposed strengthening directly. It asks what the core identity claim contributes *in the finite AP3I graph language*, without silently adding constraints designed to recover IAR.

## Core-to-formal translation

| Core consequence | Formal translation in the AP3I language | Expected logical role |
|---|---|---|
| **Immanent, not higher-order** | A mode is a context itself; no second monitoring vertex/context is added | The untyped compatibility graph has no higher-order layer, so this is a typing condition, not a graph discriminator |
| **Partial/bounded, not total** | Modes are proper maximal contexts and contents have coverage by such contexts | This is AP3I F2; universal compatibility is excluded in this implementation |
| **Non-objectifying** | No subject/object edge or external representation node occurs in the grammar | Again a typing condition; the untyped graph cannot distinguish objectifying from non-objectifying implementations |
| **Real boundary** | Quotient grammar relations by \(S_4\) vocabulary relabellings; only structural isomorphism classes count | Collapses label variants without selecting one physical mode or one grammar |

The starting family is AP3I’s 37 labelled grammars satisfying F1–F5.

## Registered test

1. Reproduce 37 labelled survivor grammars.
2. Quotient them by all \(S_4\) relabellings.
3. Register the number and representative context structures of remaining structural grammar families.
4. Verify that universal compatibility is absent and that the IAR-like overlapping-triple grammar is one survivor.
5. Do **not** add a further selector unless it has an independent core/phenomenological argument that would remain defensible even if it excluded IAR.

## Interpretation rule

If multiple structural families remain, the four core consequences have genuinely narrowed the grammar class but have not derived a unique grammar. Immanence and non-objectification must then be formalised in a richer language before they can supply further selection; treating their vacuous satisfaction in the simple graph as a derivation would be invalid.
