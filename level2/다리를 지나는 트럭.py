#다리를 건너는데 걸리는 시간 = length+1
#
def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = []
    
    for w in truck_weights:
        #1초가 더해졌을 때 나갈 차량 구하기
        if queue and queue[0][0] <= answer:
            weight += queue.pop(0)[1]
            
        #다리무게 여유 있을떄 차량 추가    
        if w <= weight:
            weight -= w
            queue.append([answer+bridge_length,w])
            answer += 1
        #여유가 없을 시 차량이 나가는 시간까지 대기
        else:
            while queue and w > weight:
                q = queue.pop(0)
                weight += q[1]
                answer = q[0]
            # print(answer)
            queue.append([answer+bridge_length,w])
            weight -= w
            answer += 1
        # print(answer-1,queue,weight)
    
    answer = queue[-1][0]+1

    
    return answer
