n= input()
n= int(n)
lst = input().split()
x=1
y=1
for i in lst:
    if i=='R':
        if x+1 > n:
            continue
        else:
            x=x+1
    if i=='L':
        if x-1 < 1:
            continue
        else:
            x=x-1
    if i=='U':
        if y-1<1:
            continue
        else:
            y=y-1
    if i=='D':
        if y+1>n:
            continue
        else:
            y=y+1

print(y,x)




         

