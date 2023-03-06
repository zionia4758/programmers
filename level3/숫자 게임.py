def solution(A, B):
    A.sort()
    B.sort()
    answer = 0
    for a in A:
        while True:
            b=B.pop(0)
            if b>a:
                answer+=1
                break
            if len(B)==0:
                break
        if len(B)==0:
            break
        
    return answer
