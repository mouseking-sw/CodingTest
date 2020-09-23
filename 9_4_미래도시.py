n,m= map(int,input().split())
INF= int(1e9)
graph = [[INF] * (m+1) for _ in range(n+1) ]

for a in range(1,n+1):
    for b in graph:
        if a==b:
            graph[a][b]=0  #자기자신 노드 0으로 초기회

for i in range(m):
    a,b= map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

# 거쳐 갈 노드 k와 최종목적지 노드 x 입력
x,k = map(int,input().split())

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]= min(graph[a][b],graph[a][k]+graph[k][b])

distance = graph[1][k]+ graph[k][x]


if distance >= INF:
    print("-1")

else: 
    print(distance)

