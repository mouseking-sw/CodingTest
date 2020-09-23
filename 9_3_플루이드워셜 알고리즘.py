INF = int(1e9)

n= int(input())
m= int(input())

graph = [ [INF]*(n+1) for _ in range(n+1)] # N * N 매트릭스가 만들어짐

for a in range(1,n+1):  
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0     # graph[1][1]=0, graph[2][2]=0, grapph[3][3]=0

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b]= c   # a에서 b로 가는 비용이 c라는 뜻

for k in range(1,n+1):  # 플루이드 워셜 알고리즘
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]= min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=' ')
print()

