#!/usr/bin/env python3
"""AP4D1: matched-extension non-entailment of record law from IFG_P1."""
from __future__ import annotations
import json
from pathlib import Path


def main():
    base_flow = {
        'phase_domain_order_type': 'Z',
        'phase_types': ['P', 'Q'],
        'successor': 'n -> n+1',
        'shared_ordered_trace': ['r0<r1'],
        'phase_origin_gauge': 'shift with P/Q alternation',
        'component_rule': 'connected successor component',
    }
    F0 = {
        'name': 'bare_IFG_P1',
        'base_flow': base_flow,
        'witness_domain': [],
        'record_function': False,
        'diagonal_code': False,
        'perturbation_metric': False,
        'decoder': False,
        'public_interface': False,
    }
    F3 = {
        'name': 'IFG_P1_plus_AP4C1',
        'base_flow': base_flow,
        'witness_domain': ['w1', 'w2', 'w3'],
        'record_function': True,
        'diagonal_code': True,
        'perturbation_metric': 'radius-one Hamming',
        'decoder': 'majority trace decoder',
        'public_interface': 'stipulated three independent witness evaluations',
    }
    same_reduct = F0['base_flow'] == F3['base_flow']
    record_law_differs = (F0['diagonal_code'] != F3['diagonal_code'] and F0['decoder'] != F3['decoder'])
    checks = {
        'matched_models_share_exact_IFG_P1_reduct': same_reduct,
        'bare_IFG_model_has_no_record_code_structure': not F0['record_function'] and not F0['decoder'],
        'AP4C1_extension_has_added_witness_code_metric_and_decoder': bool(F3['witness_domain']) and F3['diagonal_code'] and bool(F3['decoder']),
        'same_flow_reduct_disagrees_on_record_law': record_law_differs,
        'IFG_P1_does_not_entail_AP4C1_record_law': same_reduct and record_law_differs,
        'result_does_not_claim_public_objectivity_or_physical_time': True,
    }
    result = {
        'scope': ('Matched finite-language expansion audit after postulate adoption. It proves non-entailment of '\
                  'the AP4C1 record law from IFG_P1; it does not assess physical implementation.'),
        'F0_bare_flow': F0,
        'F3_record_extension': F3,
        'registered_checks': checks,
        'all_registered_checks_pass': all(checks.values()),
        'restricted_conclusion': ('IFG_P1 supplies an ordered internal trace but not a witness domain, public interface, '\
                                  'error model, redundancy, metric, or decoder. AP4C1 remains an independently added '\
                                  'conditional record law compatible with—but not recovered from—the adopted flow grammar.'),
    }
    Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Intrinsic_Flow_Record_Entailment_Audit_v1.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
