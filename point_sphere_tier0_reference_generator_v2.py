#!/usr/bin/env python3
"""Tier-0 nonlinear reference generator v2.

Implements the frozen delayed-interface-tracking system in
Point-Sphere_Tier0_Nonlinear_Generator_v2_Specification.md. Scores are still
computed at intended candidate locations only; this is a generator check, not
a blind Tier-0 count-recovery result.
"""
from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import numpy as np

SEED = 20261019
N = 50_000
BURN = 1_000
RIDGE = 1e-4


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))


@dataclass
class System:
    name: str
    names: list[str]
    w: np.ndarray
    pairs: dict[tuple[int, int, int], float]
    candidates: list[dict]

    def probabilities(self, x, clamp=None):
        z = self.w[:, 0] + self.w[:, 1:] @ x
        for (target, i, j), value in self.pairs.items():
            z[target] += value * x[i] * x[j]
        p = sigmoid(z)
        if clamp:
            for key, value in clamp.items():
                p[key] = value
        return p


def m1(name="M1_v2_controller"):
    names = ["y1", "y2", "m", "b", "r"]
    w = np.zeros((5, 6))
    w[0] = [-2.0, 0.4, 0.4, 2.2, 0.0, 0.0]
    w[1] = [-2.0, 0.4, 0.4, 2.2, 0.0, 0.0]
    w[2] = [-1.3, 0.1, 0.1, 0.4, 2.8, 0.0]
    w[3] = [-0.7, 0.0, 0.0, 0.0, 0.8, 1.6]
    w[4] = [-0.3, 0.0, 0.0, 0.0, 0.0, 0.8]
    pairs = {(0, 1, 2): 0.4, (1, 0, 2): 0.4, (2, 3, 0): 0.3}
    c = {"A": [0, 1, 2], "B": [3], "R": [4], "M": 2}
    return System(name, names, w, pairs, [c])


def m2():
    base = m1()
    names = [f"{node}_{suffix}" for suffix in ("a", "b") for node in base.names]
    w = np.zeros((10, 11))
    pairs = {}
    for block in range(2):
        off = 5 * block
        for t in range(5):
            w[off+t, 0] = base.w[t, 0]
            w[off+t, 1+off:1+off+5] = base.w[t, 1:]
        for (t, i, j), value in base.pairs.items():
            pairs[(off+t, off+i, off+j)] = value
    cands = [
        {"A": [0, 1, 2], "B": [3], "R": [4, 5, 6, 7, 8, 9], "M": 2},
        {"A": [5, 6, 7], "B": [8], "R": [0, 1, 2, 3, 4, 9], "M": 7},
    ]
    return System("M2_v2_two_controllers", names, w, pairs, cands)


def m3():
    s = m2()
    s.name = "M3_v2_exterior_bypass"
    s.w[2, 1+4] = 0.95
    s.w[7, 1+9] = 0.95
    return s


def m4():
    s = m1("M4_v2_memory_without_use")
    s.w[0, 1+2] = 0.0
    s.w[1, 1+2] = 0.0
    s.pairs.pop((0, 1, 2))
    s.pairs.pop((1, 0, 2))
    return s


def simulate(s, seed, n=N, burn=BURN, clamp=None):
    rng = np.random.default_rng(seed)
    x = rng.integers(0, 2, size=len(s.names)).astype(float)
    rows = []
    for t in range(n+burn):
        x = (rng.random(len(x)) < s.probabilities(x, clamp)).astype(float)
        if t >= burn:
            rows.append(x.copy())
    return np.asarray(rows)


def fit_logistic(x, y, iters=1_250, lr=0.30):
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


def d_defect(s, c, data):
    contexts=data[np.linspace(0,len(data)-1,min(2000,len(data)),dtype=int)]
    defect=0.0
    for r in c["R"]:
        for x in contexts:
            x0=x.copy();x1=x.copy();x0[r]=0;x1[r]=1
            defect=max(defect,float(np.max(np.abs(s.probabilities(x0)[c["A"]]-s.probabilities(x1)[c["A"]]))))
    return defect


def tracking_loss(data, c):
    y1,y2=c["A"][:2]
    b=c["B"][0]
    # y_t responds through M to the slower, two-step-old interface reference.
    return float(np.mean(0.5*((data[2:,y1]-data[:-2,b])**2+(data[2:,y2]-data[:-2,b])**2)))


def evaluate(s,c,data,seed):
    tr,te=data[:len(data)//2],data[len(data)//2:]
    a,b,m=c["A"],c["B"],c["M"]
    xtr,ytr=tr[:-1],tr[1:];xte,yte=te[:-1],te[1:]
    full=nll(xtr[:,a+b],ytr[:,a],xte[:,a+b],yte[:,a])
    local=np.mean([nll(xtr[:,[j]+b],ytr[:,[j]],xte[:,[j]+b],yte[:,[j]]) for j in a])
    nonm=[j for j in a if j!=m]
    with_m=nll(xtr[:,a+b],ytr[:,nonm],xte[:,a+b],yte[:,nonm])
    without=nll(xtr[:,nonm+b],ytr[:,nonm],xte[:,nonm+b],yte[:,nonm])
    base=nll(np.zeros((len(xtr),0)),ytr[:,a],np.zeros((len(xte),0)),yte[:,a])
    normal=simulate(s,seed,n=12_000,burn=500)
    lesioned=simulate(s,seed,n=12_000,burn=500,clamp={m:0})
    return {
        "candidate": {k:c[k] for k in ("A","B","R","M")},
        "D_exact_intervention_defect": d_defect(s,c,data),
        "I_heldout_joint_loss_gain": float(local-full),
        "S_heldout_M_prediction_gain": float(without-with_m),
        "L_tracking_loss_intact": tracking_loss(normal,c),
        "L_tracking_loss_lesioned": tracking_loss(lesioned,c),
        "L_tracking_loss_increase": float(tracking_loss(lesioned,c)-tracking_loss(normal,c)),
        "P_one_step_predictive_persistence_gain": float(base-full),
    }


def main():
    systems=[m1(),m2(),m3(),m4()]
    results=[]
    for i,s in enumerate(systems):
        data=simulate(s,SEED+17*i)
        results.append({
            "system":s.name,
            "nodes":s.names,
            "n_samples":len(data),
            "intended_candidate_count":len(s.candidates) if s.name.startswith(("M1","M2")) else 0,
            "intended_candidates":[evaluate(s,c,data,SEED+100*i+j) for j,c in enumerate(s.candidates)]
        })
    payload={
        "scope":"Version-2 nonlinear intended-location generator check with a preregistered delayed-interface tracking target. No blind enumeration or count-recovery claim.",
        "seed":SEED,
        "n_samples_after_burn_in":N,
        "results":results,
    }
    Path(__file__).with_name("Point-Sphere_Tier0_Nonlinear_v2.json").write_text(json.dumps(payload,indent=2)+"\n")
    print(json.dumps(payload,indent=2))

if __name__=="__main__":
    main()
