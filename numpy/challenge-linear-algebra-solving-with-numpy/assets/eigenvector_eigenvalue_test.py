import sys

sys.path.append("/home/labex/project")

import unittest
import numpy as np

from eigenvector_eigenvalue import eigenvector_eigenvalue

class TestMatrixInversion(unittest.TestCase):
    def test_eigenvector_eigenvalue(self):
        A = np.array([[1, 2], [2, 1]])
        eigvals, eigvecs = eigenvector_eigenvalue(A)
        self.assertTrue(np.allclose(eigvecs @ np.diag(eigvals) @ np.linalg.inv(eigvecs), A))


if __name__ == '__main__':
    unittest.main()