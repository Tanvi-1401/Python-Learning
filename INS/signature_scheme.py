import hashlib

# Step 1: User input (message)
message = input("Enter message to sign: ")

# Step 2: Private and Public key (simple numbers for demo)
private_key = int(input("Enter private key: "))
public_key = private_key  # (for simplicity, same key used)

# Step 3: Create hash of message
hash_msg = int(hashlib.sha256(message.encode()).hexdigest(), 16)

# Step 4: Sign the message
signature = (hash_msg * private_key) % 100000

print("\nMessage Hash:", hash_msg)
print("Digital Signature:", signature)

# Step 5: Verify the signature
verify = (hash_msg * public_key) % 100000

print("\nVerification Value:", verify)

# Step 6: Check
if verify == signature:
    print("Signature Verified! Message is authentic.")
else:
    print("Verification Failed!")