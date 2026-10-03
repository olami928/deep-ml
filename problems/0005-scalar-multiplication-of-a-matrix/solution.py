def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	new_list = [[0]* len(matrix[0]) for _ in range(len(matrix))]

	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			new_list[i][j] = scalar * matrix[i][j]

	return new_list