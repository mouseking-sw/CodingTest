n,k= map(int,input().split())
a= list(map( int, input().split()))
b= list(map( int, input().split()))

while k!=0 : # a의 최소값과 b의 최대값과 바꾼다
    min_a =min(a)
    idx_a=a.index(min_a)
    max_b =max(b)
    idx_b=b.index(max_b)
    a[idx_a],b[idx_b]= b[idx_b],a[idx_a]
    k-=1 
print(sum(a))




