alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key   = "QWERTYUIOPASDFGHJKLZXCVBNM"

text = input("Enter text: ").upper()
choice = input("Enter E for Encrypt or D for Decrypt: ")

result = ""

for ch in text:
    if ch.isalpha():
        if choice == "E":
            index = alpha.index(ch)
            result += key[index]
        else:   # Decrypt
            index = key.index(ch)
            result += alpha[index]
    else:
        result += ch

print("Result:", result)
