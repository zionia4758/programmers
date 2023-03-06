#가장 작은건 무조건 남기기 가능
#양쪽도 무조건 남기기 가능
#pivot기준 좌 우 가장 작은값,2번쨰작은값 총 4개중 1개 이상 보다 작을때
#예시1 : 가장작은값 and 가장작은값보다 작을때
#2 : 가장작은값 and 두번째 작은값보다 작을때
#3 : 두번쨰 작은값 and 가장 작은값보다 작을때
#O(3n)=3000000
#그냥 양쪽의 min값보다 하나 이상 작을때
def solution(a):
    if len(a)<=2:
        return len(a)
    answer = 2
    upper = 1000000000
    leftMin = []
    minNum=upper
    for n in a:
        leftMin.append(min(minNum,n))
        minNum = min(minNum,n)
    rightMin = []
    minNum=upper
    for n in a[::-1]:
        rightMin.append(min(minNum,n))
        minNum = min(minNum,n)
    rightMin = rightMin[::-1]
    idx = 1
    for n in a[1:-1]:
        compare = leftMin[idx-1]+rightMin[idx+1]
        if n<leftMin[idx-1] or n <rightMin[idx+1]:
            answer+=1
        idx+=1
    return answer
