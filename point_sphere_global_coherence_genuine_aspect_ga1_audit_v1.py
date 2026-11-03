#!/usr/bin/env python3
"""GA1 finite coherence-boundary audit.

This script checks only the stated finite witness semantics.  It does not
interpret the finite candidates as literal ground structure or decide which
semantic expansion is metaphysically true.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path

ATOMS = ("p", "q", "r", "s")
CANDIDATES = {
    "a_bottom": frozenset({("p", True), ("p", False)}),
    "a_d": frozenset({("p", True)}),
    "a_f": frozenset({("q", True)}),
    "a_g": frozenset({("r", True)}),
    "a_x": frozenset({("s", True)}),
}
# These are the entire fixed GA1 structural reduct, alongside candidate content.
NG = {"a_bottom": True, "a_d": True, "a_f": True, "a_g": False, "a_x": True}
# An internally contradictory candidate cannot belong to an admissible proper context.
CTX = {"a_bottom": False, "a_d": True, "a_f": True, "a_g": True, "a_x": False}
EXPANSIONS = {
    "M_plus": {
        "Det_G": {"a_d"},
        "GA": {"a_d"},
    },
    "M_minus": {
        "Det_G": set(),
        "GA": set(),
    },
}


def satisfies(valuation: dict[str, bool], content: frozenset[tuple[str, bool]]) -> bool:
    return all(valuation[atom] is sign for atom, sign in content)


def coherent(content: frozenset[tuple[str, bool]]) -> bool:
    return any(
        satisfies(dict(zip(ATOMS, values)), content)
        for values in itertools.product((False, True), repeat=len(ATOMS))
    )


def ncd_holds(expansion: dict[str, set[str]], coherence: dict[str, bool]) -> bool:
    # NCD: GA(a) implies Coh(a).
    return all(coherence[name] for name in expansion["GA"])


def main() -> None:
    coherence = {name: coherent(content) for name, content in CANDIDATES.items()}
    structural_reduct = {
        name: {
            "content": sorted((atom if sign else f"not {atom}") for atom, sign in content),
            "Coh": coherence[name],
            "NG": NG[name],
            "Ctx": CTX[name],
        }
        for name, content in CANDIDATES.items()
    }

    # The structural projection is deliberately copied into each expansion.
    # Only Det_G and GA vary across them.
    expansion_structural_reducts = {
        name: {candidate: dict(data) for candidate, data in structural_reduct.items()}
        for name in EXPANSIONS
    }

    assertions = {
        "a_bottom_unsatisfiable": coherence["a_bottom"] is False,
        "all_nonbottom_witnesses_satisfiable": all(
            coherence[name] for name in ("a_d", "a_f", "a_g", "a_x")
        ),
        "ncd_holds_M_plus": ncd_holds(EXPANSIONS["M_plus"], coherence),
        "ncd_holds_M_minus": ncd_holds(EXPANSIONS["M_minus"], coherence),
        "ncd_excludes_a_bottom_in_every_expansion": all(
            "a_bottom" not in expansion["GA"]
            for expansion in EXPANSIONS.values()
        ),
        "same_structural_reduct_in_both_expansions": (
            expansion_structural_reducts["M_plus"]
            == expansion_structural_reducts["M_minus"]
            == structural_reduct
        ),
        "a_d_passes_all_structural_filters": (
            coherence["a_d"] and NG["a_d"] and CTX["a_d"]
        ),
        "a_d_genuine_only_in_M_plus": (
            "a_d" in EXPANSIONS["M_plus"]["GA"]
            and "a_d" not in EXPANSIONS["M_minus"]["GA"]
        ),
        "a_d_determinate_only_in_M_plus": (
            "a_d" in EXPANSIONS["M_plus"]["Det_G"]
            and "a_d" not in EXPANSIONS["M_minus"]["Det_G"]
        ),
        "coherence_does_not_imply_NG": coherence["a_g"] and not NG["a_g"],
        "coherence_does_not_imply_Ctx": coherence["a_x"] and not CTX["a_x"],
        "coherence_NG_Ctx_do_not_entail_GA": (
            coherence["a_d"] and NG["a_d"] and CTX["a_d"]
            and "a_d" not in EXPANSIONS["M_minus"]["GA"]
        ),
        "coherence_NG_Ctx_do_not_entail_Det_G": (
            coherence["a_d"] and NG["a_d"] and CTX["a_d"]
            and "a_d" not in EXPANSIONS["M_minus"]["Det_G"]
        ),
    }
    result = {
        "audit": "GA1 coherence/non-contradiction boundary audit v1",
        "semantics": "finite classical bivalent satisfiability witness class",
        "candidates": structural_reduct,
        "expansions": {
            name: {
                "Det_G": sorted(data["Det_G"]),
                "GA": sorted(data["GA"]),
            }
            for name, data in EXPANSIONS.items()
        },
        "assertions": assertions,
        "passed": all(assertions.values()),
        "limits": [
            "The finite semantics witnesses a non-entailment only.",
            "The audit does not select a metaphysically true Det_G extension.",
            "NCD is an explicit framework-level necessity bridge, not bare logic.",
            "Non-classical rivals require their own declared satisfaction semantics.",
        ],
    }
    destination = Path(__file__).with_name(
        "Point-Sphere_Global_Coherence_Genuine_Aspect_Criterion_GA1_Audit_v1.json"
    )
    destination.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    assert result["passed"], json.dumps(result, indent=2)
    print(f"PASS: {destination.name} ({len(assertions)} assertions)")


if __name__ == "__main__":
    main()
