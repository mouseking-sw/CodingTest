from collections import deque  # deque라이브러리

def bfs(graph,start,visited):
    queue =deque([start])
    visited[start]= True

    while queue: # queue 빌때 까지
        v = queue.popleft()
        print(v,end=' ')

        for i in graph[v]:
            if not visited[i]: #방문하지 않았다면 queue삽입
                queue.append(i)
                visited[i]= True

graph = [
    [],
    [2,3,8],
    [1,7,],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]

]
visited = [False]*9  # 초기 방문자 리스트 False로 초기화
bfs(graph,1,visited) # 1번 노드 부터 시작