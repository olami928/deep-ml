import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	# Your code here
	value = x
	derivative = 1.0

	for func in reversed(functions):
		if func == "square":
			local_derivative = 2 * value
			value = value **2
		elif func == "sin":
			local_derivative = np.cos(value)
			value = np.sin(value)
		elif func == 'exp':
			value = np.exp(value)
			local_derivative = value
		elif func == 'log':
			local_derivative = 1 / value
			value = np.log(value)
		else:
			raise ValueError(f"Unknown function: {func}")
		derivative *= local_derivative
	return derivative
