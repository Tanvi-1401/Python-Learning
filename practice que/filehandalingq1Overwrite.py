with open("practice que/practice.txt", "r") as f:
    data = f.read()
    
new_data = data.replace("python", "Java")
print(new_data)

with open("practice que/practice.txt", "w") as f:   
    f.write(new_data)
