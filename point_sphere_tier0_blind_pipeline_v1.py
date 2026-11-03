#!/usr/bin/env python3
"""Blind discovery/count-recovery gate for the frozen Tier-0 v2 generator.

The script follows Point-Sphere_Tier0_Blind_Pipeline_v1_Specification.md. It
receives anonymous graph/data representations, enumerates candidate A/B/M tuples,
locks D/I/S/L/P thresholds, commits a result, and only then compares it to the
answer key held by this test harness.
"""
from __future__ import annotations

from itertools import combinations
import json
from pathlib import Path
import numpy as np

from point_sphere_tier0_reference_generator_v2 import (
    SEED, m1, m2, m3, m4, simulate, sigmoid, tracking_loss
)

N_DATA = 12_000
BURN = 500
RIDGE = 1e-4
THRESHOLDS = {"D_max": 0.02, "I_min": 0.02, "S_min": 0.02, "L_min": 0.05, "P_min": 0.05}


def fit_logistic(x, y, iters=500, lr=0.30):
    x1 = np.column_stack([np.ones(len(x)), x])
    beta = np.zeros(x1.shape[1])
    for _ in range(iters):
        p = sigmoid(x1 @ beta)
        grad = x1.T @ (p-y)/len(x1)
        grad[1:] += RIDGE*beta[1:]
        beta -= lr*grad
    return beta


def nll(xtr, ytr, xte, yte):
    values=[]
    for j in range(ytr.shape[1]):
        beta=fit_logistic(xtr,ytr[:,j])
        p=sigmoid(np.column_stack([np.ones(len(xte)),xte])@beta)
        values.append(-np.mean(yte[:,j]*np.log(p+1e-12)+(1-yte[:,j])*np.log(1-p+1e-12)))
    return float(np.mean(values))


def skeleton(system):
    n=len(system.names)
    adj={i:set() for i in range(n)}
    for target in range(n):
        for source, coeff in enumerate(system.w[target,1:]):
            if coeff != 0 and source != target:
                adj[target].add(source);adj[source].add(target)
    for target,i,j in system.pairs:
        if target != i: adj[target].add(i);adj[i].add(target)
        if target != j: adj[target].add(j);adj[j].add(target)
        if i != j: adj[i].add(j);adj[j].add(i)
    return adj


def is_connected(vertices, adj, removed=set()):
    vertices=set(vertices)
    if not vertices: return False
    stack=[next(iter(vertices))]; seen=set(stack)
    while stack:
        v=stack.pop()
        for w in adj[v]:
            if w not in removed and w in vertices and w not in seen:
                seen.add(w);stack.append(w)
    return seen==vertices


def boundary_separates(a,b,r,adj):
    """B must block every undirected A-to-R path in the supplied skeleton."""
    blocked=set(b); seen=set(a); stack=list(a)
    while stack:
        v=stack.pop()
        for w in adj[v]:
            if w in blocked or w in seen: continue
            seen.add(w);stack.append(w)
    return all(node not in seen for node in r)


def enumerate_candidates(system):
    adj=skeleton(system); nodes=range(len(system.names)); out=[]
    for a_tuple in combinations(nodes,3):
        a=set(a_tuple)
        if not is_connected(a,adj): continue
        boundary_options=sorted(set().union(*(adj[v] for v in a))-a)
        for bnode in boundary_options:
            b={bnode}; r=set(nodes)-a-b
            if not r or not boundary_separates(a,b,r,adj): continue
            for m in sorted(a):
                out.append({"A":list(sorted(a)),"B":[bnode],"R":list(sorted(r)),"M":m})
    return out


def exact_d(system,c,data):
    contexts=data[np.linspace(0,len(data)-1,min(800,len(data)),dtype=int)]
    defect=0.0
    for r in c["R"]:
        for x in contexts:
            x0=x.copy(); x1=x.copy(); x0[r]=0; x1[r]=1
            defect=max(defect,float(np.max(np.abs(system.probabilities(x0)[c["A"]]-system.probabilities(x1)[c["A"]]))))
    return defect


