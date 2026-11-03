#!/usr/bin/env python3
"""Finite-transition-table D/I calibration for Tier-0 blind-pipeline v1."""
from __future__ import annotations
import copy
import json
from pathlib import Path
import numpy as np

from point_sphere_tier0_reference_generator_v2 import m1,m2,m3,m4,simulate,sigmoid
import point_sphere_tier0_blind_pipeline_v1 as blind
from point_sphere_tier0_global_mode_null import global_mode_null

SEEDS=list(range(20261120,20261125))
LENGTHS=[3_000,12_000]
STATIONARY_TOL=1e-13


def states_for(n):
    x=np.arange(1<<n,dtype=np.uint32)[:,None]
    return ((x >> np.arange(n,dtype=np.uint32)) & 1).astype(float)


def probability_table(system, states):
    z=system.w[:,0][None,:]+states@system.w[:,1:].T
    for (t,i,j),v in system.pairs.items(): z[:,t]+=v*states[:,i]*states[:,j]
    return sigmoid(z)


def transition_kernel(system, states, probs):
    n=len(system.names); M=len(states); logp=np.zeros((M,M),dtype=float)
    for j in range(n):
        right=states[:,j][None,:]
        logp+=np.where(right==1,np.log(probs[:,j,None]+1e-300),np.log(1-probs[:,j,None]+1e-300))
    P=np.exp(logp)
    return P


def stationary(P):
    pi=np.full(len(P),1/len(P))
    for it in range(1,10001):
        nxt=pi@P
        err=float(np.abs(nxt-pi).sum())
        pi=nxt
        if err<STATIONARY_TOL:return pi,it,err
    raise RuntimeError('stationary iteration did not converge')


def binary_entropy(q):
    q=np.clip(q,1e-300,1-1e-300)
    return -(q*np.log(q)+(1-q)*np.log(1-q))


def cond_entropy(pi, probs, states, target, features):
    codes=np.zeros(len(states),dtype=np.int64)
    for k,j in enumerate(features): codes |= (states[:,j].astype(np.int64)<<k)
    ncode=1<<len(features)
    masses=np.bincount(codes,weights=pi,minlength=ncode)
    succ=np.bincount(codes,weights=pi*probs[:,target],minlength=ncode)
    q=np.divide(succ,masses,out=np.zeros_like(succ),where=masses>0)
    return float(np.sum(masses*binary_entropy(q)))


def exact_i(pi,probs,states,c):
    vals=[]
    for j in c['A']:
        hlocal=cond_entropy(pi,probs,states,j,[j]+c['B'])
        hfull=cond_entropy(pi,probs,states,j,c['A']+c['B'])
        vals.append(hlocal-hfull)
    return float(np.mean(vals))


def exact_d(system,states,c):
    d=0.0
    for r in c['R']:
        x0=states.copy();x1=states.copy();x0[:,r]=0;x1[:,r]=1
        p0=probability_table(system,x0);p1=probability_table(system,x1)
        d=max(d,float(np.max(np.abs(p0[:,c['A']]-p1[:,c['A']]))))
    return d


def inherited_i(data,c):
    tr,te=data[:len(data)//2],data[len(data)//2:]
    xtr,ytr=tr[:-1],tr[1:];xte,yte=te[:-1],te[1:]
    a,b=c['A'],c['B']
    full=blind.nll(xtr[:,a+b],ytr[:,a],xte[:,a+b],yte[:,a])
    local=np.mean([blind.nll(xtr[:,[j]+b],ytr[:,[j]],xte[:,[j]+b],yte[:,[j]]) for j in a])
    return float(local-full)


def candidate(system):
    c=copy.deepcopy(system.candidates[0])
    c['R']=sorted(set(range(len(system.names)))-set(c['A'])-set(c['B']))
    return c


def family_systems():
    return [('M1',m1()),('M2',m2()),('M3',m3()),('M4',m4()),('M5',global_mode_null())]


def moments(xs):
    x=np.array(xs,dtype=float)
    return {'mean':float(x.mean()),'bias':float(x.mean()),'rmse':float(np.sqrt(np.mean(x*x))),
            'min':float(x.min()),'max':float(x.max())}


def main():
    exact=[]; records=[]
    for k,(label,system) in enumerate(family_systems()):
        c=candidate(system); states=states_for(len(system.names)); probs=probability_table(system,states)
        P=transition_kernel(system,states,probs)
        rowsums=P.sum(axis=1)
        pi,niter,err=stationary(P)
        dtrue=exact_d(system,states,c); itrue=exact_i(pi,probs,states,c)
        entry={'family':label,'n_nodes':len(system.names),'candidate':c,'state_count':len(states),
               'kernel_max_row_normalisation_error':float(np.max(np.abs(rowsums-1))),
               'stationary_iterations':niter,'stationary_last_l1_step':err,
               'D_table_exact':dtrue,'I_table_exact':itrue}
        exact.append(entry)
        for n in LENGTHS:
            for seed in SEEDS:
                data=simulate(system,seed+10000*k,n=n,burn=500)
                dhat=blind.exact_d(system,c,data)
                ihat=inherited_i(data,c)
                records.append({'family':label,'n_data':n,'seed':seed,'D_hat':dhat,'I_hat':ihat,
                                'D_exact':dtrue,'I_exact':itrue,'D_error':dhat-dtrue,'I_error':ihat-itrue})
        print(label,'D',dtrue,'I',itrue,'stationary iter',niter,flush=True)
    summary={}
    for label,_ in family_systems():
        r=[x for x in records if x['family']==label]
        summary[label]={'D_error':moments([x['D_error'] for x in r]),'I_error':moments([x['I_error'] for x in r])}
    allD=[x['D_error'] for x in records];allI=[x['I_error'] for x in records]
    payload={'scope':'Finite-state exact D/I calibration of inherited blind pipeline. No thresholds changed; no interval coverage claim.',
             'specification':'Point-Sphere_Tier0_Exact_Table_Calibration_v1_Specification.md',
             'stationary_tolerance':STATIONARY_TOL,'seeds':SEEDS,'lengths':LENGTHS,
             'exact':exact,'records':records,'summary_by_family':summary,
             'pooled':{'D_error':moments(allD),'I_error':moments(allI)},
             'implementation_pass':bool(all(e['kernel_max_row_normalisation_error']<1e-12 for e in exact)
                                        and exact[0]['D_table_exact']==0 and exact[1]['D_table_exact']==0
                                        and exact[2]['D_table_exact']>0.02 and exact[3]['D_table_exact']==0
                                        and exact[4]['D_table_exact']>0.02)}
    Path(__file__).with_name('Point-Sphere_Tier0_Exact_Table_Calibration_v1.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps({'implementation_pass':payload['implementation_pass'],'pooled':payload['pooled']},indent=2))
if __name__=='__main__':main()
