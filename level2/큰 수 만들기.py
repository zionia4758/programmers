def solution(number, k):
    cnt = 0
    answer = [number[0]]

    number = number[1:]
    for n in number:
        if cnt == k:
            answer.append(n)
            continue
        while answer and int(answer[-1]) < int(n):
            answer.pop(-1)
            cnt += 1

            if cnt == k:
                break
        answer.append(n)
    if cnt!=k:
        answer = answer[:-(k-cnt)]
   #print(answer)
    return "".join(answer)
