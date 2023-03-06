def solution(n):
    if n == 1:
        return 1
    answer = 0
    #cnt개 -> a~b = b+a/2*cnt=n , b-a=cnt+1 b+a=2n/cnt
    for cnt in range(1,n):
        left = 2*n/cnt-cnt+1
        if left>0 and left%2==0:
            answer+=1
    return answer
