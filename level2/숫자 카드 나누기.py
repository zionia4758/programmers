#A=철수 B=영희
#한쪽의 최대공약수
#한쪽에 
from math import gcd
def solution(arrayA, arrayB):
    answer = 0
    gcdA = arrayA[0]
    for a in arrayA[1:]:
        gcdA = gcd(gcdA,a)
    gcdB = arrayB[0]
    for b in arrayB[1:]:
        gcdB = gcd(gcdB,b)
        
    answer = gcdA
    for n in arrayB:
        if n%gcdA ==0:
            answer = 0
            break
    flag = True
    for n in arrayA:
        if n%gcdB == 0:
            flag = False
            break
    if flag:
        answer = max(gcdA,gcdB)
    return answer
