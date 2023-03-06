from collections import defaultdict as dd
import sys
sys.setrecursionlimit(10**6)
def search(node,a,graph):
    is_visit[node] = 1
    cnt = 0
    for next_n in graph[node]:
        if is_visit[next_n]==1:
            continue
        cnt += search(next_n,a,graph)
        a[node] += a[next_n]
        a[next_n]=0

    return abs(a[node])+cnt
    
    


def solution(a, edges):
    global is_visit
    is_visit = [0]*len(a)
    answer = 0
    graph = dd(list)
    if not any(a):
        return 0
    if sum(a) != 0:
        return -1
    for x,y in edges:
        graph[x].append(y)
        graph[y].append(x)

    answer = search(0,a,graph)



        
        
    
    return answer
