def repfree(s):
    a = set()  
    for t in s:
        if t in a:
            return False  
        a.add(t)
    return True  

print(repfree("zb%78"))      # True
print(repfree("(7)(a"))      # False
print(repfree("a)*(?"))      # True
print(repfree("abracadabra"))# False
