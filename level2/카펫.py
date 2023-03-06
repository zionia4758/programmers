#yellow = n*m일때
#brown = 2(n+m)+4
def solution(brown, yellow):
    answer = []
    for n in range(1,int(yellow**0.5)+1):
        
        if yellow%n !=0:
            continue
        m=yellow//n
        if n+n+m+m+4 == brown:
            answer=[m+2,n+2]
    return answer
