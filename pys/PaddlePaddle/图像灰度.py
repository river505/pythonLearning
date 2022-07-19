import cv2
# import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('../img/SatomiIshihara.jpg',1)
color=('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256]) #hist是一个shape为(256,1)的数组，表示0-255每个像素值对应的像素个数，下标即为相应的像素值
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()