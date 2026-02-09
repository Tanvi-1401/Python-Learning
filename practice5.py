nums = [1, 2, 2, 3, 3, 1, 1]
check = []

for i in nums:
    if i not in check:
        print(i, "->", nums.count(i))
        check.append(i)
        
print(check)