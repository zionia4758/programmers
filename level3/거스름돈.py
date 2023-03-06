
def solution(n, money):
    answer = 0
    
    cnt = [0]*(n+1)
    cnt[0]=1

    for m in money:
        for i in range(m,n+1):
            cnt[i]+=cnt[i-m]

    return cnt[n]
    
 
