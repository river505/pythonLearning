import  collections as cl
q=cl.deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
print(q)

q.appendleft(4)
print(q)

q.pop()
print(q)

print(q.popleft())
print(q)

q.append([1,2,3,4,5,6,7])
print(q)

q.append('asd')
print(q)
try:
    q.append(q[1,2]) #不能同时加两个
except:
    q.extend(q[1]) #extend里边要加 列表 等 可迭代对象
print(q)