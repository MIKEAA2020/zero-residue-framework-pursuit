#!/usr/bin/env python3
"""Uncertainty-aware N=16 mass-tuning follow-up for the frozen lambda-phi4 target.

This follows the retained short-bisection failure.  It changes no physical target,
action, observable, or sampler family; it replaces only the inadequate pilot tuning
precision with independent longer chains at a fixed local mass bracket.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from point_sphere_lambda_phi4_pilot import N, TARGET_Z, L_PHYS, run_chain, z_from_g

SEED=20261026
MASSES=[0.045,0.050,0.055]
BURN=1_000
TRAJ=8_000
NCHAINS=4


def main():
    records=[]
    for i,m2 in enumerate(MASSES):
        chains=[run_chain(m2,SEED+100*i+j,BURN,TRAJ) for j in range(NCHAINS)]
        per=[z_from_g(c['records'][:,1],c['records'][:,2]) for c in chains]
        z=float(np.mean(per)); se=float(np.std(per,ddof=1)/np.sqrt(NCHAINS))
        records.append({"m2":m2,"z_by_chain":per,"z_mean":z,"z_se_across_chains":se,
                        "z_95_approx":[z-3.182*se,z+3.182*se],
                        "acceptance_by_chain":[c['acceptance'] for c in chains]})
    # Freeze a local linear interpolation rule across the adjacent measured means
    # that straddle the target, if such points exist; otherwise explicitly refuse selection.
    selected=None
    for lo,hi in zip(records[:-1],records[1:]):
        if (lo['z_mean']-TARGET_Z)*(hi['z_mean']-TARGET_Z)<=0:
            frac=(TARGET_Z-lo['z_mean'])/(hi['z_mean']-lo['z_mean'])
            selected=float(lo['m2']+frac*(hi['m2']-lo['m2']))
            break
    payload={
        "scope":"N=16 uncertainty-aware follow-up mass tuning. Not production and not a continuum/scaling result.",
        "target_z":TARGET_Z,"masses":MASSES,"burn":BURN,"trajectories_per_chain":TRAJ,"n_chains":NCHAINS,
        "records":records,"linear_interpolated_mass_candidate":selected,
        "next_gate":"Run new independent diagnostic chains at the selected candidate only if the target is bracketed; otherwise expand the pre-logged local bracket and retain this failure."}
    Path(__file__).with_name('Point-Sphere_Interacting_LambdaPhi4_Mass_Tuning_v2.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps(payload,indent=2))
if __name__=='__main__': main()
