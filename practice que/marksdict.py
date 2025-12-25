marks = {}

x = int(input("enter phy marks: "))
marks.update({"phy" : x})
y = int(input("enter chem marks: "))
marks.update({"chem" : y})
z = int(input("enter math marks: "))
marks.update({"math" : z})

print(marks)