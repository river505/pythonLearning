#控制字典中元素顺序
from collections import OrderedDict

d=OrderedDict()
d['foo']=1
d['bar']=2
d['spam']=[1,2]
d['grok']=4
for key in d:
    print(key,d[key])
print(d)

dd={'fgh':456,'asd':123,'jkl':789}
dd['asd']=100
dd['aa']=0.2
dd['jkl']=dd['fgh']
dd['asa']=11

print(dd.values())
print(dd)