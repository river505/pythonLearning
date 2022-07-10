import numpy as np
prices={
    'ACME':45.23,
    'AAPL':612.78,
    'IBM':205.55,
    'HPQ':37.20,
    'FB':10.75
}
#
print(min(prices))
print(min(prices.items())) #items 获得键值对
print(max(prices.values()))# values 获得值
print(min(zip(prices.values(),prices.keys()))) # zip整合两个对象为元组

priceSortedDict=sorted(zip(prices.values(),prices.keys()))
print(priceSortedDict)

asd=[1,2,3,5,4,8,7,6]
print(1,sorted(asd))
print(asd)
print(np.sort(asd))
print(2,asd.sort())
print(asd)
asd.extend([1,9])
print(2,asd)
asd.sort()
print(2,asd)
asd.extend([1,9])
print(2,asd)
print(4,np.sort(asd)) #np.sort list的sort()均不改变原来顺序，而是返回新的对象
print(5,asd)