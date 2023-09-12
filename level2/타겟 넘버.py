def dfs(remain,cur, target):
    if not remain:
        if cur == target:
            return 1
        else:
            return 0
    else:
        return dfs(remain[1:], cur+remain[0], target) + dfs(remain[1:], cur-remain[0], target)
            

def solution(numbers, target):
    answer = dfs(numbers,0,target)
    
    return answer
