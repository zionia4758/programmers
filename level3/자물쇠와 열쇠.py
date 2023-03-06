#열쇠 1(돌기) 가 자물쇠 0(홈)과 만나야함
#lock 좌표 기준  -n+1 ~m+n-1 위치까지 
from itertools import product
def rotate(key):
    r_key = [list(l) for l in zip(*key[::-1])]
    return r_key
def put_key(n,m,x,y,key,lock):
    cnt = 0
    for dy in range(n):
        for dx in range(n):
            py = dy+y
            px = dx+x
            if px<0 or py<0 or px>=m or py>=m:
                continue
            if lock[py][px]==0 and key[dy][dx]==1:
                cnt+=1
            if lock[py][px]==1 and key[dy][dx]==1:
                return -1
    return cnt
    
    
def solution(key, lock):
    n=len(key)
    m=len(lock)
    answer = True
    r_key = [key]
    target_cnt =0
    for l in lock:
        target_cnt+= l.count(0)
    for i in range(3):
        r_key.append(rotate(r_key[-1]))
    
    for y in range(-n+1,m+n):
        for x in range(-n+1,m+n):
            for r in r_key:
                result = put_key(n,m,x,y,r,lock)
                if result == target_cnt:
                    return True
    
    
    
    return False
