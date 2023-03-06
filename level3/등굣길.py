def findRoute(route,y,x):
    if y>=len(route):
        return 0
    if x>=len(route[0]):
        return 0
    if route[y][x]==-1:
        return 0
    if route[y][x]!=0:
        return route[y][x]


    route[y][x] = (findRoute(route,y+1,x) + findRoute(route,y,x+1))%1000000007
    return route[y][x]



def solution(m, n, puddles):
    route = [[0]*m for i in range(n) ]
    for p in puddles:
        route[p[1]-1][p[0]-1]=-1
    route[n-1][m-1]=1
    #print(route)
    findRoute(route,0,0)
    

    answer = route[0][0]
    return answer 
