#포화이진트리 노드개수 = 2^n-1 = 이진법으로 2^n-1자리수가 되도록
def is_avail(n_str):
    str_len = len(n_str)
    pivot = str_len//2
    if str_len == 1:
        return True
    if n_str[pivot]=='0':
        if n_str[pivot//2]==0 and n_str[pivot+1+pivot//2]==0:
            return True
        return False
    if str_len == 3:
        return True
    return is_avail(n_str[:pivot]) and is_avail(n_str[pivot+1:])
def solution(numbers):
    answer = []
    for n in numbers:
        num_str = bin(n)[2:]
        l = len(num_str)
        cnt=0
        while l>0:
            l//=2
            cnt+=1
        num_str = '0'*(2**cnt-len(num_str)-1)+num_str
        print(is_avail(num_str))
        if is_avail(num_str):
            answer.append(1)
        else:
            answer.append(0)
    return answer
