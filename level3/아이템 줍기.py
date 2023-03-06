#(x1-px)*(x2-px) 와(y1-py)*(y2-py) 하나는 0 하나는  0 이하-> 도형위
#(x1-px)*(x2-px)<0 and (y1-py)*(y2-py)<0 -> 도형 안
#나머지 -> 도형 밖

def isEdge(rectangle, point):
    result = False
    for r in rectangle:
        caseOne = (r[0]-point[0])*(r[2]-point[0])
        caseTwo = (r[1]-point[1])*(r[3]-point[1])
        #도형안에 점이 존재
        if caseOne<0 and caseTwo <0:
            return False
        #도형위에 점이 존재
        if caseOne*caseTwo == 0 and caseOne+caseTwo<=0:
            result=True
        #그 외는 도형 밖에 점이 존재
    return result
        

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 10000
    for r in rectangle:
        r[0]*=2
        r[1]*=2
        r[2]*=2
        r[3]*=2
    item = [itemX*2, itemY*2]
    pos = [characterX*2,characterY*2]
    direct = [[1,0],[-1,0],[0,1],[0,-1]]
    #첫 방향 
    for firstDirect in direct:
        #절반만 움직여보기
        nextPos = [pos[0]+firstDirect[0],pos[1]+firstDirect[1]]
        before = pos[:]
        if isEdge(rectangle,nextPos):
            cnt = 1
            nextPos[0]+=firstDirect[0]
            nextPos[1]+=firstDirect[1]
            while nextPos != item:
                cnt+=1
                #방향성이 정해지면 다음 루트는 한개만 가능
                for d in direct:
                    if [nextPos[0]+d[0]*2,nextPos[1]+d[1]*2] == before:
                        continue
                    nextDirect = [nextPos[0]+d[0],nextPos[1]+d[1]]
                    if isEdge(rectangle,nextDirect):
                        before = nextPos[:]
                        nextPos[0]+=2*d[0]
                        nextPos[1]+=2*d[1]
                        break
            answer = min(answer,cnt)

    
    
    
    return answer
