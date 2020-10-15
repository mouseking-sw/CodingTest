## https://programmers.co.kr/learn/courses/30/lessons/60057 ## 참고

def solution(s):
    answer = len(s)

    for step in range(1,len(s)//2+1):  # 2로나눈 몫에다가 +1   범위 설정 최대로 압축할 수 있는 숫자계산
        compressed =""
        prev = s[0:step]
        count=1
        for j in range(step,len(s),step): # step 증가 시키면서 이전문자와 비교
            if prev == s[j:j+step]:
                count +=1
            else: # 더이상 압축 불가능한 경우
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]
                count =1
        compressed += str(count)+prev if count >= 2 else prev
        answer = min(answer,len(compressed)) #문자열중 짧은 것
    return answer
