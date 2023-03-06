#s -> e -> t1,t2로 갈때 cost[s][e]+cost[e][t1]+cost[e][t2]를 최소화
#플로이드워셜
#200*200*200
def floyde(costMap,n):

    for k in range(n):
        for y in range(n):
            for x in range(n):
                costMap[x][y]=min(costMap[x][y], costMap[x][k]+costMap[k][y])
                #print(costMap[x][y],x,y,k)


def solution(n, s, a, b, fares):
    answer = 0
    s-=1
    a-=1
    b-=1
    #costMap[s][t] = s에서 t로 가는 최저 요금
    costMap = [[1000000]*n for i in range(n)]
    for i in range(n):
        costMap[i][i]=0

    for f in fares:
        costMap[f[0]-1][f[1]-1]=f[2]
        costMap[f[1]-1][f[0]-1]=f[2]

    floyde(costMap,n)
    answer=100000000
    def getCost(costMap,a,b):
        s=max(a,b)
        t=min(a,b)
        return costMap[s][t]

    for e in range(n):
        answer = min(answer,costMap[s][e]+costMap[e][a]+costMap[e][b])
        
    graph = [[0]*n for i in range(n)]
    for f in fares:
        graph[f[0]-1][f[1]-1]=1
        graph[f[1]-1][f[0]-1]=1


    return answer
