# Program to perform insertion and deletion in an array (list)

arr = []

n = int(input("Enter number of elements: "))

print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

print("Original array:", arr)

# INSERTION
pos = int(input("Enter position to insert element: "))
val = int(input("Enter element to insert: "))

arr.insert(pos, val)
print("Array after insertion:", arr)

# DELETION
del_val = int(input("Enter element to delete: "))

if del_val in arr:
    arr.remove(del_val)
    print("Array after deletion:", arr)
else:
    print("Element not found in array")
