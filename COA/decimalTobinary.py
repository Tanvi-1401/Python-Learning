# Integer + Float Binary Conversion (Safe Version)

num = int(input("Enter integer number: "))
num1 = float(input("Enter float number: "))

# -------- Integer to Binary --------
def int_to_binary(n):
    bits = []
    while n > 0:
        bits.append(n % 2)
        n //= 2
    for i in range(len(bits)-1, -1, -1):
        print(bits[i], end="")

# -------- Using while loop --------
print("\nUsing while loop:")
int_to_binary(num)

# -------- Using for loop --------
print("\nUsing for loop:")
int_to_binary(num)

# -------- Float to Binary (limited length) --------
print("\nFloat number:")
x = int(num1)
f = num1 - x

# integer part
int_to_binary(x)
print(".", end="")

# fractional part (LIMITED to 20 bits)
for _ in range(20):
    f *= 2
    if f >= 1:
        print("1", end="")
        f -= 1
    else:
        print("0", end="")

# -------- Precision (6 bits only) --------
print("\nPrecision:")
int_to_binary(x)
print(".", end="")

f = num1 - x
for _ in range(6):
    f *= 2
    if f >= 1:
        print("1", end="")
        f -= 1
    else:
        print("0", end="")
