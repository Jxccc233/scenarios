## Sub-Challenge: Linear Equation Solver

### TODO

Write a Python function `solve_linear_equation(A, b)` that takes two NumPy matrices A and b as input and solves the linear equation Ax = b using matrix inversion. The function should return the solution x as a NumPy array. If the matrix A is not invertible or the dimensions of A and b do not match, the function should raise a `ValueError` with an appropriate error message.

### Example Input

```python
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

b = np.array([5, 6])

solve_linear_equation(A, b)  # should return array([-4. ,  4.5])
```
