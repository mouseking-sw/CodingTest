data = input()
count0 =0 #전부 0으로 바뀌는 경우
count1 =0 #전부 1로 바뀌는 경우

if data[0] =='1': #문자열중 맨 첫번째 
    count0 +=1  # 0은 1로 바꿔야 하기 때문에 숫자 0의 경우 전부 1로 바뀌는 경우 count
else:
    count1 +=1

for i in range( len(data)-1): # 두번째열부터 
    if data[i] != data[i+1]: # data[0] != data[1] .... 데이가 연속되지 않는 경우
        if data[i+1]=='1': # 다음수에서 1로 바뀌면
            count0 +=1     # 000000... 으로 카운트 증가
        else:              ## 다음수에서 0으로 바뀌면
            count1 +=1     # 111111.. 으로 카운트 증가

print(min(count0,count1))
