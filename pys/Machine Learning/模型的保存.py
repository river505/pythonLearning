
#注意asdf.pkl使用了标准化数据 导出应用时其数据也应先标准化
from sklearn.datasets  import load_boston
import pickle
housing = load_boston()
X=housing.data
y=housing.target

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25)

from sklearn.neural_network import MLPRegressor
model=MLPRegressor(max_iter=1000)
model.fit(X_train,y_train)
print(model.score(X_test,y_test))
# import joblib
# joblib.dump(model,'MPL4boston.pkl')
from sklearn.metrics import r2_score
print(r2_score(y_test,model.predict(X_test)))
from sklearn.linear_model import ElasticNet

enet = ElasticNet()
enet.fit(X_train,y_train)
y_predict_enet = enet.predict(X_test)



print('SCORE:{:.4f}'.format( enet.score(X_test, y_test)))#模型评分


