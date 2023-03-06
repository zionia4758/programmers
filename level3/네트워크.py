def solution(n, computers):
    answer = 0
    linkGraph = {}
    for x in range(n):
        linkGraph[x]=[]
        for y in range(n):
            if x==y:
                continue
            if computers[x][y]==1:
                linkGraph[x].append(y)
    cnt =0
    comList = [i for i in range(n)]
    while len(comList)>0:
        i=comList.pop(0)
        curLink = [i]
        nextFind = linkGraph[i]
        while len(nextFind)>0:
            nextIdx = nextFind.pop(0)
            if nextIdx not in curLink:
                curLink.append(nextIdx)
                nextFind+=linkGraph[nextIdx]
                comList.pop(comList.index(nextIdx))

        answer+=1
    return answer
