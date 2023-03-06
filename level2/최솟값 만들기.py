def func(a,b):
    length = min(len(a),len(b))
    total = 0
    for i in range(length):
        total += a.pop(0)*b.pop()
    return total

def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    answer = func(A,B)

    return answer
