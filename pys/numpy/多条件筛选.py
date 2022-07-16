import numpy as np
a=[1,2,3,4,5,6]
asd=np.array(a)
print(np.logical_and(asd>4 , asd<6))
print(np.logical_or(asd<3 , asd>5))
print(asd[np.logical_not(asd<3 , asd>5)])
print(asd[np.logical_xor(asd<6 , asd>1)]) #条件结果相同为F 相异为T