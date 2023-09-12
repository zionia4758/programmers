def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    already = -1
    for num in arr:
        if num == already:
            continue
        else:
            already = num
            answer.append(num)
    return answer
