from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for s in permutations(dungeons,len(dungeons)):
        p = k
        cnt = 0
        for d in s:
            if p<d[0]:
                continue
            p-=d[1]
            cnt += 1
        answer = max(answer,cnt)
    return answer
