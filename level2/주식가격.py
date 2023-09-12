def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i,price in enumerate(prices):
        while stack and stack[-1][1] > price:
            stack_i, stack_price = stack.pop()
            answer[stack_i] = i - stack_i
        stack.append((i,price))
    end_i = len(prices)-1
    while stack:
        i,price = stack.pop()
        answer[i] = end_i - i
    
    return answer
