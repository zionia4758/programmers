def solution(land):
    answer = 0
    idx = -1
    before = [0,0,0,0]
    for l in land:
        for i in range(4):
            l[i] += max(before[:i]+before[i+1:])
        before = l

    return max(land[-1])
