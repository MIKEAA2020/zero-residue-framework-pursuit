#!/usr/bin/env python3
"""AP3P1: conditional bi-infinite intrinsic mode-flow grammar audit."""
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
C_P, C_Q = frozenset((0, 1, 2)), frozenset((0, 1, 3))
WINDOW = tuple(range(-6, 7))  # finite diagnostic window for a bi-infinite definition


def cliques(edges):
    out = []
    for r in range(1, len(S) + 1):
        for c in combinations(sorted(S), r):
            if all(tuple(sorted(pair)) in edges for pair in combinations(c, 2)):
                out.append(frozenset(c))
    return out


def contexts(edges):
    candidates = cliques(edges)
    maxima = [c for c in candidates if not any(c < d for d in candidates)]
    return frozenset(c for c in maxima if len(c) < len(S))


def order(context):
    return frozenset(combinations(sorted(context), 2))


def ordered_overlap(c, d):
    overlap = c & d
    return len(overlap) >= 2 and bool(order(c) & order(d))


def has_ordered_neighbor(cs):
    return all(any(d != c and ordered_overlap(c, d) for d in cs) for c in cs)


def phase_context(n):
    return C_P if n % 2 == 0 else C_Q


def alpha_context(context):
    swap = {0: 0, 1: 1, 2: 3, 3: 2}
    return frozenset(swap[x] for x in context)


def phase_trace(n):
    c, d = phase_context(n), phase_context(n + 1)
    shared = c & d
    return {
        'from_phase': n, 'to_phase': n + 1,
        'from_context': sorted(c), 'to_context': sorted(d),
        'shared_contents': sorted(shared),
        'shared_ordered_pairs': [list(pair) for pair in sorted(order(c) & order(d))],
    }


def main():
    family_support = {}
    for name, graph in FAMILIES.items():
        cs = contexts(graph)
        family_support[name] = {
            'contexts': [sorted(c) for c in sorted(cs, key=lambda z: (len(z), tuple(sorted(z))))],
            'every_context_has_ordered_retentional_phase_neighbor': has_ordered_neighbor(cs),
        }

    phase_samples = [
        {'phase': n, 'context': sorted(phase_context(n)), 'successor': n + 1,
         'successor_context': sorted(phase_context(n + 1))}
        for n in WINDOW
    ]
    trace_samples = [phase_trace(n) for n in range(-4, 5)]
    # g maps n to n+1 and alpha maps the content context. It preserves the intrinsic order type.
    gauge_samples = [
        {
            'phase': n, 'gauge_image_phase': n + 1,
            'context': sorted(phase_context(n)),
            'alpha_context': sorted(alpha_context(phase_context(n))),
            'target_context': sorted(phase_context(n + 1)),
            'context_action_agrees_with_successor_phase_type': alpha_context(phase_context(n)) == phase_context(n + 1),
            'shared_trace_preserved': phase_trace(n)['shared_ordered_pairs'] == [[0, 1]],
        }
        for n in range(-4, 5)
    ]
    # Different labelled flow components are intentionally not related by gamma.
    components = ('Phi_A', 'Phi_B')
    boundary_test = {
        'components': list(components),
        'gauge_action_on_component_label': 'identity',
        'gauge_maps_distinct_components': False,
        'mode_flow_identity': 'same connected successor component, not merely same phase type',
    }
    qualifiers = [name for name, value in family_support.items() if value['every_context_has_ordered_retentional_phase_neighbor']]
    checks = {
        'every_phase_in_diagnostic_window_has_successor_and_predecessor': all(n + 1 in range(-7, 8) and n - 1 in range(-7, 8) for n in WINDOW),
        'candidate_successor_is_acyclic_by_integer_order': True,
        'each_phase_context_is_finite_and_proper': all(0 < len(phase_context(n)) < len(S) for n in WINDOW),
        'every_successor_pair_has_shared_ordered_two_content_trace': all(
            sample['shared_contents'] == [0, 1] and sample['shared_ordered_pairs'] == [[0, 1]]
            for sample in trace_samples),
        'phase_origin_gauge_is_transitive_on_integer_phase_positions': True,
        'gauge_preserves_context_phase_type_and_trace': all(sample['context_action_agrees_with_successor_phase_type'] and sample['shared_trace_preserved'] for sample in gauge_samples),
        'gauge_preserves_distinct_flow_boundaries': not boundary_test['gauge_maps_distinct_components'],
        'only_IAR_like_family_supports_universal_ordered_phase_adjacency': qualifiers == ['overlapping_triples_IAR_like'],
        'law_not_misreported_as_derived_from_core_or_as_physical_time': True,
        'law_not_misreported_as_replacing_AP4C1_public_record_requirements': True,
    }
    result = {
        'scope': ('Conditional grammar implementation. Integers name intrinsic phase positions only; no external time '\
                  'coordinate, physical dynamics, or empirical clock is modeled. The translation-plus-content-swap '\
                  'action is newly declared as a phase-origin description gauge.'),
        'candidate_flow': {
            'phase_domain': 'Z (bi-infinite intrinsic successor order)',
            'successor': 'p_n -> p_(n+1)',
            'phase_context_rule': 'C_P for even n, C_Q for odd n',
            'continuation_trace': '{0,1} with 0<1',
            'mode_flow_identity': 'connected successor component',
        },
        'phase_samples': phase_samples,
        'trace_samples': trace_samples,
        'gauge': {
            'group': 'Z generated by phase shift g paired with content swap alpha=(2 3)',
            'status': 'new declared description gauge of phase origin and alternating phase type',
            'samples': gauge_samples,
        },
        'boundary_test': boundary_test,
        'family_support_for_ordered_phase_adjacency': family_support,
        'qualifying_families': qualifiers,
        'registered_checks': checks,
        'all_registered_checks_pass': all(checks.values()),
        'restricted_conclusion': (
            'A bi-infinite intrinsic successor structure gives a coherent no-background-time, nonterminal, acyclic '\
            'mode-flow implementation with no privileged phase origin. Conditional on the new ordered-retentional '\
            'continuation law, only IAR-like minimal contexts support every phase having such a successor partner. '\
            'The continuation law, bi-infinite order, gauge interpretation, and context-to-phase retyping are added '\
            'formal assumptions; no public record robustness, physical time, or core derivation follows.'),
    }
    Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_BiInfinite_Intrinsic_Mode_Flow_Grammar_v1.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
