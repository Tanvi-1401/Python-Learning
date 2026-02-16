import math

def encrypt(text, key):
    col = len(key)
    row = math.ceil(len(text) / col)

    # Padding with X
    text += 'X' * (row * col - len(text))

    # Create matrix row-wise
    matrix = []
    k = 0
    for i in range(row):
        matrix.append(list(text[k:k+col]))
        k += col

    print("\nMatrix Form:")
    print(" ".join(key))   # print key above columns
    for r in matrix:
        print(" ".join(r))

    # Arrange columns based on key order
    cipher = ""
    key_order = sorted(list(key))

    for num in key_order:
        col_index = key.index(num)
        for r in range(row):
            cipher += matrix[r][col_index]

    return cipher


def decrypt(cipher, key):
    col = len(key)
    row = math.ceil(len(cipher) / col)

    matrix = [['' for _ in range(col)] for _ in range(row)]

    key_order = sorted(list(key))
    k = 0

    # Fill column-wise based on key order
    for num in key_order:
        col_index = key.index(num)
        for r in range(row):
            matrix[r][col_index] = cipher[k]
            k += 1

    # Read row-wise
    text = ""
    for r in range(row):
        for c in range(col):
            text += matrix[r][c]

    return text


# -------- Main Program --------
text = input("Enter Plain Text: ")
key = input("Enter numeric key: ")

encrypted = encrypt(text, key)
print("\nEncrypted Text:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted Text:", decrypted)
