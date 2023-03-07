# Matrix Inversion

### TODO

Write a Python function `invert_matrix(matrix)` that takes a NumPy matrix as input and returns the inverse of the matrix. If the input matrix is not invertible, the function should raise a `ValueError` with an appropriate error message.

### Example Input

```python
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[1, 0, 0],
              [0, 2, 0],
              [0, 0, 3]])

C = np.array([[1, 2],
              [3, 4]])

D = np.array([[1, 2, 3],
              [4, 5, 6]])

invert_matrix(A)  # should return:
# array([[-0.5       ,  1.        , -0.5       ],
#        [ 1.        , -2.        ,  1.        ],
#        [-0.5       ,  1.        , -0.5       ]])

invert_matrix(B)  # should return:
# array([[1.        , 0.        , 0.        ],
#        [0.        , 0.5       , 0.        ],
#        [0.        , 0.        , 0.33333333]])

invert_matrix(C)  # should return:
# array([[-2. ,  1. ],
#        [ 1.5, -0.5]])

invert_matrix(D)  # should raise a ValueError with the message "Matrix is not invertible"
```