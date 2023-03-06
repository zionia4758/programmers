from collections import defaultdict as dd

def solution(n, edge):
    graph =dd(list)
    for v in edge:
        graph[v[0]].append(v[1])
        graph[v[1]].append(v[0])
        
    nextNode = [1]
    already = set([1])
    print(already)

    while True:
        nextLevel = []
        for v in nextNode:
            for nextV in graph[v]:
                if nextV not in already:
                    already.add(nextV)
                    nextLevel.append(nextV)

        if len(nextLevel)==0:
            break
        nextNode = nextLevel[:]
    answer = len(nextNode)
    return answer
