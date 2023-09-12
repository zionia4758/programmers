from collections import Counter
def solution(nums):
    c = Counter(nums)
    return min(len(c), len(nums)//2)
