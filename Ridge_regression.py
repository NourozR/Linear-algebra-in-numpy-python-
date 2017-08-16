import numpy as np
from sklearn.preprocessing import StandardScaler

# HIGHLY CORRELATED INPUT
x = np.matrix([[1,2,1], [2,4,2],[3,6,3], [4,7,3],
	           [5,7,2], [6,7,1],[7,8,1],[8,10,2],
	           [9,13,4],[10,13,3]]) 
y = np.matrix([3,9,11,15,13,13,17,21,24,28]).T

# SCALING IS A MUST CONDITION FOR RIDGE REGRESSION
x = StandardScaler().fit_transform(x)
y = StandardScaler().fit_transform(y)

# CALCULATING W MATRIX FOR REGRESSION
w = np.dot(np.linalg.inv(np.dot(x.T,x)), np.dot(x.T,y))

# ESTIMATION OF Y
y_est = np.dot(x,w)

# FUNCTION TO CALCULATE RMSE(ROOT MEANS SQUARE ERROR)
def rmse(y, y_est):

	rmse = np.sqrt(np.mean(np.square(y - y_est)))
	return rmse

# REGULARIZATION PARAMETER
reg_param = 0.1

# CALCULATION OF W FOR RIDGE REGRESSION: w = (x'x + lamda^2*I)^-1x'y
w_ridge = np.dot(np.linalg.inv((np.dot(x.T,x)) + (reg_param**2)*np.identity(3)), np.dot(x.T,y))

# ESTIMATION OF Y FOR RIDGE REGRESSION
y_est_ridge = np.dot(x, w_ridge)

# RMSE FOR BOTH METHODS
rmse_ = rmse(y, y_est)
rmse_ridge = rmse(y, y_est_ridge)
print "RMSE FOR REGRESSION:", rmse_ # THIS IS 0.9363
print "RMSE FOR RIDGE REGRESSION:", rmse_ridge # THIS IS 0.1731

# DATA SET WAS SMALL, SO VERY HIGH CORRELATION IS USED HERE
# HOWEVER, IF DATASET IS BIG AND HIGH CORRELATION AMONG DATA IS PRESENT,
# THE SAME METHOD COULD BE USED FOR BETTER RMSE! 







