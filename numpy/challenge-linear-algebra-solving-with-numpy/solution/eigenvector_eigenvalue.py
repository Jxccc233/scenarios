import numpy as np

def eigenvector_eigenvalue(matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Calculates the eigenvectors and eigenvalues of the input matrix using NumPy and Linear Algebra libraries.

    Args:
        matrix: A NumPy matrix for which to calculate eigenvectors and eigenvalues.

    Returns:
        A tuple of two NumPy arrays: eigenvectors and eigenvalues.
    """
    return np.linalg.eig(matrix)