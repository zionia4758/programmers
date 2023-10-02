from datetime import datetime,timedelta
from heapq import heappush, heappop
def line_parsing2(line):
    day,t,p = line.split()
    h,m,s = t.split(":")
    h = int(h)
    m = int(m)
    s,ms = s.split('.')
    s=int(s)
    ms = int(ms)
    complete_time = timedelta(hours = h, minutes = m, seconds = s, milliseconds = ms)
    
    process_time = timedelta(seconds = float(p[:-1]))
    
    if complete_time > process_time:
        start_time =complete_time - process_time + timedelta(milliseconds = 1)
    else:
        start_time = timedelta(seconds=0)
    complete_time += timedelta(seconds = 1)
    return [start_time,complete_time,process_time]

def solution(lines):
    answer = 0
    traffic = []
    for i,line in enumerate(lines):
        traffic.append(line_parsing2(line))
    traffic.sort(key = lambda x:x[0])

    cur_time = timedelta(seconds=0)
    queue = []
    #시작과 끝나는 시간 기준으로 
    while traffic:
       #작업완료물 제거
        while queue and queue[0] <= cur_time:
            heappop(queue)

        #처리할 작업 갱신
        while traffic and traffic[0][0] <= cur_time:
            heappush(queue,traffic.pop(0)[1])
    
        #최대 처리 정답 갱신
        answer = max(answer,len(queue))
        
        #다음 시간으로 옮기기
        if traffic:
            cur_time = traffic[0][0]


    return answer
