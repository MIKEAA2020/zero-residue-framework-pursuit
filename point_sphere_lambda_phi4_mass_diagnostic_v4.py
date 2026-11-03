#!/usr/bin/env python3
"""Independent diagnostic at the logged interpolation candidate m0^2=0.05612."""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from point_sphere_lambda_phi4_pilot import (TARGET_Z, L_PHYS, run_chain, z_from_g,
                                             integrated_tau, basic_split_rhat)

SEED=20261028
M2=0.05612
BURN=1_000
TRAJ=10_000
NCHAINS=4

def main():
    chains=[run_chain(M2,SEED+i,BURN,TRAJ) for i in range(NCHAINS)]
    per_z=[z_from_g(c['records'][:,1],c['records'][:,2]) for c in chains]
    z=float(np.mean(per_z));se=float(np.std(per_z,ddof=1)/np.sqrt(NCHAINS))
    diag={}
    for col,name in enumerate(['M','G0','Gp']):
        xs=[c['records'][:,col] for c in chains]
        tau=[integrated_tau(x) for x in xs]
        diag[name]={'tau_int_by_chain':tau,'combined_approx_ess':float(sum(map(len,xs))/(2*max(tau))),
                    'basic_split_rhat':basic_split_rhat(xs)}
    payload={'scope':'Independent N=16 diagnostic at the v2/v3 interpolation candidate. Still pre-production.',
             'm2':M2,'target_z':TARGET_Z,'burn':BURN,'trajectories_per_chain':TRAJ,'n_chains':NCHAINS,
             'z_by_chain':per_z,'z_mean':z,'z_se_across_chains':se,'z_95_approx':[z-3.182*se,z+3.182*se],
             'acceptance_by_chain':[c['acceptance'] for c in chains], 'diagnostics':diag,
             'within_production_mass_band':bool(abs(z-TARGET_Z)<=0.05),
             'note':'Production still requires the fixed ESS and 500-tau run-length conditions even if mass tuning succeeds.'}
    Path(__file__).with_name('Point-Sphere_Interacting_LambdaPhi4_Mass_Diagnostic_v4.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps(payload,indent=2))
if __name__=='__main__':main()
