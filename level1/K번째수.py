def solution(array, commands):
    answer = []
    for i,j,k in commands:
        sort_arr = sorted(array[i-1:j])
        answer.append(sort_arr[k-1])
    return answer
