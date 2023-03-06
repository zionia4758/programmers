from itertools import permutations
def matchId(u,b):
    if len(u)!=len(b):
        return False
    for i in range(len(u)):
        if b[i]=='*':
            continue
        if b[i]!=u[i]:
            return False
    return True
        
def solution(user_id, banned_id):
    userLen = len(user_id)
    banLen = len(banned_id)

    answer = 0
    caseList=set()
    for idxs in permutations(range(userLen),banLen):
        flag = True
        oneCase = []
        for i in range(len(idxs)):
            if not matchId(user_id[idxs[i]],banned_id[i]):
                flag=False
                break
            oneCase.append(user_id[idxs[i]])
        if flag:
            caseList.add(tuple(sorted(idxs)))
    answer= len(caseList)
    return answer
