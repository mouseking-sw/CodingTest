array = [7,5,9,0,3,1,6,2,4,8]
for i in array(len(array)):
    min_index = i
    for j in range(j+1,len(array)):
        if array[min_index] > array[j]: # 현재까지 최소 값 인덱스와 비교하면서 값이 작으면 작은 값의 인덱스를 min_index 저장 
            min_index =j
    array[i],array[min_index] = array[min_index], array[i] # 파이썬 문법인데 array[i]<=>array[min_index] 값을 스위치 할 수 있다
print(array)
