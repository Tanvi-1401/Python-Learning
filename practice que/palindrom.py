list1 = [1, 2, 3]
list2 = ["T","a", "a", "T"]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrom")
else:
    print("Not Palindrom")
    