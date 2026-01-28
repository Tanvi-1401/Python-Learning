# Decimal to Octal (Exact Notebook Output)

num = int(input("Enter integer number: "))
num1 = float(input("Enter float number: "))

# -------- Integer to Octal --------
def int_to_octal(n):
    digits = []
    while n > 0:
        digits.append(n % 8)
        n //= 8
    for i in range(len(digits)-1, -1, -1):
        print(digits[i], end="")

# -------- Using while loop --------
print("\nUsing while loop:")
int_to_octal(num)

# -------- Using for loop --------
print("\nUsing for loop:")
int_to_octal(num)

# -------- Float number --------
print("\nFloat number:")
x = int(num1)
f = num1 - x

int_to_octal(x)
print(".", end="")

# print 7 digits (as in notebook)
for _ in range(7):
    f *= 8
    d = int(f)
    print(d, end="")
    f -= d

# -------- Precision --------
print("\nPrecision:")
int_to_octal(x)
print(".", end="")

f = num1 - x
for _ in range(6):
    f *= 8
    d = int(f)
    print(d, end="")
    f -= d
