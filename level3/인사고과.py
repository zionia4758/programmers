#사원끼리 비교 100000 * 100000 너무큼
#평가합이 높다 -> 작은 사람보다 절대 둘다 작을 수 없다
#각 a점수별 max b값을 저장하여 O(1)로 탐색가능하게 처리

def solution(scores):
    answer = 1
    
    #max(scores)도 [0]값의 max를 찾으나 확실하게 하기 위해
    max_a = max(list(zip(*scores))[0])
    wan = scores.pop(0)
    max_list = [0]*(max_a+2)
    scores = list(filter(lambda x:x[0]+x[1]>sum(wan),scores))
    for s in scores:
        max_list[s[0]]=max(max_list[s[0]],s[1])
    max_val = 0
    for i in range(max_a,-1,-1):
        max_val = max(max_list[i],max_val)
        max_list[i] = max_val
    if max_list[wan[0]+1]>wan[1]:
        return -1
    for s in scores:
        if max_list[s[0]+1]>s[1]:
            continue
        answer += 1
    
    return answer