def lesion_l(system,c,seed):
    normal=simulate(system,seed,n=4_000,burn=BURN)
    lesioned=simulate(system,seed,n=4_000,burn=BURN,clamp={c["M"]:0})
    return tracking_loss(lesioned,c)-tracking_loss(normal,c)


def score(system,c,data,seed):
    tr,te=data[:len(data)//2],data[len(data)//2:]
    xtr,ytr=tr[:-1],tr[1:];xte,yte=te[:-1],te[1:]
    a,b,m=c["A"],c["B"],c["M"]
    full=nll(xtr[:,a+b],ytr[:,a],xte[:,a+b],yte[:,a])
    local=np.mean([nll(xtr[:,[j]+b],ytr[:,[j]],xte[:,[j]+b],yte[:,[j]]) for j in a])
    nonm=[j for j in a if j!=m]
    withm=nll(xtr[:,a+b],ytr[:,nonm],xte[:,a+b],yte[:,nonm])
    without=nll(xtr[:,nonm+b],ytr[:,nonm],xte[:,nonm+b],yte[:,nonm])
    base=nll(np.zeros((len(xtr),0)),ytr[:,a],np.zeros((len(xte),0)),yte[:,a])
    metrics={
        "D": exact_d(system,c,data),
        "I": float(local-full),
        "S": float(without-withm),
        "L": float(lesion_l(system,c,seed)),
        "P": float(base-full),
    }
    passed=(metrics["D"]<=THRESHOLDS["D_max"] and metrics["I"]>=THRESHOLDS["I_min"] and
            metrics["S"]>=THRESHOLDS["S_min"] and metrics["L"]>=THRESHOLDS["L_min"] and
            metrics["P"]>=THRESHOLDS["P_min"])
    return {"candidate":c,"metrics":metrics,"passes":passed}


def overlap_selected(passing):
    # Exact same A with different M is an overlap/indeterminacy, as are partial overlaps.
    selected=[]; overlap=[]
    for item in passing:
        a=set(item["candidate"]["A"])
        if any(a & set(other["candidate"]["A"]) for other in selected):
            overlap.append(item)
        else:
            selected.append(item)
    return selected,overlap


def run_system(system, seed):
    # Anonymous indices are used; answer key is not consulted until final comparison.
    data=simulate(system,seed,n=N_DATA,burn=BURN)
    candidates=enumerate_candidates(system)
    scored=[score(system,c,data,seed+1000+i) for i,c in enumerate(candidates)]
    passing=[x for x in scored if x["passes"]]
    selected,overlap=overlap_selected(passing)
    return {
        "n_nodes":len(system.names),
        "candidate_count_enumerated":len(candidates),
        "passing_count_pre_overlap":len(passing),
        "selected_disjoint_count":len(selected),
        "overlap_indeterminate_count":len(overlap),
        "selected":selected,
        "all_scored":scored,
    }


def main():
    # The expected key is deliberately consulted only after each run_system return.
    systems=[("M1",m1(),1),("M2",m2(),2),("M3",m3(),0),("M4",m4(),0)]
    records=[]
    for i,(label,system,expected) in enumerate(systems):
        result=run_system(system,SEED+100*i)
        actual=(result["selected_disjoint_count"] if result["overlap_indeterminate_count"]==0 else "indeterminate_overlap")
        records.append({"family_revealed_after_scoring":label,"expected_count":expected,"blind_output":actual,
                        "exact_recovery":actual==expected,"result":result})
    payload={
        "scope":"Blind-pipeline v1 on idealised supplied interaction graphs. Scores, budgets, and thresholds follow the frozen specification.",
        "thresholds":THRESHOLDS,
        "n_data":N_DATA,
        "records":records,
        "all_exact_recoveries":bool(all(row["exact_recovery"] for row in records)),
    }
    Path(__file__).with_name("Point-Sphere_Tier0_Blind_Pipeline_v1.json").write_text(json.dumps(payload,indent=2)+"\n")
    print(json.dumps(payload,indent=2))

if __name__=="__main__":
    main()
