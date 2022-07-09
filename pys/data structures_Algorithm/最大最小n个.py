import heapq
#1.最大最小n个
'''
nums=input()
nums=[int(i) for i in nums.split()]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(4,nums))
'''

#2.按某项排序
datas_1=[['asd',12],['dsa',13],['ads',14],['das',15],['ads',16]]
datas_1.sort(reverse=True)
print(datas_1)
datas_1.sort(reverse=True,key=lambda s:s[1])
print(datas_1)

print(heapq.nlargest(2,datas_1,key=lambda s:s[1]))

datas_2=[{'name':'chen','ages':22},{'name':'zhang','ages':19},{'name':'li','ages':21},{'name':'wang','ages':20}]
print(heapq.nlargest(2,datas_2,key=lambda s:s['ages']))