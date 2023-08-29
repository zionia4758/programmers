answer = []

def move(n,pivot,sub,target):
    if n == 1:
        answer.append([pivot,target])
    else:
        move(n-1,pivot,target,sub)
        answer.append([pivot,target])
        move(n-1,sub,pivot,target)
    

def solution(n):
    move(n,1,2,3)
    
    return answer
