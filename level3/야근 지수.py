from collections import Counter
def solution(n, works):
    answer = 0
    if n>=sum(works):
        return 0
    workList = Counter(works)
    print(workList)
    key = max(list(workList.keys()))
    while n>0:
        if n >= workList[key]:
            cnt = workList[key]
            n-=cnt
            workList.update(Counter({key-1:cnt}))
            workList.pop(key)
        else:
            workList[key]-=n
            workList.update({key-1:n})
            n=0
        key = max(list(workList.keys()))
        if n==0:
            break
    print(workList)
    for key in workList.keys():
        answer += key*key*workList[key]
    return answer
