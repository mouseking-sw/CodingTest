n = input()  #문자열 입력

mid =int(len(n)/2) # 문자열의 중간값 인덱스
end =int(len(n))   # 문자열의 끝 인덱스      


print(n[0:mid])
sum1=0 # 처음부터 mid까지 합
sum2=0 # 
for i in n[0:mid]:
    i= int(i)
    sum1+=i

for i in n[mid:end]:
    i=int(i)
    sum2+=i

if sum1==sum2:
    print("LUCKY")
else: 
    print("READY")



