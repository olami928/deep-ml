def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	new_mat = []
	if len(a) != len(b):
		return -1
	else:
		for i in range(len(a)):
			new_mat.append(a[i] + b[i]) 

	return new_mat
