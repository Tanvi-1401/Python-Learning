# check prime number
def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# find primitive roots
def primitiveRoot(p):

    if not isPrime(p):
        print("Number is not prime")
        return

    print("Primitive roots of", p, "are:")

    for g in range(2, p):

        s = set()

        for i in range(1, p):
            value = (g ** i) % p
            s.add(value)

        if len(s) == p - 1:
            print(g)


# input
p = int(input("Enter prime number: "))
primitiveRoot(p)