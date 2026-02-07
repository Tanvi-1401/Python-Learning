lst = [1,2,3,4,5,6,7,8,9,10]

for i in range(5, len(lst)-1):
    lst[i] = lst[i+1]

lst = lst[:len(lst)-1]

print(lst)