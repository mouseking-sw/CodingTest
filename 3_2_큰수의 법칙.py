## 배열의 크기:n, 숫자가 더해지는 횟수: m, k, 연속해서 더해 질 수 있는 횟수##
n,m,k =map( int, input().split() )
print(n,m,k)
data = list( map(int, input().split() ) )
print(data)
data.sort()
data.reverse()
sum=0
for i in range(m): # 0~ m-1 :m개
    if k > 0: #연속해서 k번을 더 할 수 있을 경우
        sum+= data[0]
        k= k-1
    elif k==0: # 연속해서 k번을 더할 수 없을 경우
        sum+= data[1]
        k=3
print(sum)    

    

# data = list(map(int,data))
# print(data)
