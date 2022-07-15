#Axis  change
import numpy as np
ar=np.arange(24).reshape(2,3,4)
print(ar)
print(ar.transpose(1,2,0))#数字代表该数字位置上的维度为原来的第几个维度，从0开始
print(ar.transpose(1,2,0).shape)
print(ar.shape)