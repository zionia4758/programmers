v=1
h=0
def solution(board):
    answer = 0
    ret = [[ [98765421,987654321] for x in range(len(board[0]))] for y in range(len(board))]
    ret[0][0][0]=0
    ret[0][0][1]=0
    queue = [[0,0,h],[0,0,v]]
    x_len = len(board[0])
    y_len = len(board)
    direct = [[0,1,h],[0,-1,h],[1,0,v],[-1,0,v]]
    while queue:
        y,x,before_d = queue.pop(0)
        for dy,dx,d in direct:
            next_x = dx+x
            next_y = dy+y

            if next_x <0 or next_x == x_len:
                continue
            if next_y < 0 or next_y == y_len:
                continue
            if board[next_y][next_x] == 1:
                continue
            if before_d == d:
                cost = 100
            else:
                cost = 600
            if ret[next_y][next_x][d] > ret[y][x][before_d] + cost:
                ret[next_y][next_x][d] = ret[y][x][before_d] + cost
                queue.append([next_y,next_x,d])
            #print(queue)
    #print(ret)
    return min(ret[-1][-1])
