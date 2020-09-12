#N이 1이 될 때 까지 작업 반복수행 N에서 1을 뺀다 K로 나눈다. 최소 횟수는?
n, k = map(int,input().split())
count=0
while n != 1:
    if n%k == 0:
        n=n/k
        count +=1
        print(n)
    else:
        n=n-1 
        count +=1
        print(n)
print(count)
