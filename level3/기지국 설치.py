import math
def solution(n, stations, w):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    startRange = 1
    for i in stations:
        answer += math.ceil((i-w-startRange)/(2*w+1))
        startRange = i+w+1

    if startRange<=n:
        answer += math.ceil((n-startRange+1)/(w*2+1))
    return answer
