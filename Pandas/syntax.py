import pandas as pd

std_data = [(1, "Tanvi", 33, "A", "Female", "Gujarat"),
            (2, "Rahul", 25, "B", "Male", "Maharashtra"),
            (3, "Priya", 28, "A", "Female", "Karnataka"),
            (4, "Amit", 30, "B", "Male", "Delhi"),
            (5, "Sneha", 27, "A", "Female", "West Bengal")]
df = pd.DataFrame(std_data, columns=[
                  "Student_ID", "Name", "Age", "Grade", "Gender", "State"])
# print(df)

# df = pd.read_csv("Student.csv")
# print(df)

#--- Accessing specific rows and columns ---#
#print(df.head(2))
#print(df.tail(2))
#print(df.shape)
#print(df.columns)
#print(df.Age) # df['Age', 'Address']
#print(df.size)
#print(df.dtypes)
#print(df.values)
print(df.index)

