import heapq
#jobs가 index0에 대해 정렬 되어 있다 가정
def solution(jobs):
    jobLen = len(jobs)
    answer = 0
    endTime = 0
    jobList = []
    jobs.sort(key = lambda x:x[0])
    while len(jobList)>0 or len(jobs)>0:
        while len(jobs)>0 and jobs[0][0]<=endTime:
            other = jobs.pop(0)
            heapq.heappush(jobList,[other[1],other[0]])
        if len(jobList)==0:
            endTime = jobs[0][0]
        else:
            target = heapq.heappop(jobList)

            answer+=endTime-target[1]+target[0]
            endTime += target[0]
    return answer//jobLen
