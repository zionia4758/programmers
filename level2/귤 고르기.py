def solution(k, tangerine):
    answer = 0
    cnt = {}
    for t in tangerine:
        if t not in cnt:
            cnt[t] = 1
            continue
        cnt[t]+=1

    cntList = list(cnt.values())
    cntList.sort(reverse=True)
    for n in cntList:
        k-=n
        answer+=1
        if k<=0:
            break
    return answer
