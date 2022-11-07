import sympy
from sympy.interactive.printing import init_printing
from sympy.matrices import Matrix
from sympy.physics.quantum import Operator
from sympy.physics.quantum import TensorProduct
init_printing(pretty_print=True)

#3a

sympy.pprint("3(a)")
sympy.pprint("\na\u00b5")
Aµ = Matrix([('a0'),('a1'), ('a2'), ('a3')])
sympy.pprint(Aµ)

sympy.pprint("\nb\u00b5")
Bµ= Matrix([('b0'),('b1'), ('b2'), ('b3')])
sympy.pprint(Bµ)

sympy.pprint("\naµ + bµ")
sum = Aµ + Bµ
sympy.pprint(sum)

sympy.pprint("\n")
def s(x,y):
    g = sympy.diag('1','-1','-1','-1')
    return x.dot(g*y)

sympy.pprint("\nS = aµbµ")
s = s(Aµ,Bµ)
sympy.pprint(s)

#3b
sympy.pprint("\n")
sympy.pprint("Matrix P")
p = Matrix([('E'),('Px'), ('0'), ('0')])
sympy.pprint(p)

sympy.pprint("\n")
sympy.pprint("Matrix Λ")
Λ = Matrix([('Y','-Y*B',0,0),('-B*Y','Y',0,0),(0,0,1,0),(0,0,0,1)])
sympy.pprint(Λ)
sympy.pprint("\nVerification Λ.p")
dot = Λ*p
sympy.pprint(dot)

