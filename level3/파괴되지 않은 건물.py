#type 1=공격 2=회복
#1회당 최대 1000*1000 배열 수정 * 250000번
#데미지를 먼저 주고 부셔진 판에 대해 수리 -> 시간초과
#각 영역이 몇번 겹치는지 계산필요
def solution(board, skill):
    answer = 0
    y_len = len(board)
    x_len = len(board[0])
    damage = [[0]*(x_len+1) for y in range(y_len+1)]
    

    for t,y1,x1,y2,x2,degree in skill:
        point = -degree if t==1 else degree
        damage[y1][x1]+=point
        damage[y2+1][x1]-=point
        damage[y1][x2+1]-=point
        damage[y2+1][x2+1]+=point

    for x in range(x_len):
        d=0
        for y in range(y_len):
            temp=damage[y][x]
            damage[y][x]+=d
            d+=temp
    
    for y in range(y_len):
        d = 0
        for x in range(x_len):
            d+=damage[y][x]
            board[y][x]+=d

    for line in board:
        for hp in line:
            if hp>0:
                answer+=1
    return answer
