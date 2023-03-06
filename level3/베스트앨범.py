from collections import defaultdict
def solution(genres, plays):
    answer = []
    playCnt = defaultdict(lambda :0) 
    idx = 0
    playIndex = defaultdict(lambda : [])
    genrePlay = defaultdict(lambda : [])
    for p in zip(genres,plays):
        playCnt[p[0]]+=p[1]
        playIndex[p].append(idx)
        idx += 1
        genrePlay[p[0]].append(p[1])
    for g in genrePlay:
        genrePlay[g].sort(reverse = True)
    playCnt = sorted(playCnt.items(),key = lambda x: x[1],reverse = True)
   # print(genrePlay)
        
    for i in playCnt:
        nextG = i[0]
        for idx in range(min(len(genrePlay[nextG]),2)):
            gList = genrePlay[nextG]
            answer.append(playIndex[(nextG,gList[idx])].pop(0))

            


    return answer
