#导入一张图片，绘制图像各个通道的灰度值直方图，通过设置bins决定直方图柱数，
#0-255表示每个像素位置的RGB灰度数值
#横坐标为灰度值，纵坐标为个数
#明亮的图片 灰度值大 取值区域靠近横轴右侧 （黑白图片或单个通道中255为白色 0为黑色）

import cv2
import matplotlib.pyplot as plt
img=cv2.imread('../../img/SatomiIshihara.jpg',0)
# 1 加载彩色 ； 0 灰度模式 ； -1 包含alpha通道的彩色模式
#绘制所有通道灰度值直方图
plt.hist(img.reshape(-1),bins=256,range=(0,256))#img是（255，255，3）的数组，reshape([-1])改为一行列数位置
#reshape([-1,1]) 一列行数位置
#bins 还可以传入数组 每个数字表示间隔点
plt.show()

#绘制各个通道灰度值
img_2=cv2.imread('../../img/SatomiIshihara.jpg',1)
color=('r','g','b')
for i,col in enumerate(color):
    histr=      cv2.calcHist([img_2],[i],None,[256],[0,256])#OpenCV像素统计函数
    plt.plot(histr,color=col)
    plt.xlim([0,256])
plt.show()
