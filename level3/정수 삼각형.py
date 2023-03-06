#depth,targetIdx
def searchRoute(triangle,dpTri,depth,targetIdx):
    if depth == len(dpTri):
        return 0
    if dpTri[depth][targetIdx]!=-1:
        return dpTri[depth][targetIdx]
    else:
        dpTri[depth][targetIdx] = triangle[depth][targetIdx]+max(
            searchRoute(triangle,dpTri,depth+1,targetIdx),
                                     searchRoute(triangle,dpTri,depth+1,targetIdx+1))
        return dpTri[depth][targetIdx]
    

def solution(triangle):
    dpTri = [[-1]*(i+1) for i in range(len(triangle))]
    searchRoute(triangle,dpTri,0,0)
    answer = dpTri[0][0]
    return answer
