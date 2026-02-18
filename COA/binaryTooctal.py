binary = input("Enter binary number: ")

decimal = 0
power = 0

# Binary → Decimal
for digit in binary[::-1]:
    decimal += int(digit) * (2 ** power)
    power += 1

# Decimal → Octal
octal = ""
while decimal > 0:
    octal = str(decimal % 8) + octal
    decimal = decimal // 8

print("Octal number is:", octal)
