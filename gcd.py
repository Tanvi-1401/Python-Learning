m = int(input("Enter m: "))
n = int(input("Enter n: "))

# def gcd(x, y):
#     fx=[]
#     for i in range(1, x+1):
#         if x%i==0:
#             fx.append(i)
#     fy=[]        
#     for j in range(1, y+1):
#         if y%j==0:
#             fy.append(j)
#     cf = []
#     for factor in fx:
#         if factor in fy:
#             cf.append(factor)
#     return(cf[-1])

#----- another
# def gcd(x, y):
#     cf=[]
#     for i in range(1, min(x,y)+1):
#         if(x%i==0 and y%i==0):
#             cf.append(i)
#     return(cf[-1])

#----- another
def gcd(x, y):
    
    for i in range(1, min(x,y)+1):
        if(x%i==0 and y%i==0):
            mrcf = i
    return(mrcf)

print(gcd(m,n))