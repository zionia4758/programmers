#n진법
#t개만큼 구하기
#n^k개마다 자리수가 늘어남
#t개*m명 자리수만큼 미리 구해두기
def convert_10_to_n(num, n):
    result = ""
    convert = [str(num) for num in range(10)]+['A','B','C','D','E','F']
    while num >= n:
        result += convert[num%n]
        num //= n
    result += convert[num]
    result = result[::-1]
    return result

def solution(n, t, m, p):
    answer = ''

    converted = []
    total_len = 0
    num = 0
    while total_len < t*m+p:
        converted += convert_10_to_n(num,n)
        num += 1
        total_len += len(converted[-1])

    converted_str = "".join(converted)
    p -= 1
    answer = converted_str[p:t*m+p:m]
    answer = "".join(answer)

    
    return answer
