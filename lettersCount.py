# count letter in sentence without spaces

sentence = input("Enter a sentence: ")
new = sentence.replace(" ","")
count = 0
for i in new:
    count += 1
print(count)