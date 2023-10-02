from itertools import permutations
def cal(nums, exps, target):
    i = 0
    while i < len(exps):
        if exps[i] == target:
            if target == '+':
                nums[i] = nums[i]+nums[i+1]
                nums.pop(i+1)
            elif target == '-':
                nums[i] = nums[i]-nums[i+1]
                nums.pop(i+1)
            elif target == '*':
                nums[i] = nums[i]*nums[i+1]
                nums.pop(i+1)
            exps.pop(i)
            continue
        i += 1


def solution(expression):
    answer = 0
    nums = []
    exps = []
    num = ""
    for e in expression:
        if e == '+' or e == '-' or e == '*':
            nums.append(int(num))
            num = ''
            exps.append(e)
        else:
            num += e
    nums.append(int(num))
    exp_type = ['+','-', '*']

    for order in permutations(exp_type,3):
        new_nums = nums[:]
        new_exps = exps[:]

        for target in order:
            cal(new_nums,new_exps,target)

        answer = max(answer,abs(new_nums[0]))
    return answer
