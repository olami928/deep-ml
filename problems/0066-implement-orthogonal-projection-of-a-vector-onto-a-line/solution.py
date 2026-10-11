
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	v_dot_L = sum(vi * li for vi, li in zip(v, L))
	L_dot_L = sum(li * li for li in L)

	scale = v_dot_L / L_dot_L

	return [scale * li for li in L]