def caesar(text, shift, choice):
    result = ""

    for ch in text:
        if ch.isalpha():
            if choice == "E":
                result += chr(ord(ch) + shift)
            elif choice == "D":
                result += chr(ord(ch) - shift)
        else:
            result += ch

    return result


text = input("Enter text: ")
shift = int(input("Enter shift: "))
choice = input("Enter E for Encrypt or D for Decrypt: ")

print("Result:", caesar(text, shift, choice))
