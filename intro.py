# CALCULATING ANGLE BETWEEN TWO VECTORS
import numpy as np 
import math
a = np.array([1, 2, 3,0])
b = np.array([4,5,6,7])

cosine_angle = a.dot(b)/(np.linalg.norm(a)*np.linalg.norm(b))
print np.arccos(cosine_angle)*180/math.pi

# TRANSPOSE AND MULTIDIMENTIONAL ARRAY/MATRIX
c = np.array([[1,2,3,4], [8,4,2,0], [4,0,3,2]])
print c.dot(c.T)

# RANDOM NUMBER GENERATION FROM GAUSSIAN DISTRIBUTION
d = np.random.randn(100,100)
print d, d.mean(), d.var()

# INVERSE MATRIX CALCULATION AND VALIDATION
e = np.array([[1,8,0], [3,-2,1], [7,0,-2]])
inverse_matrix = np.linalg.inv(e)
print inverse_matrix
print e.dot(inverse_matrix)
print inverse_matrix.dot(e)








