import sys

sys.path.append("/home/labex/project")

import unittest
import numpy as np

from invert_matrix import invert_matrix

class TestMatrixInversion(unittest.TestCase):
    def test_invert_matrix(self):
        A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        B = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
        C = np.array([[1, 2], [3, 4]])
        D = np.array([[1, 2, 3], [4, 5, 6]])
        self.assertTrue(np.allclose(invert_matrix(A), np.array([[-0.5, 1., -0.5], [1., -2., 1.], [-0.5, 1., -0.5]])))
        self.assertTrue(np.allclose(invert_matrix(B), np.array([[1., 0., 0.], [0., 0.5, 0.], [0., 0., 0.33333333]])))
        self.assertTrue(np.allclose(invert_matrix(C), np.array([[-2., 1.], [1.5, -0.5]])))
        with self.assertRaises(ValueError):
            invert_matrix(D)
            
if __name__ == '__main__':
    unittest.main()