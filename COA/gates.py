# WAP to implement XOR, XNOR, NOR and NAND gates

a = int(input("Enter first input (0 or 1): "))
b = int(input("Enter second input (0 or 1): "))

# NOt
not_a = 1 - a
not_b = 1 - b

# XOR Gate
xor = (a + b - a*b)

# XNOR Gate
xnor = (1 - (a + b - a*b))

# OR Gate
or_gate = (a + b - a*b)

# NOR Gate
nor = (1 - (a + b - a*b))

# AND Gate
and_gate = (a * b)

# NAND Gate
nand = (1 - (a * b))

print("OR Output:", int(or_gate))
print("XOR Output:", int(xor))
print("XNOR Output:", int(xnor))
print("NOR Output:", int(nor))
print("AND Output:", int(and_gate))
print("NAND Output:", int(nand))
print("NOT A Output:", int(not_a))
print("NOT B Output:", int(not_b))
