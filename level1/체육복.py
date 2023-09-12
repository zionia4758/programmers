def solution(n, lost, reserve):
    answer = 0
    wear = [1]*n
    for l in lost:
        wear[l-1] -= 1
    for r in reserve:
        wear[r-1] += 1
    for idx in range(len(wear)):
        if wear[idx] == 0:
            if idx > 0 and wear[idx-1] == 1:
                answer += 1
            elif idx < len(wear)-1 and wear[idx+1] == 2:
                answer += 1
                wear[idx+1] -= 1
        else:
            answer += 1
            wear[idx] -= 1
    return answer
