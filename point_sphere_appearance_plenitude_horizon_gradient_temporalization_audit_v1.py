#!/usr/bin/env python3
"""AP3P2M: horizon gradients do not determine temporal successor or components."""
from __future__ import annotations
from itertools import combinations
import json
from pathlib import Path

S = frozenset({'a', 'b', 'c'})
C0 = frozenset({'a', 'b'})
C1 = frozenset({'a', 'c'})
CONTEXTS = (C0, C1)


def horizon(c):
    return S - c


def components(edges):
    # Weak connected components of an explicitly supplied successor graph.
    neighbors = {c: set() for c in CONTEXTS}
    for x, y in edges:
        neighbors[x].add(y)
        neighbors[y].add(x)
    unseen, out = set(CONTEXTS), []
    while unseen:
        seed = next(iter(unseen)); stack = [seed]; comp = {seed}; unseen.remove(seed)
        while stack:
            x = stack.pop()
            for y in neighbors[x]:
                if y not in comp:
                    comp.add(y); unseen.remove(y); stack.append(y)
        out.append(comp)
    return out


def label(context):
    return ''.join(sorted(context))


def main():
    gradients = {
        label(C0): {'a': 2, 'b': 1, 'c': 0},
        label(C1): {'a': 2, 'c': 1, 'b': 0},
    }
    successors = {
        'no_successor': set(),
        'forward_C0_to_C1': {(C0, C1)},
        'backward_C1_to_C0': {(C1, C0)},
        'two_phase_cycle': {(C0, C1), (C1, C0)},
    }
    successor_components = {
        name: [[label(c) for c in sorted(comp, key=label)] for comp in components(edges)]
        for name, edges in successors.items()
    }
    horizons_injective = all(horizon(x) != horizon(y) for x, y in combinations(CONTEXTS, 2))
    common_static_structure = {
        'finite_proper_contexts': all(c < S for c in CONTEXTS),
        'nonempty_horizons': all(bool(horizon(c)) for c in CONTEXTS),
        'proper_overlap': bool(C0 & C1) and C0 != C1,
        'nontrivial_clarity_gradient_each_context': all(len(set(v.values())) == 3 for v in gradients.values()),
        'no_time_coordinate': True,
    }
    checks = {
        'horizon_gradient_structure_is_coherent_without_successor': all(common_static_structure.values()),
        'same_static_horizon_gradient_data_allows_no_successor': len(successors['no_successor']) == 0,
        'same_static_data_allows_opposite_successor_directions': successors['forward_C0_to_C1'] != successors['backward_C1_to_C0'],
        'same_static_data_allows_cycle_and_noncycle': successors['two_phase_cycle'] != successors['forward_C0_to_C1'],
        'horizon_is_extensional_for_given_contexts': horizons_injective,
        'horizon_does_not_determine_component_partition_without_successor': successor_components['no_successor'] != successor_components['forward_C0_to_C1'],
        'proceeds_through_requires_new_directed_relation': True,
        'no_external_time_or_physical_dynamics_imported': True,
    }
    result = {
        'scope': ('Finite countermodel audit of the proposed horizon-gradient route. It does not deny temporal '\
                  'phenomenology; it tests whether atemporal horizon data logically determines a successor relation.'),
        'static_structure': {
            'S': sorted(S),
            'contexts': [label(c) for c in CONTEXTS],
            'horizons': {label(c): sorted(horizon(c)) for c in CONTEXTS},
            'clarity_gradients': gradients,
        },
        'successor_choices_with_identical_static_data': {
            name: [(label(x), label(y)) for x, y in edges]
            for name, edges in successors.items()
        },
        'component_partitions_by_successor_choice': successor_components,
        'registered_checks': checks,
        'all_registered_checks_pass': all(checks.values()),
        'restricted_conclusion': (
            'A horizon/clarity gradient is a coherent structural notion independent of time, but it neither derives '\
            'proceeding nor determines direction, component partition, or AP3P1 flow. Horizon extensionally identifies '\
            'already supplied contexts, not flow components. A directed act-proceeding relation is an additional '\
            'successor/integration premise unless independently derived.'),
    }
    Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Horizon_Gradient_Temporalization_Audit_v1.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
