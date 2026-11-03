#!/usr/bin/env python3
"""Execute the frozen lower-grid response-surface extension v2."""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from point_sphere_lambda_phi4_pilot import run_chain
from point_sphere_lambda_phi4_response_surface_tuning_v1 import block_z, fit_response, validate

SEED=20261031
NEW_MASSES=[0.048,0.050]
NCHAINS=4
BURN=1_000
TRAJ=20_000

def main():
    previous=json.loads(Path(__file__).with_name('Point-Sphere_Interacting_LambdaPhi4_Response_Surface_Tuning_v1.json').read_text())
    new=[]
    for i,m2 in enumerate(NEW_MASSES):
        chains=[run_chain(m2,SEED+1_000*i+j,BURN,TRAJ) for j in range(NCHAINS)]
        blocks=np.array([v for c in chains for v in block_z(c['records'])],dtype=float)
        from point_sphere_lambda_phi4_pilot import z_from_g
        new.append({'m2':m2,'block_z':blocks.tolist(),'block_n':int(len(blocks)),
                    'z_mean':float(blocks.mean()),'block_variance':float(blocks.var(ddof=1)),
                    'z_by_chain':[z_from_g(c['records'][:,1],c['records'][:,2]) for c in chains],
                    'acceptance_by_chain':[c['acceptance'] for c in chains]})
    grid=sorted(previous['grid']+new,key=lambda r:r['m2'])
    fit=fit_response(grid); validation=None
    if fit['usable']:
        validation=validate(round(fit['root_m2'],6))
    payload={'scope':'Frozen v2 lower-grid extension combined with all locked response-surface-v1 observations.',
             'specification':'Point-Sphere_Interacting_LambdaPhi4_N16_Response_Surface_Tuning_v2_Specification.md',
             'new_configuration':{'seed':SEED,'masses':NEW_MASSES,'n_chains':NCHAINS,'burn':BURN,'trajectories':TRAJ},
             'grid':grid,'fit':fit,'validation':validation,
             'tuning_pass':bool(fit['usable'] and validation is not None and validation['passes'])}
    Path(__file__).with_name('Point-Sphere_Interacting_LambdaPhi4_Response_Surface_Tuning_v2.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps(payload,indent=2))
if __name__=='__main__':main()
