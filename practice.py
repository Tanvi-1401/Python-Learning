# students = {
#     "A": [80, 70, 90],
#     "B": [85, 75, 95]
# }

# highest = 0
# top = ""

# for s in students:
#     marks = students[s]
#     print(marks)
#     total = 0

#     for m in marks:
#         total = total + m

#     avg = total / len(marks)
#     print(s, "Average =", avg)

#     if avg > highest:
#         highest = avg
#         top = s

# print("Top Student:", top)

students = {
    "A": [80, 70, 90],
    "B": [85, 75, 95]
}
avg = []
def avg(marks):
    total = 0
    for m in marks:
        total = total + m
    avgAll = total / len(marks)
    avg.append(avgAll)
    return avgAll

for s in students:
    x = map(avg, students.values())
    
print(max(avg))