n= int(input())
array = list(map(int,input().split()))
d= [0]*100  # 계산된 결과를  저장함   d[i] i까지 계산된 결과
d[0] = array[0]
d[1] = max(array[0],array[1])

for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+array[i]) # i-1까지의 계산결과와 i-2까지의 계산 결과의 +현재의 배열 더한 것중 큰 값 저장 


print(d[n-1])

