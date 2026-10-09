import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute the rank of a matrix.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero
    
    Returns:
        The rank of the matrix (integer)
    """
    A = np.array(A, dtype=float)

    if A.ndim != 2 or A.size == 0:
        return 0

    m, n = A.shape
    row = 0

    for col in range(n):
        if row >= m:
            break
        pivot = row + np.argmax(np.abs(A[row:, col]))

        if abs(A[pivot, col]) <= tol:
            continue 

        A[[row, pivot]] = A[[pivot, row]]

        for r in range(row + 1,m):
            factor = A[r, col] / A[row, col]

            A[r, col:] -= factor * A[row, col:]

        row += 1
    return row
