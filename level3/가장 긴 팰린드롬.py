#ret[idx]=idx기준 가장 긴 팰린드롬
#2500*1250
def solution(s):
    answer = 1
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for l in range(0,len(s)):
        for r in range(l+1,len(s)+1):
            substr = s[l:r]
            if substr == substr[::-1]:
                answer=max(answer,len(substr))
    return answer

