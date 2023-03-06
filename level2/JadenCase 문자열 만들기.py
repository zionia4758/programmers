def solution(s):
    answer = ''
    sList = list(map(str.lower,s.split(" ")))
    wList = []
    for w in sList:
        if w=="":
            wList.append("")
            continue
        wList.append(w[0].upper()+w[1:])
    
    answer = " ".join(wList)
    return answer
