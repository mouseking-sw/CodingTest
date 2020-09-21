def fibo(x):
    if x==1 or x==2:
        return 1
    return fibo(x-1)+fibo(x-2)  # 
print(fibo(4))
    ### 이 함수를 사용할경우 했던 계산을 반복적으로 수행하기 때문에 불필요한 연산이 많다는 단점 
    