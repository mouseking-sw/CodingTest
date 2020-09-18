n,k = map(int,input().split())
a= list(map( int, input().split()))
b= list(map( int, input().split()))

a.sort()     #  a는 오름차순으로 정렬
b.sort(reverse=True) #b는 내림차순으로 정렬

for i in range(k):
    if a[i] <b[i]:
        a[i],b[i]=b[i],a[i]

    else: 
        break
print(sum(a))