#table에서 도형리스트뽑기
#piece 는 최대 1*6크기
#빈칸 또한 6칸 이내라는 점 (중요)
from collections import defaultdict as dd
def get_piece(table,target):
    piece_map = []
    t_len = len(table)
    for y in range(t_len):
        for x in range(t_len):
            if table[y][x]==target:
                table[y][x]=1-target
                piece = [[y,x]]
                queue = [[y,x]]
                idx = 0
                while queue:
                    py,px = queue.pop()
                    for dy,dx in [[0,1],[0,-1],[1,0],[-1,0]]:
                        ny = py+dy
                        nx = px+dx
                        if ny<0 or ny>=t_len or nx<0 or nx>=t_len:
                            continue
                        if table[ny][nx]==target:
                            table[ny][nx]=1-target
                            queue.append([ny,nx])
                            piece.append([ny,nx])
                        idx +=1 
                piece_map.append(piece)
    return piece_map
def regularization(piece):
    len_list=[]
    for l in zip(*piece):
        len_list.append([min(l),max(l)])

    r_piece =[ [0]*(len_list[1][1]-len_list[1][0]+1) for i in range(len_list[0][1]-len_list[0][0]+1)]
    for y,x in piece:
        r_piece[y-len_list[0][0]][x-len_list[1][0]]=1
    return r_piece
def rotate(piece):
    r_piece = [list(l) for l in zip(*piece[::-1])]
    return r_piece

def match(blank_dict,piece_dict):
    cnt = 0
    for b_idx in blank_dict:
        if b_idx not in piece_dict:
            #print("not match")
            continue
        for blank in blank_dict[b_idx]:
            piece_list = piece_dict[b_idx]
            for i in range(len(piece_list)):
                piece = piece_list[i]
                if rotate_n_same(blank,piece):
                    cnt+=b_idx
                    #print(blank,piece)
                    piece_list.pop(i)
                    break
    #print(cnt)
    return cnt
def rotate_n_same(blank,piece):
    for r in range(4):
        if blank == piece:
            return True
        piece = rotate(piece)
    return False
def solution(game_board, table):
    answer = -1

    piece_list = get_piece(table,1)
    piece_dict = dd(list)
    for p in piece_list:
        r_piece = regularization(p)
        piece_dict[len(p)].append(r_piece)
    blank_list = get_piece(game_board,0)
    blank_dict = dd(list)
    for b in blank_list:
        b_piece = regularization(b)
        blank_dict[len(b)].append(b_piece)
    answer = match(blank_dict,piece_dict)
    return answer
