import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


fileway='auto-mpg.data'
list =['mpg','cylinders','displacement','horsepower','weight','acceleration','model year']
# mpg - > 燃油效率
# cylinders -> 气缸
# displacement - > 排量
# horsepower - > 马力
# weight - > 重量
# acceleration - > 加速度
# model year - > 型号年份
#异常处理 删去异常行
base = pd.read_csv(fileway,delim_whitespace=True,names=list,usecols=[0,1,2,3,4,5,6],na_values=['?'])
base.dropna(axis=0,inplace=True)

fig = plt.figure(figsize=(6,9))

ax1 = fig.add_subplot(3,2,1)
ax2 = fig.add_subplot(3,2,2)
ax3 = fig.add_subplot(3,2,3)
ax4 = fig.add_subplot(3,2,4)
ax5 = fig.add_subplot(3,2,5)
ax1.scatter(base['cylinders'],base['mpg'],alpha=0.5)
ax1.set_title('cylinders')
ax2.scatter(base['displacement'],base['mpg'],alpha=0.5)
ax2.set_title('displacement')
ax3.scatter(base['weight'],base['mpg'],alpha=0.5)
ax3.set_title('weight')
ax4.scatter(base['acceleration'],base['mpg'],alpha=0.5)
ax4.set_title('acceleration')
ax5.scatter([float(x) for x in base['horsepower'].tolist()],base['mpg'],alpha=0.5)
ax5.set_title('horsepower')

plt.tight_layout(pad=3)

# plt.show()

from sklearn.model_selection import train_test_split
Y = base['mpg']
X = base[['weight']]
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr = lr.fit(X_train,Y_train)
ax6 = fig.add_subplot(3,2,6)
ax6.scatter(X_train, Y_train, color = 'red', alpha=0.3)
ax6.scatter(X_train, lr.predict(X_train),color = 'green',alpha=0.3)
plt.xlabel('weight')
plt.ylabel('mpg')
plt.title('train data')
# plt.show()

plt.scatter(X_test,Y_test,color = 'blue',alpha=0.3)
plt.scatter(X_train,lr.predict(X_train),color='purple',alpha=0.1)
plt.xlabel('weight')
plt.ylabel('mpg')
plt.title('test data')
plt.show()

print(lr.coef_)
print(lr.intercept_)
print('score = {}'.format(lr.score(X,Y)))
