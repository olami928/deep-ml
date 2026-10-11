def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	n_features = len(vectors)
	n_obs = len(vectors[0])
	means = [sum(f) / n_obs for f in vectors]

	cov = [[0.0] * n_features for _ in range(n_features)]

	for i in range(n_features):
		for j in range(n_features):
			total = sum(
				(vectors[i][k] - means[i]) * (vectors[j][k] - means[j])
				for k in range(n_obs)
			)
			cov[i][j] = total / (n_obs - 1)

	return cov