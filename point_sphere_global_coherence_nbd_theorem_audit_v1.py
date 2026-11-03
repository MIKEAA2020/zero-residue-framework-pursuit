#!/usr/bin/env python3
"""GC1 finite semantic audit.

This enumerates the frozen realization-model families from the specification.
It does not model a metaphysical ground or prove a global-coherence thesis.
It verifies which conclusions follow from the declared finite predicates.
"""
from dataclasses import dataclass
import json
from pathlib import Path
from typing import FrozenSet, Tuple

Point = int
Permutation = Tuple[Point, ...]

IDENTITY: Permutation = (0, 1)
SWAP: Permutation = (1, 0)


@dataclass(frozen=True)
class Model:
    name: str
    omega: FrozenSet[Point]
    aspects: FrozenSet[Point]
    realized: FrozenSet[Point]
    group: Tuple[Permutation, ...]
    differentiators: Tuple[FrozenSet[Point], ...]
    aspect_domain_primitive: bool


def image(p: Permutation, subset: FrozenSet[Point]) -> FrozenSet[Point]:
    return frozenset(p[x] for x in subset)


def well_formed(m: Model) -> bool:
    return m.aspects <= m.omega and m.realized <= m.aspects


def equivariant(m: Model) -> bool:
    return all(image(p, m.realized) == m.realized for p in m.group)


def same_orbit(m: Model, x: Point, y: Point) -> bool:
    return any(p[x] == y for p in m.group)


def separated_by_differentiator(m: Model, x: Point, y: Point) -> bool:
    return any((x in d) != (y in d) for d in m.differentiators)


def nbd(m: Model) -> bool:
    for x in m.aspects:
        for y in m.aspects:
            if same_orbit(m, x, y) and ((x in m.realized) != (y in m.realized)):
                if not separated_by_differentiator(m, x, y):
                    return False
    return True


def mec(m: Model) -> bool:
    return m.aspects <= m.realized


def selector_debt(m: Model) -> bool:
    return bool(m.differentiators) or m.aspect_domain_primitive


def make_models() -> Tuple[Model, ...]:
    both = frozenset({0, 1})
    zero = frozenset({0})
    return (
        Model("empty_invariant", both, both, frozenset(), (IDENTITY, SWAP), (), False),
        Model("full_invariant", both, both, both, (IDENTITY, SWAP), (), False),
        Model("primitive_exclusive", both, both, zero, (IDENTITY, SWAP), (), False),
        Model("marked_exclusive", both, both, zero, (IDENTITY, SWAP), (zero,), False),
        Model("restricted_aspect_domain", both, zero, zero, (IDENTITY,), (zero,), True),
        Model("classical_unmarked_selection", both, both, zero, (IDENTITY, SWAP), (), False),
        Model("appearance_full_domain", both, both, both, (IDENTITY, SWAP), (), False),
    )


def main() -> None:
    models = make_models()
    expected = {
        "empty_invariant": (True, True, True, False, False),
        "full_invariant": (True, True, True, True, False),
        "primitive_exclusive": (True, False, False, False, False),
        "marked_exclusive": (True, False, True, False, True),
        "restricted_aspect_domain": (True, True, True, True, True),
        "classical_unmarked_selection": (True, False, False, False, False),
        "appearance_full_domain": (True, True, True, True, False),
    }

    print("GC1 finite NBD / realization semantic audit")
    print("model                         S0     S1     S2     S3   selector-debt")
    print("-" * 78)
    for m in models:
        got = (well_formed(m), equivariant(m), nbd(m), mec(m), selector_debt(m))
        assert got == expected[m.name], (m.name, got, expected[m.name])
        print(f"{m.name:28} " + " ".join(f"{str(x):5}" for x in got))

    by_name = {m.name: m for m in models}
    # S0 admits the primitive selective model: bare consistency does not entail NBD.
    assert well_formed(by_name["primitive_exclusive"]) and not nbd(by_name["primitive_exclusive"])
    # S1 admits empty and full invariant supports, so it does not entail nonempty realization/MEC.
    assert equivariant(by_name["empty_invariant"]) and not mec(by_name["empty_invariant"])
    assert equivariant(by_name["full_invariant"]) and mec(by_name["full_invariant"])
    # A marker can discharge formal NBD while making a selector primitive visible.
    assert nbd(by_name["marked_exclusive"]) and selector_debt(by_name["marked_exclusive"])
    # Full realization of a restricted domain does not erase the domain-selection burden.
    assert mec(by_name["restricted_aspect_domain"]) and selector_debt(by_name["restricted_aspect_domain"])
    # The same NBD test diagnoses the unmarked creator-selection analogue.
    assert not nbd(by_name["classical_unmarked_selection"])
    # The full-domain appearance analogue satisfies S1/S2/S3, but S3 is a declared rule here.
    assert mec(by_name["appearance_full_domain"])

    results = {}
    for m in models:
        results[m.name] = {
            "S0_well_formed": well_formed(m),
            "S1_equivariant": equivariant(m),
            "S2_nbd": nbd(m),
            "S3_mec": mec(m),
            "selector_debt": selector_debt(m),
            "aspect_domain_primitive": m.aspect_domain_primitive,
        }
    payload = {
        "audit": "GC1 finite NBD / realization semantic audit v1",
        "scope": "Finite semantic non-entailment check; not a metaphysical-ground model or proof of global coherence.",
        "results": results,
        "conclusions": {
            "S0_does_not_entail_S2_NBD": True,
            "S1_does_not_entail_nonempty_realization_or_S3_MEC": True,
            "marked_selection_makes_selector_debt_visible": True,
            "restricted_domain_MEC_leaves_domain_selection_debt": True,
            "no_bare_logic_or_local_rationality_to_NBD_theorem": True,
        },
    }
    out = Path("Point-Sphere_Global_Coherence_NBD_Theorem_Audit_v1.json")
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print("\nSUMMARY")
    print("[PASS] S0 does not entail NBD or maximal realization.")
    print("[PASS] S1/no-preference does not entail nonempty realization or MEC.")
    print("[PASS] NBD exposes unmarked exclusive selection; a marker satisfies it only with visible selector debt.")
    print("[PASS] MEC relative to a restricted aspect domain leaves aspect-domain selection as an independent debt.")
    print("[PASS] The creation-selection and appearance-realization families can be compared under one declared NBD test.")
    print("[NON-DERIVATION] The audit supplies no theorem that bare logic or local rationality entails NBD/CI.")
    print(f"[WRITE] {out}")


if __name__ == "__main__":
    main()
