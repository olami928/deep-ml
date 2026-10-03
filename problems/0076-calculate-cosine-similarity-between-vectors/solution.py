import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	result = 0
	a = 0
	b = 0
	c = 0
	if len(v1) != len(v2) or v1.ndim != v2.ndim:
		return -1

	for i in range(len(v1)):
		a += (v1[i]) * (v2[i])
	for i in range(len(v1)):
		b += v1[i]**2
	b = np.sqrt(b)
	
	for i in range(len(v2)):
		c += v2[i]**2
	c = np.sqrt(c)

	result = a / (b * c)

	return result

