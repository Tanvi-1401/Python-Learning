binary = input("Enter binary number: ")

decimal = 0
power = 0

# Binary → Decimal
for digit in binary[::-1]:
    decimal += int(digit) * (2 ** power)
    power += 1

# Decimal → Hexadecimal
hexa = ""
hex_chars = "0123456789ABCDEF"

while decimal > 0:
    hexa = hex_chars[decimal % 16] + hexa
    decimal = decimal // 16

print("Hexadecimal number is:", hexa)
