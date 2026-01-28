text = input("Enter text: ").upper()
key = input("Enter key: ").upper()
choice = input("Enter E for Encrypt or D for Decrypt: ")

result = ""
k = 0

for ch in text:
    if ch.isalpha():
        key_val = ord(key[k % len(key)]) - 65

        if choice == "E":
            new = (ord(ch) - 65 + key_val) % 26
        else:
            new = (ord(ch) - 65 - key_val) % 26

        result += chr(new + 65)
        k += 1
    else:
        result += ch

print("Result:", result)
