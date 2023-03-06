def solution(msg):
    answer = []
    word_set = {}
    msg_len = len(msg)
    max_num = 1
    for c in range(ord('A'),ord('Z')+1):
        word_set[chr(c)]=max_num
        max_num += 1
    idx = 0
    while idx < len(msg):
        for exist in list(word_set.keys())[::-1]:
            if msg[idx:].startswith(exist):
                #print(word_set[exist])
                answer.append(word_set[exist])
                if msg_len-idx > len(exist):
                    word_set[msg[idx:idx+len(exist)+1]]=max_num
                    max_num += 1
                idx += len(exist)
                break
    #print(word_set)
    return answer
