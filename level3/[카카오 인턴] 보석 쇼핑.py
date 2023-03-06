from collections import defaultdict as dd
from collections import Counter


def solution(gems):
    gem_len = len(gems)
    gem_set = set(gems)
    gem_cnt = len(gem_set)
    answer = [0,gem_len]
    if gem_cnt == gem_len:
        return [1,gem_len]
    start = 0
    end = gem_cnt
    gem_list = Counter(gems[start:end])
    window = False
    i=0
    while end<=gem_len :
        if not window:
            if len(gem_list)<gem_cnt:
                gem_list[gems[end]]+=1
                end +=1
            else:
                answer = [start,end]
                window = True
                gem_list[gems[start]]-=1
                if gem_list[gems[start]]==0:
                    del gem_list[gems[start]]
                start+=1
        if window:
            if end-start < gem_cnt:
                break
            if len(gem_list)>= gem_cnt:
                answer = [start,end]
                gem_list[gems[start]]-=1
                if gem_list[gems[start]]==0:
                    del gem_list[gems[start]]
                start +=1
            else:
                if end==gem_len:
                    break
                gem_list[gems[start]]-=1
                gem_list[gems[end]]+=1
                if gem_list[gems[start]]==0:
                    del gem_list[gems[start]]
                start+=1
                end+=1
        
    answer[0]+=1
    return answer
