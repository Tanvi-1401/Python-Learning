import numpy as np

x = np.array([
    [11, 33, 55],
    [22, 44, 66],
    [77, 14, 7]
])

print("Sorting row wise:\n ",np.sort(x))
# print("Sorting row wise:\n ",np.sort(x, axis=1))
print("Sorting column wise:\n ",np.sort(x, axis=0))

print("Sorting indexing row wise:\n ", np.argsort(x, axis=1))
print("Sorting indexing column wise:\n ", np.argsort(x, axis=0))

#--- FOR 1D ARRAY REVERESE CONCEPT IN SORTING ---#
y = np.array([11, 33, 55, 22, 44, 66, 77, 14, 7])
print("1D Array Sorting:\n ", np.sort(y)[::-1])
print("1D Array Sorting Indexing:\n ", np.argsort(y)[::-1])
