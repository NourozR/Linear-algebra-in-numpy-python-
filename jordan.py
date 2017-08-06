import numpy as np
from sympy import Matrix

# Matrix a (this is one example matrix from wiki page!!)
a = np.matrix([[5, 4, 2, 1], [0, 1, -1, -1], [-1, -1, 3, 0], [1, 1, -1, 2]])

# converting it for sympy library
m = Matrix(a)
print "Matrix a:", np.asarray(m)

# Decompostion to Normal jordan form
P, J = m.jordan_form()
print "J matrix:", np.asarray(J)
print "P matrix:", np.asarray(P) 

# Again Converting matrix for Numpy library
P_  = np.array(P)
J_ = np.array(J)
P_inv = np.array(P.inv())

# Recontruction of the matrix a. T is now same as a
T = np.dot(np.dot(P_, J_), P_inv)
print "Recontructed Matrix:", T

# Jordan Cells from matrix m
P, J_cells = m.jordan_cells()
print "All Jordan Cells:", J_cells

# Determining if we get a Nilpotent matrix
J3 = J_cells[2]
normal_form = np.dot(np.amax(np.diag(J3)),(np.identity(J3.shape[1])))
N = np.subtract(J3, normal_form)
N_ = Matrix(N)
print "Nilpotent matrix?:", N_.is_nilpotent()









