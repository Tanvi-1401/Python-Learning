def selection(arr1):
    n = len(arr1)
    for i in range(n - 1):
        mini = i
        for j in range(i + 1, n):
            if arr1[j] < arr1[mini]:
                mini = j
        # swap AFTER inner loop
        arr1[i], arr1[mini] = arr1[mini], arr1[i]

arr1 = [24, 41, 33, 42, 17]
selection(arr1)
print("Sorted array is:", arr1)
