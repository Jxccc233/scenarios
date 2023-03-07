import sys

sys.path.append("/home/labex/project")

import unittest
import numpy as np

from determinant_matrix import determinant_matrix

class TestMatrixInversion(unittest.TestCase):
    def test_determinant_matrix(self):
        A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        B = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
        self.assertEqual(determinant_matrix(A), -0.0)
        self.assertEqual(determinant_matrix(B), 6.0)

if __name__ == '__main__':
    unittest.main()