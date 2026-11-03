#!/usr/bin/env python3
"""Execute frozen Tier-0 robustness/count-recovery grid v1 (B-C1)."""
from __future__ import annotations
import copy
import json
from pathlib import Path
import numpy as np

from point_sphere_tier0_reference_generator_v2 import System, m1, m2, m3, m4
import point_sphere_tier0_blind_pipeline_v1 as blind
from point_sphere_tier0_global_mode_null import global_mode_null

SCALES=[0.90,1.00,1.10]
LENGTHS=[3_000,12_000]
SEEDS=list(range(20261110,20261115))


def scale_system(system: System, gamma: float) -> System:
    w=system.w.copy(); w[:,1:]*=gamma
    pairs={key:gamma*value for key,value in system.pairs.items()}
    return System(system.name, list(system.names), w, pairs, copy.deepcopy(system.candidates))


def append_background(system: System, count: int, name: str) -> System:
    old=len(system.names); new=old+count
    w=np.zeros((new,new+1)); w[:old,0]=system.w[:,0];w[:old,1:1+old]=system.w[:,1:]
    for i in range(count):
        k=old+i
        w[k,0]=-0.4
        w[k,1+k]=0.7
    names=list(system.names)+[f'bg_{i}' for i in range(count)]
    return System(name,names,w,dict(system.pairs),copy.deepcopy(system.candidates))


def systems():
    return [
        ('M1',m1(),1),
        ('M1N',append_background(m1(),5,'M1_background10'),1),
        ('M2',m2(),2),
        ('M2N',append_background(m2(),4,'M2_background14'),2),
        ('M3',m3(),0),
        ('M4',m4(),0),
        ('M5',global_mode_null(),0),
    ]


def wilson(k:int,n:int,z:float=1.96):
    if n==0:return [float('nan'),float('nan')]
    p=k/n;den=1+z*z/n;cen=(p+z*z/(2*n))/den
    half=z*np.sqrt((p*(1-p)+z*z/(4*n))/n)/den
    return [float(cen-half),float(cen+half)]


def main():
    # No source answer key is passed to blind.run_system; it is consulted only after returned scoring.
    records=[]; idx=0
    for label,base,expected in systems():
        for gamma in SCALES:
            system=scale_system(base,gamma)
            for n in LENGTHS:
                blind.N_DATA=n
                for seed in SEEDS:
                    result=blind.run_system(system,seed)
                    output=(result['selected_disjoint_count'] if result['overlap_indeterminate_count']==0 else 'indeterminate_overlap')
                    records.append({'run_index':idx,'family_revealed_after_scoring':label,'expected_count':expected,
                                    'gamma':gamma,'n_data':n,'seed':seed,'blind_output':output,
                                    'exact_recovery':output==expected,'result':result})
                    idx+=1
                    print(f'{idx}/210 {label} gamma={gamma} n={n} seed={seed} output={output}',flush=True)
    positives=[x for x in records if x['expected_count']>0]
    nulls=[x for x in records if x['expected_count']==0]
    exact=sum(x['exact_recovery'] for x in positives)
    fps=sum(not x['exact_recovery'] for x in nulls)
    summary={
        'positive_exact_recoveries':exact,'positive_runs':len(positives),
        'positive_rate':exact/len(positives),'positive_wilson_95':wilson(exact,len(positives)),
        'false_positive_runs':fps,'null_runs':len(nulls),'false_positive_rate':fps/len(nulls),
        'false_positive_wilson_95':wilson(fps,len(nulls)),
        'count_gate_pass':exact>=114,
        'false_positive_gate_pass':fps<=4,
        'all_grid_gates_pass':bool(exact>=114 and fps<=4),
    }
    payload={'scope':'Frozen Tier-0 robustness grid v1 using supplied ideal interaction skeletons; no table-estimator calibration claim.',
             'specification':'Point-Sphere_Tier0_Robustness_Grid_v1_Specification.md',
             'scales':SCALES,'lengths':LENGTHS,'seeds':SEEDS,'thresholds':blind.THRESHOLDS,
             'records':records,'summary':summary}
    Path(__file__).with_name('Point-Sphere_Tier0_Robustness_Grid_v1.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
