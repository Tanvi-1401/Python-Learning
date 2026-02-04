# def threesquares(m):
#     if m <= 0:
#         return False

#     limit = int(m ** 0.5) + 1

#     for a in range(limit):
#         for b in range(limit):
#             for c in range(limit):
#                 if a*a + b*b + c*c == m:
#                     return True

#     return False
  
def threesquares(m):
    orignal = m
    while m % 4 == 0:
        m //= 4
    if m % 8 == 7:
        return False
    else:
        return True
    
print(threesquares(6))
print(threesquares(188))
print(threesquares(1000))