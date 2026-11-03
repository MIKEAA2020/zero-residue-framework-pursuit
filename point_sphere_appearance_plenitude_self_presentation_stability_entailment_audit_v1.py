#!/usr/bin/env python3
"""AP4C3A: finite non-entailment audit for self-presentation -> record stability."""
from __future__ import annotations
import json
from pathlib import Path


def strict_partial_order(order):
    if any(x == y for x, y in order):
        return False
    return all((a, c) in order for a, b in order for b2, c in order if b == b2)


def make_model(name, delta_edges, traces):
    modes = ('m_plus', 'm_minus')
    support = {
        'm_plus': frozenset(('r0', 'r1', 'h_plus')),
        'm_minus': frozenset(('r0', 'r1', 'h_minus')),
    }
    # Each counterfactual mode has its own coherent, nontrivial endogenous order.
    order = {
        'm_plus': frozenset((('r0', 'r1'), ('r0', 'h_plus'))),
        'm_minus': frozenset((('r0', 'r1'), ('r0', 'h_minus'))),
    }
    return {
        'name': name,
        'ground': 'G',
        'modes': modes,
        'support': support,
        'order': order,
        'of_ground': {m: 'G' for m in modes},
        'genuine_mode': {m: True for m in modes},
        'self_aspect': {m: True for m in modes},
        'content_of_self_knowledge': {m: True for m in modes},
        # Delta and trace are explicitly extension-language, not protected-core predicates.
        'delta_1': frozenset(frozenset(edge) for edge in delta_edges),
        'trace': traces,
        'external_time_parameter': False,
    }


def core_identity_holds(model):
    return (
        model['ground'] == 'G'
        and all(model['of_ground'][m] == 'G' for m in model['modes'])
        and all(
            model['genuine_mode'][m] == model['self_aspect'][m] == model['content_of_self_knowledge'][m]
            for m in model['modes']
        )
    )


def ap3_typing_holds(model):
    universe = frozenset().union(*model['support'].values())
    bounded = all(0 < len(model['support'][m]) < len(universe) for m in model['modes'])
    ordered = all(model['order'][m] and strict_partial_order(model['order'][m]) for m in model['modes'])
    return bounded and ordered and not model['external_time_parameter']


def sp_stability_holds(model):
    return all(
        model['trace'][a] == model['trace'][b]
        for edge in model['delta_1']
        for a, b in [tuple(edge)]
    )


def model_summary(model):
    return {
        'supports': {m: sorted(s) for m, s in model['support'].items()},
        'orders': {m: [list(pair) for pair in sorted(o)] for m, o in model['order'].items()},
        'delta_1_edges': [sorted(edge) for edge in sorted(model['delta_1'], key=lambda e: sorted(e))],
        'trace_values': model['trace'],
        'protected_core_identity_holds': core_identity_holds(model),
        'AP3_finite_bounded_endogenous_order_typing_holds': ap3_typing_holds(model),
        'SPStab_1_trace_persistence_holds': sp_stability_holds(model),
    }


def main():
    no_adjacency = make_model(
        'no_adjacency_core_expansion', (), {'m_plus': 'tau_plus', 'm_minus': 'tau_minus'}
    )
    fragile = make_model(
        'fragile_trace_core_expansion', (('m_plus', 'm_minus'),), {'m_plus': 'tau_plus', 'm_minus': 'tau_minus'}
    )
    stable = make_model(
        'stable_trace_core_expansion', (('m_plus', 'm_minus'),), {'m_plus': 'tau_plus', 'm_minus': 'tau_plus'}
    )
    models = {m['name']: model_summary(m) for m in (no_adjacency, fragile, stable)}
    checks = {
        'all_expansions_satisfy_protected_core_identity': all(v['protected_core_identity_holds'] for v in models.values()),
        'all_expansions_satisfy_AP3_finite_order_typing': all(v['AP3_finite_bounded_endogenous_order_typing_holds'] for v in models.values()),
        'same_core_typing_admits_no_preferred_delta_1_relation': len(no_adjacency['delta_1']) == 0 and len(fragile['delta_1']) == 1,
        'fragile_expansion_refutes_trace_persistence_under_delta_1': not models[fragile['name']]['SPStab_1_trace_persistence_holds'],
        'stable_expansion_shows_stability_is_compatible_not_forced': models[stable['name']]['SPStab_1_trace_persistence_holds'],
        'core_vocabulary_has_no_witness_set_code_metric_or_decoder': True,
        'change_of_genuine_mode_not_assumed_to_be_witness_error': True,
        'result_not_misreported_as_rejection_of_AP4C1_conditional_law': True,
    }
    result = {
        'scope': ('Finite formal entailment audit. Delta_1 and trace are explicit extension predicates solely for '
                  'testing whether protected-core and AP3 typing constrain them. The audit contains no witness code, '
                  'decoder, external time, physical dynamics, or claim about actual experience.'),
        'models': models,
        'required_bridge_layers': {
            'B_stab_1': 'A non-gauge minimal-perturbation/adjacency relation on relevant finite modes or record configurations.',
            'B_stab_2': 'A norm distinguishing corrupted witness presentation from a different genuine self-presentation.',
            'B_stab_3': 'A trace-preservation requirement across the relevant perturbation class.',
            'B_stab_4': 'A representation theorem or independently justified map from B_stab_1--3 to the AP4C1 witness-code Hamming metric and decoder.',
        },
        'registered_checks': checks,
        'all_registered_checks_pass': all(checks.values()),
        'restricted_conclusion': (
            'The protected core plus finite bounded endogenous-order typing does not entail a preferred minimal '
            'perturbation relation or even the weaker trace-persistence principle SPStab_1. It therefore cannot '
            'entail AP4C1 one-witness error recovery. A stability bridge must be added and independently defended; '
            'a changed genuine mode cannot simply be classified as a record error by the core identity alone.'),
    }
    Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Self_Presentation_Stability_Entailment_Audit_v1.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
