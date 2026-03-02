binary = input("Enter binary number: ")

decimal = 0
power = 0

binary = int(binary)

while binary > 0:
    digit = binary % 10
    decimal = decimal + digit * (2 ** power)
    binary = binary // 10
    power = power + 1

print("Decimal value is:", decimal)