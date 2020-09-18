array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array [1:] # 1을 제외한 리스트 최초의 피벗은 0 인덱스 이므로

    left_side= [ x for x in tail if x< pivot] # pivot 보다 작은 값  리스트 
    right_side= [ x for x in tail if x> pivot] # pivot 보다 큰 값  리스트 

    return quick_sort(left_side)+[pivot]+ quick_sort(right_side) 
print(quick_sort(array))