octal = input("Enter octal number: ")

decimal = 0
power = 0

# Octal → Decimal
for digit in octal[::-1]:
    decimal += int(digit) * (8 ** power)
    power += 1

# Decimal → Hex
hexa = ""
hex_chars = "0123456789ABCDEF"

while decimal > 0:
    hexa = hex_chars[decimal % 16] + hexa
    decimal = decimal // 16

print("Hexadecimal number is:", hexa)
