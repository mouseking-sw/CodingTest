n="567"

#숫자형태의 문자열을  공백없이 입력 받을 때 방법
a=[]

for i in range( len(n) ) :
    a.append(int(n[i]))
sum =0
print(a)

for i in a:
    if sum + i > sum * i:
        sum=sum+i
        print(i,sum,1)
    elif sum + i < sum * i:
        sum=sum* i
        print(i,sum,2)
    else:
        sum=sum+i
        print(i,sum,3)

print(sum)





