import numpy as np
def solution(begin, target, words):
    if target not in words:
        return 0
    #by BFS
    
    if begin not in words:
        words.insert(0,begin)
    transMap = {}
    wLen = len(words[0])
    
    for w in words:
        transMap[w]=[]
        for otherW in words:
            if otherW == begin:
                continue
            cnt = 0
            for c in zip(w,otherW):
                if c[0]==c[1]:
                    cnt+=1
            if cnt == wLen-1:
                transMap[w].append(otherW)
    
    alreadyMove = []
    nextMove = [(begin,0)]
    while len(nextMove)>0:
        cur,cnt = nextMove.pop(0)
        moveList = transMap[cur]
        for nextW in moveList:
            if nextW == target:
                return cnt+1

            if nextW not in nextMove:
                alreadyMove.append(nextW)
                nextMove.append((nextW,cnt+1))
        
    
    '''
    
    ##other answer by graph
    
    print(transMap)
    graph = np.array([[0]*len(words) for i in range(len(words))])
    for i in range(len(words)):
        w = words[i]
        for toW in transMap[w]:
            graph[i][words.index(toW)]=1
    arriveGraph = np.array(graph[:])
    endIdx = words.index(target)

    cnt = 1
    while arriveGraph[0][endIdx] == 0:
        arriveGraph = arriveGraph @ graph
        cnt += 1
        if cnt == len(words):
            return 0
    return cnt
    
    '''
    
    
    answer = 0
    return answer
