hexa = input("Enter hexadecimal number: ").upper()

decimal = 0
power = 0
hex_chars = "0123456789ABCDEF"

for digit in hexa[::-1]:
    decimal += hex_chars.index(digit) * (16 ** power)
    power += 1

octal = ""
while decimal > 0:
    octal = str(decimal % 8) + octal
    decimal = decimal // 8

print("Octal number is:", octal)
