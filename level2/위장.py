from collections import defaultdict as dd
def solution(clothes):
    cloth_set = dd(list)
    for c in clothes:
        cloth_set[c[1]].append(c[0])
    answer = 1
    for c in cloth_set:
        answer*=len(cloth_set[c])+1
    return answer-1
