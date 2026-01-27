#---Adition ---#

import numpy as np
x = np.array([[1, 2]
              ,[3, 4]])
y = np.array([[5, 6]
              ,[7, 8]])
print(x + y)

#---Subtraction ---#
print(x - y)

#---Multiplication(Array Form) ---#
print(x * y)

#---Multiplication(Matrix Form) ---#
print(x @ y)

#---Division ---#
print(y / x)

#---Exponentiation ---#
print(y ** x)

#---Modulus ---#
print(y % x)

#---Transpose ---#
print(x.transpose())
print(y.T)
