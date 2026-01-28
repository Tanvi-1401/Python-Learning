import numpy as np

# ---------- BASIC FUNCTIONS ----------
def text_to_num(text):
    return [ord(c) - 65 for c in text]

def num_to_text(nums):
    return ''.join(chr(int(n) + 65) for n in nums)

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# ---------- INPUT ----------
plain = input("Enter Plain Text: ").upper().replace(" ", "")
key_word = input("Enter Key Word: ").upper().replace(" ", "")

# Padding plaintext
while len(plain) % 3 != 0:
    plain += "X"

# Padding key
while len(key_word) < 9:
    key_word += "X"
key_word = key_word[:9]

# ---------- KEY MATRIX ----------
key_nums = text_to_num(key_word)
K = np.array(key_nums).reshape(3, 3)

print("\nKey Matrix:")
print(K)

# ---------- ENCRYPTION ----------
cipher = ""

for i in range(0, len(plain), 3):
    P = np.array(text_to_num(plain[i:i+3])).reshape(3, 1)
    C = np.dot(K, P) % 26
    cipher += num_to_text(C.flatten())

print("\nCipher Text:", cipher)

# ---------- DECRYPTION ----------
det = int(round(np.linalg.det(K))) % 26
det_inv = mod_inverse(det, 26)

adj = np.round(det * np.linalg.inv(K)).astype(int) % 26
K_inv = (det_inv * adj) % 26

print("\nInverse Key Matrix:")
print(K_inv)

decrypted = ""

for i in range(0, len(cipher), 3):
    C = np.array(text_to_num(cipher[i:i+3])).reshape(3, 1)
    P = np.dot(K_inv, C) % 26
    decrypted += num_to_text(P.flatten())

print("\nDecrypted Text:", decrypted)
