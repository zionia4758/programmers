#초단위 배열로 count할 경우 3600*24 *시청시간합 -> 시간초과



def solution(play_time, adv_time, logs):
    answer = 0
    time_log = []
    adv_time = sum(list(map(lambda x:x[0]*int(x[1]), zip([3600,60,1],adv_time.split(':')))))
    play_time = sum(list(map(lambda x:x[0]*int(x[1]), zip([3600,60,1],play_time.split(':')))))
    start_log = []
    end_log = []
    total_time = [0]*(play_time+2)
    for l in logs:
        start, end = l.split('-')
        s_time = sum(list(map(lambda x:x[0]*int(x[1]), zip([3600,60,1],start.split(':')))))
        e_time = sum(list(map(lambda x:x[0]*int(x[1]), zip([3600,60,1],end.split(':')))))
        total_time[s_time+1] += 1
        total_time[e_time+1] -= 1
    for i in range(1, play_time+1):
        total_time[i] = total_time[i-1] + total_time[i] 
    for i in range(1,play_time+1):
        total_time[i] = total_time[i-1] + total_time[i] 
        
    max_time = 0
    for i in range(play_time-adv_time+1):
        if max_time < total_time[i+adv_time]-total_time[i]:
            max_time = total_time[i+adv_time]-total_time[i]
            answer = i

    return f"{answer//3600:02}:{answer//60%60:02}:{answer%60:02}"
