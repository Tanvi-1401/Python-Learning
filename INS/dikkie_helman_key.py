# Diffie-Hellman Key Exchange

# Step 1: Public values (taken from user)
p = int(input("Enter a prime number (p): "))
g = int(input("Enter a primitive root (g): "))

# Step 2: Private keys (chosen secretly)
a = int(input("Enter private key of User A: "))
b = int(input("Enter private key of User B: "))

# Step 3: Calculate public keys
A = (g ** a) % p   # Public key of A
B = (g ** b) % p   # Public key of B

print("\nPublic key of A:", A)
print("Public key of B:", B)

# Step 4: Generate shared secret key
key_A = (B ** a) % p   # A computes key
key_B = (A ** b) % p   # B computes key

print("\nSecret key computed by A:", key_A)
print("Secret key computed by B:", key_B)

# Step 5: Verify
if key_A == key_B:
    print("\nKey Exchange Successful! Shared Secret Key =", key_A)
else:
    print("\nKey Exchange Failed!")