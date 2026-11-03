#!/usr/bin/env python3
"""Frozen HMC versus checkerboard conditional-Gaussian MH crosscheck at N=16."""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from point_sphere_lambda_phi4_pilot import (
    N, LAMBDA_HAT, run_chain, observables, z_from_g, integrated_tau, basic_split_rhat
)

SEED=20261101
M2=0.055
HMC_BURN=1_000; HMC_TRAJ=20_000
CB_BURN=5_000; CB_SWEEPS=50_000
NCHAINS=4

I,J=np.indices((N,N)); RED=(I+J)%2==0; BLACK=~RED
SIGMA=1/np.sqrt(4+M2)


def cb_chain(seed: int):
    rng=np.random.default_rng(seed); phi=rng.normal(scale=.2,size=(N,N))
    accepts=[]; records=[]
    for t in range(CB_BURN+CB_SWEEPS):
        for mask in (RED,BLACK):
            neigh=np.roll(phi,1,0)+np.roll(phi,-1,0)+np.roll(phi,1,1)+np.roll(phi,-1,1)
            old=phi[mask]
            proposal=neigh[mask]/(4+M2)+SIGMA*rng.normal(size=old.shape)
            # The quadratic conditional is the proposal density, so only V4 changes.
            delta=LAMBDA_HAT/24*(proposal**4-old**4)
            take=np.log(rng.random(size=old.shape)) < np.minimum(0.,-delta)
            phi[mask]=np.where(take,proposal,old)
            if t>=CB_BURN: accepts.append(float(np.mean(take)))
        if t>=CB_BURN: records.append(observables(phi))
    return {'acceptance':float(np.mean(accepts)),'records':np.asarray(records)}


def summary(chains):
    zc=[z_from_g(c['records'][:,1],c['records'][:,2]) for c in chains]
    mean=float(np.mean(zc)); se=float(np.std(zc,ddof=1)/np.sqrt(NCHAINS)); ci=[mean-3.182*se,mean+3.182*se]
    diagnostics={}
    for col,name in enumerate(['M','G0','Gp']):
        xs=[c['records'][:,col] for c in chains]; taus=[integrated_tau(x) for x in xs]
        diagnostics[name]={'tau_int_by_chain':taus,'combined_approx_ess':float(sum(map(len,xs))/(2*max(taus))),
                           'basic_split_rhat':basic_split_rhat(xs)}
    return {'z_by_chain':zc,'z_mean':mean,'z_se_across_chains':se,'z_95_approx':ci,
            'acceptance_by_chain':[c['acceptance'] for c in chains],'diagnostics':diagnostics}


def overlap(a,b): return max(a[0],b[0])<=min(a[1],b[1])

def main():
    hmc=[run_chain(M2,SEED+i,HMC_BURN,HMC_TRAJ) for i in range(NCHAINS)]
    cb=[cb_chain(SEED+10_000+i) for i in range(NCHAINS)]
    hs,cs=summary(hmc),summary(cb)
    hgood=all(x['basic_split_rhat']<=1.01 for x in hs['diagnostics'].values())
    cgood=all(x['basic_split_rhat']<=1.01 for x in cs['diagnostics'].values())
    payload={'scope':'N=16 frozen sampler crosscheck at a diagnostic unselected mass; no tuning or physical conclusion.',
             'specification':'Point-Sphere_Interacting_LambdaPhi4_N16_Sampler_Crosscheck_Specification.md',
             'configuration':{'seed':SEED,'m2':M2,'hmc_burn':HMC_BURN,'hmc_trajectories':HMC_TRAJ,
                              'checkerboard_burn_sweeps':CB_BURN,'checkerboard_retained_sweeps':CB_SWEEPS},
             'hmc':hs,'checkerboard_metropolis':cs,
             'intervals_overlap':overlap(hs['z_95_approx'],cs['z_95_approx']),
             'basic_rhat_pass':bool(hgood and cgood),
             'crosscheck_pass':bool(overlap(hs['z_95_approx'],cs['z_95_approx']) and hgood and cgood),
             'note':'The crosscheck does not select a mass and does not substitute for target production diagnostics.'}
    Path(__file__).with_name('Point-Sphere_Interacting_LambdaPhi4_Sampler_Crosscheck_v1.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps(payload,indent=2))
if __name__=='__main__':main()
