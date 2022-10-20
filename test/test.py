import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


# Creating a numpy array with 4 elements:
l = np.array([1,2,3,4])
print(f"My array: {l}")


# Creating and pretty-printing matrices with sympy
sp.init_printing(pretty_print=True)

v = sp.Matrix([0,1,2])
print("\nVector")
sp.pprint(v)

print("\nMatrix:")
M = sp.Matrix([[1, 2, 3], [3, 2, 1]])
sp.pprint(M)

B = M*v
print("\nMatrix X Vector:")
sp.pprint(B)


# Creating Gaussian distributed random numbers
# using numpy and plot them using matplotlib
np.random.seed(1)
x = np.random.normal(125, 4, 1000)

fig, ax = plt.subplots()
ax.hist(x, bins=10, linewidth=0.5, edgecolor="white")
ax.set_xlabel('Entries')
plt.show()
plt.savefig('normal_distr.pdf')
