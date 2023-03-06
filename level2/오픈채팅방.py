def solution(record):
    answer = []
    id_name = {}
    log = []
    for r in record:
        comd  = r.split(' ')
        u_id = comd[1]
        if comd[0] == 'Enter':
            log.append(['E',u_id])
            id_name[u_id]=comd[2]
        elif comd[0] == 'Leave':
            log.append(["L",u_id])
        elif comd[0] == 'Change':
            id_name[u_id]=comd[2]
    for l in log:
        if l[0]=='E':
            answer.append(f'{id_name[l[1]]}님이 들어왔습니다.')
        elif l[0]=='L':
            answer.append(f"{id_name[l[1]]}님이 나갔습니다.")
    return answer
