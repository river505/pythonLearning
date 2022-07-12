import pandas as pd
import numpy as np
#整体上有四个索引：行、列的位置索引（0，1，2，…）、行的标签索引（index）、列标签（columns）
asd=np.array(range(15)).reshape(3,5)
df = pd.DataFrame(asd,index=['小李','小王','小张'],columns=['a','b','c','d',7] )
print(df.where(df>4)) #df全 满足条件不变 其余（other）默认变为NaN
print(df[df['b']>5]) #成立的部分行
print(df.query('5<b')) #成立的部分
print(df.query('a<b'))
print(df.mask(5<df['a']))
print(df.mask(5<df))
df=df.where(~(df==0),-1) #-1 默认为other的参数
print(df)
df=df.mask(df==-1,100) #符合条件的变 默认为NaN
print(df)