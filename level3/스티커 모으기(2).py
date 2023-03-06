
def solution(sticker):
    s_len = len(sticker)
    answer = 0
    ret = [[0]*s_len for i in range(2)]
    if s_len <=3:
        return max(sticker)
    ret[1][0] = sticker[0]
    ret[0][1] = sticker[1]
    ret[1][1]= sticker[0]
    for i in range(2,s_len):
        ret[0][i]=max(ret[0][i-1],ret[0][i-2]+sticker[i])
        ret[1][i] = max(ret[1][i-1],ret[1][i-2]+sticker[i])

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    return max(ret[1][-2],ret[0][-1])
