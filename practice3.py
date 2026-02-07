lst = [9, 8, 7, 86, 25, 67, 3, 2, 1]

for i in range(len(lst)-1):
    for j in range(len(lst)-1-i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst)