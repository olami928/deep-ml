import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
    # Your code here

    X = np.array(features, dtype=float)
    y = np.array(labels, dtype=float)
    weights = np.array(initial_weights, dtype=float)
    bias = float(initial_bias)

    mse_values = []

    for epoch in range(epochs):
        z = np.dot(X, weights) + bias
        predictions = 1 / (1 + np.exp(-z))

        errors = predictions - y
        mse = np.mean(errors ** 2)
        mse_values.append(mse)

        delta = 2 * errors * predictions * (1 -predictions)
        dw = np.mean(delta[:, None] * X, axis=0)
        db = np.mean(delta)

        weights -= learning_rate * dw
        bias -= learning_rate * db

    return (
            np.round(weights, 4).tolist(),
            np.round(bias, 4).tolist(),
            np.round(mse_values, 4).tolist()
        )