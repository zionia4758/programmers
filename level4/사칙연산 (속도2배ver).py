
#완전탐색 = 각 부호별로 묶어서 모든 경우의 수 해보기 = 최대 100!
#DP 적용 = 각 부호별 트리 만들어보기?
#== 트리처럼 구현하되, 각 subtree에 따른 최대값을 찾아보자

#start에서 end까지  최소, 최대값을 저장하는 배열
                
                    
def solution(arr):
    nums = arr[::2]
    ops = arr[1::2]
    
    min_dp = [[97654321]*len(nums) for j in range(len(nums))]
    max_dp = [[-9765432]*len(nums) for j in range(len(nums))]
    for i in range(len(nums)):
        max_dp[i][i] = int(nums[i])
        min_dp[i][i] = int(nums[i])
        # print(max_dp[i][i])
    for cnt in range(1,len(nums)):
        for start in range(len(nums)-cnt): #start에서 cnt개수만큼 구간 start:start+cnt
            max_candi = []
            min_candi = []
            for i in range(cnt): #start:start+cnt를 start:start+i 와 start+i:start+cnt로 나눈다
                if ops[start+i] == '-':
                    max_candi.append(max_dp[start][start+i] - min_dp[start+i+1][start+cnt])
                    min_candi.append(min_dp[start][start+i] - max_dp[start+i+1][start+cnt])
                if ops[start+i] == '+':
                    max_candi.append(max_dp[start][start+i] + max_dp[start+i+1][start+cnt])
                    min_candi.append(min_dp[start][start+i] + min_dp[start+i+1][start+cnt])
            # print(start,cnt)
            # print(max_candi,min_candi)
            max_dp[start][start+cnt] = max(max_candi)
            min_dp[start][start+cnt] = min(min_candi)
    # print(max_dp[0][len(nums)-1])
    
    return max_dp[0][len(nums)-1]
