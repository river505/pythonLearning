#支持向量机分类 已做过Kmeans聚类 不再检查数据集缺失值等

#生成200个点只绘制出100余个？ 检查无重复点 原因见 41行
import numpy as np
from matplotlib import colors
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import  datasets
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
#iris数据集自变量sepal length,sepal width, petal length, petal width
#萼片长度，萼片宽度，花瓣长度，花瓣宽度
iris=datasets.load_iris()
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
# model= svm.SVC()
model=svm.SVC(C=0.8,kernel='linear',decision_function_shape='ovr')
model.fit(x_train,y_train)
print(model.score(x_test,y_test))# 数据结构简单 评分接近甚至等于1.0

#可视化 利用第一、二个特征，绘制二维图
iris=datasets.load_iris()
x=iris.data[:,:2]
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
model= svm.SVC()
# model=svm.SVC(C=0.8,kernel='linear',decision_function_shape='ovr')
model.fit(x_train,y_train)

def draw(model,x):
    fig=plt.figure(figsize=(100,100))
    iris_feature = 'sepal length','sepal width', 'petal length', 'petal width'
    x1_min,x1_max=x[:,0].min(),x[:,0].max()
    x2_min, x2_max = x[:,1].min(), x[:,1].max()
    #生成网络采样点
    x1,x2=np.mgrid[ x1_min:x1_max:200j,x2_min:x2_max:200j ] #起始：终止：个数
    #步长为复数(j) 表示点数，左闭右闭
    #步长为实数 表示间隔，左闭右开
    #生成样本点 样本点只为绘制背景伪色彩区间 并未显示 显示的仍为数据集的点
    grid_test=np.stack((x1.ravel(),x2.ravel()),axis=1) #对应位置组合
    # print('grid test;\n',grid_test[:2])
    #计算样本到决策面的距离
    z=model.decision_function(grid_test)
    # print('the distance to decision plane:\n',z[:2])
    grid_hat=model.predict(grid_test)
    grid_hat= grid_hat.reshape(x1.shape)
    cm_light=mpl.colors.ListedColormap(['#A0FFA0','#FFA0A0','#A0A0FF'])
    cm_dark=mpl.colors.ListedColormap(['g','b','r'])
    plt.pcolormesh(x1,x2,grid_hat,cmap=cm_light)
    #创建具有非规则矩形网格的伪彩色图
    #根据y_predict结果 划分颜色 x1，x2分别为横纵坐标，当y_predict更换为降水量等结果图更多样
    #相关内容在matplotlib文件夹下
    # plt.scatter(x[:,0],x[:,1])
    plt.scatter(x[:,0],x[:,1],c=np.squeeze(y),edgecolors='k',s=50,cmap=cm_dark)
    #plt.scatter(x,y,c= '颜色可选,划分颜色的依据，并不指明颜色，和参数hue类似见boston_house.py',
    #   marker= '点的样式', cmap= '颜色变化（序列）',
    #   alpha=“透明度”, linewidths=“线宽”,s=‘点的大小’)
    plt.scatter(x_test[:,0],x_test[:,1],c=np.squeeze(y_test),
                s=120,edgecolors='w',cmap=cm_dark,zorder=10)
    # plt.scatter(x_test[:, 0], x_test[:, 1], s=120, zorder=10)
    #zorder控制绘图顺序 越大越晚在上层
    # Artist
    # Z - order默认值
    # Patch / PatchCollection  1
    # Line2D / LineCollection  2
    # Text 3
    plt.show()
    # grid_test=pd.DataFrame(grid_test)
    # print(grid_test[grid_test.duplicated(keep=False)])

draw(model,x)
# print(x[:,0].min(),x[:,0].max(), x[:,1].min(), x[:,1].max())




