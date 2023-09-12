#n -> n 1,n-1 2,n-2 .. n-1,1
#카탈랑수
def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    
    cnt = [0]*(n+1)
    cnt[0] = 1
    cnt[1] = 1
    cnt[2] = 2
    cnt[3] = 5
    for i in range(4,n+1):
        for j in range(1,i+1):
            # print(j,i-j)
            cnt[i] += cnt[j-1]*cnt[i-j]

    # print(cnt)
    
    return cnt[n]

