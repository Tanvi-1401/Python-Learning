a = int(input("Enter first number: "))
b = int(input("Enter secont number: "))
c = int(input("Enter third number: "))

if(a > b):
    if(a > c):
        print("a is greatest.")
if(b > a):
    if(b > c):
        print("b is greatest.")
if(c > b):
    if(c > a):
        print("c is greatest.")
