import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	if mode == "row":
		return list(np.mean(matrix, axis=1))
	elif mode == "column":
		return list(np.mean(matrix, axis=0))
	else:
		return "Operation not supported"