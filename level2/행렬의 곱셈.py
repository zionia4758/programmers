def solution(arr1, arr2):
    answer = []
    for y in arr1:
        line = []
        for x in zip(*arr2):
            line.append(sum(list(map(lambda x:x[0]*x[1],zip(y,x)))))
        answer.append(line)
    return answer
