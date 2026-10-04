def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	# Your code here
	
	outcomes = range(1, n+1)

	mean = sum(outcomes) / n

	sum_diff = [(value - mean) **2 for value in outcomes]

	standard_deviation = sum(sum_diff) / n

	return (mean, standard_deviation)