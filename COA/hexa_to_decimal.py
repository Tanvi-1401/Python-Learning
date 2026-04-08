# Hexadecimal to Decimal (without built-in)

hex_num = input("Enter Hexadecimal number: ").upper()

decimal = 0
power = 0

for digit in reversed(hex_num):
    if '0' <= digit <= '9':
        value = ord(digit) - ord('0')
    else:
        value = ord(digit) - ord('A') + 10

    decimal += value * (16 ** power)
    power += 1

print("Decimal value is:", decimal)