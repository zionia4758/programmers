def solution(people, limit):
    answer = 0
    total = 0
    upper = list(filter(lambda x:x>limit//2, people))
    lower = list(filter(lambda x:x<=limit//2, people))
    upper.sort()
    lower.sort(reverse = True)
    while upper:
        answer += 1
        remain = limit-upper.pop()
        if not lower or remain<lower[-1]:
            continue
        lower.pop()
    answer += (len(lower)+1)//2
    return answer
