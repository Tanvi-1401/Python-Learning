# 3D Matrices (Depth × Rows × Columns)
A = [[[1, 2], [3, 4]],
     [[5, 6], [7, 8]]]

B = [[[8, 7], [6, 5]],
     [[4, 3], [2, 1]]]

depth = len(A)
rows = len(A[0])
cols = len(A[0][0])

# ---------------- ADDITION ----------------
add = []
for d in range(depth):
    layer = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[d][i][j] + B[d][i][j])
        layer.append(row)
    add.append(layer)

# ---------------- SUBTRACTION ----------------
sub = []
for d in range(depth):
    layer = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[d][i][j] - B[d][i][j])
        layer.append(row)
    sub.append(layer)

# ---------------- TRANSPOSE ----------------
transpose = []
for d in range(depth):
    layer = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(A[d][i][j])
        layer.append(row)
    transpose.append(layer)

# ---------------- MULTIPLICATION ----------------
mul = []
for d in range(depth):
    layer = []
    for i in range(rows):
        row = []
        for j in range(cols):
            s = 0
            for k in range(cols):
                s += A[d][i][k] * B[d][k][j]
            row.append(s)
        layer.append(row)
    mul.append(layer)

# ---------------- OUTPUT ----------------

# print("\nAddition:")
# for d in range(depth):
#     print("Layer", d)
#     for row in add[d]:
#         print(row)
#     print()


print("Addition:", add)
print("Subtraction:", sub)
print("Transpose:", transpose)
print("Multiplication:", mul)