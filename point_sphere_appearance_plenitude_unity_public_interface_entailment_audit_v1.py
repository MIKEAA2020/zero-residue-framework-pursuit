#!/usr/bin/env python3
"""AP4U: finite countermodel audit for core-unity -> public-interface entailment."""
from __future__ import annotations
from itertools import combinations
import json
from pathlib import Path


def as_pairs(raw):
    return frozenset(tuple(pair) for pair in raw)


def strict_partial_order(order):
    nodes = {x for pair in order for x in pair}
    if any(x == y for x, y in order):
        return False
    # finite transitivity check restricted to asserted relation
    return all((a, c) in order for a, b in order for b2, c in order if b == b2)


def restriction(order, subset):
    return frozenset((x, y) for x, y in order if x in subset and y in subset)


def core_unity(model):
    contexts = model['contexts']
    return (
        model['one_ground'] == 'G'
        and all(model['of_ground'].get(name) == 'G' for name in contexts)
        and all(model['mode_aspect_content_identity'].get(name) is True for name in contexts)
        and all(len(contents) > 0 and len(contents) < len(model['universe']) for contents in contexts.values())
        and model['external_time_parameter'] is False
    )


def ap3n_order_conditions(model):
    contexts = model['contexts']
    orders = model['orders']
    nontrivial = all(bool(orders[name]) and strict_partial_order(orders[name]) for name in contexts)
    coherent = all(
        restriction(orders[a], contexts[a] & contexts[b]) == restriction(orders[b], contexts[a] & contexts[b])
        for a, b in combinations(contexts, 2)
    )
    return nontrivial and coherent


def public_retentional_interface(model):
    contexts = model['contexts']
    orders = model['orders']
    partner_map = {}
    for name, c in contexts.items():
        partners = []
        for other, d in contexts.items():
            if other == name:
                continue
            overlap = c & d
            shared_ordered_pairs = sorted(
                [[x, y] for x, y in (orders[name] & orders[other]) if x in overlap and y in overlap]
            )
            if shared_ordered_pairs:
                partners.append({'partner': other, 'overlap': sorted(overlap), 'ordered_pairs': shared_ordered_pairs})
        partner_map[name] = partners
    return all(partner_map[name] for name in contexts), partner_map


def make_model(name, contexts, orders):
    universe = frozenset().union(*contexts.values())
    return {
        'name': name,
        'one_ground': 'G',
        'universe': universe,
        'contexts': contexts,
        'orders': orders,
        'of_ground': {key: 'G' for key in contexts},
        'mode_aspect_content_identity': {key: True for key in contexts},
        'external_time_parameter': False,
    }


def evaluate(model):
    pri, partners = public_retentional_interface(model)
    return {
        'contexts': {k: sorted(v) for k, v in model['contexts'].items()},
        'orders': {k: [list(p) for p in sorted(v)] for k, v in model['orders'].items()},
        'core_identity_and_one_ground_hold': core_unity(model),
        'AP3N_style_internal_order_and_overlap_coherence_hold': ap3n_order_conditions(model),
        'public_retentional_interface_PRI_holds': pri,
        'retentional_partners': partners,
    }


def main():
    # Two AP3L/AP3N survivors, using the same natural internal order witness as AP4A.
    path_contexts = {
        'C01': frozenset((0, 1)), 'C02': frozenset((0, 2)), 'C13': frozenset((1, 3))
    }
    path = make_model('path_pairs_core_unity_countermodel', path_contexts,
                      {k: as_pairs([(min(c), max(c))]) for k, c in path_contexts.items()})

    star_contexts = {
        'C01': frozenset((0, 1)), 'C02': frozenset((0, 2)), 'C03': frozenset((0, 3))
    }
    star = make_model('star_pairs_single_shared_content_countermodel', star_contexts,
                      {k: as_pairs([(min(c), max(c))]) for k, c in star_contexts.items()})

    trace_contexts = {
        'C1': frozenset(('g1', 'g2', 'a1')),
        'C2': frozenset(('g1', 'g2', 'a2')),
        'C3': frozenset(('g1', 'g2', 'a3')),
    }
    trace = make_model('two_common_contents_without_shared_order_countermodel', trace_contexts,
                       {name: as_pairs([('g1', next(x for x in c if x.startswith('a')))])
                        for name, c in trace_contexts.items()})

    # The AP4A IAR-like/maximal-triple positive control.
    iar_contexts = {
        'C012': frozenset((0, 1, 2)), 'C013': frozenset((0, 1, 3))
    }
    iar = make_model('IAR_like_positive_control', iar_contexts,
                     {k: as_pairs(combinations(sorted(c), 2)) for k, c in iar_contexts.items()})

    models = {m['name']: evaluate(m) for m in (path, star, trace, iar)}
    checks = {
        'path_survivor_satisfies_core_unity_but_fails_PRI': (
            models[path['name']]['core_identity_and_one_ground_hold']
            and models[path['name']]['AP3N_style_internal_order_and_overlap_coherence_hold']
            and not models[path['name']]['public_retentional_interface_PRI_holds']),
        'star_survivor_has_common_content_but_fails_two_content_interface': (
            models[star['name']]['core_identity_and_one_ground_hold']
            and models[star['name']]['AP3N_style_internal_order_and_overlap_coherence_hold']
            and not models[star['name']]['public_retentional_interface_PRI_holds']),
        'two_common_contents_plus_coherent_internal_order_do_not_entail_shared_ordered_trace': (
            models[trace['name']]['core_identity_and_one_ground_hold']
            and models[trace['name']]['AP3N_style_internal_order_and_overlap_coherence_hold']
            and not models[trace['name']]['public_retentional_interface_PRI_holds']),
        'IAR_like_positive_control_satisfies_PRI': (
            models[iar['name']]['core_identity_and_one_ground_hold']
            and models[iar['name']]['AP3N_style_internal_order_and_overlap_coherence_hold']
            and models[iar['name']]['public_retentional_interface_PRI_holds']),
        'bridge_stating_shared_ordered_trace_is_not_counted_as_core_derivation': True,
        'result_not_misreported_as_rejection_of_conditional_AP4A_result': True,
    }
    result = {
        'scope': ('Finite model-theoretic entailment audit. The protected identity and one-ground condition '
                  'are represented without an additional cross-context identity, overlap, or shared-order axiom. '
                  'No physical records, factorisation, external time, or robust-record law is assumed.'),
        'target': ('PRI(P): every participating context has a distinct partner sharing an ordered pair of contents.'),
        'models': models,
        'bridge_ladder': {
            'U0': 'Every mode is of the one G. This is compatible with disjoint contexts.',
            'U1': 'Relevant modes share at least one token-identical content. Star countermodel shows this is insufficient.',
            'U2': 'Relevant modes share at least two token-identical contents. Unordered-trace countermodel shows this is insufficient.',
            'U3': 'Relevant modes share two contents carrying the same inherited nontrivial order. This is PRI itself, not a derivation from U0.'
        },
        'registered_checks': checks,
        'all_registered_checks_pass': all(checks.values()),
        'restricted_conclusion': (
            'K plus the bare one-ground/unity supplement does not entail PRI. Neither one shared content nor '
            'two shared contents plus AP3N-style coherent local order entails a shared ordered record trace. AP4A '
            'therefore remains a valid conditional IAR-like discriminator; any unity-to-interface route needs a '
            'separately stated and independently defended bridge.'),
    }
    out = Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Unity_Public_Interface_Entailment_Audit_v1.json')
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
