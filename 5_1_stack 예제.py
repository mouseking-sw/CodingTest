stack =[]
# 삽입(5)-삽입(2)-삽입 (3)-삽입 (7)-삭제()- 삽입(1) -삽입(4)-삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])  ## stack 처음부터 끝까지 -1 칸 간격으로 역순으로

print(stack[::2])  ## index 처음부터 끝까지 2칸 간격으로 


