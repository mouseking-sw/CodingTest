n,m = map(int,input().split())
array= list(map(int,input().split()))

start=0
end = max(array)

result= 0

while start <= end:
    total = 0
    h = (start + end) //2
    for x in array:
        if x > h:  #떡이 짤림
            total += x- h #짤린떡 더하기 
    if total < m: # 떡의 양이 부족한 경우(떡 짤린 토탈이 m에 미치지 않으면 )
        end = h -1 # 기계 길이를 줄인다.

    else:  #떡이 충분히 짤린 경우
        result = h # 떡 짜르는 기계 길이 저장
        start = h +1

print (result)
