import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

x = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
y = np.array([[[9,10],[11,12]],[[13,14],[15,16]]])

np.concatenate((a,b), axis=0)