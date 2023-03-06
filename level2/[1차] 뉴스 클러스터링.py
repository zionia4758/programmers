from collections import defaultdict as dd
def solution(str1, str2):
    answer = 0
    str1=str1.lower()
    str2=str2.lower()
    
    s1 = [a+b  for a,b in zip(str1,str1[1:]) if a.isalpha() and b.isalpha()]
    s2 = [a+b for a,b in zip(str2,str2[1:]) if a.isalpha() and b.isalpha()]
    inter_set = set(s1) & set(s2)
    union_set = set(s1) | set(s2)
    
    up=0
    for s in inter_set:
        up+=min(s1.count(s),s2.count(s))
    down = 0
    for s in union_set:
        down+=max(s1.count(s),s2.count(s))
    if down == 0:
        return 65536
    return 65536*up/down//1
