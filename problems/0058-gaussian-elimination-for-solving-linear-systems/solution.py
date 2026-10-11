import numpy as np

def gaussian_elimination(A, b):
	"""
	Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
	:param A: Coefficient matrix
	:param b: Right-hand side vector
	:return: Solution vector x
	"""
	A = np.array(A, dtype=float)
	b = np.array(b, dtype=float)
	n = len(b)

	for k in range(n):

		p = k + np.argmax(np.abs(A[k:, k]))

		if p != k:
			A[[k, p]] = A[[p, k]]

			b[[k, p]] = b[[p, k]]

		for i in range(k + 1, n):
			factor = A[i, k] / A[k, k]
			A[i, k:] -= factor * A[k, k:]
			b[i] -= factor * b[k]
	x = np.zeros(n)
	for i in range(n - 1, -1, -1):
		x[i] = (b[i] - A[i, i+1:] @ x[i+1:]) / A[i,i]

	return x