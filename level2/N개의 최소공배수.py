from math import gcd
def solution(arr):
    pivot = 1
    for n in arr:
        g = gcd(pivot,n)
        pivot *= n//g
    return pivot
