#Escape squence character

str1 = "This is a Python string Info.\nReady to learn!" # next line
print(str1) 

str2 = "This is a Python string Info.\tReady to learn!" # tab space
print(str2) 

#Concateation
str3 = "Tanvi"
str4 = "Joshi"
final_str = str3 + str4

print(final_str)

# length of string
len_final = len(final_str)
print(len_final)

#indexing
str5 = "Tanvi Joshi"
print(str5[4])

#slicing (negative indexing)
str6 = "apple"
print(str6[-3:-1])
print(str6[0:3])
print(str6[:4])# -- appl
print(str6[2:])# [2:len(str6)] -- ple
