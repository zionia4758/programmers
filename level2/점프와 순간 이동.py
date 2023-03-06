def solution(n):
    ans = 0
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    ans = bin(n)[2:].count('1')

    return ans
