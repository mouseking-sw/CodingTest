import sys
input = sys.stdin.readline
INF = int(1e9)

n,m =map(int,input().split())

start = int(input())
graph=[[] for i in range(n+1)] ## [[], [], [], [], [], [], [], [], [], []]... 이런 형태가 된다.

visited= [False]*(n+1)    #방문자 테이블
distance = [INF]* (n+1)     #최단 거리 테이블

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c)) # 


def get_smallest_node():
    min_value =INF
    index =0
    for i in range(1,n+1):
        if distance[i]< min_value and not visited[i]:
            min_value = distance[i]
            index=i
    return index


def dijkstra(start):

    distance[start]=0
    visited[start]= True
    for j in graph[start]:
        distance[j[0]]= j[1]

    for i in range(n-1):
        now = get_smallest_node()
        visited[now] =True

        for j in graph[now]:
            cost= distance[now]+ j[1]

            if cost< distance[j[0]]:
                distance[j[0]]=cost
dijkstra(start)

for i in range(1,n+1):
    if distance[i]== INF:
        print("INFINITY")
    else:
        print(distance[i])
# print(graph)

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
# graph= [[], [(2, 2), (3, 5), (4, 1)], [(3, 3), (4, 2)], [(2, 3), (6, 5)], [(3, 3), (5, 1)], [(3, 1), (6, 2)], []]