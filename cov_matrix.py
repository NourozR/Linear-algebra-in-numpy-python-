import numpy as np

# USING SVD to calculate COV matrix
def cov(X0):
    print "Matrix:"
    print X0
    X = X0 - X0.mean(axis=0) # matrix is centered
    U, s, V = np.linalg.svd(X, full_matrices = 0)
    C = np.dot(np.dot(V.T,np.diag(s**2)),V) # Using SVD 
    cov_mat = C/(X0.shape[0] - 1)
    print "Covariance Matrix:"
    print (cov_mat)

a = np.matrix([[1,2,0],[-2,3,-4],[5,3,-1], [7,-2,3]])
print cov(a)

# Calculating COV matrix from basic defination

def cov_easy(x):
	print "Matrix:"
	print x
	x_centered = x - x.mean(axis = 0) # matrix is centered
	cov_mat = np.dot(x_centered.T, x_centered)/(x.shape[0] - 1) # using defination of covariance matrix
	print "Covariance matrix:"
	print cov_mat

print cov_easy(a)	
