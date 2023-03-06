import heapq

def solution(operations):
    answer = []
    for op in operations:
        ops = op.split(" ")
        comd = ops[0]
        num = int(ops[1])
        
        if comd == 'I':
            heapq.heappush(answer,num)
        elif comd == 'D':
            if len(answer) ==0:
                continue
            if num == 1:
                newAnswer = heapq.nsmallest(len(answer)-1,answer)
                heapq.heapify(newAnswer)
                answer = newAnswer
            elif num == -1:
                heapq.heappop(answer)

    if len(answer) == 0:
        return [0,0]
    else:
        return [max(answer),min(answer)]
