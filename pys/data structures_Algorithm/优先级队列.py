#优先级队列 元素出队列的顺序由优先级决定，可按递增或递减顺序，c++中用堆完成（大根堆、小根堆、stl：priority_queue）
#heapq
import heapq
class PriorityQueue:
    def __init__(self):
        self._queue=[]
        self._index=0
    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]
q=PriorityQueue()
q.push('a',11)
q.push('asd',100)
print(q.pop())
q.push([1,2,3],13)