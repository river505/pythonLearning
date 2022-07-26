#聚类 现有的数据进行聚集成类，聚类标准是事前不知道的
#K-Means 无监督 聚类 按照样本间的距离大小，将样本划分为K各簇，让簇内部的点尽量紧密连接

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import  datasets
iris=datasets.load_iris()
# print(iris)
irispd=pd.DataFrame(iris.data)
irispd['y']=(iris.target)
print(irispd.isna().sum())
x=iris.data
#无监督学习 用不上：
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.2)

from sklearn.cluster import KMeans
model=KMeans(3)  #参数 'n_clusters='（可省） : 聚类组数
model.fit(x)
print(model.labels_)
asd=model.labels_
x0=x[asd==0]
x1=x[asd==1]
x2=x[asd==2]
fig=plt.figure(figsize=(8,4))
ax=plt.subplot(1,2,1)
ax.scatter(x0[:,0],x0[:,1],c='red',label='0')
ax.scatter(x1[:,0],x1[:,1],c='b',label='1')
ax.scatter(x2[:,0],x2[:,1],c='g',label='2')
bx=plt.subplot(1,2,2)
bx.scatter(x0[:,2],x0[:,3],c='red',label='0')
bx.scatter(x1[:,2],x1[:,3],c='b',label='1')
bx.scatter(x2[:,2],x2[:,3],c='g',label='2')
ax.legend()
plt.legend()
plt.show()

ax=plt.subplot(projection='3d')
ax.scatter(x0[:,0],x0[:,1],x0[:,2],c='red',label='0')
ax.scatter(x1[:,0],x1[:,1],x1[:,2],c='b',label='1')
ax.scatter(x2[:,0],x2[:,1],x2[:,2],c='g',label='2')
plt.legend()
plt.show()