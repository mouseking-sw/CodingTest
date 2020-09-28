#특정원소 속한 집합 찾기

def find_parent(parent,x):
    if parent[x] !=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent( parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b) # 두 원소가 속한 집합 찾기
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
# 노드의 개수와 간선의 개수 입력
v,e = map(int,input().split())
parent =[0]*(v+1)

edges=[]
reuslt = 0

for i in range (1,v+1): # 부모를 자기자신으로 초기화
    parent[i]=i

for _ in range(e):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()
result=0
for edge in edges:
    cost,a,b = edge

    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
print(result)
