graph = [ [] for i in range(3)]

# 0번 노드에 연결된 노드 정보 (1,7) 1반 노드이고 7의 비용이 발생한다.
graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7)) # 1번 노드가 0번노드에 연결 되어 있고 비용은 7

graph[2].append((0,5)) # 2번 노드가 0번노드에 연결 되어 있고 비용은 5

print(graph)
