#!/usr/bin/env python3
"""Pre-production HMC pilot for the frozen finite-volume lambda-phi^4_2 target.

This implements the action and finite-volume mass observable in
Point-Sphere_Interacting_LambdaPhi4_Target_Specification_v1.md. It is explicitly
not the target's production run: it tunes m0^2 at N=16 and measures preliminary
mixing diagnostics needed to size a later four-chain production calculation.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np

SEED = 20261025
N = 16
L_PHYS = 1.0
LAMBDA_PHYS = 10.0
LAMBDA_HAT = LAMBDA_PHYS / N**2
TARGET_Z = 4.0
MASS_TOL = 0.12  # broader than production tolerance; pilot stopping only
TUNE_BRACKET = (-0.02, 0.14)
TUNE_ITERS = 6
TUNE_BURN = 400
TUNE_TRAJ = 1200
PILOT_BURN = 1_000
PILOT_TRAJ = 5_000
STEP_SIZE = 0.16
N_LEAPFROG = 10


def action(phi: np.ndarray, m2: float) -> float:
    dx0 = np.roll(phi, -1, axis=0) - phi
    dx1 = np.roll(phi, -1, axis=1) - phi
    return float(0.5*np.sum(dx0*dx0 + dx1*dx1) + 0.5*m2*np.sum(phi*phi) + LAMBDA_HAT/24*np.sum(phi**4))


def grad_action(phi: np.ndarray, m2: float) -> np.ndarray:
    lap = 4*phi - np.roll(phi, 1, 0) - np.roll(phi, -1, 0) - np.roll(phi, 1, 1) - np.roll(phi, -1, 1)
    return lap + m2*phi + (LAMBDA_HAT/6.0)*phi**3


def hmc_step(phi: np.ndarray, m2: float, rng: np.random.Generator):
    p0 = rng.normal(size=phi.shape)
    h0 = action(phi,m2) + 0.5*np.sum(p0*p0)
    q = phi.copy(); p = p0.copy()
    p -= 0.5*STEP_SIZE*grad_action(q,m2)
    for i in range(N_LEAPFROG):
        q += STEP_SIZE*p
        if i != N_LEAPFROG-1:
            p -= STEP_SIZE*grad_action(q,m2)
    p -= 0.5*STEP_SIZE*grad_action(q,m2)
    p = -p
    h1 = action(q,m2) + 0.5*np.sum(p*p)
    dh = float(h1-h0)
    accept = np.log(rng.random()) < min(0.0,-dh)
    return (q if accept else phi), bool(accept), dh


def observables(phi: np.ndarray):
    v=N*N
    ft=np.fft.fft2(phi)
    g0=float(abs(ft[0,0])**2/v)
    gp=float(0.5*(abs(ft[1,0])**2+abs(ft[0,1])**2)/v)
    return float(phi.sum()),g0,gp


def z_from_g(g0: np.ndarray, gp: np.ndarray) -> float:
    ratio=float(np.mean(g0)/np.mean(gp))
    denom=ratio-1.0
    if denom <= 0: return float('nan')
    p2=4*N*N*np.sin(np.pi/N)**2
    return float(np.sqrt(p2/denom)*L_PHYS)


def integrated_tau(x: np.ndarray, max_lag: int=500) -> float:
    x=np.asarray(x,dtype=float); x=x-x.mean(); n=len(x)
    if n < 10 or np.allclose(x,0): return 0.5
    # direct form is robust enough for this small preliminary pilot
    ac=[]
    var=float(np.dot(x,x)/n)
    for lag in range(1,min(max_lag,n//2)):
        rho=float(np.dot(x[:-lag],x[lag:])/(n-lag)/var)
        if rho <= 0: break
        ac.append(rho)
    return float(max(0.5,0.5+sum(ac)))


def basic_split_rhat(chains: list[np.ndarray]) -> float:
    split=[]
    for x in chains:
        h=len(x)//2
        split += [x[:h],x[h:2*h]]
    n=min(len(x) for x in split)
    split=np.array([x[:n] for x in split],dtype=float)
    means=split.mean(axis=1); vars_=split.var(axis=1,ddof=1)
    w=vars_.mean(); b=n*means.var(ddof=1)
    vhat=(n-1)/n*w+b/n
    return float(np.sqrt(vhat/w)) if w>0 else float('nan')


def run_chain(m2: float, seed: int, burn: int, ntraj: int, store: bool=True):
    rng=np.random.default_rng(seed)
    phi=rng.normal(scale=0.2,size=(N,N))
    accepts=[]; dh=[]; records=[]
    for t in range(burn+ntraj):
        phi,acc,delta=hmc_step(phi,m2,rng)
        if t>=burn:
            accepts.append(acc); dh.append(delta)
            if store: records.append(observables(phi))
    rec=np.asarray(records)
    return {
        "acceptance":float(np.mean(accepts)), "mean_abs_delta_h":float(np.mean(np.abs(dh))),
        "max_abs_delta_h":float(np.max(np.abs(dh))), "records":rec,
    }


def tune_mass():
    lo,hi=TUNE_BRACKET
    log=[]
    # z grows monotonically with m2 in the symmetric parameter neighbourhood.
    for i in range(TUNE_ITERS):
        mid=(lo+hi)/2
        trials=[run_chain(mid,SEED+100*i+j,TUNE_BURN,TUNE_TRAJ) for j in range(2)]
        g0=np.concatenate([x['records'][:,1] for x in trials]); gp=np.concatenate([x['records'][:,2] for x in trials])
        z=z_from_g(g0,gp)
        entry={"iteration":i,"m2":mid,"z":z,"acceptance":float(np.mean([x['acceptance'] for x in trials]))}
        log.append(entry)
        if not np.isfinite(z):
            lo=mid
        elif z < TARGET_Z:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2,log


def main():
    m2,tune_log=tune_mass()
    chains=[run_chain(m2,SEED+10_000+i,PILOT_BURN,PILOT_TRAJ) for i in range(4)]
    names=['M','G0','Gp']
    by_name={}
    for col,name in enumerate(names):
        xs=[c['records'][:,col] for c in chains]
        tau=[integrated_tau(x) for x in xs]
        total=sum(len(x) for x in xs)
        by_name[name]={
            "mean":float(np.mean(np.concatenate(xs))),
            "tau_int_by_chain":tau,
            "minimum_ess":float(min(len(x)/(2*t) for x,t in zip(xs,tau))),
            "combined_approx_ess":float(total/(2*max(tau))),
            "basic_split_rhat":basic_split_rhat(xs),
        }
    g0=np.concatenate([c['records'][:,1] for c in chains]); gp=np.concatenate([c['records'][:,2] for c in chains])
    z=z_from_g(g0,gp)
    # Connected 4th-moment pilot observable, consistently normalised with the target spec.
    mvals=np.concatenate([c['records'][:,0] for c in chains]); v=N*N
    chi=float(np.mean(mvals*mvals)/v)
    chi4=float((np.mean(mvals**4)-3*np.mean(mvals*mvals)**2)/v)
    mr2=(z/L_PHYS)**2
    gr=float(-mr2*chi4/(chi*chi))
    payload={
        "scope":"Pre-production N=16 HMC pilot only. It does not satisfy the frozen target's production ESS/length requirements or assert a continuum result.",
        "implementation":{"N":N,"L_physical":L_PHYS,"lambda_physical_L2":LAMBDA_PHYS,"lambda_hat":LAMBDA_HAT,
                          "step_size":STEP_SIZE,"n_leapfrog":N_LEAPFROG,"seed":SEED},
        "mass_tuning":{"target_z":TARGET_Z,"pilot_tolerance":MASS_TOL,"bracket":TUNE_BRACKET,"iterations":tune_log,"selected_m2":m2},
        "pilot_results":{"z":z,"chi":chi,"chi4":chi4,"g_R":gr,
                         "acceptance_by_chain":[c['acceptance'] for c in chains],
                         "mean_abs_delta_h_by_chain":[c['mean_abs_delta_h'] for c in chains],
                         "max_abs_delta_h_by_chain":[c['max_abs_delta_h'] for c in chains],
                         "diagnostics":by_name},
        "production_gate":{"mass_within_pilot_tolerance":bool(abs(z-TARGET_Z)<=MASS_TOL),
                           "acceptance_in_target_band":bool(all(0.65<=c['acceptance']<=0.90 for c in chains)),
                           "all_basic_rhat_le_1_01":bool(all(v['basic_split_rhat']<=1.01 for v in by_name.values())),
                           "note":"Even if preliminary gates pass, a new production run with the frozen target's ESS and 500-tau length requirements remains required."}
    }
    Path(__file__).with_name('Point-Sphere_Interacting_LambdaPhi4_Pilot_N16.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps(payload,indent=2))

if __name__=='__main__':
    main()
