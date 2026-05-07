def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]   # choose first element as pivot
    left = []
    right = []

    for i in arr[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


# User Input
n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)

print("Original array:", arr)

sorted_arr = quick_sort(arr)
print("Sorted array (Quick Sort):", sorted_arr)