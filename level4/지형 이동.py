#시작지점에서 모든 갈수있는곳 heapq에 넣기
#갈수있는곳에서 최소 비용으로 갈수있는 곳 추가한 뒤 heapq에 넣기
#전체 영역이 나올떄까지 반복하기
from heapq import heapify, heappop,heappush
def is_valid(y,x):
    if y>=0 and y<n and x>=0 and x<n:
        return True
    return False
    

def solution(land, height):
    global n
    answer = 0
    n = len(land)
    
    direction = [[1,0],[-1,0],[0,1],[0,-1]]
    cost_map = [[99999] * n for _ in range(n)]
    cost_map[0][0] = 0
    visited = set()
    heap_queue = [[0,0,0]]


    while len(visited) != n*n:
        cost,y,x = heappop(heap_queue)
        if (y,x) in visited:
            continue
        visited.add((y,x))
        answer += cost
        for d in direction:
            next_y = y+d[0]
            next_x = x+d[1]
            if not is_valid(next_y,next_x):
                continue
            if (next_y,next_x) not in visited:
                cost = abs(land[next_y][next_x] - land[y][x])
                if cost<=height:
                    cost = 0
                heappush(heap_queue,(cost,next_y,next_x))
                    
    
    return answer
