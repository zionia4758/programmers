#redix sort 응용? 

                
#tree 구조 사용하면 좋을듯
def solution(words):
    global answer
    answer = 0
    
    def dict_add(word_dict,word):
        global answer
        if not word:
            return
        prefix = word[0]
        if prefix in word_dict:
            child = word_dict[prefix]
            if type(child) == str:
                before_word = child
                word_dict[prefix] = {}
                dict_add(word_dict[prefix],before_word)
                dict_add(word_dict[prefix],word[1:])
                answer += 1
            else:
                dict_add(word_dict[prefix],word[1:])
                answer += 1
        else:
            word_dict[prefix] = word[1:]
            answer += 1

    word_dict = {}
    for word in words:
        dict_add(word_dict,word)
    
    return answer
