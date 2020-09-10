def find_parent(parent,x):

    if parent[x] != x:
        return find_parent(parent,parent[x])
    return x    

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:  # 작은수가 부모가 된다.
        parent[b]=a
    else:    
        parent[a]=b

v,e = map(int,input().split()) # V: 노드의 갯수, e: 간선의 수

parent= [0]*(v+1) 

for i in range(1,v+1):
    parent[i]=i

for i in range(e):
    a,b = map(int,input().split())
    union_parent(parent,a,b)

print('각 원소가 속한 집합:', end='')
for i in range(1,v+1):
    print(find_parent(parent,i),end='')
print()

print('부모 테이블: ', end='' )
for i in range(1,v+1):
    print(parent[i], end=' ')


