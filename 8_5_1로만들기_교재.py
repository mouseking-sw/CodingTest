x = int(input())

d = [0] * 300013

for i in range(2,x+1): # 2부터 x까지  #1을 더해주는 건 함수의 호출 횟수 때문
    d[i]= d[i-1]+1
    if i%2 == 0:
        d[i]=min(d[i],d[i//2]+1)
    if i%3 == 0:
        d[i]=min(d[i],d[i//3]+1)
    if i%5 == 0:
        d[i]=min(d[i],d[i//5]+1)
print(d[x])