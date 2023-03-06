#123 223 333

def solution(n, left, right):
    answer = []
    for idx in range(left,right+1):
        y=idx//n
        x=idx%n
        answer.append(max(y,x)+1)
    
    return answer
