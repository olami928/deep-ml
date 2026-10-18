import numpy as np

def jacobian_matrix(f, x: list[float], h: float = 1e-5) -> list[list[float]]:
	"""
	Compute the Jacobian matrix using numerical differentiation.
	
	Args:
		f: Function that takes a list and returns a list
		x: Point at which to evaluate the Jacobian
		h: Step size for finite differences
	
	Returns:
		Jacobian matrix as list of lists
	"""
	# Your code here
	x = np.array(x, dtype=float)
	fx = np.array(f(x), dtype=float)

	m = len(fx)
	n = len(x)

	jacobian = np.zeros((m,n))

	for j in range(n):
		x_step = x.copy()
		x_step[j] += h
		f_step = np.array(f(x_step), dtype=float)

		jacobian[:,j] = (f_step - fx) / h

	return jacobian.tolist()