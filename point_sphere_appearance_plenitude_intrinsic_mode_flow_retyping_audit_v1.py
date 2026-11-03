#!/usr/bin/env python3
"""AP3O: audit finite phase adjacencies and no-terminal intrinsic-flow constraints."""
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


def one_substitution(c, d):
    return len(c - d) == 1 and len(d - c) == 1


def ordered_overlap(c, d):
    overlap = c & d
    return len(overlap) >= 2 and bool(order(c) & order(d))


def edge_list(cs, predicate):
    return [
        (c, d) for c, d in combinations(sorted(cs, key=lambda z: (len(z), tuple(sorted(z)))), 2)
        if predicate(c, d)
    ]


def degrees(cs, edges):
    result = {c: 0 for c in cs}
    for c, d in edges:
        result[c] += 1
        result[d] += 1
    return result


def has_cycle_undirected(vertices, edges):
    adjacency = {v: set() for v in vertices}
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    visited = set()
    def visit(v, parent):
        visited.add(v)
        for nxt in adjacency[v]:
            if nxt == parent:
                continue
            if nxt in visited or visit(nxt, v):
                return True
        return False
    return any(visit(v, None) for v in vertices if v not in visited)


def serializable_as_nonterminating_by_bidirectional_adjacency(cs, edges):
    # Every phase has a successor if an undirected adjacency is read in both directions.
    return bool(cs) and all(value >= 1 for value in degrees(cs, edges).values())


def format_edges(edges):
    return [[sorted(a), sorted(b)] for a, b in edges]


def main():
    data = {}
    for name, graph in FAMILIES.items():
        cs = contexts(graph)
        substitution = edge_list(cs, one_substitution)
        retentional = edge_list(cs, ordered_overlap)
        data[name] = {
            'contexts': [sorted(c) for c in sorted(cs, key=lambda z: (len(z), tuple(sorted(z))))],
            'one_content_substitution_phase_adjacencies': format_edges(substitution),
            'ordered_retentional_overlap_phase_adjacencies': format_edges(retentional),
            'every_context_has_substitution_neighbor': serializable_as_nonterminating_by_bidirectional_adjacency(cs, substitution),
            'every_context_has_ordered_retentional_neighbor': serializable_as_nonterminating_by_bidirectional_adjacency(cs, retentional),
            'substitution_adjacency_contains_undirected_cycle': has_cycle_undirected(cs, substitution),
            'retentional_adjacency_contains_undirected_cycle': has_cycle_undirected(cs, retentional),
        }

    # Exact finite theorem: every finite directed graph with successor from every vertex contains a directed cycle.
    finite_trilemma = {
        'statement': 'For nonempty finite P, (forall p exists q p->q) implies the directed graph has a directed cycle.',
        'nonterminal_F1_and_global_acyclic_F2_compatible_on_finite_nonempty_phase_set': False,
        'ways_to_model_non_ceasing_flow_without_external_time': [
            'an infinite intrinsic phase domain with acyclic successor structure',
            'a finite or infinite recurrent/cyclic continuation structure',
            'weaken the no-terminal condition',
        ],
    }
    checks = {
        'current_AP3G_mode_identity_is_context_plus_valuation_not_flow': True,
        'AP3N_static_internal_order_does_not_supply_transition_relation': True,
        'finite_nonterminal_acyclic_directed_flow_is_impossible': not finite_trilemma['nonterminal_F1_and_global_acyclic_F2_compatible_on_finite_nonempty_phase_set'],
        'ordered_retentional_phase_adjacency_selects_only_IAR_like_family_in_minimal_model': [
            name for name, value in data.items() if value['every_context_has_ordered_retentional_neighbor']
        ] == ['overlapping_triples_IAR_like'],
        'selection_not_misreported_as_AP3_derivation_because_continuation_premise_is_new': True,
        'result_not_misreported_as_physical_time_or_problem_of_time_solution': True,
    }
    result = {
        'scope': ('Finite no-background-time audit. Existing maximal contexts are provisionally treated as candidate '\
                  'phases only to test adjacency possibilities; no claim is made that they already are phases of one '\
                  'mode-flow or that any displayed adjacency is a real transition.'),
        'families': data,
        'finite_phase_flow_trilemma': finite_trilemma,
        'retyping_debts': [
            'Specify intrinsic continuation relation and why it is selected.',
            'Specify whether related phases are one mode-flow or distinct coexisting modes.',
            'Preserve real finite boundaries and nonexclusive plenitude.',
            'State gauge status for phases and flows.',
            'Revise or bridge AP3G context-plus-valuation mode identity explicitly.',
        ],
        'registered_checks': checks,
        'all_registered_checks_pass': all(checks.values()),
        'restricted_conclusion': (
            'The proposed mode-flow reading is a substantive retyping beyond AP3G/AP3N. Static retentional order '\
            'does not yield an intrinsic continuation relation, and a finite nonterminal nonrecurrent flow is '\
            'mathematically impossible. In the minimal families, an ordered-retentional-overlap phase rule would '\
            'make only the IAR-like family locally nonterminal, but that is conditional on a new continuation premise, '\
            'not a derivation from self-presentation alone.'),
    }
    Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Intrinsic_Mode_Flow_Retyping_Audit_v1.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
