#!/usr/bin/env python3
"""Execute frozen R1c matched admissibility-family diagnostic."""
from __future__ import annotations
import itertools,json,math
from pathlib import Path

OMEGA=(0,1,2,3)
S4=list(itertools.permutations(OMEGA))

def image(subset,perm): return frozenset(perm[x] for x in subset)
def full_invariant(subset): return all(image(subset,p)==frozenset(subset) for p in S4)

def main():
    d0=frozenset({0})
    d1={str(m):{'realized_set':[m],'S4_invariant':full_invariant({m})} for m in OMEGA}
    # c4 generator (0 1 2 3), its orbit from 0 is all Omega.
    c4_orbit=frozenset(OMEGA)
    uniform={str(x):1/4 for x in OMEGA}
    # H={identity,(01)(23)}.
    h_orbit=frozenset({0,1})
    c={str(q):{'realized_set':[q],'S4_invariant':full_invariant({q})} for q in OMEGA}
    payload={
      'scope':'Frozen R1c toy diagnostic of genuine primitive structure. No metaphysical ranking or physics claim.',
      'specification':'Point-Sphere_Realization_Rule_Admissibility_Families_v1_Specification.md',
      'common_domain':list(OMEGA),'full_symmetry_group_size':len(S4),
      'D0_bare_determinate':{'realized_set':sorted(d0),'S4_invariant':full_invariant(d0),
                              'diagnostic':'A bare singleton is not invariant under the declared full symmetry.'},
      'D1_marker_determinate':{'variants':d1,'marker_value_count':4,'marker_choice_bits':math.log2(4),
                                'diagnostic':'Changing m changes the output while common-domain structure stays fixed.'},
      'O0_full_transitive_orbit':{'realized_set':sorted(c4_orbit),'orbit_size':4,'S4_invariant':full_invariant(c4_orbit),
                                  'finite_uniform_measure':uniform,'measure_normalized':sum(uniform.values())==1,
                                  'diagnostic':'The full orbit is symmetry-natural in the toy; the chosen C4 action remains a declared belt bridge.'},
      'O1_restricted_orbit':{'subgroup':'{e,(01)(23)}','seed':0,'realized_set':sorted(h_orbit),'orbit_size':2,
                             'S4_invariant':full_invariant(h_orbit),'subgroup_partition':'{0,1}|{2,3}',
                             'diagnostic':'The restricted orbit requires both subgroup/partition structure and a seed; it is not invariant under the full common symmetry.'},
      'C_selector':{'variants':c,'selector_value_count':4,'selector_choice_bits':math.log2(4),
                    'diagnostic':'Changing q changes the output while E/common-domain structure stays fixed.'},
      'all_required_diagnostics_complete':True
    }
    Path(__file__).with_name('Point-Sphere_Realization_Rule_Admissibility_Families_v1.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps(payload,indent=2))
if __name__=='__main__':main()
