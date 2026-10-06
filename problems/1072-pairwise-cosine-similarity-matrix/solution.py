import numpy as np

def pairwise_cosine_similarity(X):
    # Your code here
    norm = np.linalg.norm(X, axis=1, keepdims=True)

    x_norm = X / ( norm + 1e-8)

    similarity = x_norm @ x_norm.T

    return similarity