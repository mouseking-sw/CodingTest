# print(ord('A'))
str1 = input()  # 문자열 입력
array =[]
sum1=0
for i in range(len(str1)):
    a=str1[i]
    if ord('A')<= ord(a):  ## ord('A') : 몇일까? 
        array.append(a)
    else:
        a= int(a)    
        sum1+= a

array.append(sum1)

print(array)   

for i in array:
    print(i,end='')



    




