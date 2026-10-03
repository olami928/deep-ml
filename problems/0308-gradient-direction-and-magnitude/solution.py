import numpy as np
from numpy import linalg

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	gradient = np.array(gradient)
	magnitude = linalg.norm(gradient)
	if magnitude == 0:
		direction = np.zeros_like(gradient)
	else:
		direction  = gradient / magnitude

	return {
		"magnitude": magnitude,
		"direction": direction,
		"descent_direction": -direction
	}