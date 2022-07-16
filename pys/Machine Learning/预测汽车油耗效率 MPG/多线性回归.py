from sklearn.linear_model import LinearRegression

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
mul = ['weight','horsepower','displacement'] # 选择三个变量进行建立模型
mul_lr = LinearRegression()
mul_lr.fit(base[mul],base['mpg']) # 训练模型
base['mpg_prediction'] = mul_lr.predict(base[mul])
base.head()

mul_score = mul_lr.score(base[mul],base['mpg'])
print(mul_score)
from sklearn.metrics import mean_squared_error as mse
mse = mse(base['mpg'],base['mpg_prediction'])
print('mse = %f'%mse)
print('rmse = %f'%np.sqrt(mse))
fig = plt.figure(figsize = (6,8))

ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)
ax1.scatter(base['weight'], base['mpg'], c='blue', alpha=0.3)
ax1.scatter(base['weight'], base['mpg_prediction'], c='red', alpha=0.3)
ax1.set_title('weight')
ax2.scatter([ float(x) for x in base['horsepower'].tolist()], base['mpg'], c='blue', alpha=0.3)
ax2.scatter([ float(x) for x in base['horsepower'].tolist()], base['mpg_prediction'], c='red', alpha=0.3)
ax2.set_title('horsepower')
ax3.scatter(base['displacement'], base['mpg'], c='blue', alpha=0.3)
ax3.scatter(base['displacement'], base['mpg_prediction'], c='red', alpha=0.3)
ax3.set_title('displacement')
plt.tight_layout(pad=3)
plt.show()
