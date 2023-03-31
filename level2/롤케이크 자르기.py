from collections import Counter as C
def solution(topping):
    answer = 0
    total_len = len(topping)
    idx = 1
    left = C(topping[:idx])
    right = C(topping[idx:])
    while idx < total_len:
        if len(left) == len(right):
            answer += 1
        target = topping[idx]
        left[target] += 1
        right[target] -= 1
        if right[target] == 0:
            del(right[target])
        idx += 1
    return answer
