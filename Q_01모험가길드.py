#공포도가 x면 x명 필요 여행을 떠날 수 있는 그룹 최대값
# 못떠나는 사람 있어도 됨
n= int(input())
x= list(map(int,input().split()))

x.sort()
# 1 2 2 2 3
count=0
r=n
#count 그룹수
#r 잔여 명수?

#while r !=0:
for i in x:
    if r < i:
        # print(r,i,count,'a')
        break
    else:
        r=r-i
        count+=1
        # print(r,i,count,'b')
print(count)




