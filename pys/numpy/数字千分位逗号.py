import numpy as np
import pandas as pd
import wave
asd=pd.read_csv('asd.csv',thousands=',',sep=' ',header=None)
#asd=np.loadtxt('asd.csv',delimiter=' ')
print(asd)