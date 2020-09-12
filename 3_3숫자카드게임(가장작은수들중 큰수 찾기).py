#가장 작은수들중 큰 수 찾기
n, m = map( int, input().split() )   #가로:m(열) # 세로(행) n
arr=[]
for i in range(n):
    a= list( map(int, input().split()) )
    arr.append(a)
# print(arr)
min_list=[0] * m # 행별로 최소 값을 기록하는 리스트를 만듬
for i in range(n):
    min_list[i]=min(arr[i])
print(max(min_list))



# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

#2

# 2 4
# 7 3 1 8
# 3 3 3 4

# 3
