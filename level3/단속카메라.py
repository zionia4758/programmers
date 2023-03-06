def solution(routes):
    answer = 0
    routes.sort(key = lambda k:k[0])
    end = routes[0][1]
    for r in routes:
        if r[0]>end:
            answer +=1
            end = r[1]
        else:
            end = min(end,r[1])
    answer += 1
    return answer
