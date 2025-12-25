# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("Enter element to fint: "))
i = 0

while i < len(nums):
    if(nums[i] == x):
        print("Found at indx", i)
    i += 1
    