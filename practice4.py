# tuple = tuple(map(int, input("Enter numbers separated by space: ").split()))
# print("Tuple:", tuple)

n = [1, 2, 3, 4, 5, 6, 7]
sum = 0
for i in n:
    sum = sum + i
avg = sum / len(n)
print("Average of numbers:", avg)