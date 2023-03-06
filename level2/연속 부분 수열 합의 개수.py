def solution(elements):
    answer = 0
    e_len = len(elements)
    elements += elements
    sum_set = set()
    for length in range(1,e_len+1):
        for i in range(0,e_len):
            sum_set.add(sum(elements[i:i+length]))
    
    return len(sum_set)
