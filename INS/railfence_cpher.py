def encrypt_rail_fence(text, key):
    rail = [['\n' for i in range(len(text))] for j in range(key)]
    
    dir_down = False
    row, col = 0, 0
    
    for i in range(len(text)):
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        
        rail[row][col] = text[i]
        col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1
    
    result = ""
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result += rail[i][j]
    
    return result


def decrypt_rail_fence(cipher, key):
    rail = [['\n' for i in range(len(cipher))] for j in range(key)]
    
    dir_down = False
    row, col = 0, 0

    # Mark zig-zag pattern
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        elif row == key - 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    # Fill cipher text
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    # Read zig-zag
    result = ""
    row, col = 0, 0
    dir_down = False

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        elif row == key - 1:
            dir_down = False

        result += rail[row][col]
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    return result


# --------- Main Program ----------

text = input("Enter Plain Text: ")
key = int(input("Enter key (rails): "))

encrypted = encrypt_rail_fence(text, key)
print("Encrypted Text:", encrypted)

decrypted = decrypt_rail_fence(encrypted, key)
print("Decrypted Text:", decrypted)
