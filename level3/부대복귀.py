#다익스트라도 시간초과뜸

#dest기준으로 bfs
from collections import defaultdict

def solution(n, roads, sources, destination):
    answer = []
    graph = defaultdict(list)
    for r in roads:
        graph[r[0]].append(r[1])
        graph[r[1]].append(r[0])
    dist = [-1]*(n+1)
    d=0
    searchList = [destination]
    isVisit=[0]*(n+1)
    isVisit[destination]=1
    while searchList:
        nodeList = searchList[:]
        searchList.clear()
        for node in nodeList:
            dist[node]=d
            nextNodeList = graph[node]
            for nextNode in nextNodeList:
                if isVisit[nextNode]==0:
                    searchList.append(nextNode)
                    isVisit[nextNode]=1

        d+=1
    for s in sources:
        answer.append(dist[s])
    return answer
