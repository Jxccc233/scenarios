## Sub-Challenge: Matrix Rank Calculation

### TODO

Write a Python function `matrix_rank(matrix)` that takes a NumPy matrix as input and calculates its rank. The function should return the rank of the matrix as an integer.

### Example Input

```python
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

C = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]])

matrix_rank(A)  # should return 2

matrix_rank(B)  # should return 2

matrix_rank(C)  # should return 2
```
