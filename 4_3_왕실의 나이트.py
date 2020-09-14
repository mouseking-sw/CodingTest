xy=input()
xy= list(xy)
convert = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8} # 문자열을 dictionary type으로 활용
### y = int(ord(input_data[0])) - int(ord('a'))+ 1 ## ASCII 코드를 숫자화 하는 방법을 사용 할 수도 있음

x= convert[xy[0]]
y= int(xy[1])
count = 0
type1= [(-2,1),(2,1),(-2,-1),(2,-1)
        ,(1,2),(1,-2),(-1,2),(-1,-2)]
print(x,y)
for i in type1:
    x2=x + i[0]
    y2=y + i[1]
    print(i,x,y)
    if (x2>=1  and x2 <= 8) and (y2>=1 and y2 <= 8):
        count+=1
print(count)



