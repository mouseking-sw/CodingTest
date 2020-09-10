#서로소 집합 알고리즘
def find_parent(parent,x): # 부모를 찾는다. x에대하여 최종root  # parent 변수의 의미? 
    
    if parent[x] != x: # 자기 자신이 부모가 아니면  최초의 경우 자기자신이 부모로 설정되어 있다고 생각해야 할 것
        parent[x]=find_parent(parent,parent[x]) #자신의 부모의 부모를 찾는다 
    return find_parent[x]  # x= find_parent[x] 의 경우를 계속 찾는다.

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
    parent[i]=i # 부모를 자기 자신으로 초기화

for i in range(e):
    a,b = map(int,input().split()) # a: 입력노드  b:  입력노드 부모(루트)
    union_parent(parent,a,b)

print('각 원소가 속한 집합:', end='')
for i in range(1,v+1):
    print(find_parent(parent,i),end='')
print()

print('부모 테이블: ', end='' )
for i in range(1,v+1):
    print(parent[i], end=' ')


