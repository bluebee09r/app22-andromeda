import sympy as sp
import math

from sympy.interactive.printing import init_printing
init_printing(use_unicode=False, wrap_line=False)
from sympy.matrices import Matrix, eye, zeros, ones, diag, GramSchmidt


#FORMATION OF MATRICES A AND B
print("FORMATION OF MATRICES A AND B")
print("\nMatrix A:")
A = Matrix([[1,2] , [3,3]])
B = Matrix([[20,20] , [10,10]])
sp.pprint(A)
print("Matrix B:")
sp.pprint(B)

#PRODUCG OF A AND B
C =A*B
print("\n\nPRODUCT OF A AND B")
sp.pprint(C)


#FIRST ELEMENT OF A
print("\n\nFIRST ELEMENT OF A")
sp.pprint(A[0])

#TRANSPOSE OF A
Trn = A.T
print("TRANSPOSE OF A")
sp.pprint(Trn)

#INVERSE OF A
A_inv = A.inv()
print("INVERSE OF A")
sp.pprint(A_inv)

#CHECK THE RESULT OF INVERSE OF A
A_ch = A_inv*A
print("CHECKING THE RESULT OF INVERSE OF A EXPLICITLY")
sp.pprint(A_ch)

#FORMATION OF PAULI MATRICES
from sympy import I
Px = Matrix([[0,1],[1,0]])
Py = Matrix([[0,-I],[I,0]])
Pz = Matrix([[1,0],[0,-1]])
sp.pprint(Px)
sp.pprint(Py)
sp.pprint(Pz)

#TRACES OF THE PAULI MATRICES
Tr_Px = Px.trace()
Tr_Py = Py.trace()
Tr_Pz = Pz.trace()
print("\n \nTRACES OF PAULI MATRICES")
sp.pprint(Tr_Px)
sp.pprint(Tr_Py)
sp.pprint(Tr_Pz)

#DETERMINANT OF THE PAULI MATRICES
D_Px = Px.det()
D_Py = Py.det()
D_Pz = Pz.det()
print("\n \nDETERMINANTS OF THE PAULI MATRICES")
print("Determinant of Px:")
sp.pprint(D_Px)
print("Determinant of Py:")
sp.pprint(D_Py)
print("Determinant of Pz:")
sp.pprint(D_Pz)

#ANTI-COMMUTATOR RELATION OF PAULI MATRICES
from sympy.matrices import Matrix
from sympy.physics.quantum import AntiCommutator
from sympy.physics.quantum import Operator
from sympy.physics.paulialgebra import Pauli
P1 = Operator(Pauli(1))
P2 = Operator(Pauli(2))
P3 = Operator(Pauli(3))

sp.pprint(P1)
sp.pprint(P2)
sp.pprint(P3)

print("WITH P1 AND P2")
print("{P1,P2}")
ac1 = AntiCommutator(P1,P2);
sp.pprint(ac1)
ac1.doit()
sp.pprint(ac1.doit())
acp1 = Pauli(1)*Pauli(2) + Pauli(2)*Pauli(1)
sp.pprint(acp1)


print("\n\nWITH P2 AND P3")
print("{P2,P3}")
ac2 = AntiCommutator(P2,P3);
sp.pprint(ac2)
ac2.doit()
sp.pprint(ac2.doit())
acp2 = Pauli(2)*Pauli(3) + Pauli(3)*Pauli(2)
sp.pprint(acp2)

print("\n\nWITH P3 AND P1")
print("{P3,P1}")
ac3 = AntiCommutator(P3,P1);
sp.pprint(ac3)
ac3.doit()
sp.pprint(ac3.doit())
acp3 = Pauli(3)*Pauli(1) + Pauli(1)*Pauli(3)
sp.pprint(acp3)

print("\n\nWITH P1 AND P1")
print("{P1,P1}")
ac11 = AntiCommutator(P1,P1)
ac11.doit()
sp.pprint(ac11.doit())
acp11 = Pauli(1)*Pauli(1) + Pauli(1)*Pauli(1)
sp.pprint(acp11)

print("\n\nWITH P2 AND P2")
print("{P2,P2}")
ac22 = AntiCommutator(P2,P2)
ac22.doit()
sp.pprint(ac22.doit())
acp22 = Pauli(2)*Pauli(2) + Pauli(2)*Pauli(2)
sp.pprint(acp22)

print("\n\nWITH P3 AND P3")
print("{P3,P3}")
ac33 = AntiCommutator(P3,P3)
ac33.doit()
sp.pprint(ac33.doit())
acp33 = Pauli(3)*Pauli(3) + Pauli(3)*Pauli(3)
sp.pprint(acp33)


