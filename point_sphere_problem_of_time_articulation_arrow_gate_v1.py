#!/usr/bin/env python3
"""Execute frozen T5 articulation/arrow gate."""
from __future__ import annotations
import itertools, json, math
from pathlib import Path
import numpy as np

A0=1.1; GRID=[1.1,1.2,1.5,2.0,3.0]; LN2=math.log(2)

def entropy(rho):
    vals=np.linalg.eigvalsh((rho+rho.conj().T)/2)
    vals=np.clip(vals,0,1)
    return float(-sum(x*math.log(x) for x in vals if x>1e-14))

def ptrace(rho, keep, dims):
    keep=list(keep); traced=[i for i in range(len(dims)) if i not in keep]
    dk=int(np.prod([dims[i] for i in keep]));out=np.zeros((dk,dk),complex)
    kept_idx=list(itertools.product(*[range(dims[i]) for i in keep]))
    trace_idx=list(itertools.product(*[range(dims[i]) for i in traced]))
    for oi,ki in enumerate(kept_idx):
      for oj,kj in enumerate(kept_idx):
       for t in trace_idx:
        ii=[None]*len(dims);jj=[None]*len(dims)
        for n,x in zip(keep,ki):ii[n]=x
        for n,x in zip(keep,kj):jj[n]=x
        for n,x in zip(traced,t):ii[n]=jj[n]=x
        flat_i=np.ravel_multi_index(tuple(ii),dims);flat_j=np.ravel_multi_index(tuple(jj),dims)
        out[oi,oj]+=rho[flat_i,flat_j]
    return out

def mi(rho, A, B, dims):
    return entropy(ptrace(rho,A,dims))+entropy(ptrace(rho,B,dims))-entropy(ptrace(rho,A+B,dims))

def main():
  P=np.array([[0.,1.],[1.,0.]])
  Q=np.diag([1.,-1.])
  rows=[]
  for a in GRID:
    D=math.exp(-(a**3-A0**3));rho=.5*np.array([[1.,D],[D,1.]])
    er=entropy(rho);A=2*er;O=float(np.trace(rho@Q));symmetric=np.max(np.abs(P@rho@P-rho))
    rows.append({'a':a,'D':D,'rho_eigenvalues':np.linalg.eigvalsh(rho).tolist(),
     'branch_environment_articulation_2S_B':A,'orientation_O':O,'branch_exchange_invariance_max_abs_error':float(symmetric)})
  # GHZ state and alternative environment coordinates / declared factorisation.
  psi=np.zeros(8,complex);psi[0]=1/math.sqrt(2);psi[7]=1/math.sqrt(2);rho=np.outer(psi,psi.conj())
  # CNOT control E1 target E2 maps |111> -> |110>.
  U=np.zeros((8,8),complex)
  for b,e1,e2 in itertools.product(range(2),repeat=3):
    old=np.ravel_multi_index((b,e1,e2),(2,2,2));new=np.ravel_multi_index((b,e1,e2^e1),(2,2,2));U[new,old]=1
  rhop=U@rho@U.conj().T
  original=[mi(rho,[0],[1],[2,2,2]),mi(rho,[0],[2],[2,2,2])]
  primed=[mi(rhop,[0],[1],[2,2,2]),mi(rhop,[0],[2],[2,2,2])]
  threshold=.5*LN2
  output_rho=np.diag([1.,0.])
  result={'scope':'T5 finite quantum-information gate, using T4 branch state and a separate three-qubit factorisation illustration. It is not a general no-go theorem for all possible articulation laws.',
   'standing_wave_grid':rows,
   'outgoing_input':{'orientation_O':float(np.trace(output_rho@Q)),'branch_environment_articulation_2S_B':2*entropy(output_rho)},
   'factorisation_illustration':{'threshold_half_ln2':threshold,
     'original_GHZ_I_B_E1_E2':original,'original_fragments_above_threshold':sum(x>=threshold-1e-12 for x in original),
     'primed_coordinates_I_B_E1prime_E2prime':primed,'primed_fragments_above_threshold':sum(x>=threshold-1e-12 for x in primed)},
   'registered_checks':{},'conclusion':''}
  c=result['registered_checks']
  c['G1_branch_neutral_articulation_and_zero_standing_orientation']=all(r['branch_exchange_invariance_max_abs_error']<1e-12 and abs(r['orientation_O'])<1e-12 for r in rows)
  c['G2_outgoing_orientation_is_nonzero_and_input_specified']=abs(result['outgoing_input']['orientation_O']-1)<1e-12
  c['G3_fragment_redundancy_changes_with_declared_factorisation']=result['factorisation_illustration']['original_fragments_above_threshold']!=result['factorisation_illustration']['primed_fragments_above_threshold']
  c['G4_articulation_grows_while_standing_orientation_stays_zero']=all(rows[i+1]['branch_environment_articulation_2S_B']>=rows[i]['branch_environment_articulation_2S_B']-1e-12 for i in range(len(rows)-1)) and all(abs(r['orientation_O'])<1e-12 for r in rows)
  result['all_registered_checks_pass']=all(c.values())
  result['conclusion']='The generous articulation proxy grows as WKB branches become environmentally distinguishable, but it is invariant under branch interchange and its standing-wave orientation remains zero. The outgoing orientation is nonzero only because the outgoing branch was specified. Fragment redundancy further depends on an environmental decomposition. This candidate therefore provides a conditional record diagnostic, not a branch-neutral physical orientation law.'
  Path(__file__).with_name('Point-Sphere_Problem_of_Time_Articulation_Arrow_Gate_v1.json').write_text(json.dumps(result,indent=2)+'\n')
  print(json.dumps(result,indent=2))
if __name__=='__main__':main()
