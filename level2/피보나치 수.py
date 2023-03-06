def solution(n):
    answer = 0
    fibo = [0,1]
    for i in range(n-2):
        temp = fibo[1]
        fibo[1] = (fibo[0]+fibo[1])%12345667
        fibo[0] = temp
    return (fibo[1]+fibo[0])%1234567
