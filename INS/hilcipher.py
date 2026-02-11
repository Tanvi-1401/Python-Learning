# Modular inverse
def mod_inverse(a, m=26):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1


# Determinant 2x2
def det2(k):
    return (k[0][0]*k[1][1] - k[0][1]*k[1][0]) % 26


# Determinant 3x3
def det3(k):
    d = (k[0][0]*(k[1][1]*k[2][2] - k[1][2]*k[2][1])
        - k[0][1]*(k[1][0]*k[2][2] - k[1][2]*k[2][0])
        + k[0][2]*(k[1][0]*k[2][1] - k[1][1]*k[2][0]))
    return d % 26


# Adjoint (2x2 and 3x3)
def adjoint(k, n):
    if n == 2:
        adj = [[k[1][1], -k[0][1]],
               [-k[1][0], k[0][0]]]

    elif n == 3:
        adj = [[0]*3 for _ in range(3)]

        adj[0][0] = k[1][1]*k[2][2] - k[1][2]*k[2][1]
        adj[0][1] = k[0][2]*k[2][1] - k[0][1]*k[2][2]
        adj[0][2] = k[0][1]*k[1][2] - k[0][2]*k[1][1]

        adj[1][0] = k[1][2]*k[2][0] - k[1][0]*k[2][2]
        adj[1][1] = k[0][0]*k[2][2] - k[0][2]*k[2][0]
        adj[1][2] = k[0][2]*k[1][0] - k[0][0]*k[1][2]

        adj[2][0] = k[1][0]*k[2][1] - k[1][1]*k[2][0]
        adj[2][1] = k[0][1]*k[2][0] - k[0][0]*k[2][1]
        adj[2][2] = k[0][0]*k[1][1] - k[0][1]*k[1][0]

    # mod 26 correction
    for i in range(n):
        for j in range(n):
            adj[i][j] = adj[i][j] % 26

    return adj


# Inverse matrix
def inverse_matrix(k, n):
    if n == 2:
        det = det2(k)
    else:
        det = det3(k)

    inv_det = mod_inverse(det)

    if inv_det == -1:
        print("❌ Not invertible (Determinant has no modular inverse)")
        return None

    adj = adjoint(k, n)

    inv = [[(adj[i][j] * inv_det) % 26 for j in range(n)] for i in range(n)]
    return inv


# Encryption / Decryption process
def process(text, n, k):
    text = text.upper().replace(" ", "")

    while len(text) % n != 0:
        text += 'X'

    result = ""

    for i in range(0, len(text), n):
        vector = [ord(text[i+j]) - 65 for j in range(n)]
        res = [0]*n

        for row in range(n):
            for col in range(n):
                res[row] += k[row][col] * vector[col]
            res[row] %= 26

        for j in range(n):
            result += chr(res[j] + 65)

    return result


# ---------------- MAIN ----------------

keyStr = input("Enter key string (4 letters for 2x2, 9 letters for 3x3): ").upper()
text = input("Enter plaintext: ").upper()

if len(keyStr) == 4:
    n = 2
    k = [[ord(keyStr[i*2+j]) - 65 for j in range(2)] for i in range(2)]

elif len(keyStr) == 9:
    n = 3
    k = [[ord(keyStr[i*3+j]) - 65 for j in range(3)] for i in range(3)]

else:
    print("Invalid key length! Use 4 or 9 letters.")
    exit()

print("Key Matrix:", k)

# Encryption
encrypted = process(text, n, k)
print("Encrypted:", encrypted)

# Decryption
inverse = inverse_matrix(k, n)

if inverse:
    print("Inverse Matrix:", inverse)
    decrypted = process(encrypted, n, inverse)
    print("Decrypted:", decrypted[:len(text)])
