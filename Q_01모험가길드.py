#공포도가 x면 x명 필요 여행을 떠날 수 있는 그룹 최대값
# 못떠나는 사람 있어도 됨
n= int(input())
x= list(map(int,input().split()))

x.sort()
x.reverse()
count=0
r=n
#count 그룹수
#r 잔여 명수?

while r !=0:
    for i in x:
        if r ==0:
            break
        else:
         r=r-i
         count+=1
print(count)

### 남은 그룹이 있어도 된다는 점에서 착안 가장 공포도가 높은 그룹부터 그룹화 후 count 1+ 





