n = int (input())

a= n//5
b= n%5
count=1
while a!=0:
    a=a//5
    count+=1
while b !=1:
    if b % 2 ==0:
        b= b/2
        count+=1
    else:
        b=b-1
        count+=1
print(count)




