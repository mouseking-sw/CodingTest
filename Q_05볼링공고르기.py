n,m =  map(int,input().split())
a = list( map(int,input().split()) ) 
a.sort()
# app=0
arr =[]
for i in range(n): 
    for j in range(n):
        if i != j:
            app= (a[i],a[j])
            arr.append(app)
print(arr)

## set 자료형으로 전환하여 중복 제거
arr= set(arr)  
arr= list(arr)



print(len(arr))
print(arr)