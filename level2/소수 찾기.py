from itertools import permutations

def isPrime(num):
    if num < 2:
        return False
    pivot = int(num*0.5)+1
    for div in range(2,pivot):
        if num%div == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    combis =  sum([list(permutations(numbers,l)) for l in range(1,len(numbers)+1)] , [])
    
    combis = [int("".join(combi)) for combi in combis]
    combis = set(combis)

    for num in combis:
        if isPrime(num):
            answer += 1
    return answer
