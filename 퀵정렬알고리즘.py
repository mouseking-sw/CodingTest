array =[5,7,9,0,3,1,6,2,4,8]


def quick_sort(array,start,end):
    if start >=end:
        return
    pivot = start # 왼쪽 은 작은수 오른쪽은 큰수 증가 인덱스를 시켜가며 비교 할 값
    left = start+1
    right =end
    while left <=right:
        
        while left <=end and array[left] <= array[pivot]: # 인덱스를 하나씩 증가시키면서 피봇보다 작은값
            left +=1
        while right > start and array[right]>= array[pivot]: # 인덱스를 하나씩 감소시키면서 피봇보다 큰 값
            right -=1
        if left > right : # 엇갈렸다면(왼쪽이 크다면 ) 피봇과 right를 교체함
            array[right], array[pivot]= array[pivot], array[right]
        else:
            array[left],array[right]= array[right],array[left]
    quick_sort(array,start,right-1) # right를 기준으로 왼쪽 재귀적 수행
    quick_sort(array,right+1,end)   # right를 기준으로 오른쪽 재귀적 수행


quick_sort(array,0, len(array)-1)
print(array)

        