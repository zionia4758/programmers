from collections import defaultdict as dd
import heapq
def search(idx, queue, sheep,wolf, info):
    if info[idx]==0:
        sheep += 1
    else:
        wolf += 1
    if sheep-wolf ==0:
        return 0
    queue.remove(idx)
    queue.extend(graph[idx])
    result = sheep
    for next_idx in queue:
        result = max(result, search(next_idx,queue[:],sheep,wolf,info))
    return result


def solution(info, edges):
    global graph
    answer = 0
    sheep_cnt = 0
    wolf_cnt = [0]*len(info)
    graph = dd(list)
    for e in edges:
        graph[e[0]].append(e[1])

    answer = search(0,[0],0,0,info)
    return answer
