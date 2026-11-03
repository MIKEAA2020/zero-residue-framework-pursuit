#!/usr/bin/env python3
"""GC4 finite semantic audit of CI-to-truth and rival closure bridges.

It demonstrates non-entailment among typed claims. It does not prove that any
ultimate fact is brute, that a non-aware ground exists, or that a framework is
false; those are philosophical positions represented for bridge testing.
"""
from dataclasses import dataclass
import json
from pathlib import Path
from typing import Tuple


@dataclass(frozen=True)
class Model:
    name: str
    RN: bool
    OCI: bool
    EC: bool
    aware_plenitude: bool
    taxonomy_exhaustive: bool
    equivalence_checked: bool
    unique_candidate: bool
    phenomenal_adequacy: bool
    physical_adequacy: bool
    truth: bool


def main() -> None:
    models: Tuple[Model, ...] = (
        Model("locally_rational_primitive", True, False, False, False, False, False, False, False, False, False),
        Model("essence_closed_neutral", True, True, True, False, True, True, False, False, True, False),
        Model("coherent_but_incomplete", True, True, True, True, True, True, True, False, False, False),
        Model("equivalent_formulations", True, True, True, True, True, False, False, True, True, False),
        Model("taxonomy_extension", True, True, True, False, False, True, False, True, True, False),
        Model("oracle_complete_theory", True, True, True, True, True, True, True, True, True, True),
    )

    print("GC4 CI-to-truth and rival-closure semantic audit")
    print("model                       RN OCI EC AG+P Tax Eq Uniq Phi Phys True")
    print("-" * 81)
    results = {}
    for m in models:
        row = (m.RN, m.OCI, m.EC, m.aware_plenitude, m.taxonomy_exhaustive,
               m.equivalence_checked, m.unique_candidate, m.phenomenal_adequacy,
               m.physical_adequacy, m.truth)
        print(f"{m.name:27} " + " ".join(f"{str(x):4}" for x in row))
        results[m.name] = {
            "RN": m.RN, "OCI": m.OCI, "EC": m.EC,
            "aware_plenitude": m.aware_plenitude,
            "taxonomy_exhaustive": m.taxonomy_exhaustive,
            "equivalence_checked": m.equivalence_checked,
            "unique_candidate": m.unique_candidate,
            "phenomenal_adequacy": m.phenomenal_adequacy,
            "physical_adequacy": m.physical_adequacy,
            "truth": m.truth,
        }

    by_name = {m.name: m for m in models}
    # B1: RN does not entail OCI.
    assert by_name["locally_rational_primitive"].RN and not by_name["locally_rational_primitive"].OCI
    # B3: EC does not entail aware plenitude.
    assert by_name["essence_closed_neutral"].EC and not by_name["essence_closed_neutral"].aware_plenitude
    # Internal abstract coherence/uniqueness does not substitute for adequacy.
    c = by_name["coherent_but_incomplete"]
    assert c.unique_candidate and not c.phenomenal_adequacy and not c.physical_adequacy and not c.truth
    # A named taxonomy must test equivalence and extension, not merely count labels.
    assert not by_name["equivalent_formulations"].equivalence_checked
    assert not by_name["taxonomy_extension"].taxonomy_exhaustive
    # Only the oracle model has truth as an input; no nontrivial truth bridge is encoded.
    assert by_name["oracle_complete_theory"].truth

    payload = {
        "audit": "GC4 CI-to-truth and rival-closure semantic audit v1",
        "scope": "Finite non-entailment audit; not a proof of metaphysical truth or a complete rival taxonomy.",
        "results": results,
        "conclusions": {
            "RN_does_not_entail_OCI": True,
            "EC_does_not_entail_aware_ground_or_plenitude": True,
            "internal_unique_coherence_does_not_replace_phenomenal_and_physical_adequacy": True,
            "named_rival_list_needs_equivalence_and_extension_controls": True,
            "no_nontrivial_CI_to_truth_theorem_established": True,
        },
    }
    out = Path("Point-Sphere_Global_Coherence_Truth_Rival_Closure_Audit_v1.json")
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print("\nSUMMARY")
    print("[PASS] Rational inquiry alone does not entail an ontology with no ultimate primitive fact.")
    print("[PASS] Essential closure alone does not select awareness or plenitude.")
    print("[PASS] Internal coherence/unique survival cannot replace phenomenal and physical adequacy.")
    print("[PASS] A rival taxonomy requires extension and equivalence controls.")
    print("[NON-DERIVATION] No nontrivial CI-to-truth theorem is supplied by the stated premises.")
    print(f"[WRITE] {out}")


if __name__ == "__main__":
    main()
