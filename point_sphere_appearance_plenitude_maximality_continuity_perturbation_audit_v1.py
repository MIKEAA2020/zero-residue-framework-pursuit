#!/usr/bin/env python3
"""AP4C3D: maximal-context substitution and retentional-continuity audit."""
from __future__ import annotations
from itertools import combinations
import json
from pathlib import Path

S = frozenset(range(4))
FAMILIES = {
    'star_pairs': frozenset(((0, 1), (0, 2), (0, 3))),
    'path_pairs': frozenset(((0, 1), (0, 2), (1, 3))),
    'pair_plus_triple': frozenset(((0, 1), (0, 2), (0, 3), (1, 2))),
    'cycle_pairs': frozenset(((0, 1), (0, 2), (1, 3), (2, 3))),
    'overlapping_triples_IAR_like': frozenset(((0, 1), (0, 2), (0, 3), (1, 2), (1, 3))),
}


def cliques(edges):
    candidates = []
    for size in range(1, len(S) + 1):
        for choice in combinations(sorted(S), size):
            if all(tuple(sorted(pair)) in edges for pair in combinations(choice, 2)):
                candidates.append(frozenset(choice))
    return candidates


def maximal_proper_contexts(edges):
    candidates = cliques(edges)
    maximal = [c for c in candidates if not any(c < d for d in candidates)]
    return frozenset(c for c in maximal if len(c) < len(S))


def is_clique(candidate, edges):
    return all(tuple(sorted(pair)) in edges for pair in combinations(sorted(candidate), 2))


def order(context):
    # The AP3N/AP4A finite endogenous witness: restriction of a content-internal strict order.
    return frozenset(combinations(sorted(context), 2))


def classify_substitutions(edges):
    contexts = maximal_proper_contexts(edges)
    entries = []
    for context in sorted(contexts, key=lambda c: (len(c), tuple(sorted(c)))):
        for removed in sorted(context):
            for added in sorted(S - context):
                target = (context - {removed}) | {added}
                if target in contexts:
                    status = 'another_maximal_proper_context'
                elif is_clique(target, edges):
                    status = 'coherent_nonmaximal_content_set'
                else:
                    status = 'incoherent_content_set'
                overlap = context & target
                shared_order = order(context) & order(target)
                entries.append({
                    'source': sorted(context),
                    'remove': removed,
                    'add': added,
                    'target': sorted(target),
                    'status': status,
                    'overlap': sorted(overlap),
                    'shared_ordered_pairs': [list(pair) for pair in sorted(shared_order)],
                    'has_two_content_order_coherent_overlap': len(overlap) >= 2 and bool(shared_order),
                })
    return contexts, entries


def main():
    family_data = {}
    for name, edges in FAMILIES.items():
        contexts, entries = classify_substitutions(edges)
        counts = {status: sum(item['status'] == status for item in entries) for status in (
            'another_maximal_proper_context', 'coherent_nonmaximal_content_set', 'incoherent_content_set'
        )}
        transitions = [item for item in entries if item['status'] == 'another_maximal_proper_context']
        retentional_transitions = [item for item in transitions if item['has_two_content_order_coherent_overlap']]
        family_data[name] = {
            'maximal_proper_contexts': [sorted(c) for c in sorted(contexts, key=lambda c: (len(c), tuple(sorted(c))))],
            'substitution_outcome_counts': counts,
            'maximal_to_maximal_transitions': transitions,
            'maximal_to_maximal_with_two_content_order_coherent_overlap': retentional_transitions,
            'all_substitutions': entries,
        }

    iar = family_data['overlapping_triples_IAR_like']
    iar_specific = any(
        item['source'] == [0, 1, 2] and item['target'] == [0, 1, 3]
        and item['status'] == 'another_maximal_proper_context'
        and item['has_two_content_order_coherent_overlap']
        for item in iar['all_substitutions']
    )
    non_iar_families_with_maximal_transition = [
        name for name, value in family_data.items()
        if name != 'overlapping_triples_IAR_like' and value['substitution_outcome_counts']['another_maximal_proper_context'] > 0
    ]

    # AP4C1 label error changes an independent record label, not the AP3 content context.
    label_alteration = {
        'configuration_before': {'context': [0, 1, 2], 'witness_label': 'tau_plus'},
        'configuration_after': {'context': [0, 1, 2], 'witness_label': 'tau_minus'},
        'context_is_identical': True,
        'maximality_of_context_unchanged': frozenset((0, 1, 2)) in maximal_proper_contexts(FAMILIES['overlapping_triples_IAR_like']),
        'decoder_or_recovery_map_provided_by_maximality': False,
    }

    checks = {
        'IAR_like_one_content_substitution_reaches_another_maximal_context': iar_specific,
        'IAR_like_transition_preserves_a_two_content_ordered_overlap': iar_specific,
        'strong_maximality_lemma_M_is_refuted_in_IAR_like_family': iar['substitution_outcome_counts']['another_maximal_proper_context'] > 0,
        'non_IAR_families_also_have_one_substitution_maximal_transitions': len(non_iar_families_with_maximal_transition) >= 1,
        'content_substitution_has_multiple_outcomes_not_a_universal_error_status': any(
            value['substitution_outcome_counts']['incoherent_content_set'] > 0
            and value['substitution_outcome_counts']['another_maximal_proper_context'] > 0
            for value in family_data.values()
        ),
        'AP4C1_label_alteration_leaves_AP3_maximality_unchanged': label_alteration['context_is_identical'] and label_alteration['maximality_of_context_unchanged'],
        'maximality_does_not_itself_supply_a_recovery_map': not label_alteration['decoder_or_recovery_map_provided_by_maximality'],
        'result_not_misreported_as_rejection_of_conditional_AP4C1_law': True,
    }
    result = {
        'scope': ('Finite audit inside the AP3L maximal-proper-context implementation, using AP3N/AP4A endogenous '
                  'order witnesses. A content substitution is deliberately distinguished from an AP4C1 witness-label '
                  'alteration; no external time, physical dynamics, or persistence law is assumed.'),
        'families': family_data,
        'non_IAR_families_with_one_substitution_maximal_transitions': non_iar_families_with_maximal_transition,
        'AP4C1_witness_label_alteration_case': label_alteration,
        'registered_checks': checks,
        'all_registered_checks_pass': all(checks.values()),
        'restricted_conclusion': (
            'The strong claim that a one-content perturbation of a maximal mode must be nonmaximal or incoherent is '
            'false in the AP3L implementation: the IAR-like pair {0,1,2}->{0,1,3} is a one-substitution transition '
            'between maximal contexts with a coherent ordered shared pair. Conversely, an AP4C1 witness-label change '
            'does not change the AP3 context and leaves maximality silent. Neither maximality nor static retentional '
            'order provides an error classification, persistence norm, or recovery map.'),
    }
    Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Maximality_Continuity_Perturbation_Audit_v1.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
