# Binary to Hex and Hex to Binary

choice = input("Enter choice (1: Binary to Hex, 2: Hex to Binary): ")

# Binary → Hex
if choice == '1':
    binary = input("Enter Binary number: ")

    # make length multiple of 4
    while len(binary) % 4 != 0:
        binary = '0' + binary

    hex_result = ""

    for i in range(0, len(binary), 4):
        group = binary[i:i+4]

        decimal = 0
        power = 0

        for bit in reversed(group):
            decimal += int(bit) * (2 ** power)
            power += 1

        if decimal < 10:
            hex_result += str(decimal)
        else:
            hex_result += chr(decimal - 10 + ord('A'))

    print("Hexadecimal value is:", hex_result)

# Hex → Binary
elif choice == '2':
    hex_num = input("Enter Hexadecimal number: ").upper()

    binary = ""

    for digit in hex_num:
        if '0' <= digit <= '9':
            value = ord(digit) - ord('0')
        else:
            value = ord(digit) - ord('A') + 10

        temp = ""
        for i in range(4):
            temp = str(value % 2) + temp
            value //= 2

        binary += temp

    print("Binary value is:", binary)

else:
    print("Invalid choice")