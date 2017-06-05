import numpy as np 

A = np.matrix([[2,1,3],[-1,0,2],[3,0,-2],[4,2,6]]) # clearly, 1st and 4th rows are linealy dependent
print "shape of A:", np.shape(A)

print "rank of A:", np.linalg.matrix_rank(A) # Rank = maximum number of independent columns/rows 

U,S,V = np.linalg.svd(A)
print "rank of singular vector U:", np.linalg.matrix_rank(U) # all columns of U are indendent vectors, so this should be 4