def solution(progresses, speeds):
    answer = []
    end_date = []
    for p,s in zip(progresses, speeds):
        end_date.append((100-p+s-1)//s)
    start = 0
    for d in end_date:
        if d <= start:
            answer[-1] += 1
        else:
            start = d
            answer.append(1)
    return answer
