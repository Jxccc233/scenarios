import sys

sys.path.append("/home/labex/project")

import unittest
import numpy as np

from matrix_rank import matrix_rank

class TestMatrixInversion(unittest.TestCase):
    def test_matrix_rank(self):
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        C = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
        self.assertEqual(matrix_rank(A), 2)
        self.assertEqual(matrix_rank(B), 2)
        self.assertEqual(matrix_rank(C), 2)




if __name__ == '__main__':
    unittest.main()