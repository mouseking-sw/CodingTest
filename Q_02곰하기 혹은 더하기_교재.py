data =input()

result = int(data[0])

for i in range(1,len(data)):
    num = int(data[i])
    if num <=1 or result <=1:  # 인덱스가 1이면 더하고 1보다 크면 곱한다.
        result +=num
    else:
        result *= num

print(result)