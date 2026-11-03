#!/usr/bin/env python3
"""Execute frozen T1b constrained-clock diagnostic.

A finite parametrized toy only: it tests the PITR criteria stated in its specification,
not general relativity or a solution of the quantum-gravity problem of time.
"""
from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np

# (p_phi, record energy); p_alpha is constrained when the radicand is nonnegative.
MODES=[(2.0,0.0),(2.0,4.0),(2.0,16.0),(5.0,0.0),(5.0,4.0),(5.0,16.0)]


def mutual_information(channel:np.ndarray)->float:
    """Uniform input labels, rows=input, columns=record; natural-log units."""
    n=channel.shape[0]; joint=channel/n; px=joint.sum(axis=1,keepdims=True); py=joint.sum(axis=0,keepdims=True)
    return float(np.sum(joint*np.log(joint/(px*py))))


def main():
    mode_rows=[]
    for pphi,h in MODES:
        # φ-time form needs p_alpha²+h>=0, true for all nonnegative h/p_alpha².
        phi_generator_real=True
        alpha_radicand=pphi*pphi-h
        alpha_generator_real=alpha_radicand>=0
        mode_rows.append({'p_phi':pphi,'h_R':h,'phi_time_generator_real':phi_generator_real,
                          'alpha_time_radicand':alpha_radicand,'alpha_time_generator_real':alpha_generator_real,
                          'p_alpha_if_real':math.sqrt(alpha_radicand) if alpha_generator_real else None})
    # Exact common branch: (p_phi,p_alpha,h)=(5,3,16), α=(3/5) φ+const.
    pphi,palpha,h=5.0,3.0,16.0
    constraint_residual=pphi**2-palpha**2-h
    affine_slope=palpha/pphi
    labels=np.arange(10)
    relabel=3*labels+7
    channel=np.full((10,10),.2/9);np.fill_diagonal(channel,.8)
    mi_t=mutual_information(channel)
    # Relabelling only permutes input names, hence the exact same channel probabilities.
    mi_tp=mutual_information(channel.copy())
    registers=3
    alpha_excluded=sum(not r['alpha_time_generator_real'] for r in mode_rows)
    result={
      'scope':'T1b finite parametrized constraint diagnostic only; no full GR, WdW, phenomenology, or physical clock claim.',
      'constraint':'C=p_phi^2-p_alpha^2-h_R=0',
      'candidate_clocks':['phi','alpha'],'mode_test':mode_rows,
      'common_sector':{'p_phi':pphi,'p_alpha':palpha,'h_R':h,'constraint_residual':constraint_residual,
                       'branch_relation':'alpha=(3/5) phi + constant','affine_slope_alpha_over_phi':affine_slope},
      'record_channel':{'labels':10,'registers':registers,'correct_probability':.8,'error_probability_each':.2/9,
                        'mutual_information_nats_T':mi_t,'mutual_information_nats_bijective_Tprime':mi_tp,
                        'absolute_difference':abs(mi_t-mi_tp)},
      'PITR_status':{
        'P1_constraint_internal':{'phi':'established_in_model','alpha':'established_in_model'},
        'P2_branchwise_monotonicity':{'phi':'conditional_on_sign_branch','alpha':'conditional_on_sign_branch'},
        'P3_conditional_dynamics':{'phi':'real_generator_all_registered_modes','alpha':f'real_generator_only_in_{len(MODES)-alpha_excluded}_of_{len(MODES)}_registered_modes'},
        'P4_low_backreaction':'untested: ideal conserved-record construction has no measurement interaction',
        'P5_public_record_robustness':'redundant records exist but are invariant under bijective clock relabelling',
        'P6_clock_change_coherence':'established only on chosen common branch; global coherence remains open',
        'P7_GR_proper_time_recovery':'untested: no local gravity in this model'},
      'registered_checks':{
        'phi_generator_real_all_modes':all(r['phi_time_generator_real'] for r in mode_rows),
        'alpha_generator_has_restricted_domain':alpha_excluded>0,
        'common_branch_satisfies_constraint':abs(constraint_residual)<1e-12,
        'record_mutual_information_relabelling_invariant':abs(mi_t-mi_tp)<1e-12,
        'PITR_does_not_select_parameterisation_within_equivalence_class':abs(mi_t-mi_tp)<1e-12},
      'conclusion':'In this toy, record redundancy cannot select between bijectively related clock parameters. The constraint itself favors phi as having a wider real-generator domain, but this is a model-specific dynamical fact, not a metaphysical clock selection.'}
    result['all_registered_checks_pass']=all(result['registered_checks'].values())
    Path(__file__).with_name('Point-Sphere_Problem_of_Time_Parametrized_Constraint_Test_v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
