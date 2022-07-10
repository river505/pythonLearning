asd={
    'x':'1',
    'y':'3',
    'z':'5'
}
dsa={
    'x':'3',
    'y':'3',
    'a':'7'
}
print(asd.keys()&dsa.keys())
print(asd.keys()-dsa.keys())
print(asd.values()==dsa.values()) #判断是否完全相同 values不能用& -等
print(asd.items()&dsa.items())

#过滤

c={i:asd[i] for i in asd.keys()-dsa.keys()}
print(c)