import heapq
import sys
input =sys.stdin.readline
INF= int(1e9)

n,m = map(int,input().split())
start = int(input())

graph= [[]for i in range(n+1)]  ## [[], [], [], [], [], [], [], [], [], []]... 이런 형태가 된다.

distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c)) #   [[], [(2, 3), (4, 5)], [], [], [], [], [], [], [], []] graph[1]에서 (2,3),(4,3)을 append했을 경우
                           #   [(2, 3), (4, 5)]  1번 노드에서 2노드로 가는데 비용이 3  4노드로 가는데 비용이 5

def dijkstra(strat):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist, now = heapq.heappop(q) # (거리, 노드)

        if distance[now]<dist:
            continue  # 현재 노드가 처리된 적이 있다면 무시!   힙에 있던 거리보다 작다면 이미 처리된 적이 있다고 본다. 
        
        for i in graph[now]:
            cost = dist +i[1] # i[1]은 노드의 비용을 나타낸다 graph[1][1]->>> 

            if cost < distance[i[0]]: #다른 노드를 거쳐 이동하는 거리가 더 짧은 경우
                distance[i[0]]= cost      # 작은 cost로 distance table을 갱신
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])

# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2    
