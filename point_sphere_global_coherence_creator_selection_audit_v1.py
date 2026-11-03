#!/usr/bin/env python3
"""GC2 finite classification of creator-selection reply types.

The code verifies the declared case taxonomy. It does not formalize a deity,
prove a metaphysical theorem from logic alone, or judge religious traditions.
"""
from dataclasses import dataclass
import json
from pathlib import Path
from typing import Tuple


@dataclass(frozen=True)
class Reply:
    name: str
    strict_simplicity: bool
    weak_nbd: bool
    strong_nbd: bool
    contingent_exclusive_actualization: bool
    selector_or_determination_debt: bool
    note: str


def main() -> None:
    replies: Tuple[Reply, ...] = (
        Reply(
            "unmarked_contingent_selection",
            True,
            False,
            False,
            True,
            False,
            "No difference-maker is supplied; fails even weak NBD.",
        ),
        Reply(
            "intrinsic_differentiator",
            False,
            True,
            True,
            True,
            False,
            "Supplies a nonprimitive difference-maker but violates frozen strict-simplicity typing.",
        ),
        Reply(
            "extrinsic_single_act",
            True,
            True,
            False,
            True,
            True,
            "Can count as a weak differentiator, but is circular/primitive unless an independent account fixes why its relation targets this outcome.",
        ),
        Reply(
            "primitive_agent_causation",
            True,
            True,
            False,
            True,
            True,
            "Preserves a primitive free selection and weak NBD, but leaves a terminal selector under strong NBD.",
        ),
        Reply(
            "necessary_determination",
            True,
            True,
            True,
            False,
            True,
            "Avoids contingent selection only if the exact-totality bridge is independently supplied; it is a C-Nec-D rather than C-Cont structure.",
        ),
    )

    expected = {
        "unmarked_contingent_selection": (True, False, False, True, False),
        "intrinsic_differentiator": (False, True, True, True, False),
        "extrinsic_single_act": (True, True, False, True, True),
        "primitive_agent_causation": (True, True, False, True, True),
        "necessary_determination": (True, True, True, False, True),
    }

    print("GC2 creator-selection reply audit")
    print("reply                         SSS    NBD-w  NBD-s  CEA    debt")
    print("-" * 76)
    results = {}
    for r in replies:
        got = (
            r.strict_simplicity,
            r.weak_nbd,
            r.strong_nbd,
            r.contingent_exclusive_actualization,
            r.selector_or_determination_debt,
        )
        assert got == expected[r.name], (r.name, got, expected[r.name])
        print(f"{r.name:28} " + " ".join(f"{str(x):5}" for x in got))
        results[r.name] = {
            "strict_simplicity": r.strict_simplicity,
            "weak_nbd": r.weak_nbd,
            "strong_nbd": r.strong_nbd,
            "contingent_exclusive_actualization": r.contingent_exclusive_actualization,
            "selector_or_determination_debt": r.selector_or_determination_debt,
            "note": r.note,
        }

    by_name = {r.name: r for r in replies}
    # No reply maintains frozen SSS + CEA + strong NBD.
    assert not any(
        r.strict_simplicity and r.contingent_exclusive_actualization and r.strong_nbd
        for r in replies
    )
    # Weak NBD admits primitive/extrinsic answers, so weak NBD alone is not a no-go.
    assert by_name["extrinsic_single_act"].weak_nbd
    assert by_name["primitive_agent_causation"].weak_nbd
    # Necessary determination exits the contingent-selection target class.
    assert not by_name["necessary_determination"].contingent_exclusive_actualization

    payload = {
        "audit": "GC2 creator-selection reply audit v1",
        "scope": "Finite case-classification audit; conditional only; not an adjudication of historical theology.",
        "results": results,
        "conclusions": {
            "no_frozen_SSS_CEA_strong_NBD_reply_in_declared_taxonomy": True,
            "weak_NBD_alone_does_not_rule_out_primitive_or_extrinsic_selection": True,
            "necessary_determination_avoids_CEA_by_changing_realization_rule": True,
            "appearance_not_proven_by_creator_selection_debt": True,
        },
    }
    out = Path("Point-Sphere_Global_Coherence_Creator_Selection_Audit_v1.json")
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print("\nSUMMARY")
    print("[PASS] Under frozen strong NBD, no declared reply preserves SSS and contingent exclusive actualization.")
    print("[PASS] Under weak NBD, primitive agent causation and extrinsic-act replies remain formally live with a selector debt.")
    print("[PASS] Necessary determination avoids the contingent-selection dilemma only by becoming a different realization-rule family.")
    print("[NON-TRANSFER] Creator-selection debt does not by itself prove Appearance or plenitude.")
    print(f"[WRITE] {out}")


if __name__ == "__main__":
    main()
