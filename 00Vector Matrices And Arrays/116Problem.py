#  Adding and Subtracting Matrices

# Load the library
import numpy as np

# Create matrix
matrix_a = np.array([[1, 1, 1],
                     [1, 1, 1],
                     [1, 1, 2]])
# Create matrix
matrix_b = np.array([[1, 3, 1],
                     [1, 3, 1],
                     [1, 3, 8]])

# add
print(np.add(matrix_a, matrix_b))

# subtract
print(np.subtract(matrix_a, matrix_b))
