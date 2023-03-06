def solution(s):
    answer = []
    cnt = 0
    zero_cnt = s.count('0')
    total_zero=0
    while s!="1":
        s = bin(len(s)-zero_cnt)[2:]
        cnt+=1
        total_zero+=zero_cnt
        zero_cnt = s.count('0')
    answer=[cnt,total_zero]
    return answer
