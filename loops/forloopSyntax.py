# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for val in nums:
#     print(val)

# #--------    
# tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# for val in nums:
#     print(val)

#--------    
# str = "Tanvi"

# for char in str:
#     print(char)

#---------
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for val in nums:
#     print(val)
    
#---------
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49]

x = int(input("enter num to find: "))

idx = 0
for el in nums:
    if(el == x):
        print("Number found at indax", idx)
    idx += 1