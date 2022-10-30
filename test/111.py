import sympy
from sympy.interactive.printing import init_printing
init_printing(use_unicode=False, wrap_line=False,pretty_print=True)
from sympy.matrices import Matrix
from sympy.physics.quantum import AntiCommutator
from sympy.physics.quantum import Operator
from sympy.physics.paulialgebra import Pauli
A = Operator('A')
B = Operator('B')

print("Matrix A")
A = Matrix([(1,2),(3,3)])
sympy.pprint(A)
print("\n")
print("Matrix B")
B = Matrix([[20,20],[10,10]])
sympy.pprint(B)
print("\n")
print("Matrix Product of A and B")
sympy.pprint(A*B)
print("\n")

print("Element A^01 of the Matrix A")
sympy.pprint(A[1])
print("\n")
print("Transpose of Matrix A")
sympy.pprint(A.T)
print("\n")

print("Inverse of Element A")
Ai = A.inv()
sympy.pprint(Ai)
print("\n")

print("Verification")
sympy.pprint(A*Ai)
print("\n")

print("Pauli Matrices")
print("\n")
print("Sigma1")
P1 = Matrix([[0,1],[1,0]])
sympy.pprint(P1)
print("\n")
print("Trace of Sigma1 Pauli Matrix")
P1T = P1.trace()
sympy.pprint(P1T)
print("\n")

print("Sigma2")
from sympy import I
P2 = Matrix([[0,-I], [I,0]])
sympy.pprint(P2)
print("\n")
print("Trace of Sigma2 Pauli Matrix")
P2T = P2.trace()
sympy.pprint(P2T)
print("\n")
print("Sigma3")
P3 = Matrix([[1,0],[0,-1]])
sympy.pprint(P3)
print("\n")
print("Trace of Sigma3 Pauli Matrix")
P3T = P3.trace()
sympy.pprint(P3T)

#DETERMINANT
print("\n")
print("Determinant of Sigma Matrices")
print("\n")
D1 = sympy.det(P1)
sympy.pprint(D1)
print("\n")
D2 = sympy.det(P2)
sympy.pprint(D2)
print("\n")
D3 = sympy.det(P3)
sympy.pprint(D3)
print("\n")
#Anticommutator
print("Verification of Anticommutator Relation")
print("\n")
pa1 = Pauli(1)
pa2 = Pauli(2)
pa3 = Pauli(3)
print("\n")
paa1 = Operator (pa1)
paa2 = Operator (pa2)
paa3 = Operator (pa3)
print("Anticommutator of sigma1 and sigma2")
ac = AntiCommutator(paa1,paa2); ac
{paa1,paa2}
ac.doit()
sympy.pprint(ac.doit())
acp1 = Pauli(1)*Pauli(2) + Pauli(2)*Pauli(1)
sympy.pprint(acp1)
print("\n")
print("Anticommutator of sigma2 and sigma3")
ac2 = AntiCommutator(paa2,paa3);ac2
{paa2,paa3}
ac2.doit()
sympy.pprint(ac2.doit())
acp2 = Pauli(2)*Pauli(3) + Pauli(3)*Pauli(2)
sympy.pprint(acp2)
print("\n")
print("Anticommutator of sigma1 and sigma3")
ac3 = AntiCommutator(paa1,paa3);ac3
{paa1,paa3}
ac3.doit()
sympy.pprint(ac3.doit())
acp3 = Pauli(1)*Pauli(3) + Pauli(3)*Pauli(1)
sympy.pprint(acp3)
print("\n")
print("Anticommutator of sigma1 and sigma1")
ac11 = AntiCommutator(paa1,paa1);ac11
{paa1,paa1}
ac11.doit()
sympy.pprint(ac11.doit())
acp11 = Pauli(1)*Pauli(1) + Pauli(1)*Pauli(1)
sympy.pprint(acp11)
print("\n")
print("Anticommutator of sigma2 and sigma2")
ac22 = AntiCommutator(paa2,paa2);ac22
{paa2,paa2}
ac22.doit()
sympy.pprint(ac22.doit())
acp22 = Pauli(2)*Pauli(2) + Pauli(2)*Pauli(2)
sympy.pprint(acp22)
print("\n")
print("Anticommutator of sigma3 and sigma3")
ac33 = AntiCommutator(paa3,paa3);ac33
{paa3,paa3}
ac33.doit()
sympy.pprint(ac33.doit())
acp33 = Pauli(3)*Pauli(3) + Pauli(3)*Pauli(3)
sympy.pprint(acp33)