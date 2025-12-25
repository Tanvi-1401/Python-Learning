student = {
    "name" : "Tanvi Joshi",
    "subjects" : {
        "phy" : 98,
        "chem" : 70,
        "math" : 99,
    }
}

# print(len(student))# ans 2
# print(len(list(student.keys())))# ans 2
# print(list(student.values()))

#------------
# pairs = list(student.items())
# print(pairs[0])
# print(student.items())

#------------
# print(student["name2"]) # --error
# print(student.get("name2")) # --none

#------------
new_dict = {"city" : "Gujarat", "name" : "Tashi"}
print(student.update(new_dict)) # or print(student.update({"city" : "Gujarat"}))
print(student)
