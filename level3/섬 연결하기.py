from collections import defaultdict as dd
def solution(n, costs):
    costs.sort(key= lambda x:x[2])
    start = costs.pop(0)
    connected = set([start[0],start[1]])

    answer = start[2]
    for i in range(n-2):
        for v in costs:
            if (v[0] in connected) == (v[1] not in connected):
                connected.add(v[0])
                connected.add(v[1])
                answer+=v[2]
                break
    return answer
