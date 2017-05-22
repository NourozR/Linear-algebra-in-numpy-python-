# SINGULAR VALUE DECOMPOSITION IN NUMPY

import numpy as np 
import math

a = np.matrix([[-2,1,4,5], [2,0,4,-2], [3,0,9,-1]])
U, E, V = np.linalg.svd(a)
print "U:" , U
print "E:" , E
print "V:" , V

# LET'S FINDOUT THE AMAZING CHARACTERISTICS OF SVD

x1 = U.dot(U.T)
x2 = V.dot (V.T)

print "x1:", x1 # This should be a 3*3 identity matrix
print "x2:" , x2 # This should be a 4*4 identity matrix

# CALCULATING INVERSE MATRIX FROM SVD

b = np.matrix([[-2,1,4,5], [2,0,4,-2], [3,0,9,-1],[-2,7,0,3]])
b_inv = np.linalg.inv(b)
print "b_inv:", b_inv 
U_b, E_b, V_b = np.linalg.svd(b)
print "U_b:" , U_b
print "E_b:" , E_b
print "V_b:" , V_b

z = (V_b.T).dot(np.diag(np.reciprocal(E_b))).dot(U_b.T)
print "z:", z
print "b_inv:", b_inv

# VALIDATION OF INVERSE MATRIX
print z.dot(np.linalg.inv(b_inv))
 
# CALCULATING EIGENVECTORS AND EIGENVALUES FROM  SVD 

print np.linalg.eigvals(b)
print E_b
b_b = b.dot(b.T)
print b_b
print np.sqrt(np.linalg.eigvals(b_b))

