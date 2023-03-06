import copy
def solution(board):
    y_len = len(board)
    x_len = len(board[0])
    total_len = x_len*y_len
    
    max_val_board =copy.deepcopy(board)

    for idx in range(total_len-1-x_len , -1 , -1):

        x_idx = idx%x_len
        y_idx = idx//x_len
        #print(y_idx,x_idx)
    
        if board[y_idx][x_idx]==0:
            continue
        if x_idx>=x_len-1 or y_idx>=y_len-1:
            continue
        down = board[y_idx+1][x_idx]
        right= board[y_idx][x_idx+1]
        cross = board[y_idx+1][x_idx+1]
        #print(down,right,cross)
        board[y_idx][x_idx]= min(down,right,cross)+1
           
    #print(board)
    max_side_len = max(map(max,board))

                       
    return max_side_len**2
