#나가는 화살표 = 팀장
#들어오는 화살표 = 팀원

#모든 팀에서 1명 이상 직원 참여시키기
#참여 팀원의 평균 매출액 최소화
#정확히 1명의 팀장만 받으므로 순환구조는 없음

from collections import defaultdict as dd

upper = 2**31-1

    
def solution(sales, links):
    answer = 0
    graph = dd(list)
    #dp[len(sales)][2] . 0 = 출석x 1 = 이미 팀이 출석
    dp = [[upper,upper] for _ in range(len(sales))]
    for link in links:
        graph[link[0]-1].append(link[1]-1)
    #1번부터 시작해서 각 팀으로 내려가면서 차출하기
    #각 팀마다 최소매출액 팀원 or 여러 팀에 속한사람 을 고를 수 있다.
    def search(team_num, already_pick):
        #이미 출석한 팀이면 팀장이 출석할 필요가 없다
        #단, 출석하지 않은 팀일 때 상황에 따라 팀장이 출석하는것이 좋을 수도 있음
        idx = 0 if not already_pick else 1
                
        #dp 확인
        if dp[team_num][idx] != upper:
            return dp[team_num][idx]
            
        team_member = graph[team_num]
        boss_member = [member for member in team_member if member in graph.keys()]
        #만약 최하위 팀일 경우 바로 리턴
        if not boss_member:
            dp[team_num][1] = 0
            dp[team_num][0] = min(sales[member] for member in team_member+[team_num])
            return dp[team_num][idx]
        
        #팀이 아직 출석하지 않은 경우
        #팀 내에서 한명은 출석해야 함
        if not already_pick:
            #1. 팀장이 출석하는 경우
            total_sales = sales[team_num]
            for member in boss_member:
                total_sales += search(member,False)
            dp[team_num][0] = total_sales
            #2. 다른팀 팀장인 팀원이 출석하는 경우
            for other_boss in boss_member:
                total_sales = sales[other_boss] + search(other_boss,True)
                for member in boss_member:
                    if other_boss == member:
                        continue
                    total_sales += search(member,False)
                dp[team_num][0] = min(dp[team_num][0], total_sales)

            #3. 최소 판매액 팀원이 출석하는 경우
            min_member = min(team_member, key = lambda x:sales[x])
            if min_member != team_num and min_member not in boss_member:
                total_sales = sales[min_member]
                for member in boss_member:
                    total_sales += search(member,False)
                dp[team_num][0] = min(dp[team_num][0], total_sales)
            return dp[team_num][0]
            
        #이미 출석한 팀의 경우
        if already_pick:
            dp[team_num][1] = sum(search(member,False) for member in boss_member)
            return dp[team_num][1]
            
    answer = search(0,False)
    # print(dp)
    return answer
