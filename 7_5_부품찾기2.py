
def binary_search (instock,target,start,end): # 배열, 목표값, 인덱스시작, 인덱스끝
    while start<=end:
        mid = (start+end) //2
        if  instock[mid]==target:
            return mid
        elif instock[mid] > target:
            end= mid-1
        else:
            start = mid +1
    return None  ## 다 뒤져 봤는데 없어 그럼 None으로 return해야지 while문 안에 들어가 있지 않다는 것에 유의

n= int(input())
instock= list(map( int,input().split()))
instock.sort()  # 이진탐색은 전제조건이 순차 정렬 이다.
m= int(input())
finding = list(map( int,input().split()))


for i in finding:
    result=binary_search(instock,i,0,n-1) 
    if  result != None:
        print('yes',end=' ')
    else:   
        print('no',end=' ')
