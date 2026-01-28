# Decimal to Hexadecimal (Notebook Style)

num = int(input("Enter integer number: "))
num1 = float(input("Enter float number: "))

hex_map = "0123456789ABCDEF"

# -------- Integer to Hex --------
def int_to_hex(n):
    digits = []
    while n > 0:
        digits.append(hex_map[n % 16])
        n //= 16
    for i in range(len(digits)-1, -1, -1):
        print(digits[i], end="")

# -------- Using while loop --------
print("\nUsing while loop:")
int_to_hex(num)

# -------- Using for loop --------
print("\nUsing for loop:")
int_to_hex(num)

# -------- Float number --------
print("\nFloat number:")
x = int(num1)
f = num1 - x

int_to_hex(x)
print(".", end="")

# 7 digits like notebook
for _ in range(7):
    f *= 16
    d = int(f)
    print(hex_map[d], end="")
    f -= d

# -------- Precision --------
print("\nPrecision:")
int_to_hex(x)
print(".", end="")

f = num1 - x
for _ in range(6):
    f *= 16
    d = int(f)
    print(hex_map[d], end="")
    f -= d
