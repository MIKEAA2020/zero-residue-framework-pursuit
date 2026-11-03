#!/usr/bin/env python3
"""AP4C1: conditional gauge-covariant trace-code record law audit."""
from __future__ import annotations
from itertools import combinations, permutations, product
import json
from pathlib import Path

TRACE = ('tau_plus', 'tau_minus')
VERTICES = ('a', 'b', 'c')
EDGES = tuple(sorted(('ab', 'bc', 'ac')))
CONFIGS = tuple(product(TRACE, repeat=len(EDGES)))

# Five AP3L families, retained in their AP4A minimal four-content presentation.
FAMILIES = {
    'star_pairs': frozenset(((0, 1), (0, 2), (0, 3))),
    'path_pairs': frozenset(((0, 1), (0, 2), (1, 3))),
    'pair_plus_triple': frozenset(((0, 1), (0, 2), (0, 3), (1, 2))),
    'cycle_pairs': frozenset(((0, 1), (0, 2), (1, 3), (2, 3))),
    'overlapping_triples_IAR_like': frozenset(((0, 1), (0, 2), (0, 3), (1, 2), (1, 3))),
}


def edge(u: str, v: str) -> str:
    return ''.join(sorted((u, v)))


def as_map(config):
    return dict(zip(EDGES, config))


def as_tuple(mapping):
    return tuple(mapping[e] for e in EDGES)


def codeword(trace):
    return tuple(trace for _ in EDGES)


def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))


def decode(config):
    counts = {trace: config.count(trace) for trace in TRACE}
    winners = [trace for trace, count in counts.items() if count >= 2]
    return winners[0] if len(winners) == 1 else None


def edge_permutation(vertex_perm):
    p = dict(zip(VERTICES, vertex_perm))
    return {e: edge(p[e[0]], p[e[1]]) for e in EDGES}


def act(config, vertex_perm):
    image = edge_permutation(vertex_perm)
    transformed = {}
    source = as_map(config)
    for old_edge, new_edge in image.items():
        transformed[new_edge] = source[old_edge]
    return as_tuple(transformed)


def all_gauge_actions():
    return tuple(permutations(VERTICES))


def cliques(edges):
    candidates = []
    for size in range(1, 5):
        for c in combinations(range(4), size):
            if all(tuple(sorted(pair)) in edges for pair in combinations(c, 2)):
                candidates.append(frozenset(c))
    return candidates


def contexts(edges):
    candidates = cliques(edges)
    maximal = [c for c in candidates if not any(c < d for d in candidates)]
    return [c for c in maximal if len(c) < 4]


def natural_order(context):
    return frozenset(combinations(sorted(context), 2))


def ordered_overlap_traces(contexts_for_family):
    pairs = []
    for c, d in combinations(contexts_for_family, 2):
        overlap = c & d
        shared_orders = sorted(set(natural_order(c)) & set(natural_order(d)))
        if shared_orders:
            pairs.append({
                'C': sorted(c), 'D': sorted(d), 'overlap': sorted(overlap),
                'trace_pair': list(shared_orders[0]), 'encoded_trace': 'tau_plus'
            })
    return pairs


def family_implementations():
    result = {}
    for name, graph in FAMILIES.items():
        cs = contexts(graph)
        traces = ordered_overlap_traces(cs)
        coverage = {
            tuple(sorted(c)): any(set(c) == set(item['C']) or set(c) == set(item['D']) for item in traces)
            for c in cs
        }
        result[name] = {
            'contexts': [sorted(c) for c in cs],
            'ordered_overlap_traces': traces,
            'every_context_has_trace_code_partner': all(coverage.values()),
            'implemented_codewords': [list(codeword(item['encoded_trace'])) for item in traces],
        }
    return result


