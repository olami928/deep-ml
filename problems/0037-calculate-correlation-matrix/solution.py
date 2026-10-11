import numpy as np

def calculate_correlation_matrix(X, Y=None):
	# Your code here 
	X = np.array(X, dtype=float)

	if Y is None:
		Y = X
	else:
		Y = np.array(Y, dtype=float)

	n = X.shape[0]
	X_centered = X - X.mean(axis=0)
	Y_centered = Y - Y.mean(axis=0)

	cov = X_centered.T @ Y_centered / (n - 1)

	x_std = X.std(axis=0, ddof=1)
	y_std = Y.std(axis=0, ddof=1)

	return cov / np.outer(x_std, y_std)