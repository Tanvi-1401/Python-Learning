def matrix(key):
    key = key.upper().replace("J", "I")
    m = []

    for ch in key:
        if ch.isalpha() and ch not in m:
            m.append(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in m:
            m.append(ch)

    return [m[i:i+5] for i in range(0, 25, 5)]


def position(mat, ch):
    for i in range(5):
        for j in range(5):
            if mat[i][j] == ch:
                return i, j


def print_matrix(mat):
    print("\nPlayfair Cipher Matrix:")
    for row in mat:
        print(" ".join(row))


def playfair(text, key, mode):
    text = text.upper().replace("J", "I").replace(" ", "")
    mat = matrix(key)

    # 👉 matrix print here
    print_matrix(mat)

    result = ""
    i = 0

    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "X"

        if a == b:
            b = "X"
            i += 1
        else:
            i += 2

        r1, c1 = position(mat, a)
        r2, c2 = position(mat, b)

        if r1 == r2:  # same row
            if mode == "E":
                result += mat[r1][(c1+1) % 5] + mat[r2][(c2+1) % 5]
            else:
                result += mat[r1][(c1-1) % 5] + mat[r2][(c2-1) % 5]

        elif c1 == c2:  # same column
            if mode == "E":
                result += mat[(r1+1) % 5][c1] + mat[(r2+1) % 5][c2]
            else:
                result += mat[(r1-1) % 5][c1] + mat[(r2-1) % 5][c2]

        else:  # rectangle
            result += mat[r1][c2] + mat[r2][c1]

    return result


# -------- MAIN --------
key = input("Enter key: ")
text = input("Enter text: ")
choice = input("Enter E for Encrypt or D for Decrypt: ")

print("\nResult:", playfair(text, key, choice))
