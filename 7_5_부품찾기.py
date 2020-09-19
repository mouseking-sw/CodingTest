n= int(input())
instock= list(map( int,input().split()))
m= int(input())
finding = list(map( int,input().split()))

for i in finding:
    if i in instock:
        print('yes',end=' ')
    else:
        print('no', end=' ') 