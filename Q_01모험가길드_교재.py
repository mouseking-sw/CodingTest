n = int(input())
data = list(map(int,input().split()))
data.sort()

result =0 # 총그룹수
count=0 # 모험가의 수 

for i in data: # 공포도를 낮은 것부터 하나씩
    count +=1 # 현재 그룹에 해당 모험가 포함 시키기
    if count>= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 
        result +=1 # 그룹 증가시키기
        count =0 

print (result)