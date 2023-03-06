def solution(n, t, m, timetable):
    answer = ''
    times = []
    for time in timetable:
        times.append(sum(map(lambda time: int(time[0])*time[1],zip(time.split(':'),[60,1]))))
    times.sort()
    startTime = 540
    timeList = []
    last = 0
    cnt = 0
    for i in range(n):
        cnt = 0
        while cnt<m and len(times)>0 and times[0]<=startTime+i*t:
            last = times.pop(0)
            cnt+=1
    if cnt==m:
        answer = last-1
    else:
        answer = 540+(n-1)*t
    return str(answer//60).zfill(2)+":"+str(answer%60).zfill(2)
