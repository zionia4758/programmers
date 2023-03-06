from queue import PriorityQueue
def solution(n, k, enemy):
    answer = 0
    enenmySum = 0
    defenceCnt = 0
    dList = PriorityQueue()
    for num in enemy:
        if defenceCnt < k:
            dList.put(num)
            answer+=1
            defenceCnt += 1
            continue
        else:
            minD = dList.get()
            dList.put(max(minD,num))
            num = min(minD,num)
            n -= num
            if n <0:
                break
            else:
                answer+=1
    
    return answer
