import sys

sys.path.append("/home/labex/project")

import unittest
import numpy as np

from solve_linear_equation import solve_linear_equation

class TestMatrixInversion(unittest.TestCase):
  def test_solve_linear_equation(self):
        A = np.array([[1, 2], [3, 4]])
        b = np.array([5, 6])
        self.assertTrue(np.allclose(solve_linear_equation(A, b), np.array([-4., 4.5])))
        with self.assertRaises(ValueError):
            solve_linear_equation(np.array([[1, 2, 3], [4, 5, 6]]), b)
        with self.assertRaises(ValueError):
            solve_linear_equation(A, np.array([5, 6, 7]))




if __name__ == '__main__':
    unittest.main()