#len(g or s) = 도시의 개수
#g,s = 금 은 보유량
#w = 최대 운반량
#t = 이동 시간
#각 도시들에서 a,b만큼의 금과 은을 가져오기
#운영체제 알고리즘 응용해야할듯 (x)
#이때 금과 은을 얼마만큼 가져올지 어떻게 정해야 할까? (x)

#도시의 개수가 많다 = 이진탐색 사용

def solution(a, b, g, s, w, t):
    
    #자원을 정해진 시간동안 가져올 수 있는 양을 계산하자
    def take_limit(i, time):
        #(2n-1)t=time
        max_trial = (time//t[i] +1)//2 
        return min(max_trial * w[i], g[i]+s[i])
    
    def can_make(time):
        move_sum = 0
        a_sum = 0
        b_sum = 0
        move_list = []
        #g,s와 각 도시별 trial동안 운반가능한 자원을 배열로 관리하자
        for i in range(len(g)):
            max_move = take_limit(i,time)
            move_list.append(max_move)
            a_sum += min(g[i],max_move)
            b_sum += min(s[i],max_move)
        #각 도시별 운반가능량과 g,s가 있을 때 어떻게 운송 비율을 최적화할까?
        # print(move_list)
        
        
        #test용 - 대부분 케이스에서 성공. 자원이 극단적인 케이스에서 실패
        if sum(move_list) >= a+b and a_sum >=a and b_sum>=b:
            return True
        else:
            return False
        
    
    bottom = 0
    top = 10**16
    
    mid = (bottom+top)//2
    while mid < top:
        #운반가능
        # print(mid)
        if can_make(mid):
            top = mid
            mid = (top+bottom)//2
            
        
        #운반 불가능
        else:
            bottom = mid+1
            mid = (top+bottom)//2
    
    return bottom
