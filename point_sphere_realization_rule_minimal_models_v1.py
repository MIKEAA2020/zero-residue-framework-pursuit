#!/usr/bin/env python3
"""Frozen R1b realization-rule toy-family diagnostic."""
from __future__ import annotations
import json
from pathlib import Path

OMEGA=[0,1,2,3]


def action(k,x): return (x+k)%4


def main():
    # D: displayed f(E)=0. Relabel with a permutation to show the output is not
    # label-independent unless f itself is supplied by a derivation.
    f_output=0
    relabel={0:2,1:0,2:3,3:1}
    d={
        'realized_set':[f_output], 'realized_size':1,
        'relabelled_displayed_output':relabel[f_output],
        'diagnostic':'A unique output follows only after supplying f. The label 0 has no invariant privilege under relabelling.'
    }
    # O: finite C4 orbit and its unique invariant uniform distribution.
    orbit=sorted({action(k,0) for k in range(4)})
    measure={str(x):1/len(orbit) for x in orbit}
    invariant=all(measure[str(action(k,x))]==measure[str(x)] for k in range(4) for x in orbit)
    o={
        'orbit':orbit,'orbit_size':len(orbit),'finite_invariant_uniform_measure':measure,
        'measure_is_C4_invariant':invariant,
        'gauge_reading_quotient_size':1,
        'substantive_reading_distinct_totality_count':len(orbit),
        'diagnostic':'The same formal orbit is one totality on the gauge reading and four only on a separately declared substantive-distinctness reading.'
    }
    # C: fixed E and varying q.
    c={'selector_variants':{str(q):[q] for q in OMEGA},'distinct_outputs_with_fixed_E':len(OMEGA),
       'diagnostic':'With E held fixed, q changes the output. q is an indispensable extra selection parameter in this family.'}
    noncompact={
        'group':'Z acting on Z by translation',
        'equal_point_mass_argument':[
            'Translation invariance gives every integer the same point mass p.',
            'If p>0, the countable total mass diverges.',
            'If p=0, countable additivity gives total mass 0 rather than 1.'
        ],
        'normalized_translation_invariant_probability_exists':False,
        'diagnostic':'Finite-orbit uniformity does not generalise automatically to a non-compact/infinite orbit.'
    }
    payload={'scope':'R1b frozen toy-family diagnostic. It diagnoses formal costs and does not decide metaphysical truth, physics, or probability.',
             'specification':'Point-Sphere_Realization_Rule_Minimal_Model_Families_v1_Specification.md',
             'common_domain':OMEGA,'C_Nec_D':d,'C_Nec_O':o,'C_Cont':c,'noncompact_warning':noncompact,
             'all_required_diagnostics_complete':bool(invariant and o['gauge_reading_quotient_size']==1 and len(c['selector_variants'])==4 and not noncompact['normalized_translation_invariant_probability_exists'])}
    Path(__file__).with_name('Point-Sphere_Realization_Rule_Minimal_Model_Families_v1.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps(payload,indent=2))
if __name__=='__main__':main()
