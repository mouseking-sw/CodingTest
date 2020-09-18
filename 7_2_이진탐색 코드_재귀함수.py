def binary_search(array,target,start,end):
    if start > end:
        return None
    mid = (start + end) // 2 ## 소수점 버림 중간점 찾기
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1) # mid 보다 큰 부분을 날려버린다. mid -1임을 유의
    else: 
        return binary_search(array,target,mid+1,end)  # mid 보다 작은 부분을 날려버린다. mid +1임을 유의

n, target =list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array,target,0,n-1)

if result ==None:
    print("원소가 존재하지 않습니다.")
else: 
    print(result+1)  # index는 0 부터 시작하니까