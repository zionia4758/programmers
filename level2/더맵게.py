import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville)>1 and scoville[0] < K:
        low1 = heapq.heappop(scoville)
        low2 = heapq.heappop(scoville)
        heapq.heappush(scoville, low1+2*low2)
        answer += 1
    if scoville[0] < K:
        answer = -1
        
    return answer
