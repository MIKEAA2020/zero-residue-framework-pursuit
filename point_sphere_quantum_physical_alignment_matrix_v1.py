#!/usr/bin/env python3
"""Validate coverage and non-overclaim guards for the frozen Q1 alignment matrix.

This is a bookkeeping validator, not a physics calculation or interpretation test.
"""
from __future__ import annotations
import json
from pathlib import Path

frameworks={
 'operational_instrumentalist_QM':{
   'Q1_R':'does_not_supply','Q1_C1':'does_not_supply','Q1_C2':'does_not_supply','Q1_P':'does_not_supply','Q1_M':'formal_probability_only','Q1_F':'not_supported_by_programme_field_work'},
 'everett_unitary_branching':{
   'Q1_R':'requires_substantive_branch_and_measure_bridge','Q1_C1':'does_not_supply','Q1_C2':'records_not_carriers','Q1_P':'does_not_supply','Q1_M':'Born_weight_task_open','Q1_F':'not_supported_by_programme_field_work'},
 'bohmian_pilot_wave':{
   'Q1_R':'requires_exact_initial_totality_bridge','Q1_C1':'does_not_supply','Q1_C2':'configuration_not_individuation','Q1_P':'does_not_supply','Q1_M':'typicality_not_R_bridge','Q1_F':'not_supported_by_programme_field_work'},
 'objective_collapse_GRW_type':{
   'Q1_R':'stochastic_selector_grounding_open','Q1_C1':'does_not_supply','Q1_C2':'collapse_not_individuation','Q1_P':'does_not_supply','Q1_M':'probability_law_not_ultimate_selector','Q1_F':'not_supported_by_programme_field_work'},
 'relational_agent_relative_families':{
   'Q1_R':'does_not_supply','Q1_C1':'does_not_supply','Q1_C2':'system_agent_criterion_open','Q1_P':'does_not_supply','Q1_M':'formulation_dependent','Q1_F':'not_supported_by_programme_field_work'},
 'QFT_AQFT_structural':{
   'Q1_R':'global_state_representation_selection_open','Q1_C1':'does_not_supply','Q1_C2':'local_structure_not_individuation','Q1_P':'does_not_supply','Q1_M':'physical_measure_problem_open','Q1_F':'interacting_target_unrepaired'}
}

def main():
 required={'Q1_R','Q1_C1','Q1_C2','Q1_P','Q1_M','Q1_F'}
 coverage=all(set(v)==required for v in frameworks.values())
 no_row_confirms_hard_core=all('confirms' not in ' '.join(v.values()) for v in frameworks.values())
 no_row_derives_physics=all('derives' not in ' '.join(v.values()) for v in frameworks.values())
 candidate_debts={
  'C_Nec_D':'exact_initial_totality_or_determination_bridge',
  'C_Nec_O':'substantive_branch_or_orbit_and_measure_bridge',
  'C_Cont':'non_arbitrary_selector_grounding_bridge'}
 payload={'scope':'Q1 frozen alignment-matrix coverage/guard validation only; not a physics result.',
          'frameworks':frameworks,'candidate_specific_debts':candidate_debts,
          'hard_core_confirmed_by_matrix':False,'physics_derived_by_matrix':False,
          'interacting_field_target_status':'unrepaired_mass_selection_validation_failure_retained',
          'complete_discriminator_coverage':coverage,
          'non_overclaim_guards_pass':no_row_confirms_hard_core and no_row_derives_physics,
          'all_registered_Q1_checks_pass':coverage and no_row_confirms_hard_core and no_row_derives_physics and len(candidate_debts)==3}
 Path(__file__).with_name('Point-Sphere_Quantum_Physical_Alignment_Matrix_v1.json').write_text(json.dumps(payload,indent=2)+'\n')
 print(json.dumps(payload,indent=2))
if __name__=='__main__':main()
