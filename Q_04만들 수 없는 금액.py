n = int (input())

array=[0]*99
l = list( map(int,input().split()) )  # 변수 입력
x = []
l.sort() # 순차로 정렬
s=0
for i in range(1,100):
    array[i-1]=i

while l:         # 만들수 있는 모든 수의 집합 첫번째열 부터 순차적으로 덧셈후 다 더한 인덱스는 팝업 
    for i in l:
        s=s+i
        x.append(s)
    l.pop(0)
    s=0    



array = set(array)
x= set(x)    # 차집합 활용을 위해 set type으로 변환
m= array- x  
m = list(m)
min(m)

print(min(m)) # 만들어지지 못한 수중 가장작은 수 출력