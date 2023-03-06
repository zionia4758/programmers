from itertools import product
def solution(k, d):
    answer = 0
    dExp = d**2
    l=[i*k for i in range(d//k+1)]
    for x in l:
        remain = (dExp - x**2)**0.5
        answer += remain//k+1
        
    return answer
