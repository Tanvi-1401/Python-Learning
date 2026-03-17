# WAP to implement XOR, XNOR, NOR and NAND gates

a = int(input("Enter first input (0 or 1): "))
b = int(input("Enter second input (0 or 1): "))

# XOR Gate
xor = a ^ b

# XNOR Gate
xnor = not (a ^ b)

# NOR Gate
nor = not (a or b)

# NAND Gate
nand = not (a and b)

print("XOR Output:", int(xor))
print("XNOR Output:", int(xnor))
print("NOR Output:", int(nor))
print("NAND Output:", int(nand))