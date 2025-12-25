str = "i am learning python"

print(str.endswith("hon"))

print(str.capitalize()) # it's capitalize 1st char
print(str)# if we print str after capitalize it dosen't give output with capital i it's work one time
#if we want that change in orignal string
# we do this str = str.capitalize()

print(str.replace("a","o"))#(old value,new value)
print(str.replace("python","java"))# also replace sub string

print(str.find("am"))# gives index
print(str.find("Q"))# gives -1(bcz dosn't exists)

print(str.count("a"))# how many times a comes in string