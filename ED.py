import numpy as np 

a = np.matrix([[2,3,5,2], [1,0,1,4], [4,3,0,1], [2,3,1,6]])
print "given matrix: \n", a
print "\n"
# EIGENVALUE AND EIGENVECTORS OF MATRIX a

eig_val, eig_vect = np.linalg.eig(a)
print "eigen_values:\n", eig_val
print "\n"
print "eigen vectors: \n", eig_vect

# RECONSTRUCT MATRIX  a FROM ITS EIGENVALUES AND EIGENVECTORS

z = eig_vect.dot(np.diag(eig_val)).dot(np.linalg.inv(eig_vect))
print "\n"
print "reconstructed matrix: \n" ,z  # z matrix SHOULD BE SAME AS matrix a

# CUBE OF matrix a
a_3 = np.linalg.matrix_power(a,3)
print "\n"
print "cube of matrix a: \n", a_3

# CALCULATING POWER OF A MATRIX USING ONLY ITS EIGENVALUES AND EIGENVECTORS

a_magic_3 = eig_vect.dot(np.linalg.matrix_power(np.diag(eig_val), 3)).dot(np.linalg.inv(eig_vect))
print "cube of matrix using only eigvals/eigvects: \n", a_magic_3
is_identity = a_3.dot(np.linalg.inv(a_magic_3))
print "\n", is_identity









