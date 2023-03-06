def solution(n):
    answer = 0
    step = [0]*(n+2)
    step[0]=1
    for i in range(n):
        step[i+1]+=step[i]
        step[i+2]+=step[i]
    
    return step[n]%1234567
