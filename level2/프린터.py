import heapq
def solution(priorities, location):
    answer = 1
    q=priorities
    p_list = sorted(priorities,reverse = True)
    while True:
        next_p = q.pop(0)
        if next_p == p_list[0]:
            p_list.pop(0)
            if location==0:
                break
            answer += 1
        else:
            q.append(next_p)
        location = (location-1)%len(priorities)
    return answer
