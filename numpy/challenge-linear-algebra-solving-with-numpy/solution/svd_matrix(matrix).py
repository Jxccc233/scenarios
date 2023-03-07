import numpy as np


def svd_matrix(matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Performs Singular Value Decomposition (SVD) on the input matrix using NumPy and Linear Algebra libraries.

    Args:
        matrix: A NumPy matrix for which to perform SVD.

    Returns:
        A tuple of three NumPy matrices: U, S, and V, such that matrix = U * S * V.T
    """
    return np.linalg.svd(matrix)