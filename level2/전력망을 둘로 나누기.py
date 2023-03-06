#wires가 완전 정렬 되어 있다 가정
from collections import defaultdict
def solution(n, wires):
    answer = 100
    wires.sort(key = lambda x:x[0])
    graph=defaultdict(list)
    for w in wires:
        graph[w[0]].append(w[1])
        graph[w[1]].append(w[0])
    
    for w in wires:
        total = set([1])
        nextList = [1]
        while nextList:
            nextNode = nextList.pop(0)
            nextNodeList = graph[nextNode]
            for node in nextNodeList:
                if (w[0]==node and w[1]==nextNode) or (w[1]==node and w[0]==nextNode):
                    continue
                if node in total:
                    continue
                nextList.append(node)
                total.add(node)
        answer = min(answer, abs(2*len(total)-n))
        
    return answer
