#!/usr/bin/env python3
"""GA2a finite self-knowledge requirement / hinge-identity audit.

The model class is a witness for non-entailment from a thin self-knowledge
base. It does not decide whether a richer, independently specified semantics
of complete self-knowledge can meet the GA2 independence criterion.
"""

from __future__ import annotations

import json
from pathlib import Path

CANDIDATE = "a"

# K0 contains the thin self-knowledge package used by the audit.  It contains
# no finite-articulation condition and no Det_G, GA, Mode, or realization term.
K0_MODELS = {
    "bare_self_presence": {
        "complete": True,
        "self_knowing": True,
        "simple": True,
        "SKCont": set(),
        "R": set(),
    },
    "rich_self_presence": {
        "complete": True,
        "self_knowing": True,
        "simple": True,
        "SKCont": {CANDIDATE},
        "R": {CANDIDATE},
    },
}

# K1 = K0 + F_a, with F_a the explicitly added finite-articulation requirement
# that a is a self-knowledge content.  It is not claimed to follow from K0.
K1_MODELS = {"rich_self_presence": K0_MODELS["rich_self_presence"]}


def required(theory_models: dict[str, dict[str, object]], candidate: str) -> bool:
    """K entails SKCont(candidate) exactly when every K-model contains it."""
    return all(candidate in model["SKCont"] for model in theory_models.values())


def required_extension(theory_models: dict[str, dict[str, object]]) -> set[str]:
    return {CANDIDATE} if required(theory_models, CANDIDATE) else set()


def actual_extension(model: dict[str, object]) -> set[str]:
    """Declared realization extension; I is checked rather than manufactured here."""
    return set(model["R"])


def protected_identity_holds(model: dict[str, object]) -> bool:
    """I: every self-knowledge content is actual self-presentation."""
    return set(model["SKCont"]).issubset(actual_extension(model))


def main() -> None:
    req_k0 = required_extension(K0_MODELS)
    req_k1 = required_extension(K1_MODELS)

    # H_D is applied only after requirement has been computed in the restricted
    # self-knowledge vocabulary.  GA3/GA4 filters are represented as true for
    # this one declared witness solely to isolate the non-vacuity issue.
    structural_filters = {CANDIDATE: {"finite": True, "coherent": True, "non_gauge": True, "context": True}}
    det_k0 = set(req_k0)  # H_D: Det_G iff Req_K
    det_k1 = set(req_k1)
    # GA0 supplies these filters as necessary conditions, not a sufficient
    # GA definition.  The set below is therefore only an eligible
    # determination-candidate domain, not a GA extension.
    eligible_det_k0 = {a for a in det_k0 if all(structural_filters[a].values())}
    eligible_det_k1 = {a for a in det_k1 if all(structural_filters[a].values())}

    # I ensures self-knowledge content is actual in every model.  This checks
    # that GA2's issue is domain generation, not a second realization selector.
    I_holds_k0 = all(protected_identity_holds(model) for model in K0_MODELS.values())
    I_holds_k1 = all(protected_identity_holds(model) for model in K1_MODELS.values())

    assertions = {
        "all_K0_models_satisfy_thin_selfknowledge_core": all(
            model["complete"] and model["self_knowing"] and model["simple"]
            for model in K0_MODELS.values()
        ),
        "K0_has_bare_self_presence_countermodel": K0_MODELS["bare_self_presence"]["SKCont"] == set(),
        "K0_does_not_require_a_finite_content": req_k0 == set(),
        "K1_requires_the_explicitly_added_finite_content": req_k1 == {CANDIDATE},
        "K1_is_a_strict_enrichment_of_K0_model_class": (
            set(K1_MODELS) < set(K0_MODELS)
        ),
        "H_D_is_realization_free_in_the_audit_definition": (
            det_k0 == req_k0 and det_k1 == req_k1
        ),
        "H_D_is_vacuous_over_thin_K0": eligible_det_k0 == set(),
        "H_D_plus_F_a_yields_a_finite_eligible_determination_candidate": (
            eligible_det_k1 == {CANDIDATE}
        ),
        "protected_I_actualizes_known_content_in_K0": I_holds_k0,
        "protected_I_actualizes_known_content_in_K1": I_holds_k1,
        "K1_required_content_is_actual_in_declared_I_models": all(
            CANDIDATE in actual_extension(model)
            for model in K1_MODELS.values()
        ),
        "positive_output_enters_at_F_a_not_from_thin_K0": (
            not required(K0_MODELS, CANDIDATE)
            and required(K1_MODELS, CANDIDATE)
        ),
    }

    result = {
        "audit": "GA2a self-knowledge requirement / hinge-identity audit v1",
        "result_type": "thin-core non-entailment plus hinge-location witness",
        "theories": {
            "K0": {
                "description": "complete, self-knowing, simple; no finite-articulation axiom",
                "models": sorted(K0_MODELS),
                "Req_extension": sorted(req_k0),
                "H_D_Det_extension": sorted(det_k0),
                "eligible_Det_extension": sorted(eligible_det_k0),
            },
            "K1": {
                "description": "K0 plus explicit F_a finite self-knowledge-content requirement",
                "models": sorted(K1_MODELS),
                "Req_extension": sorted(req_k1),
                "H_D_Det_extension": sorted(det_k1),
                "eligible_Det_extension": sorted(eligible_det_k1),
            },
        },
        "assertions": assertions,
        "passed": all(assertions.values()),
        "limits": [
            "K0 not-entailing finite articulation does not prove no richer independent self-knowledge semantics exists.",
            "F_a is a labelled enrichment, not an argument that it is arbitrary or false.",
            "The audit does not show H_D and H_F are one proposition; it shows that both roles are needed for non-vacuous finite output.",
            "No grammar, phenomenology, persistence, public record, or physical law is derived.",
        ],
    }
    output = Path(__file__).with_name(
        "Point-Sphere_Global_Coherence_Genuine_Aspect_Criterion_GA2_Hinge_Identity_Audit_v1.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    assert result["passed"], json.dumps(result, indent=2)
    print(f"PASS: {output.name} ({len(assertions)} assertions)")


if __name__ == "__main__":
    main()
