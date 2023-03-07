import numpy as np


def invert_matrix(matrix: np.ndarray) -> np.ndarray:
    """
    Returns the inverse of the input matrix using NumPy and Linear Algebra libraries.
    If the input matrix is not invertible, raises a ValueError with an appropriate error message.

    Args:
        matrix: A NumPy matrix to be inverted.

    Returns:
        The inverse of the input matrix as a NumPy matrix.

    Raises:
        ValueError: If the input matrix is not invertible.
    """
    try:
        det = np.linalg.det(matrix)
        if det == 0:
            raise ValueError("Matrix is not invertible")
        return np.linalg.inv(matrix)
    except np.linalg.LinAlgError as e:
        raise ValueError("Matrix is not invertible: {}".format(e))
