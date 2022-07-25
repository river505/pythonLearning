from sklearn.linear_model import ElasticNet
from sklearn.linear_model import Lasso
from sklearn.linear_model import LassoLars
from sklearn.datasets  import load_boston
housing = load_boston()
X=housing.data
y=housing.target
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25)
enet = ElasticNet()
model1=Lasso()
model2=LassoLars()
model1.fit(X_train,y_train)
model2.fit(X_train,y_train)
enet.fit(X_train,y_train)
y_predict_enet = enet.predict(X_test)
print('弹性网SCORE:{:.4f}'.format( enet.score(X_test, y_test)))#模型评分
print('Lasso SCORE:{:.4f}'.format( model1.score(X_test, y_test)))
print('LassoLars SCORE:{:.4f}'.format( model2.score(X_test, y_test)))