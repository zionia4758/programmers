
def solution(enroll, referral, seller, amount):
    answer = []
    refer_map = {}
    for enrol,refer in zip(enroll,referral):
        refer_map[enrol]=refer
    amount_map = {}
    for e in enroll:
        amount_map[e]=0

    for target,money in zip(seller,amount):
        money *=100
        while target!='-':
            refer = refer_map[target]
            refer_money = money//10
            amount_map[target] += money-refer_money
            money = refer_money
            target = refer
            if refer_money == 0:
                break
        
    
    for e in enroll:
        answer.append(amount_map[e])
    return answer
