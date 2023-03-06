#시간에 대해 이분탐색
#t에 대해 n이 True일떄까지
def solution(n, times):
    answer = 0
    #기저사례
    left = min(times)
    #최악의 경우에 모든 사람이 심사
    right=max(times)*n
    
    while left<=right:
        t=(left+right)//2
        avail = sum([t//i for i in times])
        
        #t는 불가 그러므로 left를 t+1부터 탐색
        if avail<n:
            left = t+1
        #t는 가능 t-1도 되는지 확인
        #left = right일 때 가능하면 종료조건포함
        else:
            right = t-1
            
    return left
