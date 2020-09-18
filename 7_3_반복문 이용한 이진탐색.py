def binary_search(array, target,start,end):
    while start <= end:
        mid = (start + end) //2  # 몫만 챙기기  소수점 버림
        if array[mid] == target:
            return mid # 값을 찾았으면 함수 종료 mid값 반환
        elif array[mid] > target:  # target보다 큰 쪽은 버림
            end = mid - 1
        else:
             start = mid +1 # target보다 작은 쪽은 버림
    return None   ### 없을 경우 None

n, target = list(map(int,input().split()))
array = list(map(int, input().split()))


result = binary_search(array, target,0, n-1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1) 






    
    