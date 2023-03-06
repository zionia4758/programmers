def solution(n, words):
    answer = []
    start = words[0][0]
    cnt = 0
    idx = 0
    word_set = []
    for w in words:
        if start!=w[0] or w in word_set:
            break
        word_set.append(w)
        start = w[-1]
        idx += 1
    
    if idx == len(words):
        return [0,0]
    cnt = idx//n+1
    num = idx%n +1
    
    return [num,cnt]
