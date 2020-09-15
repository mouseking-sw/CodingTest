from collections import deque
## deque라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
print (queue)
queue.popleft() # 5 out
queue.append(1)
queue.append(4)
print (queue)
queue.popleft() # 2 out

print(queue)
queue.reverse()
print(queue)


