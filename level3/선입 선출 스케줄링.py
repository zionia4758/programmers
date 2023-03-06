#최대 25000*10000
def solution(n, cores):
    answer = len(cores)
    left = 1
    right = 500000000
    while left<=right:
        mid = (left+right)//2
        cnt = 0
        for c in cores:
            cnt+=mid//c
        if cnt<n-len(cores):
            left = mid+1
        else:
            right = mid-1

    left-=1
    cnt=n-len(cores)
    for c in cores:
        cnt -= left//c
    left+=1
    for i,c in enumerate(cores):
        if left%c==0:
            cnt-=1
        if cnt==0:
            answer=i+1
            break
    
        
    return answer
