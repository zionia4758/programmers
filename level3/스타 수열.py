from collections import Counter
from collections import defaultdict as dd

def solution(a):
    answer = -1
    val_idx = dd(list)
    for i,v in enumerate(a):
        val_idx[v].append(i)

    a_len = len(a)
    cnt_map = Counter(a).most_common()
    for v,v_cnt in cnt_map:
        idx_list = val_idx[v]
        start = 0
        cnt = 0
        if answer >= v_cnt*2:
            break
        for idx in idx_list:
            if start<idx and a[idx-1]!=v:
                cnt += 2
                start = idx+1
            elif idx+1<a_len and a[idx+1]!=v:
                start = idx+2
                cnt += 2

        answer = max(cnt,answer)
        
        

    
    return answer
