# Octal to Decimal (without built-in)

oct_num = input("Enter Octal number: ")

decimal = 0
power = 0

for digit in reversed(oct_num):
    decimal += int(digit) * (8 ** power)
    power += 1

print("Decimal value is:", decimal)