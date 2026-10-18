import numpy as np
def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	# Your code here
	sigmoid = 1 / (1 + np.exp(-x))
	sigmoid_derivative = sigmoid * (1 - sigmoid)

	tanh = np.tanh(x)
	tanh_derivative = 1 - tanh**2

	if x > 0:
		ReLU = 1.0
	else:
		ReLU = 0.0

	return {
		'sigmoid': sigmoid_derivative,
		'tanh': tanh_derivative,
		'relu': ReLU
	}