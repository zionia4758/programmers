
def solution(s):
    answer = ''
    numS = list(map(int,s.split()))
    
    return str(min(numS))+" "+str(max(numS))
