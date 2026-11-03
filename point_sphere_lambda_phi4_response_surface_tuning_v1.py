#!/usr/bin/env python3
"""Execute the frozen N=16 response-surface mass-tuning specification v1."""
from __future__ import annotations
import json
import math
from pathlib import Path
import numpy as np
from point_sphere_lambda_phi4_pilot import (
    TARGET_Z, run_chain, z_from_g, basic_split_rhat
)

SEED=20261030
MASSES=np.array([0.052,0.054,0.056,0.058,0.060],dtype=float)
NCHAINS=4
BURN=1_000
TRAJ=20_000
BLOCK=500


def gammaincc(a: float, x: float) -> float:
    """Regularized upper incomplete gamma Q(a,x), adequate for chi-square df=3."""
    if x <= 0: return 1.0
    itmax=200; eps=3e-14; fpmin=1e-300
    if x < a+1:
        ap=a; term=1/a; total=term
        for _ in range(itmax):
            ap += 1; term *= x/ap; total += term
            if abs(term) < abs(total)*eps: break
        p=total*math.exp(-x+a*math.log(x)-math.lgamma(a))
        return max(0.0,min(1.0,1-p))
    b=x+1-a; c=1/fpmin; d=1/b; h=d
    for i in range(1,itmax+1):
        an=-i*(i-a); b += 2; d=an*d+b
        if abs(d)<fpmin: d=fpmin
        c=b+an/c
        if abs(c)<fpmin: c=fpmin
        d=1/d; delta=d*c; h*=delta
        if abs(delta-1)<eps: break
    return max(0.0,min(1.0,math.exp(-x+a*math.log(x)-math.lgamma(a))*h))


def block_z(records: np.ndarray) -> list[float]:
    vals=[]
    for start in range(0,len(records),BLOCK):
        r=records[start:start+BLOCK]
        vals.append(z_from_g(r[:,1],r[:,2]))
    return vals


def response_grid():
    out=[]
    for i,m2 in enumerate(MASSES):
        chains=[run_chain(float(m2),SEED+1_000*i+j,BURN,TRAJ) for j in range(NCHAINS)]
        blocks=np.array([v for c in chains for v in block_z(c['records'])],dtype=float)
        means_by_chain=[z_from_g(c['records'][:,1],c['records'][:,2]) for c in chains]
        out.append({
            'm2':float(m2),'block_z':blocks.tolist(),'block_n':int(len(blocks)),
            'z_mean':float(blocks.mean()),'block_variance':float(blocks.var(ddof=1)),
            'z_by_chain':means_by_chain,'acceptance_by_chain':[c['acceptance'] for c in chains],
        })
    return out


def fit_response(grid):
    x=np.array([r['m2'] for r in grid]); y=np.array([r['z_mean'] for r in grid])
    vari=np.array([r['block_variance'] for r in grid]); n=np.array([r['block_n'] for r in grid])
    weights=n/vari
    X=np.column_stack([np.ones(len(x)),x]); xtwx=X.T @ (weights[:,None]*X)
    beta=np.linalg.solve(xtwx,X.T@(weights*y)); pred=X@beta
    chi=float(np.sum(weights*(y-pred)**2)); df=len(x)-2
    p=gammaincc(df/2,chi/2)
    root=float((TARGET_Z-beta[0])/beta[1]) if beta[1] != 0 else float('nan')
    return {'intercept':float(beta[0]),'slope':float(beta[1]),'predicted_z':pred.tolist(),
            'chi_square_lack_of_fit':chi,'df':df,'p_value':p,'root_m2':root,
            'weights':weights.tolist(),
            'usable':bool(beta[1]>0 and min(x)<=root<=max(x) and p>=0.05)}


def validate(m2: float):
    chains=[run_chain(m2,SEED+90_000+j,BURN,TRAJ) for j in range(NCHAINS)]
    g0=np.concatenate([c['records'][:,1] for c in chains]); gp=np.concatenate([c['records'][:,2] for c in chains])
    z=z_from_g(g0,gp)
    diag={}
    for col,name in enumerate(['M','G0','Gp']):
        xs=[c['records'][:,col] for c in chains]
        diag[name]={'basic_split_rhat':basic_split_rhat(xs)}
    return {'m2':m2,'z_pooled':z,'z_by_chain':[z_from_g(c['records'][:,1],c['records'][:,2]) for c in chains],
            'acceptance_by_chain':[c['acceptance'] for c in chains], 'diagnostics':diag,
            'passes':bool(3.95<=z<=4.05 and all(0.65<=c['acceptance']<=0.90 for c in chains)
                          and all(x['basic_split_rhat']<=1.01 for x in diag.values()))}


def main():
    grid=response_grid(); fit=fit_response(grid)
    validation=None
    if fit['usable']:
        selected=round(fit['root_m2'],6)
        validation=validate(selected)
    payload={'scope':'Frozen N=16 response-surface mass tuning v1; a selection pass is not a five-size production or continuum result.',
             'specification':'Point-Sphere_Interacting_LambdaPhi4_N16_Response_Surface_Tuning_Specification.md',
             'configuration':{'seed':SEED,'masses':MASSES.tolist(),'n_chains':NCHAINS,'burn':BURN,'trajectories':TRAJ,'block':BLOCK},
             'grid':grid,'fit':fit,'validation':validation,
             'tuning_pass':bool(fit['usable'] and validation is not None and validation['passes'])}
    Path(__file__).with_name('Point-Sphere_Interacting_LambdaPhi4_Response_Surface_Tuning_v1.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps(payload,indent=2))

if __name__=='__main__':main()
