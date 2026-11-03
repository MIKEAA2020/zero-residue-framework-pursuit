#!/usr/bin/env python3
"""Logged high-side bracket extension after v2 did not bracket z=4 by means."""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from point_sphere_lambda_phi4_pilot import TARGET_Z, run_chain, z_from_g

SEED=20261027
MASSES=[0.060,0.065]
BURN=1_000
TRAJ=8_000
NCHAINS=4

def main():
    records=[]
    for i,m2 in enumerate(MASSES):
        chains=[run_chain(m2,SEED+100*i+j,BURN,TRAJ) for j in range(NCHAINS)]
        zc=[z_from_g(c['records'][:,1],c['records'][:,2]) for c in chains]
        z=float(np.mean(zc));se=float(np.std(zc,ddof=1)/np.sqrt(NCHAINS))
        records.append({'m2':m2,'z_by_chain':zc,'z_mean':z,'z_se_across_chains':se,
                        'z_95_approx':[z-3.182*se,z+3.182*se],
                        'acceptance_by_chain':[c['acceptance'] for c in chains]})
    payload={'scope':'Pre-production high-side bracket extension; unchanged action, target, and HMC family.',
             'target_z':TARGET_Z,'burn':BURN,'trajectories_per_chain':TRAJ,'n_chains':NCHAINS,'records':records,
             'next_gate':'Combine only with the logged v2 points to identify a target-straddling pair; then run independent chains at the interpolated candidate.'}
    Path(__file__).with_name('Point-Sphere_Interacting_LambdaPhi4_Mass_Tuning_v3.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps(payload,indent=2))
if __name__=='__main__':main()
