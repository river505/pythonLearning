import joblib
import sklearn
model=joblib.load('asdf.pkl')
from sklearn.datasets  import load_boston
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
housing = load_boston()
X=housing.data
y=housing.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25)
ss_x = StandardScaler()
X_train = ss_x.fit_transform(X_train)
X_test = ss_x.transform(X_test)
ss_y = StandardScaler()
y_train = ss_y.fit_transform(y_train.reshape(-1, 1))
y_test = ss_y.transform(y_test.reshape(-1, 1))
import pickle


print(model.score(X_test,y_test))