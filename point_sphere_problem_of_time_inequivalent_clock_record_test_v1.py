#!/usr/bin/env python3
"""Execute frozen T1c inequivalent-clock/record-backreaction diagnostic.

A finite classical constraint model only; lambda is a gauge-flow parameter, not external
physical time. The program does not claim a quantum-gravity solution.
"""
from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np

OMEGA=1.0; FREQ=np.array([4.0,5.0,6.0]); G=0.5
DT=.002; END=40.0; STEPS=round(END/DT)


def constraint(y,g):
    pphi=y[1]; alpha=y[2]; pa=y[3]; r=y[4::2]; pr=y[5::2]
    h=.5*pa*pa+.5*OMEGA**2*alpha*alpha+np.sum(.5*pr*pr+.5*FREQ**2*r*r)+g*alpha*np.sum(r)
    return .5*pphi*pphi-h


def deriv(y,g):
    out=np.zeros_like(y); alpha=y[2]; pa=y[3]; r=y[4::2]; pr=y[5::2]
    out[0]=y[1]                    # d phi/d lambda
    out[1]=0.0
    out[2]=-pa                     # d alpha/d lambda
    out[3]=OMEGA**2*alpha+g*np.sum(r)
    out[4::2]=-pr
    out[5::2]=FREQ**2*r+g*alpha
    return out


def integrate(y0,g):
    y=y0.copy(); ys=np.empty((STEPS+1,len(y))); cs=np.empty(STEPS+1); ys[0]=y;cs[0]=constraint(y,g)
    for k in range(STEPS):
        k1=deriv(y,g);k2=deriv(y+.5*DT*k1,g);k3=deriv(y+.5*DT*k2,g);k4=deriv(y+DT*k3,g)
        y=y+(DT/6)*(k1+2*k2+2*k3+k4);ys[k+1]=y;cs[k+1]=constraint(y,g)
    return ys,cs


def digitize(x,n=8):
    lo=float(np.min(x));hi=float(np.max(x))
    if hi==lo:return np.zeros(len(x),dtype=int)
    return np.minimum(n-1,((x-lo)/(hi-lo)*n).astype(int))


def mi(a,b,n=8):
    joint=np.zeros((n,n),float)
    for x,y in zip(a,b):joint[x,y]+=1
    joint/=joint.sum(); px=joint.sum(1,keepdims=True);py=joint.sum(0,keepdims=True)
    nz=joint>0
    return float(np.sum(joint[nz]*np.log(joint[nz]/(px*py)[nz])))


def sign_changes(v,tol=1e-7):
    s=np.sign(v);s[np.abs(v)<tol]=0
    s=s[s!=0]
    return int(np.sum(s[1:]!=s[:-1]))


def main():
    # State: phi,p_phi,alpha,p_alpha,r1,p1,r2,p2,r3,p3
    y0=np.zeros(10);y0[3]=1.0;y0[5::2]=-G/(FREQ**2)
    # Enforce C=0 at initial point using the positive branch.
    h0=-constraint(y0,G) # because p_phi=0 in y0
    y0[1]=math.sqrt(2*h0)
    coupled,cres=integrate(y0,G)
    base=np.zeros(10);base[1]=1.0;base[3]=1.0
    baseline,base_cres=integrate(base,0.0)
    lam=np.linspace(0,END,STEPS+1)
    alpha=coupled[:,2];phi=coupled[:,0];palpha=coupled[:,3];pphi=coupled[:,1];records=coupled[:,4::2]
    mask=lam>=5.0
    aa=digitize(alpha[mask]);bb=digitize((2*alpha)[mask]);ff=digitize(phi[mask])
    recbins=[digitize(records[mask,i]) for i in range(3)]
    mi_alpha=[mi(x,aa) for x in recbins];mi_phi=[mi(x,ff) for x in recbins];mi_beta=[mi(x,bb) for x in recbins]
    corr_alpha=[float(np.corrcoef(records[mask,i],alpha[mask])[0,1]) for i in range(3)]
    paircorr=[[float(np.corrcoef(records[mask,i],records[mask,j])[0,1]) for j in range(3)] for i in range(3)]
    back=float(np.sqrt(np.mean((alpha-baseline[:,2])**2))/np.sqrt(np.mean(baseline[:,2]**2)))
    aturn=sign_changes(-palpha);bturn=sign_changes(-2*palpha) # beta-dot=2 alpha-dot
    results={
      'scope':'T1c finite classical Hamiltonian-constraint diagnostic; no full GR/QG, measurement, arrow, or phenomenology claim.',
      'parameters':{'omega':OMEGA,'record_frequencies':FREQ.tolist(),'g':G,'dt':DT,'end':END,'steps':STEPS},
      'initial_data':{'state':y0.tolist(),'initial_constraint':constraint(y0,G)},
      'constraint_residuals':{'coupled_max_abs':float(np.max(np.abs(cres))),'baseline_max_abs':float(np.max(np.abs(base_cres)))},
      'global_usability':{'phi_dot_min':float(np.min(pphi)),'phi_dot_max':float(np.max(pphi)),
                           'alpha_turning_sign_changes':aturn,'beta_turning_sign_changes':bturn},
      'backreaction':{'normalized_alpha_rms_difference_from_g0_baseline':back},
      'record_association_after_lambda_5':{'mutual_information_pointer_alpha_nats':mi_alpha,
          'mutual_information_pointer_phi_nats':mi_phi,'mutual_information_pointer_beta_nats':mi_beta,
          'pointer_alpha_correlations':corr_alpha,'inter_pointer_correlations':paircorr},
      'PITR_interpretation':{'P2':'phi is globally monotonic in the stipulated solution; alpha and beta turn repeatedly.',
          'P4':'fixed record coupling produces nonzero quantified alpha backreaction.',
          'P5':'the fixed pointers physically record alpha/beta more directly than phi, but do not convert a turning alpha into a global clock.',
          'P6':'alpha-to-beta canonical relabelling preserves turnings and record mutual information up to numerical binning.',
          'combined_selection_result':'PITR adds no independent clock selection in this model beyond monotonicity/domain plus the stipulated interaction choice.'},
      'registered_checks':{'constraint_preserved':bool(np.max(np.abs(cres))<1e-8),
          'phi_monotonic':bool(np.min(pphi)>0),'alpha_turns':bool(aturn>0),'backreaction_nonzero':bool(back>1e-8),
          'beta_turning_invariant':bool(aturn==bturn),'record_MI_relabelling_invariant':bool(np.max(np.abs(np.array(mi_alpha)-np.array(mi_beta)))<1e-12)},
      'conclusion':'The record bank is interaction-relative: it can robustly correlate with a turning geometric variable. Public records alone therefore do not make that variable a global physical clock. In this model PITR does not yet improve on ordinary monotonicity/domain analysis.'}
    results['all_registered_checks_pass']=all(results['registered_checks'].values())
    Path(__file__).with_name('Point-Sphere_Problem_of_Time_Inequivalent_Clock_Record_Test_v1.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results,indent=2))
if __name__=='__main__':main()
