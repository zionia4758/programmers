
def find_max(steals,money):
    for i in range(len(money)):
        if i >=3:
            steals[i] = max(steals[i-1], money[i] + steals[i-2], money[i] + steals[i-3])
        elif i ==2:
            steals[i] = max(steals[i-1], money[i] + steals[i-2])
        else:
            steals[i] = money[i]
    return max(steals)

def solution(money):
    if len(money)==1:
        return money[0]
    max_steal1 = [0 for _ in range(len(money)-1)]
    max_steal2=  [0 for _ in range(len(money)-1)]
    find_max(max_steal1,money[:-1])
    find_max(max_steal2,money[1:])
    return max(max_steal1[-1], max_steal2[-1])