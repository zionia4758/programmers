from collections import defaultdict as dd
import heapq
def travel(tCnt,tHash,start,answer):
    canMove = tHash[start]
    if len(answer)==tCnt+1:
        return True
    for nextT in canMove:
        if nextT[1]:
            continue
        answer.append(nextT[0])
        nextT[1]=True
        if travel(tCnt,tHash,nextT[0],answer):
            return True
        answer.pop()
        nextT[1]=False
    return False
        
    

def solution(tickets):
    answer = ['ICN']
    tCnt = len(tickets)
    tHash = dd(list)
    for t in tickets:
        tHash[t[0]].append([t[1],False])
    for h in tHash:
        tHash[h].sort()
    cnt = 0
    travel(tCnt,tHash,'ICN',answer)
    
    return answer