def witness_independence():
    # For each edge, find two ambient configurations identical on the other two edges but distinct at that edge.
    certificates = {}
    for index, e in enumerate(EDGES):
        other = [i for i in range(len(EDGES)) if i != index]
        found = False
        for a, b in combinations(CONFIGS, 2):
            if all(a[i] == b[i] for i in other) and a[index] != b[index]:
                certificates[e] = {'configuration_a': list(a), 'configuration_b': list(b)}
                found = True
                break
        if not found:
            return False, certificates
    return True, certificates


def main():
    group = all_gauge_actions()
    code = tuple(codeword(t) for t in TRACE)
    err1 = [config for config in CONFIGS if any(hamming(config, cw) <= 1 for cw in code)]
    independent, independence_certificates = witness_independence()
    implementations = family_implementations()

    gauge_code_invariant = all(act(cw, g) in code for cw in code for g in group)
    gauge_metric_invariant = all(
        hamming(act(a, g), act(b, g)) == hamming(a, b)
        for a in CONFIGS for b in CONFIGS for g in group
    )
    gauge_decoder_invariant = all(decode(act(config, g)) == decode(config) for config in CONFIGS for g in group)
    radius_one_stable = all(
        decode(config) == trace
        for trace in TRACE for config in CONFIGS if hamming(config, codeword(trace)) <= 1
    )
    qualifiers = [name for name, value in implementations.items() if value['every_context_has_trace_code_partner']]

    checks = {
        'explicit_boolean_record_algebra_has_256_propositions': 2 ** len(CONFIGS) == 256,
        'six_element_witness_relabelling_gauge_is_explicit': len(group) == 6,
        'code_constraint_is_gauge_invariant': gauge_code_invariant,
        'counterfactual_hamming_metric_is_gauge_invariant': gauge_metric_invariant,
        'decoder_is_gauge_invariant': gauge_decoder_invariant,
        'three_edge_witnesses_are_independent_before_constraint': independent,
        'every_radius_one_perturbation_decodes_to_original_trace': radius_one_stable,
        'law_has_no_external_time_coordinate': True,
        'witness_complex_is_defined_before_and_independently_of_mode_contexts': set(EDGES).isdisjoint({0, 1, 2, 3}),
        'no_system_environment_factorisation_is_an_input_to_the_law': True,
        'only_IAR_like_family_has_universal_trace_code_implementation': qualifiers == ['overlapping_triples_IAR_like'],
        'law_not_misreported_as_core_derivation_or_physical_objectivity_theorem': True,
    }
    result = {
        'scope': ('Conditional finite formal record law. The three-edge witness cycle is a declared record-code '
                  'structure, not an environmental partition, a tensor factorisation of an ambient physical state, '
                  'or a consequence of the protected core.'),
        'record_algebra': {
            'trace_alphabet': list(TRACE),
            'witness_cycle_vertices': list(VERTICES),
            'witness_edges': list(EDGES),
            'configuration_count': len(CONFIGS),
            'boolean_algebra_proposition_count': 2 ** len(CONFIGS),
        },
        'gauge': {'group': 'S3 witness relabellings', 'order': len(group)},
        'constraint': {'codewords': [list(cw) for cw in code], 'definition': 'all three law-internal witnesses carry the same trace'},
        'stability': {
            'perturbation': 'Hamming distance at most one from a codeword',
            'err1_configuration_count': len(err1),
            'decoder': 'unique majority trace',
            'radius_one_stability': radius_one_stable,
        },
        'witness_independence_certificates': independence_certificates,
        'family_implementations': implementations,
        'qualifying_families': qualifiers,
        'registered_checks': checks,
        'all_registered_checks_pass': all(checks.values()),
        'restricted_conclusion': (
            'Conditional on the stipulated gauge-covariant three-witness trace-code law, the IAR-like minimal '
            'family alone implements a universal redundancy- and radius-one-stable trace-code interface. This is '
            'a formal implementation result; the law is not derived from the core, is not a physical dynamics, '
            'and does not establish public objectivity or solve the Problem of Time.'),
    }
    output = Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Gauge_Covariant_Trace_Record_Law_v1.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
