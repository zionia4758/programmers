def solution(s):
    answer = True
    right_set = {'(':')'}
    q = []
    if len(s)%2 ==1:
        return False
    for c in s:
        if c ==')':
            if not q:
                return False
            else:
                q.pop()
        else:
            q.append(c)
    if q:
        return False
    return True
