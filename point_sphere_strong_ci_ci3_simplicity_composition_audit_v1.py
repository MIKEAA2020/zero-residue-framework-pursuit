#!/usr/bin/env python3
"""CI3 finite typing audit for simplicity/composition.

The program verifies classifications in a deliberately abstract profile space.
It proves no metaphysical thesis about an actual ultimate.  In particular,
'an internally explained unity' is a labelled bridge claim, not a certified
explanation.
"""

from __future__ import annotations

import json
from pathlib import Path

PROFILES = {
    "simple": {
        "real_constituents": 0,
        "unity_fact": False,
        "unity_explanation": "not_applicable",
        "intrinsic_unity_bridge_claim": False,
    },
    "bare_composite": {
        "real_constituents": 2,
        "unity_fact": True,
        "unity_explanation": "primitive",
        "intrinsic_unity_bridge_claim": False,
    },
    "essentially_articulated": {
        "real_constituents": 2,
        "unity_fact": True,
        "unity_explanation": "claimed_intrinsic",
        "intrinsic_unity_bridge_claim": True,
    },
    "pseudo_distinct": {
        "real_constituents": 0,
        "unity_fact": False,
        "unity_explanation": "not_applicable",
        "intrinsic_unity_bridge_claim": False,
    },
}


def residual_unity(profile: dict[str, object]) -> bool:
    """A residual unity is an ultimate union fact with no declared explanation."""
    return bool(profile["unity_fact"]) and profile["unity_explanation"] == "primitive"


def structurally_no_residue(profile: dict[str, object]) -> bool:
    """U1/U3 filter only; claimed bridges are not independently certified here."""
    return not residual_unity(profile)


def main() -> None:
    residues = {name: residual_unity(profile) for name, profile in PROFILES.items()}
    no_residue = {name: structurally_no_residue(profile) for name, profile in PROFILES.items()}

    assertions = {
        "bare_composite_has_named_residual_unity": residues["bare_composite"],
        "bare_composite_fails_structural_no_residue_filter": not no_residue["bare_composite"],
        "simple_has_no_constituent_unity_residue": (
            PROFILES["simple"]["real_constituents"] == 0
            and not residues["simple"]
        ),
        "essentially_articulated_has_real_constituents": (
            PROFILES["essentially_articulated"]["real_constituents"] > 1
        ),
        "essentially_articulated_is_not_rejected_by_component_count_alone": (
            no_residue["essentially_articulated"]
            and not residues["essentially_articulated"]
        ),
        "essentially_articulated_unity_is_marked_as_uncertified_bridge": (
            PROFILES["essentially_articulated"]["intrinsic_unity_bridge_claim"]
            and PROFILES["essentially_articulated"]["unity_explanation"] == "claimed_intrinsic"
        ),
        "pseudo_distinct_is_not_composed_merely_by_descriptive_plurality": (
            PROFILES["pseudo_distinct"]["real_constituents"] == 0
            and not residues["pseudo_distinct"]
        ),
        "no_residue_filter_does_not_entail_absolute_simplicity": (
            no_residue["essentially_articulated"]
            and PROFILES["essentially_articulated"]["real_constituents"] > 1
        ),
        "residue_filter_treats_claimed_unity_and_primitive_unity_differently": (
            residues["bare_composite"]
            and not residues["essentially_articulated"]
        ),
    }

    result = {
        "audit": "CI3 simplicity/composition typing audit v1",
        "result_type": "conditional composition-residue result plus non-entailment witness",
        "profiles": PROFILES,
        "residual_unity": residues,
        "structural_no_residue": no_residue,
        "assertions": assertions,
        "passed": all(assertions.values()),
        "limits": [
            "Claimed intrinsic unity is not validated by this finite classification.",
            "The audit does not establish that an articulated ultimate can meet strongest CI.",
            "The audit does not establish absolute simplicity from SCI alone.",
            "Finite aspecthood and external derivative reality are deferred to CI4.",
        ],
    }
    output = Path(__file__).with_name(
        "Point-Sphere_Strong_CI_CI3_Simplicity_Composition_Audit_v1.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    assert result["passed"], json.dumps(result, indent=2)
    print(f"PASS: {output.name} ({len(assertions)} assertions)")


if __name__ == "__main__":
    main()
