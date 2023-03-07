import sys

sys.path.append("/home/labex/project")

import unittest
import numpy as np

from svd_matrix import svd_matrix


class TestMatrixInversion(unittest.TestCase):
    def test_svd_matrix(self):
            A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            U, S, V = svd_matrix(A)
            self.assertTrue(np.allclose(U @ np.diag(S) @ V, A))


if __name__ == '__main__':
    unittest.main()