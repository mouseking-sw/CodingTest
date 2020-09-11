n= 1260
count=0

list= [500,100,50, 10]  # 큰 수 부터 배열
print(list)
for coin in list:
    count += n//coin
    n %= coin
print(count)
