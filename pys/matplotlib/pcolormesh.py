import numpy as np

import pandas as pd

import matplotlib as mpl

import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets # 机器学习库
scikit_iris = datasets.load_iris()

iris_feature = u'花萼长度', u'花萼宽度', u'花瓣长度', u'花瓣宽度', u'类别'

path = 'iris.data'  # 数据文件路径

data = pd.DataFrame(data=np.c_[scikit_iris['data'], scikit_iris['target']],
                     columns=np.append(scikit_iris.feature_names, ['y']))

data.columns = iris_feature

data['类别'] = pd.Categorical(data['类别']).codes

x_train = data[['花萼长度', '花瓣长度']]

y_train = data['类别']

model = DecisionTreeClassifier(criterion='entropy', min_samples_leaf=3)

model.fit(x_train, y_train)

N, M = 500, 500  # 横纵各采样多少个值

x1_min, x2_min = x_train.min(axis=0)

x1_max, x2_max = x_train.max(axis=0)

t1 = np.linspace(x1_min, x1_max, N)

t2 = np.linspace(x2_min, x2_max, M)

x1, x2 = np.meshgrid(t1, t2)  # 生成网格采样点

x_show = np.stack((x1.flat, x2.flat), axis=1)  # 测试点

y_predict = model.predict(x_show)
print(y_predict.shape)
print(x1.shape)

mpl.rcParams['font.sans-serif'] = ['SimHei']

mpl.rcParams['axes.unicode_minus'] = False

cm_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])

cm_dark = mpl.colors.ListedColormap(['g', 'r', 'b'])

plt.xlim(x1_min, x1_max)

plt.ylim(x2_min, x2_max)
print((y_predict.reshape(x1.shape)).shape)

plt.pcolormesh(x1, x2, y_predict.reshape(x1.shape), cmap=cm_light)

plt.scatter(x_train['花萼长度'], x_train['花瓣长度'], c=y_train, cmap=cm_dark, marker='o', edgecolors='k')

plt.xlabel('花萼长度')

plt.ylabel('花瓣长度')

plt.title('鸢尾花分类')

plt.grid(True, ls=':')

plt.show()
