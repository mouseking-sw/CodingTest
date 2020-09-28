from collections import deque

v,e =map(int,input().split())
indegree= [0]* (v+1)

graph = [ [] for i in range(v+1) ]
result =[]

for _ in range(e):  # 간선정보 입력
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] +=1

def topology_sort(): # 위상정렬 함수 구현
    result =[]
    q= deque()
    
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)

    while q:  #queue가 빌 때까지
        now =q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -=1
            if indegree[i] == 0:
                q.append(i)


for i in result:
    print(i,end=' ')

topology_sort()
print(graph)




