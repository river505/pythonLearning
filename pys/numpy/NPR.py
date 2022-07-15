import numpy as np
print(np.r_[-10:])
print(np.r_[0:10,np.array([1,2,3]),4.3,0])
print(np.r_[np.zeros((2,2)),np.ones((3,2))])
print(np.r_[np.zeros((2,2)),np.ones((2,2))])

print(np.r_['1',np.zeros((2,2)),np.ones((2,2))])
print(np.r_['1',np.zeros((2,2)),np.ones((2,3))])
print(np.c_['1',np.zeros((2,2)),np.ones((2,3))])
print(np.c_[np.zeros((2,2)),np.ones((2,3))])
print(np.c_[np.zeros((2,2)),np.ones(2)])
print(np.r_[np.zeros((2,2)),np.ones((1,2))])