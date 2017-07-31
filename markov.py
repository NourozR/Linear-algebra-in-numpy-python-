# A general Introduction to Markov Matrix and It's relationship with Eigen Decomposition

import numpy as np 

# Our probabilty Matrix ( Taking transpose for computational simplicity)
P = (np.matrix([[0.8, 0.15, 0.05], [0.12, 0.7, 0.18],[0.08, 0.22, 0.7]])).T

# This is initial state of the system
X0 = np.matrix([0.25, 0.45, 0.30])

# First Three States of the system 
X1 = X0.dot(P)
X2 = X1.dot(P)
X3 = X2.dot(P)
print "State 1:", X1
print "State 2:", X2
print "State 3:", X3

# Eigen Decomposition of P matrix
[S,U] = np.linalg.eig(P)
print "Eigen Vals:", S
print "Eigen Vectors:", U

# The Eigenvector corresponding to Eigenval 1 refers to the final state of the system
# Using the relation between Eigenvectors and Markov Matrix
final_state = (abs(U[:,0:1])/(abs(np.sum(U[:,0:1])))).T
print "Final State Using ED:", final_state

# From final state the statbe system calculation
stable_system = np.reshape(np.repeat(final_state,3), (3,3))
print "Stable system using ED:", stable_system

# Stable system calculation using matrix power
stable_system_p = np.linalg.matrix_power(P, 100)
print "Stable System Using Matrix Power:", stable_system_p

# Final State Calculation usinf Matrix Power
final_state_p = (stable_system_p[:,0:1]).T
print "Final State using matrix power:", final_state_p







