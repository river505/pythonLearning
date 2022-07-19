asddict={'asd':10,'sdf':15,'dfg':31,'fgh':22}
print(list(asddict.items())) #元组组成的list
asd=list(asddict.items())
asd.sort(key= lambda e:e[1],reverse=True) #list排序 设置key

print(asd)

