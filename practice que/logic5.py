x = [423,'b',37,'f']
u = x[1:]
y = u
w = x
u = u[0:]
u[1] = 53
x[2] = 47
print(y[1])
print(w[2])
print(u[1])
print(x[2])