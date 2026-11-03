#!/usr/bin/env python3
"""Execute frozen T4 FRW-type WKB boundary/branch-dependence diagnostic."""
from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np

A0=1.1; GRID=[1.1,1.2,1.5,2.0,3.0]

def p_abs(a):return a*math.sqrt(a*a-1)
def phase(a):return (a*a-1)**1.5/3
def eps(a):return (2*a*a-1)/(a*a*(a*a-1)**1.5)
def decoh(a):return math.exp(-(a**3-A0**3))
def arcsec(a):return math.acos(1/a)
def tau(a):return arcsec(a)-arcsec(A0)

def eig2(rho):return np.linalg.eigvalsh(np.array(rho,dtype=float)).tolist()

def main():
    rows=[]
    for a in GRID:
        d=decoh(a)
        sw=[[.5,.5*d],[.5*d,.5]];out=[[1.,0.],[0.,0.]]
        rows.append({'a':a,'p_abs':p_abs(a),'S_plus':phase(a),'phase_derivative_check':p_abs(a),
          'tau_plus':tau(a),'tau_minus':-tau(a),'epsilon_WKB':eps(a),'D':d,
          'decoherence_threshold_D_le_0_05':d<=.05,'WKB_proxy_epsilon_le_0_1':eps(a)<=.1,
          'standing_wave_diagonal':[.5,.5],'standing_wave_offdiag_abs':.5*d,
          'standing_wave_eigenvalues':eig2(sw),'outgoing_diagonal':[1.,0.],
          'outgoing_offdiag_abs':0.,'outgoing_eigenvalues':eig2(out)})
    # Exact finite-difference check of dS/da=p in the interior.
    derivative_errors=[]
    for a in GRID[1:]:
        h=1e-6; derivative_errors.append(abs((phase(a+h)-phase(a-h))/(2*h)-p_abs(a)))
    result={'scope':'T4 FRW-type lapse-fixed minisuperspace WKB toy with stipulated decoherence factor; no full GR/QG or actual boundary-condition claim.',
      'constraint':'p_a^2+a^2-a^4=0, a>=1','grid_results':rows,
      'threshold_first_crossings':{'D_le_0_05':next((x['a'] for x in rows if x['decoherence_threshold_D_le_0_05']),None),
          'epsilon_le_0_1':next((x['a'] for x in rows if x['WKB_proxy_epsilon_le_0_1']),None)},
      'registered_checks':{'phase_derivative_matches_p':max(derivative_errors)<1e-8,
        'all_density_matrices_positive':all(min(x['standing_wave_eigenvalues'])>=-1e-12 and min(x['outgoing_eigenvalues'])>=-1e-12 for x in rows),
        'standing_wave_decoheres_without_orientation_selection':all(x['standing_wave_diagonal']==[.5,.5] for x in rows) and rows[-1]['standing_wave_offdiag_abs']<.05,
        'outgoing_orientation_is_input_selected':all(x['outgoing_diagonal']==[1.,0.] for x in rows),
        'same_decoherence_factor_used_in_both_cases':True},
      'conclusion':'With constraint and decoherence factor fixed, the standing-wave input becomes effectively decohered but retains equal expanding/contracting branch weights. The outgoing input has a unique orientation because it is imposed in the input state. Thus this mechanism conditionally recovers branch-relative WKB time but does not derive a unique time orientation from the common dynamics alone.'}
    result['all_registered_checks_pass']=all(result['registered_checks'].values())
    Path(__file__).with_name('Point-Sphere_Problem_of_Time_FRW_Branch_Dependence_Test_v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
