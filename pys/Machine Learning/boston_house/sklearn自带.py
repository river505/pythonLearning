from sklearn.datasets import load_boston
housing = load_boston()
import numpy as np
import pandas as pd

housingdf=pd.DataFrame(housing.data)
housingdf['y']=(housing.target)
(housingdf.isna().sum())
def outlier(i):
    mean=np.mean(i)
    std=np.std(i)
    zscore=(i-mean)/std
    outliers=i[(zscore<-3)|(zscore>3)]
    print(outliers)
outlier(housingdf['y'])
print(housing.target.size)