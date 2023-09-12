def min_move(same_list,direction):
    move_cnt = 0
    for i in range(len(same_list)):
        same_list[i*direction] = True
        if all(same_list):
            return move_cnt
        move_cnt += 1

def solution(name):
    answer = 0
    for alpha in name:
        answer += min(abs(ord(alpha)-ord('A')), abs(26-(ord(alpha)-ord('A'))))

    same_list = [cur == target for cur,target in zip(['A']*len(name), name) ]

    same_list = same_list+same_list
    move_cnt = 200
    for i in range(len(name)):
        move_cnt = min(move_cnt, min_move(same_list[len(name)-i : 2*len(name)-i],1)+i)
        move_cnt = min(move_cnt, min_move(same_list[i : len(name)+i],-1)+i)
    # print(move_cnt)
    
    return answer+move_cnt
