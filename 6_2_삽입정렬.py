array =[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)): # 1부터 시작하는 이유는? i-1번 시행을 위해서?
    for j in range(i,0,-1): # 역순으로 왼쪽으로 이동
        if array[j] < array[j-1]: 
            array[j],array[j-1] = array[j-1],array[j]
        else:  #삽입될 데이터 보다 작은 데이터를 만나면 멈춘다
            break
print(array)
    