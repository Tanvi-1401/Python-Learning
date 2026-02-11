def generate_key(text, key):
    key = key.upper()
    key = list(key)
    
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


def encrypt(text, key):
    text = text.upper()
    key = generate_key(text, key)
    cipher_text = ""

    for i in range(len(text)):
        if text[i].isalpha():
            x = (ord(text[i]) - ord('A') + ord(key[i]) - ord('A')) % 26
            cipher_text += chr(x + ord('A'))
        else:
            cipher_text += text[i]

    return cipher_text


def decrypt(cipher_text, key):
    key = generate_key(cipher_text, key)
    plain_text = ""

    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            x = (ord(cipher_text[i]) - ord(key[i])) % 26
            plain_text += chr(x + ord('A'))
        else:
            plain_text += cipher_text[i]

    return plain_text


# -------- MAIN --------
text = input("Enter plaintext: ")
key = input("Enter key: ")

encrypted = encrypt(text, key)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)
