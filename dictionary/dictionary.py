# info = {
#     "name" : "Tanvi", # "key" : value
#     "age" : 18,
#     12 : 12.9,
#     "marks" : 99.45,
#     "subjects" : ["Java","c++","C","Python"],
#     "topics" : ("dict","set"),
#     "is_pass" : True,
#     7.14 : 14.07
# }

# print(type(info))
# print(info)

# print(info["name"])
# print(info["topics"])

# info["name"] = "Tashi"
# info["surname"] = "Joshi"
# print(info)

# null_dict = {}
# null_dict["name"] = "Tanvi Joshi"
# print(null_dict)

#-----nested dictionary------

student_data = {
    "name" : "Tanvi Joshi",
    "subjects" : {
        "phy" : 98,
        "chem" : 70,
        "math" : 99,
    }
}
print(student_data["subjects"]["math"])

