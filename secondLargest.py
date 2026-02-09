# without set
nums = [0, -1, -5, -2]
largest = nums[0]
second = -1
for i in nums:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i
print("Second largest number is: ", second) 
print("Largest number is: ", largest)       