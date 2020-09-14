n= int(input())
count=0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):  ## 시, 분, 초중에 하나라도 3이 있으면 count
                count+=1
                print(h,m,s)
                
print(count)
