import  numpy as np
#resize 改变数组本身 reshape不改变,
arr=np.array([1,2,3,4,5,6])
# arr.resize(2,3)
arr.reshape((2,3))
print(arr)
#ravel 展平 不改变数组本身 是一个视图（返回的对象赋给新数组后，新旧数组同变化）
print("按列展平：",arr.ravel('F'),
      "按行展平",arr.ravel())
print(arr)
