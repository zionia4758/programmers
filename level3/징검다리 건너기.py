#mid만큼 건넜을 때 0인구간이 k개 이상인지 이분탐색
def solution(stones, k):
    left = 1
    right = 200000000
    while left<=right:
        tempStone = stones[:]
        mid = (left+right)//2
        cnt = 0
        for stone in tempStone:
            
            if stone>mid:
                cnt = 0
            else:
                cnt+=1
            if cnt==k:
                break
        #mid건널수 없다
        if cnt ==k:
            right = mid-1
        #mid+1 건널 수 있다
        else:
            left = mid+1
    return left
