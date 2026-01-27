import numpy as np
a = np.array([[[1, 2], [4, 5]],
              [[8, 9], [11, 12]]])
b = np.array([[[7, 3], [10, 11]],
              [[13, 9], [11, 12]]])

print("Array a:", a)
print("Array b:", b)

# Addition
print("Addition:\n", a + b)

# Subtraction
print("Subtraction:\n", a - b)

# Multiplication
print("Multiplication:\n", np.matmul(a, b))
# print("Multiplication:\n", np.dot(a, b))  # Alternative syntax

# Division
print("Division:\n", b / a)

# Transpose
print("Transpose of a:\n", a.transpose())
print("Transpose of b:\n", b.T)
