def solution(n):
    answer = ""
    
    
#     cnt = bin(n)[2:].count('1')
#     for next_n in range(n+1,1000001):
#         if cnt == bin(next_n)[2:].count('1'):
#             return next_n
    bin_n = '0'+bin(n)[2:]
    idx = bin_n.rfind('01')
    bin_n = bin_n[:idx]+'10'+'0'*bin_n[idx+2:].count('0')+'1'*bin_n[idx+2:].count('1')
    return int(bin_n,base = 2)
