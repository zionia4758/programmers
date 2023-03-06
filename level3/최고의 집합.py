def solution(n, s):
    if n>s:
        return [-1]
    if s%n==0:
        return [s/n]*n
    else:    
        avgNum = s//n+1
        avgDownNum = s//n
        return [avgDownNum]*(n-s%n)+[avgNum]*(s%n)
    return answer
