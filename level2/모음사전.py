#완전 탐색으로만 풀어보기

alpha = ["A","E","I","O","U"]
alpha_num = {alpha:i for i,alpha in enumerate(alpha)}
# print(alpha_num)
def next_word(word):
    if len(word)<5:
        word.append("A")
        return word
    else:
        idx = 4
        num = alpha_num[word[idx]]
        while num==4:
            word.pop()
            idx -= 1
            num = alpha_num[word[idx]]
        word[idx] = alpha[num+1]
        # print(word)
# print(next_word(['A','A','E']))
    
    
def solution(word):
    answer = 1
    target = ["A"]
    idx = 0
    while "".join(target) != word:
        next_word(target)
        # print(target)
        answer += 1
    
    return answer
