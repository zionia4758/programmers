
cnt = [0,0]
def divide(x,y,l,arr):
    #큰 범위에서 작은 범위로 탐색 - 작은 범위부터 하는 것보다는 연산량이 많을 듯
    pivot = arr[y][x]

    if l <= 1:
        cnt[pivot] += 1
        return
    for i in range(y,y+l):
        if all([num == pivot for num in arr[i][x:x+l]]) == False:
            divide(x,y,l//2,arr)

            divide(x+l//2,y,l//2,arr)

            divide(x,y+l//2,l//2,arr)

            divide(x+l//2,y+l//2,l//2,arr)

            return
    cnt[pivot] += 1

def solution(arr):

    divide(0,0,len(arr[0]),arr)
    
    return cnt
