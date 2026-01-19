# Initial array
arr = []

n = int(input("Enter number of elements: "))
for i in range(n):
    arr.append(int(input("Enter element: ")))

print("Original Array:", arr)

# -------- INSERTION --------
pos = int(input("Enter position to insert: "))
ele = int(input("Enter element to insert: "))

arr.insert(pos, ele)
print("Array after insertion:", arr)

# -------- DELETION --------
pos = int(input("Enter position to delete: "))

arr.pop(pos)
print("Array after deletion:", arr)
