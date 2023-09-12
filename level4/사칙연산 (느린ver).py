
#완전탐색 = 각 부호별로 묶어서 모든 경우의 수 해보기 = 최대 100!
#DP 적용 = 각 부호별 트리 만들어보기?
#== 트리처럼 구현하되, 각 subtree에 따른 최대값을 찾아보자

#start에서 end까지  최소, 최대값을 저장하는 배열
min_max =[ [[999999,-999999] for i in range(101)] for j in range(101) ]


def search(arr,isMax,start,end,debug=True):
    nums = []
    if start==end:
        # print(int(arr[2*start]))
        return int(arr[2*start])
    if isMax:
        if min_max[start][end][1] > -999999:
            return min_max[start][end][1]
    else:
        if min_max[start][end][0] < 999999:
            return min_max[start][end][0]

    for i in range(start,end):
        # print(start,end)
        #min_max 구간 최대로 만들기
        if isMax:
            if arr[2*i+1] == '+':
                min_max[start][end][1] = max(min_max[start][end][1],
                                             search(arr,True,start,i) \
                                        + search(arr,True,i+1,end))
            else:
                min_max[start][end][1] = max(min_max[start][end][1],
                                             search(arr,True,start,i) \
                                        - search(arr,False,i+1,end))
            # print(start,end,min_max[start][end])
        # #min_max 구간 최소로 만들기
        else:
            if arr[2*i+1] == '+':
                min_max[start][end][0] = min(min_max[start][end][0],
                                             search(arr,False,start,i) \
                                         + search(arr,False,i+1,end))
            else:
                min_max[start][end][0] = min(min_max[start][end][0],
                                             search(arr,False,start,i) \
                                        - search(arr,True,i+1,end))
            # print(start,end,min_max[start][end])
    if isMax:
        return min_max[start][end][1]
    else:
        return min_max[start][end][0]
                    
                    
def solution(arr):

    answer = -1
    search(arr,True,0,len(arr)//2,False)
    # print(min_max[0][len(arr)//2][1])

    
    return min_max[0][len(arr)//2][1]
