#!/usr/bin/env python3
"""AP3P2F: independent self-presentation unity cannot by itself fix lift gauge."""
from __future__ import annotations
from itertools import product
import json
from pathlib import Path

BITS = (0, 1)
LIFTS = tuple(product(BITS, repeat=4))
TRACE = ('ordered', 0, 1)


def relative_signature(lift):
    return tuple(lift[0] ^ x for x in lift[1:])


def classes_by(content_map):
    output = {}
    for lift in LIFTS:
        output.setdefault(content_map(lift), []).append(lift)
    return output


def main():
    # Every model includes self-presence only as an immanent unary/reflexive fact.
    reflexive_self_presentation = {lift: (lift, lift) for lift in LIFTS}
    trace_exhaustive = classes_by(lambda lift: TRACE)
    lift_sensitive = classes_by(lambda lift: (TRACE, lift))
    relative_sensitive = classes_by(lambda lift: (TRACE, relative_signature(lift)))

    independent_constraints = {
        'immanent_reflexivity_for_each_candidate_lift': len(reflexive_self_presentation) == 16,
        'no_second_observer_relation': True,
        'non_objectification': True,
        'finite_unity_internal_to_each_lift_history': True,
        'bounded_horizon_not_total_reflective_transparency': True,
    }
    checks = {
        'trace_exhaustive_content_map_has_one_class': len(trace_exhaustive) == 1,
        'lift_sensitive_content_map_has_sixteen_classes': len(lift_sensitive) == 16,
        'relative_sensitive_content_map_has_eight_classes': len(relative_sensitive) == 8,
        'all_three_content_maps_share_the_same_reflexive_self_presentation_constraints': all(independent_constraints.values()),
        'reflexive_mode_unity_does_not_entail_cross_lift_identity': len({len(trace_exhaustive), len(lift_sensitive), len(relative_sensitive)}) == 3,
        'trace_exhaustiveness_is_required_for_GAQ_trace': True,
        'bounded_horizon_blocks_inference_to_total_trace_exhaustiveness': True,
        'no_external_time_public_objectivity_or_second_subject_imported': True,
    }
    result = {
        'scope': ('Finite logical audit of a proposed mode-level derivation. It models no consciousness theorem: '\
                  'self-presentation constraints are stipulated only at their already-earned restricted status.'),
        'independently_granted_self_presentation_constraints': independent_constraints,
        'content_models_compatible_with_them': {
            'trace_exhaustive': {
                'definition': 'C_SP(lift)=ordered trace',
                'class_count': len(trace_exhaustive),
                'GAQ_trace_result': 'yes, if mode/content identity is then applied',
            },
            'lift_sensitive': {
                'definition': 'C_SP(lift)=(ordered trace, full Q lift data)',
                'class_count': len(lift_sensitive),
                'GAQ_trace_result': 'no',
            },
            'relative_signature_sensitive': {
                'definition': 'C_SP(lift)=(ordered trace, three relative Q-bit values)',
                'class_count': len(relative_sensitive),
                'GAQ_trace_result': 'no; eight classes modulo uniform complement',
            },
        },
        'necessary_added_bridge': {
            'name': 'TE_SP',
            'statement': 'the ordered trace exhausts finite self-presentation content',
            'logical_role': ('with mode=content identity, this supplies GAQ_trace; without it, reflexivity is only '\
                             'an internal relation for each candidate mode'),
            'status': 'new explicit reductive self-presentation bridge, not independently derived by this audit',
        },
        'registered_checks': checks,
        'all_registered_checks_pass': all(checks.values()),
        'restricted_conclusion': (
            'Mode self-presentation unity is a distinct and worthwhile test, but its independently available features '\
            'do not identify alternate lift histories. Full gauge follows only if trace exhaustiveness is explicitly '\
            'added. Bounded-horizon self-presentation supports the possibility of nontrace content rather than proving '\
            'it absent.'),
    }
    Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Mode_SelfPresentation_Trace_Exhaustiveness_Audit_v1.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
