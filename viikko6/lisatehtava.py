from sympy.combinatorics import Permutation
from sympy.combinatorics.polyhedron import Polyhedron
from sympy.combinatorics.perm_groups import PermutationGroup

A = Permutation(123)
B = Permutation(132)
C = Permutation(124)
D = Permutation(142)
E = Permutation(134)
F = Permutation(143)
G = Permutation(234)
H = Permutation(243)
I = Permutation(12, 34)
J = Permutation(13, 24)
K = Permutation(14, 23)

PG = PermutationGroup(A, B, C, D, E, F, G, H, I, J, K)

print(PG)