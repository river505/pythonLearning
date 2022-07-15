import  numpy as np
a=np.floor(10*np.random.random((3,4)))
print(a)
a.flatten()#dncs (deflaut not change itself)
print(a)
print(a.flatten()) #副本 深拷贝
#ravel 展平 dncs
print("按列展平：",a.ravel('F'),
      "按行展平",a.ravel())
print(a)