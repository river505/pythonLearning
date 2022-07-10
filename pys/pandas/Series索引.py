import pandas as pd

asd=[1,2,3,4,5,6]
dsa=[11,22,33,44,55,66]
ser01=pd.Series(asd,index=['a','b','c','d','e','f'])
ser02=pd.Series(dsa)
print(ser01[0])
print(ser01.iloc[0])
# print(ser01.loc[0]) #loc按index索引，此处报错
print(ser01['a'])
print(ser02[5])
print()
#切片
print(ser02.loc[1:4])
print(ser02.iloc[1:4])
print(ser01.loc['a':'e'])
print()
#修改
ser02[1]='a'
print(ser02)
print()
#添加
ser02[100]=100
print(ser02)
print()
#append简单连接 append函数较其他函数特殊，由对象调用却返回一个新Series 对原来的不做更改
'''FutureWarning: 
The series.append method is deprecated 
and will be removed from pandas in a future version.
Use pandas.concat instead.
'''
try:
    ser03=ser02.append(ser01)
    ser04=ser01.append(ser02)
    print(ser03)
    print(ser04)
except:
    pass
print()
#重新分配索引的连接
ser05=ser01.append(ser02,ignore_index=True)
print(1,ser05)
