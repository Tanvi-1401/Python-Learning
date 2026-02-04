x = [1,"abcd",2,"efgh",[3,4]]  # Statement 1
y = x[0:6]                     # Statement 2
z = x                          # Statement 3
w = y                          # Statement 4
x[1] = x[1][0:3] + 'd'         # Statement 5
y[2] = 4                       # Statement 6
z[1][1:3] = 'yzw'              # Statement 7
z[0] = 0                       # Statement 8
w[4][0] = 1000                 # Statement 9
a = (x[4][1] == 4)             # Statement 10