def solution(maps):
    answer = 0
    n=len(maps)
    m=len(maps[0])
    direct = [[1,0],[-1,0],[0,1],[0,-1]]
    t = [n-1,m-1]
    queue = [[0,0,2]]
    while len(queue)>0:
        originalP = queue.pop(0)

        for d in direct:
            p=list(originalP)
            p[0]+=d[0]
            p[1]+=d[1]
            if p[:2] == t:
                return p[2]
            if p[0]<0 or p[0]>=n:
                continue
            if p[1]<0 or p[1]>=m:
                continue
            if maps[p[0]][p[1]] == 0 or maps[p[0]][p[1]] == 2:
                continue
            if maps[p[0]][p[1]] == 1:
                maps[p[0]][p[1]] = 2

            queue.append([p[0],p[1],p[2]+1])
    
    return -1
