#완전탐색시 2^n*2^n
#각 포인트 비교 - 서로 다를시 홀수 번 뒤집혀야함
#행 열 첫줄에서 안맞는거만 뒤집어보기 - 5*5
def solution(beginning, target):
    answer = 101
    lenX = len(beginning[0])
    lenY = len(beginning)
    want = [[beginning[y][x]^target[y][x]for x in range(lenX)]for y in range(lenY)]
    diffX = want[0]
    diffY = [want[i][0] for i in range(lenY)]
    result = [[diffY[y]^diffX[x] for x in range(lenX) ]for y in range(lenY)]
    
    xReverseResult = [[(diffY[y])^(1-diffX[x]) for x in range(lenX) ]for y in range(lenY)]
    yReverseResult = [[(1-diffY[y])^diffX[x] for x in range(lenX) ]for y in range(lenY)]
    xyReverseResult = [[(1-diffY[y])^(1-diffX[x]) for x in range(lenX) ]for y in range(lenY)]
    answer =101
    if want==result:
        answer = min(answer,diffX.count(1)+diffY.count(1))
    if want == xReverseResult:
        answer = min(answer,diffX.count(0)+diffY.count(1))
    if want == yReverseResult:
        answer = min(answer,diffX.count(1)+diffY.count(0))
    if want == xyReverseResult:
        answer = min(answer,diffX.count(0)+diffY.count(0))
    if answer == 101:
        answer=-1
    return answer
