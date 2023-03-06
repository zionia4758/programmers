import re
from collections import Counter
def solution(s):
    answer = []
    a=Counter(re.findall('\d+',s))
    a=sorted(a.items(),key = lambda x:x[1],reverse = True)
    for c in a:
        answer.append(int(c[0]))
    
    
    
    return answer
