#!/usr/bin/env python3
"""Execute frozen F1 pooled-Fourier-moment, chain-replicated N=16 tuning.

This is a numerical calibration protocol only. It preserves the action, target, and
validation band and intentionally computes no selected-mass coupling or continuum fit.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from point_sphere_lambda_phi4_pilot import (
    N, LAMBDA_HAT, run_chain, observables, z_from_g, integrated_tau, basic_split_rhat
)

MASSES=np.array([0.052,0.054,0.056,0.058],dtype=float)
CAL_SEED=20261110; CAL_CHAINS=6; CAL_BURN=2_000; CAL_TRAJ=12_000
BOOT=4_000; BOOT_SEED=20261210
VAL_SEED=20270110; VAL_CHAINS=6; VAL_BURN=2_000; VAL_TRAJ=24_000
CB_SEED=20280110; CB_CHAINS=4; CB_BURN=5_000; CB_SWEEPS=50_000
TARGET=4.0
I,J=np.indices((N,N)); RED=(I+J)%2==0; BLACK=~RED


def z_pairs(pairs: np.ndarray) -> np.ndarray:
    """z from [..., (mean G0, mean Gp)] without averaging nonlinear ratios."""
    ratio=pairs[...,0]/pairs[...,1]
    denom=ratio-1.0
    p2=4*N*N*np.sin(np.pi/N)**2
    out=np.full(denom.shape,np.nan,dtype=float)
    good=denom>0
    out[good]=np.sqrt(p2/denom[good])
    return out


def moment_means(chains):
    return np.array([[np.mean(c['records'][:,1]),np.mean(c['records'][:,2])] for c in chains],dtype=float)


def pooled_bootstrap(chains, seed: int):
    means=moment_means(chains); n=len(means)
    point=float(z_pairs(means.mean(axis=0))[()])
    rng=np.random.default_rng(seed)
    ind=rng.integers(0,n,size=(BOOT,n))
    boot=z_pairs(means[ind].mean(axis=1))
    return {'z_pooled':point,'z_by_chain':[float(z_pairs(x)[()]) for x in means],
            'chain_moment_means':means.tolist(),
            'bootstrap_n':BOOT,'bootstrap_95':[float(x) for x in np.quantile(boot,[.025,.975])],
            'bootstrap_90':[float(x) for x in np.quantile(boot,[.05,.95])],
            '_boot':boot}


def diagnostics(chains):
    out={}
    for col,name in enumerate(['M','G0','Gp']):
        xs=[c['records'][:,col] for c in chains]
        taus=[integrated_tau(x) for x in xs]
        out[name]={'tau_int_by_chain':[float(x) for x in taus],
                   'combined_approx_ess':float(sum(map(len,xs))/(2*max(taus))),
                   'basic_split_rhat':float(basic_split_rhat(xs))}
    return out


def fit_with_root(x: np.ndarray,y: np.ndarray):
    slope=float(np.dot(x-x.mean(),y-y.mean())/np.dot(x-x.mean(),x-x.mean()))
    intercept=float(y.mean()-slope*x.mean())
    root=float((TARGET-intercept)/slope) if slope!=0 else float('nan')
    return intercept,slope,root


def calibration():
    entries=[]; boot_y=[]
    for i,m2 in enumerate(MASSES):
        chains=[run_chain(float(m2),CAL_SEED+1_000*i+j,CAL_BURN,CAL_TRAJ) for j in range(CAL_CHAINS)]
        est=pooled_bootstrap(chains,BOOT_SEED+i)
        entry={'m2':float(m2),'estimator':{k:v for k,v in est.items() if k!='_boot'},
               'acceptance_by_chain':[float(c['acceptance']) for c in chains],
               'diagnostics':diagnostics(chains)}
        entries.append(entry); boot_y.append(est['_boot'])
    y=np.array([r['estimator']['z_pooled'] for r in entries])
    intercept,slope,root=fit_with_root(MASSES,y)
    by=np.column_stack(boot_y)
    xc=MASSES-MASSES.mean(); denom=np.dot(xc,xc)
    bslope=(by@xc)/denom
    bint=by.mean(axis=1)-bslope*MASSES.mean()
    broot=(TARGET-bint)/bslope
    finite=broot[np.isfinite(broot)]
    root90=[float(v) for v in np.quantile(finite,[.05,.95])]
    inside=(MASSES.min()<=root<=MASSES.max() and MASSES.min()<=root90[0] and root90[1]<=MASSES.max())
    usable=bool(slope>0 and inside)
    return {'entries':entries,'fit':{'intercept':intercept,'slope':slope,'root_m2':root,
             'bootstrap_root_n':int(len(finite)),'bootstrap_root_90':root90,
             'usable':usable},'selected_m2':round(root,6) if usable else None}


def cb_chain(m2:float,seed:int):
    rng=np.random.default_rng(seed); phi=rng.normal(scale=.2,size=(N,N)); records=[]; accepts=[]
    sigma=1/np.sqrt(4+m2)
    for t in range(CB_BURN+CB_SWEEPS):
        for mask in (RED,BLACK):
            neigh=np.roll(phi,1,0)+np.roll(phi,-1,0)+np.roll(phi,1,1)+np.roll(phi,-1,1)
            old=phi[mask]
            proposal=neigh[mask]/(4+m2)+sigma*rng.normal(size=old.shape)
            delta=LAMBDA_HAT/24*(proposal**4-old**4)
            take=np.log(rng.random(size=old.shape))<np.minimum(0.,-delta)
            phi[mask]=np.where(take,proposal,old)
            if t>=CB_BURN: accepts.append(float(np.mean(take)))
        if t>=CB_BURN:records.append(observables(phi))
    return {'acceptance':float(np.mean(accepts)),'records':np.asarray(records)}


def hmc_validation(m2:float):
    chains=[run_chain(m2,VAL_SEED+j,VAL_BURN,VAL_TRAJ) for j in range(VAL_CHAINS)]
    est=pooled_bootstrap(chains,20270210)
    diag=diagnostics(chains)
    min_ess=min(diag['G0']['combined_approx_ess'],diag['Gp']['combined_approx_ess'])
    gates={'z_in_frozen_band':bool(3.95<=est['z_pooled']<=4.05),
           'bootstrap_95_contains_target':bool(est['bootstrap_95'][0]<=TARGET<=est['bootstrap_95'][1]),
           'acceptance_in_target_band':bool(all(.65<=c['acceptance']<=.90 for c in chains)),
           'basic_rhat_pass':bool(all(v['basic_split_rhat']<=1.01 for v in diag.values())),
           'min_G0_Gp_ess_ge_1000':bool(min_ess>=1000)}
    return {'estimator':{k:v for k,v in est.items() if k!='_boot'},'acceptance_by_chain':[float(c['acceptance']) for c in chains],
            'diagnostics':diag,'minimum_G0_Gp_ess':min_ess,'gates':gates,'passes':bool(all(gates.values()))}


def overlap(a,b):return max(a[0],b[0])<=min(a[1],b[1])

def comparator(m2:float,hmc_interval):
    chains=[cb_chain(m2,CB_SEED+j) for j in range(CB_CHAINS)]
    est=pooled_bootstrap(chains,20280210)
    diag=diagnostics(chains)
    rhat=bool(all(v['basic_split_rhat']<=1.01 for v in diag.values()))
    ov=overlap(est['bootstrap_95'],hmc_interval)
    return {'estimator':{k:v for k,v in est.items() if k!='_boot'},'acceptance_by_chain':[float(c['acceptance']) for c in chains],
            'diagnostics':diag,'intervals_overlap_hmc':ov,'basic_rhat_pass':rhat,'passes':bool(ov and rhat)}


def main():
    cal=calibration(); validation=None; compare=None
    if cal['fit']['usable']:
        validation=hmc_validation(cal['selected_m2'])
        compare=comparator(cal['selected_m2'],validation['estimator']['bootstrap_95'])
    payload={'scope':'Frozen F1 N=16 pooled-moment/chain-replicated mass calibration; no g_R, scaling, continuum, quantum, or Point-Sphere claim.',
      'specification':'Point-Sphere_Interacting_LambdaPhi4_N16_Pooled_Chain_Tuning_v1_Specification.md',
      'calibration_configuration':{'masses':MASSES.tolist(),'n_chains':CAL_CHAINS,'burn':CAL_BURN,'trajectories':CAL_TRAJ,'bootstrap':BOOT},
      'calibration':cal,'validation':validation,'checkerboard_comparator':compare,
      'retained_prior_failure':'response_surface_v2_selected_mass_validation_failed',
      'tuning_pass':bool(cal['fit']['usable'] and validation is not None and validation['passes'] and compare is not None and compare['passes'])}
    Path(__file__).with_name('Point-Sphere_Interacting_LambdaPhi4_Pooled_Chain_Tuning_v1.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps(payload,indent=2))
if __name__=='__main__':main()
