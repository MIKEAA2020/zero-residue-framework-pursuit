#!/usr/bin/env python3
"""GC3 finite audit of the maximal-expression conditional theorem.

The data structures represent only typed bridge status. They do not model the
non-structural ground or convert a formal finite set into genuine aspects.
"""
from dataclasses import dataclass
import json
from pathlib import Path
from typing import FrozenSet, Tuple


@dataclass(frozen=True)
class AspectModel:
    name: str
    complete: bool
    self_knowing: bool
    aspects: FrozenSet[int]
    exhaustive: bool
    nonrepresentational_identity: bool
    realized: FrozenSet[int]
    aspect_domain_independent: bool
    compossibility_declared: bool
    noncomposition_typed: bool


def well_formed(m: AspectModel) -> bool:
    return m.realized <= m.aspects


def mec(m: AspectModel) -> bool:
    return m.aspects <= m.realized


def conditional_premises(m: AspectModel) -> bool:
    return m.complete and m.self_knowing and m.exhaustive and m.nonrepresentational_identity


def conditional_theorem_holds(m: AspectModel) -> bool:
    return (not conditional_premises(m)) or mec(m)


def make_models() -> Tuple[AspectModel, ...]:
    both = frozenset({0, 1})
    zero = frozenset({0})
    return (
        AspectModel("bare_self_presence", True, True, frozenset(), False, False, frozenset(), False, False, True),
        AspectModel("representational_knowledge", True, True, both, True, False, zero, True, True, True),
        AspectModel("full_nonrepresentational_aspects", True, True, both, True, True, both, True, True, True),
        AspectModel("restricted_nonrepresentational_domain", True, True, zero, True, True, zero, False, True, True),
        AspectModel("unresolved_compossibility", True, True, both, True, True, both, True, False, True),
    )


def main() -> None:
    models = make_models()
    expected = {
        # MEC is vacuously true on the empty aspect domain; that is precisely why
        # MEC alone cannot establish nonempty finite articulation.
        "bare_self_presence": (True, True, True, False, False, True),
        # The implication remains true here only because I is absent; it does
        # not yield MEC from represented exhaustive knowledge.
        "representational_knowledge": (True, False, True, True, True, True),
        "full_nonrepresentational_aspects": (True, True, True, True, True, True),
        "restricted_nonrepresentational_domain": (True, True, True, False, True, True),
        "unresolved_compossibility": (True, True, True, True, False, True),
    }
    # tuple: well_formed, MEC, conditional theorem, independent-domain, compossibility, noncomposition
    print("GC3 maximal-expression hinge audit")
    print("model                              form  MEC  cond-thm  A-independent  comp  NC")
    print("-" * 88)
    results = {}
    for m in models:
        got = (
            well_formed(m),
            mec(m),
            conditional_theorem_holds(m),
            m.aspect_domain_independent,
            m.compossibility_declared,
            m.noncomposition_typed,
        )
        assert got == expected[m.name], (m.name, got, expected[m.name])
        print(f"{m.name:34} " + " ".join(f"{str(x):5}" for x in got))
        results[m.name] = {
            "complete": m.complete,
            "self_knowing": m.self_knowing,
            "exhaustive": m.exhaustive,
            "nonrepresentational_identity": m.nonrepresentational_identity,
            "MEC": mec(m),
            "conditional_theorem_holds": conditional_theorem_holds(m),
            "aspect_domain_independent": m.aspect_domain_independent,
            "compossibility_declared": m.compossibility_declared,
            "noncomposition_typed": m.noncomposition_typed,
        }

    by_name = {m.name: m for m in models}
    # Explicit E and I make the conditional theorem valid in every listed model.
    assert all(conditional_theorem_holds(m) for m in models)
    # C and W alone do not furnish E, I, or a nonempty finite domain.
    b = by_name["bare_self_presence"]
    assert b.complete and b.self_knowing and not b.exhaustive and not b.nonrepresentational_identity and not b.aspects
    # Representational knowing leaves a possible/actual gap.
    r = by_name["representational_knowledge"]
    assert r.exhaustive and not r.nonrepresentational_identity and not mec(r)
    # MEC can hold relative to a domain whose boundary is not independently fixed.
    s = by_name["restricted_nonrepresentational_domain"]
    assert mec(s) and not s.aspect_domain_independent
    # MEC alone does not provide compossibility.
    u = by_name["unresolved_compossibility"]
    assert mec(u) and not u.compossibility_declared

    payload = {
        "audit": "GC3 maximal-expression hinge audit v1",
        "scope": "Finite bridge-status audit; not a model of the non-structural ground or proof of plenitude.",
        "results": results,
        "conclusions": {
            "conditional_identity_theorem_valid_when_E_and_I_are_explicit": True,
            "C_and_W_alone_do_not_entail_E_I_or_nonempty_finite_aspects": True,
            "representational_exhaustivity_does_not_entail_MEC": True,
            "MEC_relative_to_restricted_domain_does_not_settle_aspect_typing": True,
            "MEC_does_not_settle_compossibility": True,
            "positive_plenitude_proof_requires_independent_GC3a_to_GC3d_bridges": True,
        },
    }
    out = Path("Point-Sphere_Global_Coherence_Maximal_Expression_Audit_v1.json")
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print("\nSUMMARY")
    print("[PASS] The conditional identity theorem is valid when E and I are explicit.")
    print("[PASS] C plus W alone does not entail a finite aspect domain, exhaustivity, or non-representational realization.")
    print("[PASS] Representational self-knowledge leaves the possible/actual gap open.")
    print("[PASS] MEC can conceal aspect-domain selection and leaves compossibility independent.")
    print("[NON-DERIVATION] No positive MEC theorem follows without independent GC3a–d bridges.")
    print(f"[WRITE] {out}")


if __name__ == "__main__":
    main()
