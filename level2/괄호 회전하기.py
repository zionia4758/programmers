def solution(s):
    answer = 0
    sets = {'[':']','{':'}','(':')'}
    new_s=s+s
    for i in range(len(s)):
        test_s = new_s[i:i+len(s)]
        q = []
        right_form = True
        for c in test_s:
            if c in [']','}',')']:
                if q and sets[q[-1]]==c :
                    q.pop()
                    continue
                else:
                    right_form = False
                    break
            q.append(c)
        if not q and right_form:
            answer += 1
    return answer
