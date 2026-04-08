# Binary to Octal and Octal to Binary

choice = input("Enter choice (1: Binary to Octal, 2: Octal to Binary): ")

# Binary → Octal
if choice == '1':
    binary = input("Enter Binary number: ")

    # make length multiple of 3
    while len(binary) % 3 != 0:
        binary = '0' + binary

    octal = ""

    for i in range(0, len(binary), 3):
        group = binary[i:i+3]

        decimal = 0
        power = 0

        for bit in reversed(group):
            decimal += int(bit) * (2 ** power)
            power += 1

        octal += str(decimal)

    print("Octal value is:", octal)

# Octal → Binary
elif choice == '2':
    oct_num = input("Enter Octal number: ")

    binary = ""

    for digit in oct_num:
        value = int(digit)

        temp = ""
        for i in range(3):
            temp = str(value % 2) + temp
            value //= 2

        binary += temp

    print("Binary value is:", binary)

else:
    print("Invalid choice")