def solution(n):
    answer = [[[],[]] for _ in range(n)]

    direction = 1
    i = -1
    cnt = 1
    while n > 0:
        for _ in range(n):
            i += direction
            answer[i][0].append(cnt)
            cnt += 1
        n -= 1
        if n == 0:
            break
        for _ in range(n):
            answer[i][0].append(cnt)
            cnt += 1
        n -= 1
        direction *= -1
        if n == 0:
            break
        for _ in range(n):
            i += direction
            answer[i][1].insert(0,cnt)
            cnt += 1
        direction *= -1
        n -= 1

    answer = sum(sum(answer,[]),[])

    return answer