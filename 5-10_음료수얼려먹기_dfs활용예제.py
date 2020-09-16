
n,m = map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):

    if x<=-1 or x>= n or y<=-1 or y>= m: 
        return False
    if graph[x][y]==0: # 0인데 아직 방문하지 않았다면, 방문처리

        graph[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False  #구역을 벗어나거나 값이 0이 아니면(1이면) False를 리턴

result =0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result+=1

print(result)


