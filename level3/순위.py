def floyde(n,graph):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k]==0:
                    continue
                if graph[i][k]==graph[k][j]:
                    graph[i][j]=graph[i][k]
def solution(n, results):
    answer = 0
    graph = [[0]*n for i in range(n)]
    for r in results:
        graph[r[0]-1][r[1]-1]=1
        graph[r[1]-1][r[0]-1]=-1
    floyde(n,graph)
    for g in graph:
        if g.count(0)==1:
            answer+=1
    
    return answer
